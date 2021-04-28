# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 上午9:10
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : get_all_frames.py
# @Software: PyCharm
import cv2
import time
import os
import numpy as np


# from PIL import Image, ImageDraw, ImageFilter

# from util.noise import sp_noise


def video_to_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc, 0)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)
    count = 0
    print("Converting video..\n")
    path_image2 = "/home/luolu/PycharmProjects/video-processing/match_images/advn.png"
    image2 = cv2.imread(path_image2)
    # path_image3 = "/home/luolu/PycharmProjects/video-processing/match_images/noise02.png"
    # image3 = cv2.imread(path_image3)
    # image2 = Image.open(path_image2)
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # combine two images
        # frame = combine_two_color_images(frame, image2)
        # frame = cv2.add(frame, image2)
        # frame = cv2.bitwise_or(frame, image2)
        # paste
        # im_pil = Image.fromarray(frame)
        # image2.paste(im_pil)

        # add noise
        # frame = frame + sp_noise(frame, 0.9)

        # >150 add
        if count < 5:
            cv2.imwrite(output_loc + "/%#05d.png" % (count + 1), frame)
        # if 349 <= count < 600:
        #     frame = cv2.add(frame, image2)
        #     cv2.imwrite(output_loc + "/%#05d.png" % (count + 1), frame)
        # Write the results back to output location.
        # gray image
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # crop
        # x = 237
        # y = 60
        # h = 480
        # w = 540
        # frame = frame[y:y + h, x:x + w]
        # cv2.imwrite(output_loc + "/%#05d.jpg" % (count + 1), frame)

        # image2.save(output_loc + "/%#05d.png" % (count + 1))
        count = count + 1
        # If there are no more frames left
        if count > (video_length - 1):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print("Done extracting frames.\n%d frames extracted" % count)
            print("It took %d seconds forconversion." % (time_end - time_start))
            break


def combine_two_color_images(image1, image2):
    foreground, background = image1.copy(), image2.copy()

    foreground_height = foreground.shape[0]
    foreground_width = foreground.shape[1]
    alpha = 0.5

    # do composite on the upper-left corner of background image.
    blended_portion = cv2.addWeighted(foreground,
                                      alpha,
                                      background[:foreground_height, :foreground_width, :],
                                      1 - alpha,
                                      0,
                                      background)
    background[:foreground_height, :foreground_width, :] = blended_portion
    return background


def merge_image(back, front, x, y):
    # convert to rgba
    if back.shape[2] == 3:
        back = cv2.cvtColor(back, cv2.COLOR_BGR2BGRA)
    if front.shape[2] == 3:
        front = cv2.cvtColor(front, cv2.COLOR_BGR2BGRA)

    # crop the overlay from both images
    bh, bw = back.shape[:2]
    fh, fw = front.shape[:2]
    x1, x2 = max(x, 0), min(x + fw, bw)
    y1, y2 = max(y, 0), min(y + fh, bh)
    front_cropped = front[y1 - y:y2 - y, x1 - x:x2 - x]
    back_cropped = back[y1:y2, x1:x2]

    alpha_front = front_cropped[:, :, 3:4] / 255
    alpha_back = back_cropped[:, :, 3:4] / 255

    # replace an area in result with overlay
    result = back.copy()
    print(
        f'af: {alpha_front.shape}\nab: {alpha_back.shape}\nfront_cropped: {front_cropped.shape}\nback_cropped: {back_cropped.shape}')
    result[y1:y2, x1:x2, :3] = alpha_front * front_cropped[:, :, :3] + alpha_back * back_cropped[:, :, :3]
    result[y1:y2, x1:x2, 3:4] = (alpha_front + alpha_back) / (1 + alpha_front * alpha_back) * 255

    return result


if __name__ == "__main__":
    # Satisfying Relax Every Day With Z ER Spa Video (#2127)
    # Relax Every Day With Dr Z ER Spa Video (#2221) # Relax Every Day With Dr Zhao Video (#cf1043)
    # Relax Every Day With Dr Z ER Spa Video (#2221) # Relax Every Day With Dr Z ER Video (#tf002)
    # Relax Every Day With Dr Z ER Spa Video (#2221) # Relax Every Day With Dr Z ER Video (#yt001)

    # Relax With LLu MC HD #006
    # Relax Every Day With Dr C Er Spa Video (#2041)
    # Satisfying Relax Every Day With Dr C Er Spa Video (#2033)
    input_loc = '/media/luolu/U盘大师U盘/越南狐狸/Año nuevo chino__ vacaciones de belleza SSM201.mp4'
    output_loc = 'out_frames/'
    video_to_frames(input_loc, output_loc)
