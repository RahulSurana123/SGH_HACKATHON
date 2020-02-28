#!/usr/bin/python3
#coding=utf-8

import cv2
import os
from PIL import Image
import pytesseract
import time
import numpy as np
from datetime import datetime
import cherrypy


def detectPlateRough(image_gray,resize_h = 720,en_scale =1.08 ,top_bottom_padding_rate = 0.05):
        global watch_cascade
        if top_bottom_padding_rate>0.2:
            print("error:top_bottom_padding_rate > 0.2:",top_bottom_padding_rate)
            exit(1)
        height = image_gray.shape[0]
        padding = int(height*top_bottom_padding_rate)
        scale = image_gray.shape[1]/float(image_gray.shape[0])
        image = cv2.resize(image_gray, (int(scale*resize_h), resize_h))
        image_color_cropped = image[padding:resize_h-padding,0:image_gray.shape[1]]
        image_gray = cv2.cvtColor(image_color_cropped,cv2.COLOR_RGB2GRAY)
        watches = watch_cascade.detectMultiScale(image_gray, en_scale, 2, minSize=(36, 9),maxSize=(36*40, 9*40))
        cropped_images = []
        for (x, y, w, h) in watches:

            #cv2.rectangle(image_color_cropped, (x, y), (x + w, y + h), (0, 0, 255), 1)

            x -= w * 0.14
            w += w * 0.28
            y -= h * 0.15
            h += h * 0.3

            #cv2.rectangle(image_color_cropped, (int(x), int(y)), (int(x + w), int(y + h)), (0, 0, 255), 1)

            cropped = cropImage(image_color_cropped, (int(x), int(y), int(w), int(h)))
            cropped_images.append([cropped,[x, y+padding, w, h]])
            # cv2.imshow("imageShow", cropped)
            # cv2.waitKey(0)
            # time.sleep(3)
        return cropped_images

def cropImage(image,rect):
        # cv2.imshow("imageShow", image)
        cv2.waitKey(0)
        x, y, w, h = computeSafeRegion(image.shape,rect)
        cv2.imwrite(os.getcwd()+"yo.png", image[y:y+h,x:x+w])
        # print(pytesseract.image_to_string(image[y:y+h,x:x+w]))
        cv2.waitKey(0)
        return image[y:y+h,x:x+w]


def computeSafeRegion(shape,bounding_rect):
        top = bounding_rect[1] # y
        bottom  = bounding_rect[1] + bounding_rect[3] # y +  h
        left = bounding_rect[0] # x
        right =   bounding_rect[0] + bounding_rect[2] # x +  w
        min_top = 0
        max_bottom = shape[0]
        min_left = 0
        max_right = shape[1]

        #print(left,top,right,bottom)
        #print(max_bottom,max_right)

        if top < min_top:
            top = min_top
        if left < min_left:
            left = min_left
        if bottom > max_bottom:
            bottom = max_bottom
        if right > max_right:
            right = max_right
        return [left,top,right-left,bottom-top]
timer={}
class license_plate(object):
    def __init__(self):
        global watch_cascade
        watch_cascade = cv2.CascadeClassifier('cascade.xml')


    @cherrypy.expose()
    def detect_enter(self,im_no):
        imstr = os.getcwd() + "\\"+im_no + ".jpg"
        print(imstr)
        image = cv2.imread(imstr)
        print("yo")
        images = detectPlateRough(image, image.shape[0], top_bottom_padding_rate=0.1)
        img = cv2.imread(os.getcwd()+"yo.png", cv2.IMREAD_COLOR)
        car_no=pytesseract.image_to_string(img)
        print(car_no)
        timer.update({car_no:time.time()})
        print(datetime.now())
        return {str(car_no):"success",str(datetime.now()):"ok"}

    @cherrypy.expose()
    def detect_exit(self,im_no):
        imstr = os.getcwd() + "\\" + im_no + ".jpg"
        print(imstr)
        image = cv2.imread(imstr)
        print("yo")
        images = detectPlateRough(image, image.shape[0], top_bottom_padding_rate=0.1)
        img = cv2.imread(os.getcwd() + "yo.png", cv2.IMREAD_COLOR)
        car_no = pytesseract.image_to_string(img)
        print(car_no)
        duration=time.time()-timer[car_no]
        print(duration)
        return {str(car_no): "success", str(duration) :"ok"}
cherrypy.server.socket_host='0.0.0.0'
cherrypy.config.update({'server.socket_port':8080})
cherrypy.quickstart(license_plate())




# array = np.array(images)
# print(array)

# img=Image.fromarray(array)

# cv2.imwrite(r"C:\Users\HP\Desktop\SGH_HACKATHON\trial.png",images)
# config = ('-l eng --oem 1 --psm 3')

# cv2.imshow("./plate.png",images)
# custom_config = r'--oem 3 --psm 6'
