import os
from tkinter import PhotoImage

dir_path = os.path.dirname(os.path.realpath(__file__))

from PIL import Image, ImageFont, ImageDraw, ImageOps
import datetime

nameOfFriend=input("Enter the Name of the Friend :")
nameOfFriend = nameOfFriend.title()

bdayOfFriend=input("Enter the date of Birth(dd) :")
bdayOfFriend=f'{bdayOfFriend}.{input("Enter the month of Birth(mm) :")}'
year = datetime.date.today().year
bdayOfFriend = f'{bdayOfFriend}.{year}'

isCircle = input("Do you need Circle-crop (y?N) :").upper()

myImage = Image.open(f'{dir_path}/template.png')
W,H = myImage.size

nameOfFriendFont = ImageFont.truetype(f'{dir_path}/segoesc.ttf',42)
bdayOfFriendFont = ImageFont.truetype(f'{dir_path}/segoepr_0.ttf',32)

image_editable = ImageDraw.Draw(myImage)
# name
image_editable.text((101,330),nameOfFriend,(255,255,255),nameOfFriendFont)
# date
image_editable.text((667,452),bdayOfFriend,(255,255,255),bdayOfFriendFont)

# PhotoOfFriend
maskSize=(230,230)
mask = Image.new('L',maskSize,0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0,0)+maskSize,fill=255)

fileOfPhoto = os.listdir(f'{dir_path}/Photo of Friend/')
if(fileOfPhoto.__len__() > 1):
    print('Try Again!')
    print("please leave only 1 photo in 'Photos of Friend' folder...")
    exit()

photoOfFriend = Image.open(f'{dir_path}/Photo of Friend/{fileOfPhoto[0]}')
photoOfFriend = photoOfFriend.convert("RGBA")
croppedPhoto = ImageOps.fit(photoOfFriend, mask.size, centering=(0.5,0.5))

if(isCircle =="Y"):
    croppedPhoto.putalpha(mask)

croppedPhoto = croppedPhoto.convert("RGBA")



myImage = myImage.convert("RGBA")
myImage.paste(croppedPhoto,(570,75), croppedPhoto)



myImage.save(f'{dir_path}/Created Images/{nameOfFriend} {year} B day.png')

print("Image Created")

exit()