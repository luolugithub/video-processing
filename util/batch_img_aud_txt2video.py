# -*- coding: utf-8 -*-
"""
@Time ： 2021-04-17 10:33
@Auth ： LuoLu
@Email : argluolu@gmail.com
@File ：batch_img_aud_txt2video.py
@IDE ：PyCharm
@Motto：simple is everything
"""
import math
import os

from PIL import Image
from gtts import gTTS
import glob
import cv2
import moviepy.editor as mpe
import numpy as np
import time
import operator
from itertools import repeat
from moviepy.video.VideoClip import TextClip, ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from natsort import natsorted
from PIL import ImageOps


def pad_images_to_same_size(img2pad):
    """
    :param images: sequence of images
    :return: list of images padded so that all images have same width and height (max width and height are used)
    """
    # for img in images:
    h, w = img2pad.shape[:2]
    desired_size = max(h, w)

    delta_w = desired_size - w
    delta_h = desired_size - h
    top, bottom = (int)(delta_h / 2), (int)(delta_h - (delta_h / 2))
    left, right = (int)(delta_w / 2), (int)(delta_w - (delta_w / 2))

    color = [0, 0, 0]
    img_padded = cv2.copyMakeBorder(img2pad, top, bottom, left, right, cv2.BORDER_CONSTANT,
                                    value=color)
    return img_padded


def img_size_odd2even(image):
    # pad odd 2 even
    # new image H, W
    height, width, layers = image.shape
    # print("crop dst size: ", dst.shape[:2])
    if (height % 2) == 0:
        new_height = height
    else:
        new_height = math.ceil(height / 2) * 2
    if (width % 2) == 0:
        new_width = width
    else:
        new_width = math.ceil(width / 2) * 2
    # print(new_width, new_height)
    top, bottom = new_height, 0
    left, right = new_width, 0
    color = [0, 0, 0]
    newsize = (new_width, new_height)
    return newsize


def video_to_frames(path_video):
    # Start capturing the feed
    cap = cv2.VideoCapture(path_video, 0)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)

    return video_length


