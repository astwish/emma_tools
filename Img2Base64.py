#!/usr/bin/env python
# -*- coding: utf-8 -*-


#__from__ = 'EMMATools https://github.com/crisschan/EMMATools'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__mtime__ = '20160908'
#__instruction__=' 将图片变成base64编码，然后在web中打开，不用引入图片外部图片文件'





import base64
import os

class Img2Base64(object):
    '''
    将图片变成base64编码，然后在web中打开，不用引入图片外部图片文件
    '''
    def __init__(self,sImgDir):
        fr = open(sImgDir, 'rb')
        self.__hexImg=base64.b64encode(fr.read())
        fr.close()
    @property
    def HexImg(self):
        return self.__hexImg.decode()


if __name__=='__main__':
    img =Img2Base64('WechatIMG7.png')

    print('data:image/bmp;base64,'+img.HexImg)


