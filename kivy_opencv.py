# -*- coding: utf-8 -*

import numpy as np
import cv2

from PIL import Image

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle

class MyApp(App):
        title = "opencv on kivy"

        def build(self):
            img = cv2.imread('kai_058Kazukiya17103_TP_V.jpg',1)

            # 画像をグレイスケールに変換
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


            #cv2.imshow('opencv_normal', img)
            cv2.imshow('opencv_gray', gray_img)

            if img is None:
                print('load image')
                sys.exit(1)


            widget = Widget()

            ''' pattern1 (openCVの機能で表示)  '''
            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # openCVの色の並びはBGRなのでRGBに直す
            img2 = cv2.flip(img2, 0)    # Kivyの座標の原点は左下なので上下反転する
            
            # OpenCVの座標shapeは「高さ」、「幅」、「チャンネル」の順番 Kivyのsizeは(幅、高さ)なので逆にする必要がある
            #texture = Texture.create(size=(img2.shape[1], img2.shape[0]))
            #texture.blit_buffer(img2.tostring())

            #with widget.canvas: # 描画
            #    Rectangle(texture=texture ,pos=(0, 0), size=(img2.shape[1], img2.shape[0]))

            
            ''' pattern2 (kivyの機能のみで表示)  '''
            
            #texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr', bufferfmt='ubyte') # BGRモードで用意,ubyteはデフォルト引数なので指定なくてもよい
            #texture.blit_buffer(img.tostring(),colorfmt='bgr', bufferfmt='ubyte')  # ★ここもBGRで指定しないとRGBになって色の表示がおかしくなる
            #texture.flip_vertical()    # 画像を上下反転させる
            

            #with widget.canvas:
            #    Rectangle(texture=texture ,pos=(0, 0), size=(img.shape[1], img.shape[0]))
  
            ''' pattern3(モノクロ)  '''
            texture = Texture.create(size=(gray_img.shape[1], gray_img.shape[0]), colorfmt='bgr', bufferfmt='ubyte') # BGRモードで用意,ubyteはデフォルト引数なので指定なくてもよい

            gray_to_rgb_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)    # bilt_bufferでは1チェンネルのグレイ画像は表示できないので３チャンネルの画像に変換する

            texture.blit_buffer(gray_to_rgb_img.tostring(),colorfmt='bgr', bufferfmt='ubyte')  # ★ここもBGRで指定しないとRGBになって色の表示がおかしくなる
            texture.flip_vertical()    # 

            with widget.canvas:
                Rectangle(texture=texture ,pos=(0, 0), size=(gray_img.shape[1], gray_img.shape[0]))


            ''' Pillowで画像を表示する '''

            #pillow_img = Image.open('kai_058Kazukiya17103_TP_V.jpg', 'r')
            #texture = Texture.create(size=pillow_img.size) 
            
            #texture.blit_buffer(pillow_img.tobytes())

            #texture.flip_vertical()    # 
            #with widget.canvas:
            #    Rectangle(texture=texture ,pos=(0, 0), size=(gray_img.shape[1], gray_img.shape[0]))

            return widget

if __name__ == '__main__':
    MyApp().run()
