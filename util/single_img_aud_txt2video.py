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
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip


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

    image_resize = im.resize((resize_width, resize_height), Image.ADAPTIVE)
    background = Image.new('RGBA', (target_width, target_height), (255, 255, 255, 255))
    offset = (round((target_width - resize_width) / 2), round((target_height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert("RGB")


directory = "C:\\Users\\Administrator\\Desktop\\atest"
pathVideoOut = "D:\\video_sp_amazon"
mp3_root_dir = "/home/luolu/Desktop/mp3Amazon/"
bg_music_path = "D:\\pycharmProjects\\video-processing\\util\\bensound-memories.mp3"
counter = 0
null_counter = 0
null_video_counter = 0
size = (1920, 1080)
blank_image = np.ones((1920, 1080, 3), np.uint8)
# for filename in os.listdir(directory):
for filename in glob.glob(directory + "\\*.txt"):
    if filename.endswith('.txt'):
        # print(filename)
        asin = filename.split('.txt')[0].split("\\")[-1]
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
        # img_folder_path = directory + "/" + filename.split('.txt')[0]
        img_folder_path = filename.split('.txt')[0]
        print(img_folder_path)
        frame_array = []
        frame_array.extend(repeat(blank_image, 50))

        list_size = []
        img_count = len(glob.glob(img_folder_path + "\\*.jpg"))
        img_0_path = img_folder_path + "\\0.jpg"
        np_img0 = cv2.imread(img_0_path)
        if img_count == 0:
            null_counter += 1
            continue
        else:
            for img_file in glob.glob(img_folder_path + "\\*.jpg"):
                img = cv2.imread(img_file)

                target_width = 1920
                target_height = 1080
                #
                im = Image.open(img_file)
                result = resize_with_pad(im, target_width, target_height)
                pix = np.array(result)
                pix = pix[:, :, ::-1]
                # new_im = resize_pad_cv2(img, target_width)
                frame_array.extend(repeat(pix, 150))

            path_mp3_google = mp3_root_dir + asin + '.mp3'
            # audio_background = None
            # if os.path.exists(path_mp3_google):
            #     audio_background = mpe.AudioFileClip(path_mp3_google)
            #     print("duration audio_background", audio_background.duration)
            # else:
            #     audio_background = mpe.AudioFileClip('welcome.mp3')
            audio_background = mpe.AudioFileClip('welcome.mp3')
            bg_music = mpe.AudioFileClip(bg_music_path)

            if img_count < 4:
                for i in range(len(frame_array)):
                    frame_array.append(frame_array[i])
                for i in range(len(frame_array)):
                    frame_array.append(frame_array[i])
            elif 4 <= img_count <= 8:
                for i in range(len(frame_array)):
                    frame_array.append(frame_array[i])
            else:
                frame_array = frame_array
            frame_array.append(np_img0 * 60)
            FPS = 30
            out = cv2.VideoWriter(filename=pathVideoOut + "\\" + filename.split('.txt')[0].split("\\")[-1] + '_v.mp4',
                                  fourcc=cv2.VideoWriter_fourcc(*'mp4v'),
                                  fps=FPS,
                                  isColor=True,
                                  frameSize=size)
            for i in range(len(frame_array)):
                # writing to a image array
                out.write(frame_array[i])
            out.release()
            time.sleep(2)

            print(pathVideoOut + "\\" + filename.split('.txt')[0].split("\\")[-1] + '.mp4')
            my_clip = mpe.VideoFileClip(
                filename=pathVideoOut + "\\" + filename.split('.txt')[0].split("\\")[-1] + '_v.mp4')
            # audio_background = mpe.AudioFileClip('welcome.mp3')
            # print("type audio_background", type(audio_background))
            final_audio = mpe.CompositeAudioClip([audio_background, bg_music])
            # final_clip = CompositeVideoClip([my_clip, subtitles.set_position(('center', 'bottom'))])
            final_clip = my_clip.set_audio(final_audio)
            path_f_video = pathVideoOut + "\\" + filename.split('.txt')[0].split("\\")[-1] + '.mp4'
            final_clip.write_videofile(path_f_video, bitrate='50000k',
                                       fps=FPS, audio_bitrate='3000k',
                                       codec='mpeg4', preset="placebo",
                                       threads=4)
            time.sleep(1)
            v_len = video_to_frames(path_f_video)
            if v_len == 0:
                null_video_counter += 1
                # delete file forever
                os.system("del " + path_f_video)
            os.system("del " + pathVideoOut + "\\" + filename.split('.txt')[0].split("\\")[-1] + '_v.mp4')
            counter += 1
            print("process: ", counter)

    else:
        # print(filename)
        pass

print("counter: ", counter)
print("null file counter: ", null_counter)
print("null_video_counter: ", null_video_counter)