def resize_with_pad(im, target_width, target_height):
    '''
    Resize PIL image keeping ratio and using white background.
    '''
    target_ratio = target_height / target_width
    im_ratio = im.height / im.width
    if target_ratio > im_ratio:
        # It must be fixed by width
        resize_width = target_width
        resize_height = round(resize_width * im_ratio)
    else:
        # Fixed by height
        resize_height = target_height
        resize_width = round(resize_height / im_ratio)

    image_resize = im.resize((resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new('RGBA', (target_width, target_height), (0, 0, 0, 255))
    offset = (round((target_width - resize_width) / 2), round((target_height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert('RGB')


directory = "/home/luolu/Desktop/hd_sp_amazon(0-23-7000-7012)"
pathVideoOut = "/home/luolu/Desktop/video_sp_amazon"
mp3_root_dir = "/home/luolu/Desktop/mp3Amazon/"
bg_music_path = "/home/luolu/PycharmProjects/video-processing/util/bensound-memories.mp3"
tmp_img_dir = "/home/luolu/PycharmProjects/video-processing/tmp_img_dir/"
asin_processed = open('/home/luolu/PycharmProjects/video-processing/pqAmazon/asin.txt', mode='r+')

counter = 0
null_counter = 0
processed_counter = 0
null_video_counter = 0
size = (1920, 1080)
blank_img = np.ones((1920, 1080, 3), np.uint8)
processed_flag = False
# for filename in os.listdir(directory):
for filename in glob.iglob(directory + "/**/*.txt", recursive=True):
    asin = filename.split('.txt')[0].split("/")[-1]
    with open('/home/luolu/PycharmProjects/video-processing/pqAmazon/asin.txt') as f:
        if asin in f.read():
            print("true")
            processed_counter += 1
            processed_flag = True
        else:
            processed_flag = False
            print("new video")
        print("processed_counter: ", processed_counter)
        if filename.endswith('.txt') and processed_flag != True:
            # print(filename)

            img_folder_path = filename.split('.txt')[0]
            print(img_folder_path)
            img_count = len(glob.glob(img_folder_path + "/*.jpg"))

            if img_count == 0:
                null_counter += 1
                continue
            else:
                for img_file in glob.glob(img_folder_path + "/*.jpg"):
                    # img = cv2.imread(img_file)
                    base_name = img_file.split('/')[-1]
                    target_width = 1920
                    target_height = 1080

                    im = Image.open(img_file)
                    result = resize_with_pad(im, target_width, target_height)
                    if img_count == 1:
                        mirror_img = ImageOps.mirror(result)
                        mirror_img.save(tmp_img_dir + "100.jpg")
                        transpose_img = ImageOps.exif_transpose(result)
                        transpose_img.save(tmp_img_dir + "200.jpg")
                    elif img_count == 2:
                        mirror_img = ImageOps.mirror(result)
                        result.save(tmp_img_dir + base_name)
                        mirror_img.save(tmp_img_dir + "100.jpg")
                    else:
                        result.save(tmp_img_dir + base_name)
                    # pix = np.array(result)
                    # pix = pix[:, :, ::-1]
                    # frame_array.extend(repeat(pix, 150))
                # audio_background = None
                path_mp3_google = mp3_root_dir + asin + '.mp3'
                audio_background = mpe.AudioFileClip('welcome.mp3')
                # bg_music = mpe.AudioFileClip(bg_music_path)
                if os.path.exists(path_mp3_google):
                    audio_background = mpe.AudioFileClip(path_mp3_google)
                    print("duration audio_background", audio_background.duration)
                else:
                    with open(filename, 'r', encoding='UTF-8') as file:
                        txt_data = file.read().replace('\n', '')
                    # Language in which you want to convert
                    language = 'en-US'
                    # Passing the text and language to the engine,
                    # here we have marked slow=False. Which tells
                    # the module that the converted audio should
                    # have a high speed
                    myobj = gTTS(text=txt_data, lang=language, slow=False, tld="cn")

                    # Saving the converted audio in a mp3 file named
                    # welcome
                    print("type audio", type(myobj))
                    myobj.save('welcome.mp3')
                    time.sleep(1)
                    audio_background = mpe.AudioFileClip('welcome.mp3')
                lenth_audio = audio_background.duration

                FPS = 30
                file_list = glob.glob(tmp_img_dir + "*.jpg")  # Get all the pngs in the current directory
                real_img_count = len(glob.glob(tmp_img_dir + "*.jpg"))
                file_list_sorted = natsorted(file_list, reverse=False)  # Sort the images

                clips = [ImageClip(m).set_duration(3)
                         for m in file_list_sorted]
                clips = clips * int((lenth_audio / (3 * real_img_count)) + 1)

                final_audio = mpe.CompositeAudioClip([audio_background])
                # frame_array.append(np_img0 * 2)
                concat_clip = concatenate_videoclips(clips, method="compose")

                my_clip = concat_clip
                # print("type audio_background", type(audio_background))
                # final_audio = mpe.CompositeAudioClip([audio_background, bg_music])
                # final_clip = CompositeVideoClip([my_clip, subtitles.set_position(('center', 'bottom'))])
                final_clip = my_clip.set_audio(final_audio)
                path_f_video = pathVideoOut + "/" + filename.split('.txt')[0].split("/")[-1] + '.mp4'
                final_clip.write_videofile(path_f_video, bitrate='5000k',
                                           fps=30, audio_bitrate='3000k',
                                           threads=4)
                time.sleep(2)
                os.system("rm -rf " + tmp_img_dir + "*.jpg")
                # time.sleep(1)
                v_len = video_to_frames(path_f_video)
                if v_len == 0:
                    null_video_counter += 1
                    # delete file forever
                    os.system("rm -rf " + path_f_video)
                # os.system("rm -rf " + pathVideoOut + "/" + filename.split('.txt')[0].split("/")[-1] + '_v.mp4')
                counter += 1
                print("process: ", counter)

        else:
            # print(filename)
            pass

print("counter: ", counter)
print("null file counter: ", null_counter)
print("processed_counter: ", processed_counter)
print("null_video_counter: ", null_video_counter)
