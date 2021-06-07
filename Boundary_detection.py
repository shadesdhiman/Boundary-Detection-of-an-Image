# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:57:05 2021

@author: Dhiman
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
org_img = cv2.imread("Sample_1.png")


def No_of_cc(org_img,v_min,v_max,adj):

    gray_img = cv2.cvtColor(org_img,cv2.COLOR_BGR2GRAY)
    
    cc = 0
    n = 0
    
    map_dict = dict(())
    smart_label = dict(())
    def Rand():
        nonlocal cc
        cc = cc+1
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        bgr = [b,g,r]
        return bgr
    
    
    
    def next_num():
        nonlocal n
        nonlocal smart_label
        n = n+1
        smart_label[n] = n
        return n
    
    def bb(demo_img):
        loc = []
        for i in range(1,511):
            for j in range(1,511):
                if(demo_img[i][j]==255):
                    if(demo_img[i-1][j] ==255 and demo_img[i][j-1]==255 and demo_img[i+1][j]==255 and demo_img[i][j+1]==255):
                        loc.append((i,j))
                    else:
                        pass
        for i in range(len(loc)):
            demo_img[loc[i][0]][loc[i][1]] = 0
        return demo_img
    
      
    label = np.zeros((org_img.shape[0],org_img.shape[1]))
    
    def convert(gray_img):
        
        empty_img = np.zeros((org_img.shape[0],org_img.shape[1])) 
        for i in range(511):
            for j in range(511):
                if(gray_img[i][j]>=v_min and gray_img[i][j]<=v_max ):
                    empty_img[i][j] = 255
                else:
                    empty_img[i][j] = 0
        return empty_img.astype('uint8')
    
    
    

                    
                    
    
    
                
    empty_img = convert(gray_img)
    empty_img = bb(empty_img) 
    

           
                   
    """
    print(smart_label)
    print(map_dict)
    print(color_list)  
     """   
            


    cv2.imwrite("Result_1.jpg", empty_img)
    cv2.imshow("Final Image",empty_img)
    
    print("The number of connected component is =>",cc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

v_min = int(input("v_min : "))
v_max = int(input("v_max : "))
adj = int(input("Enter the adjacency : "))

No_of_cc(org_img,v_min,v_max,adj)