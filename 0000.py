#-*- coding:utf8 -*-

'''
  sudo apt-get update
  sudo apt-get install python-dev
  sudo apt-get install libtiff5-dev
  libjpeg8-dev zlib1g-dev
  libfreetype6-dev liblcms2-dev libwebp-dev
  tcl8.6-dev tk8.6-dev python-tk

  sudo pip3 install pillow

'''
# 把右上角图变成小图

infile="you.jpg"
outfile="you"

size=(80,80)

small_img=Image.open(infile)
small_img.thumbnail(size)
small_img.save(outfile,"JPEG")

region=Image.open(outfile).copy()
boxs=(img.size[0]-80,0,img.size[0],80)

img.paste(region,boxs)
img.save("you&me","JPEG")

参考 http://www.cnblogs.com/apexchu/p/4231041.html

