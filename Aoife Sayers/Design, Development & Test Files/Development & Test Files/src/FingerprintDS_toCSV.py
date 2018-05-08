'''
' Title: Dataset to CSV file
' Author: Aoife Sayers
' Date: 2018
' Code Version: 6
' This script generates a csv file of the dataset for further analysis
'''

import os
import pandas as pd
genders = []
fingerprintTypes = []

genderList = []
fingerprintList = []
txtFileList = []
imgFileList = []

dir = "../NISTSpecialDatabase4GrayScaleImagesofFIGS/NISTSpecialDatabase4GrayScaleImagesofFIGS/sd04/png_txt/"
for filename in os.listdir(dir):
        if filename.endswith(".txt"):
            op = dir + filename
            file = open(op)
            lines = file.readlines()
            #Gender
            genderLine = lines[0]
            genderLine = genderLine.strip('\n')
            heading, gender = genderLine.split(': ')
            genderList.append((gender))
            #Fingerprint Class
            fingerClassLine = lines[1]
            fingerClassLine = fingerClassLine.strip('\n')
            heading, fingerprintType = fingerClassLine.split(': ')
            fingerprintList.append((fingerprintType))
            #TextFile and pngs
            txtFileList.append((filename))
            file, ext = filename.split('.')
            imgFileList.append(file+'.png')


df = pd.DataFrame(list(zip(genderList, fingerprintList, txtFileList, imgFileList)),
              columns=['Gender','FingerprintType','TextFiles','ImageFiles'])

df.to_csv('../Fingerprint.csv', sep=',', encoding='utf-8')