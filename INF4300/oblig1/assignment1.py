import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage.feature as skif
import skimage as ski
from matplotlib import animation
import sys
from numpy import pi
from numba import jit
from funcs import *
#import seaborn
plot1=False
plot2=False

img0 = cv2.imread('mosaic1.png',0)
img1 = cv2.imread('mosaic2.png',0)
#img1 = cv2.imread('zebra_3.tif',0)
img0shape=img0.shape
img1shape=img1.shape



#splitting the images
#assuming that the image is L/2 in with and height
subimg00=img0[0:256 , 0:256 ]
subimg01=img0[0:256 , 256:512 ]
subimg02=img0[256:512 , 0:256 ]
subimg03=img0[256:512 , 256:512 ]
subimg10=img1[0:256 , 0:256 ]
subimg11=img1[0:256 , 256:512 ]
subimg12=img1[256:512 , 0:256 ]
subimg13=img1[256:512 , 256:512 ]
original_img=[subimg00,subimg01,subimg02,subimg03,subimg10,subimg11,subimg12,subimg13,img0,img1]
#original_img is now on the sape over


#from this point, every transformation will be in lists:
"""
element in list is described under
 img0        img1      img0     img1
|---|---| |---|---| |-------| |-------|
| 0 | 1 | | 4 | 5 | |       | |       |
|---|---| |---|---| |   8   | |   9   |
| 2 | 3 | | 6 | 7 | |       | |       |
|---|---| |---|---| |-------| |-------|


"""






###################
######PART 1#######
###################

def oppg1():
    if plot1:
        plt.subplot(121),plt.imshow(img0,cmap = 'gray')
        plt.title('Original Image1'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img1,cmap = 'gray')
        plt.title('Original Image2'), plt.xticks([]), plt.yticks([])
        plt.show()
    for i in enumerate(original_img):
        plt.imshow(i[1],cmap='gray')
        a="%s"%(i[0])
        plt.title(a,)
        plt.savefig('report/%s.png'%(i[0]))
        plt.clf()
    
        plt.imshow(ski.feature.canny(i[1]),cmap='gray')
        a="canny%s"%(i[0])
        plt.title(a,)
        plt.savefig('report/canny%s.png'%(i[0]))
        plt.clf()
    
        plt.hist(i[1].ravel(), bins=256, histtype='step', color='black') 
        a="hist%s"%(i[0])
        plt.title(a,)
        plt.savefig('report/hist%s.png'%(i[0]))
        plt.clf()
      
       
    
    


###################
######PART 2#######
###################

