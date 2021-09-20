"""
Name: Dam Tuan Minh
Class: INT3404 20
MSSV: 18020889
You should understand the code you write.
"""
import numpy as np
import cv2


def q_0(input_file, output_file, delay=1):
    """
    :param input_file:
    :param output_file:
    :param delay:
    :return:
    """
    img = cv2.imread(input_file, cv2.IMREAD_COLOR)
    cv2.imshow('Test img', img)
    # cv2.waitKey: display an Image for specific time
    cv2.waitKey(delay)

    cv2.imwrite(output_file, img)


def q_1(input_file):
    # read the image
    # imread() decodes the image into a matrix with the color channels stored in the order of Blue, Green, Red
    img = cv2.imread(input_file)
    print(img.shape)
    # convert BGR to YCbCr
    imgYCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    # cv2.imshow(imgYCC)
    # cv2.waitKey(5000)
    average = imgYCC.mean(axis=(0, 1))
    print(average)
    #convert YCbCr to RGB
    imgRGB = cv2.cvtColor(imgYCC, cv2.COLOR_YCrCb2RGB)
    # cv2.imshow(imgRGB)
    # cv2.waitKey(5000)
    average = imgRGB.mean(axis=(0, 1))
    print(average)


def q_2(input_file, clear_output_file, blurred_output_file):
    img = cv2.imread(input_file)
    blurred_apple = img[37:127, 87:177]
    cv2.imwrite(blurred_output_file, blurred_apple)
    clear_apple = img[296:475, 362:541]
    cv2.imwrite(clear_output_file, clear_apple)

def q_3(input_file)
    img = cv2.imread(input_file)


if __name__ == "__main__":
    q_0('apple.png', 'test_apple.png', 1000)
    q_1('chromatic_aberration.png')
    q_2('apple.png', 'clear_apple.png', 'blurred_apple.png')