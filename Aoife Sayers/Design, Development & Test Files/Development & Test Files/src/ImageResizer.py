'''
' Title: Resize all Images in a Folder, lines 13-18
' Author: user3237883 - StackOverflow.com
' Date: 2014
' Code Version: Feb 3 '14 
' Availability: https://stackoverflow.com/questions/21517879/python-pil-resize-all-images-in-a-folder (Accessed March 3rd 2018)
' Modified: line 16,19,20
'''

from PIL import Image
import os, sys


def resizeImages(dirPath):
    for imgFile in os.listdir(dirPath):
        print(imgFile)
        im = Image.open(dirPath + imgFile)
        imResize = im.resize((32,32), Image.ANTIALIAS)
        imResize.save(dirPath + imgFile, 'PNG', quality=90)

resizeImages('../fingerprintsdataset/train/loop/')
resizeImages('../fingerprintsdataset/train/whorl/')
resizeImages('../fingerprintsdataset/train/arch/')
resizeImages('../fingerprintsdataset/train/rightArch/')
resizeImages('../fingerprintsdataset/train/tentedArch/')

resizeImages('../fingerprintsdataset/test/loop/')
resizeImages('../fingerprintsdataset/test/whorl/')
resizeImages('../fingerprintsdataset/test/arch/')
resizeImages('../fingerprintsdataset/test/rightArch/')
resizeImages('../fingerprintsdataset/test/tentedArch/')