def oppg2():
    glcm_img=[]
    
    
    #image 0 as described in the report
    equalized0=cv2.equalizeHist(original_img[0])
    equalized0=(ski.exposure.rescale_intensity(equalized0, out_range=(0, 15)))
    
    #as mentioned, the holes are ~7px and the angle is 3pi/4
    glcm_img.append(GLCM(equalized0, [9], [2.8*pi/4,3.2*pi/4],normed1=False))
    
    plt.title("GLCM at 2.8*pi/4 and 3.2pi/4 rads")
    plt.subplot(121)
    plt.imshow(glcm_img[0][:,:,0,0])
    plt.colorbar()
    plt.subplot(122)
    plt.imshow(glcm_img[0][:,:,0,1])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG0.jpg")
    plt.clf()
    
    
    
    #image 1 as described in the report
    equalized1=cv2.equalizeHist(original_img[1])
    equalized1=(ski.exposure.rescale_intensity(equalized1, out_range=(0, 15)))
    
    glcm_img.append(GLCM(equalized1, [7], [0,pi/3],normed1=False))
    
    plt.title("GLCM at 0 and pi/2 rads")
    plt.subplot(121)
    plt.imshow(glcm_img[1][:,:,0,0])
    plt.colorbar()
    plt.subplot(122)
    plt.imshow(glcm_img[1][:,:,0,1])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG1.jpg")
    plt.clf()
    
    
    
    
    
    
    #image 2 as described in the report
    equalized2=cv2.equalizeHist(original_img[2])
    equalized2=(ski.exposure.rescale_intensity(equalized2, out_range=(0, 15)))
    
    glcm_img.append(GLCM(equalized2, [20], [3.59,1.919],normed1=False))
    
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.subplot(121)
    plt.imshow(glcm_img[2][:,:,0,0])
    plt.colorbar()
    plt.subplot(122)
    plt.imshow(glcm_img[2][:,:,0,1])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG2.jpg")
    plt.clf()
    
    
    
    
    
    
    
    #image 2 as described in the report
    equalized3=cv2.equalizeHist(original_img[3])
    equalized3=(ski.exposure.rescale_intensity(equalized3, out_range=(0, 15)))
    
    glcm_img.append(GLCM(equalized3, [20], [3.59,1.919],normed1=False))
    
    plt.subplot(121)
    plt.imshow(glcm_img[3][:,:,0,0])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.subplot(122)
    plt.imshow(glcm_img[3][:,:,0,1])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.savefig("report/GCLM_IMG3.jpg")
    plt.clf()
    
    
    
    
    #image 2 as described in the report
    equalized4=cv2.equalizeHist(original_img[4])
    equalized4=(ski.exposure.rescale_intensity(equalized4, out_range=(0, 15)))
    
    glcm_img.append(GLCM(equalized4, [20], [3.59,1.919],normed1=False))
    
    plt.subplot(121)
    plt.imshow(glcm_img[4][:,:,0,0])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.subplot(122)
    plt.imshow(glcm_img[4][:,:,0,1])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.savefig("report/GCLM_IMG4.jpg")
    plt.clf()
    
    
    #image 2 as described in the report
    equalized5=cv2.equalizeHist(original_img[5])
    equalized5=(ski.exposure.rescale_intensity(equalized5, out_range=(0, 15)))
    
    glcm_img.append(GLCM(equalized5, [20], [3.59,1.919],normed1=False))
    
    plt.subplot(121)
    plt.imshow(glcm_img[5][:,:,0,0])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.subplot(122)
    plt.imshow(glcm_img[5][:,:,0,1])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.savefig("report/GCLM_IMG5.jpg")
    plt.clf()
    
    
    #image 2 as described in the report
    equalized6=cv2.equalizeHist(original_img[6])
    equalized6=(ski.exposure.rescale_intensity(equalized6, out_range=(0, 15)))
    
    glcm_img.append(GLCM(equalized6, [20], [3.59,1.919],normed1=False))
    
    plt.subplot(121)
    plt.imshow(glcm_img[6][:,:,0,0])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.subplot(122)
    plt.imshow(glcm_img[6][:,:,0,1])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.savefig("report/GCLM_IMG6.jpg")
    plt.clf()
    
    
    #image 2 as described in the report
    equalized7=cv2.equalizeHist(original_img[7])
    equalized7=(ski.exposure.rescale_intensity(equalized7, out_range=(0, 15)))
    
    glcm_img.append(GLCM(equalized7, [20], [3.59,1.919],normed1=False))
    
    plt.subplot(121)
    plt.imshow(glcm_img[7][:,:,0,0])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.subplot(122)
    plt.imshow(glcm_img[7][:,:,0,1])
    plt.colorbar()
    plt.title("GLCM at 0 and 1.2pi/2 rads")
    plt.savefig("report/GCLM_IMG7.jpg")
    plt.clf()
    


###################
######PART 3#######
###################

def oppg3():
    inertia_attr=[5,5]#[5,5,5,5,5,5,5,5,5,5,5]
    homogenity_attr=[5,5]#[5,5,5,5,5,5,5,5,5]
    cluster_shade_attr=[5,5]#[5,5,5,5,5,5,5,5,5,5]
    inertia_img,homogenity_img,cluster_shade_img=save_features(original_img[-1], inertia_attr, homogenity_attr, 
                 cluster_shade_attr)

    return inertia_img,homogenity_img,cluster_shade_img
###################
######PART 4#######
###################

def oppg4():
    ski.filters.try_all_threshold(inertia_img[9],figsize=(19,19),verbose=False)
    plt.savefig("report/try_all_thr9")
    plt.show()
    ski.filters.try_all_threshold(inertia_img[8],figsize=(19,19),verbose=False)
    plt.savefig("report/try_all_thr8")
    plt.show()

    #applying global threshold
    
    #fist image has a good result with almost all the global theshold algortihms: using OTSU
    tresh=ski.filters.threshold_otsu(inertia_img)
    img=inertia_img<=tresh 
    
    plt.imshow(img)
    plt.title("Standard  Otsu on inertia_img_0")
    plt.show()
    
    
    
inertia_img,homogenity_img,cluster_shade_img=oppg3()   
oppg4()