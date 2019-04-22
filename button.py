# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:56:06 2019

@author: kyeoj
"""

import data_preprocess
import train_main
import os,sys,time
os.chdir(os.path.dirname(__file__))
from tkinter import *
import tkinter as tk

def button():
    button_flag = [1,1,1,1,1,1]

    data_preprocess.image_preprocess('./train_img/Sunny Deol')

    def click1():    
        """
        respond to the button1 click
        """
        # toggle button colors as a test
        if button_flag[1]:
            button1.config(bg="white")
            button_flag[1] = 0
            data_preprocess.image_preprocess('./train_img/Akshay Kumar')
            train_main.image_train('./pre_img/Akshay Kumar:./pre_img/Sunny Deol')
            
        else:
            button1.config(bg="green")
            button_flag[1] = 1
    def click2():
        """
        respond to the button2 click
        """
        # toggle button colors as a test
        if button_flag[2]:
            button2.config(bg="white")
            button_flag[2] = 0
            data_preprocess.image_preprocess('./train_img/Nawazuddin Siddiqui')
            train_main.image_train('./pre_img/Nawazuddin Siddiqui:./pre_img/Sunny Deol')
                        
        else:
            button2.config(bg="green")
            button_flag[2] = 1
    def click3():
        """
        respond to the button3 click
        """
        # toggle button colors as a test
        if button_flag[3]:
            button3.config(bg="white")
            button_flag[3] = 0
            data_preprocess.image_preprocess('./train_img/Salman Khan')
            train_main.image_train('./pre_img/Salman Khan:./pre_img/Sunny Deol')
        
        else:
            button3.config(bg="green")
            button_flag[3] = 1    
   
    def click4():
        """
        respond to the button4 click
        """    
        # toggle button colors as a test
        if button_flag[4]:
            button4.config(bg="white")
            button_flag[4] = 0
            data_preprocess.image_preprocess('./train_img/Shahrukh Khan')
            train_main.image_train('./pre_img/Shahrukh Khan:./pre_img/Sunny Deol')
        
        else:
            button4.config(bg="green")
            button_flag[4] = 1
            
    def click5():
        """
        respond to the button5 click
        """    
        # toggle button colors as a test
        if button_flag[5]:
            button5.config(bg="white")
            button_flag[5] = 0
            data_preprocess.image_preprocess('./train_img/Sunil Shetty')
            train_main.image_train('./pre_img/Sunil Shetty:./pre_img/Sunny Deol')
            
        else:
            button5.config(bg="green")
            button_flag[5] = 1
        
        
    root = tk.Tk()
    # create a frame and pack it
    frame1 = tk.Frame(root)
    frame1.pack(side=tk.TOP, fill=tk.X)
    
    # pick a (small) image file you have in the working directory ...
    filename1 = "C:/Users/kyeoj/project/Facenet-Real-time-Tensorflow/train_img/button_image/Akshay.gif"
    photo1 = tk.PhotoImage(file=filename1)
    # create the image button, image is above (top) the optional text
    button1 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo1,
                        text="optional text", bg='green', command=click1)
    button1.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button1.image = photo1

    filename2= "C:/Users/kyeoj/project/Facenet-Real-time-Tensorflow/train_img/button_image/Nawazuddin.gif"
    photo2 = tk.PhotoImage(file=filename2)
    # create the image button, image is above (top) the optional text
    button2 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo2,
                        text="optional text", bg='green', command=click2)
    button2.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button2.image = photo2

    filename3= "C:/Users/kyeoj/project/Facenet-Real-time-Tensorflow/train_img/button_image/Salman.gif"
    photo3 = tk.PhotoImage(file=filename3)
    # create the image button, image is above (top) the optional text
    button3 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo3,
                        text="optional text", bg='green', command=click3)
    button3.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button3.image = photo3
    
    filename4= "C:/Users/kyeoj/project/Facenet-Real-time-Tensorflow/train_img/button_image/Shahrukh.gif"
    photo4 = tk.PhotoImage(file=filename4)
    # create the image button, image is above (top) the optional text
    button4 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo4,
                        text="optional text", bg='green', command=click4)
    button4.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button4.image = photo4

    filename5= "C:/Users/kyeoj/project/Facenet-Real-time-Tensorflow/train_img/button_image/Sunil.gif"
    photo5 = tk.PhotoImage(file=filename5)
    # create the image button, image is above (top) the optional text
    button5 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo5,
                        text="optional text", bg='green', command=click5)
    button5.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button5.image = photo5
    # start the event loop
    root.mainloop()

