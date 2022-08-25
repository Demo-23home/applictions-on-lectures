from turtle import width
from PIL import Image
import os  

path='D:\My Photos\old photos\images'
fit_size=int(input('enter size'))
output_folder=input('enter output folder name')

if not os.path.exists('output_folder'):
    os.mkdir("output_folder")

for file_name in os.listdir():
    if not file_name in ['.jpg', '.mp4', '.PNG', '.JPG', '.jpeg']:
        continue
    image=Image.open(file_name)
    width,height=image.size
    if width>fit_size and height >fit_size:
        if width >height:
            height=int((fit_size/width)*height)
            width=fit_size
        elif height>width:
            width=int((fit_size/height)*width)
            height=fit_size
