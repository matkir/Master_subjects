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
    #from the report, we have the angle=3pi/4 and len=4
    #using a small delta on each side 
    ang=[2.8*pi/4,3*pi/4,3.2*pi/4]
    glcm_img.append(GLCM(equalized0, [4], ang ,normed1=True,symmetric1=True))
    
    plt.title("GLCM at 2.8*pi/4 rads")
    plt.imshow(glcm_img[0][:,:,0,0])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_0_0.jpg")
    plt.clf()
    plt.title("GLCM at 3*pi/4 rads")
    plt.imshow(glcm_img[0][:,:,0,1])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_0_1.jpg")
    plt.clf()
    plt.title("GLCM at 3.2*pi/4 rads")
    plt.imshow(glcm_img[0][:,:,0,2])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_0_2.jpg")
    plt.clf()
   
  
   
    #image 1 as described in the report
    equalized1=cv2.equalizeHist(original_img[1])
    equalized1=(ski.exposure.rescale_intensity(equalized0, out_range=(0, 15)))
    #from the report, we have the angle=3pi/4 and len=4
    #using a small delta on each side 
    ang=[0,pi,1.1*pi]
    glcm_img.append(GLCM(equalized0, [4], ang ,normed1=True,symmetric1=True))
    
    plt.title("GLCM at 0 rads")
    plt.imshow(glcm_img[1][:,:,0,0])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_1_0.jpg")
    plt.clf()
    plt.title("GLCM at pi rads")
    plt.imshow(glcm_img[1][:,:,0,1])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_1_1.jpg")
    plt.clf()
    plt.title("GLCM at 1.1*pi rads")
    plt.imshow(glcm_img[1][:,:,0,2])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_1_2.jpg")
    plt.clf()
   
   
   
    
    #image 2 as described in the report
    equalized1=cv2.equalizeHist(original_img[2])
    equalized1=(ski.exposure.rescale_intensity(equalized0, out_range=(0, 15)))
    #from the report, we have the angle=3pi/4 and len=4
    #using a small delta on each side 
    ang=[1.6,1.745,1.8]
    glcm_img.append(GLCM(equalized0, [4], ang ,normed1=True,symmetric1=True))
    
    plt.title("GLCM at 1.6 rads")
    plt.imshow(glcm_img[2][:,:,0,0])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_2_0.jpg")
    plt.clf()
    plt.title("GLCM at 1.745 rads")
    plt.imshow(glcm_img[2][:,:,0,1])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_2_1.jpg")
    plt.clf()
    plt.title("GLCM at 1.8 rads")
    plt.imshow(glcm_img[2][:,:,0,2])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_2_2.jpg")
    plt.clf()
  
    
    
    #image 3 as described in the report
    equalized1=cv2.equalizeHist(original_img[3])
    equalized1=(ski.exposure.rescale_intensity(equalized0, out_range=(0, 15)))
    #from the report, we have the angle=3pi/4 and len=4
    #using a small delta on each side 
    ang=np.linspace(0,2*pi,4)
    length=[2,4,8]
    glcm_img.append(GLCM(equalized0, length, ang ,normed1=True,symmetric1=True))
    
    plt.title("Isometric GLCM with len 2")
    iso=0
    for i in range(len(ang)):
        iso=np.add(glcm_img[3][:,:,0,i], iso)
    
    plt.imshow(np.divide(iso,len(ang)))
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_3_0.jpg")
    plt.clf()
    
    plt.title("Isometric GLCM with len 4")
    iso=0
    for i in range(len(ang)):
        iso=np.add(glcm_img[3][:,:,1,i], iso)
    
    plt.imshow(np.divide(iso,len(ang)))
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_3_1.jpg")
    plt.clf()
    
    plt.title("Isometric GLCM with len 8")
    iso=0
    for i in range(len(ang)):
        iso=np.add(glcm_img[3][:,:,2,i], iso)
    
    plt.imshow(np.divide(iso,len(ang)))
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_3_2.jpg")
    plt.clf()
   
    
     
    
    #image 4 as described in the report
    equalized1=cv2.equalizeHist(original_img[4])
    equalized1=(ski.exposure.rescale_intensity(equalized0, out_range=(0, 15)))
    #from the report, we have the angle=3pi/4 and len=4
    #using a small delta on each side 
    ang=[3*pi/4,pi/4,3.1*pi/4]
    glcm_img.append(GLCM(equalized0, [4], ang ,normed1=True,symmetric1=True))
    
    plt.title("GLCM at 3pi/4 rads")
    plt.imshow(glcm_img[4][:,:,0,0])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_4_0.jpg")
    plt.clf()
    plt.title("GLCM at pi/4 rads")
    plt.imshow(glcm_img[4][:,:,0,1])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_4_1.jpg")
    plt.clf()
    plt.title("GLCM at 3.1pi/4 rads")
    plt.imshow(glcm_img[4][:,:,0,2])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_4_2.jpg")
    plt.clf()
  
      
    
    #image 5 as described in the report
    equalized1=cv2.equalizeHist(original_img[5])
    equalized1=(ski.exposure.rescale_intensity(equalized0, out_range=(0, 15)))
    #from the report, we have the angle=3pi/4 and len=4
    #using a small delta on each side 
    ang=[0,pi]
    glcm_img.append(GLCM(equalized0, [4,12], ang ,normed1=True,symmetric1=True))
    
    plt.title("GLCM at 0 rads and len 4")
    plt.imshow(glcm_img[5][:,:,0,0])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_5_0.jpg")
    plt.clf()
    plt.title("GLCM at pi rads and len 12")
    plt.imshow(glcm_img[5][:,:,1,1])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_5_1.jpg")
    plt.clf()
    plt.title("GLCM at pi rads and len 4")
    plt.imshow(glcm_img[5][:,:,1,1])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_5_2.jpg")
    plt.clf()
  

    
    #image 6 as described in the report
    equalized1=cv2.equalizeHist(original_img[6])
    equalized1=(ski.exposure.rescale_intensity(equalized0, out_range=(0, 15)))
    #from the report, we have the angle=3pi/4 and len=4
    #using a small delta on each side 
    ang=[pi]
    glcm_img.append(GLCM(equalized0, [4,8,12], ang ,normed1=True,symmetric1=True))
    
    plt.title("GLCM at pi rads and len 4")
    plt.imshow(glcm_img[6][:,:,0,0])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_6_0.jpg")
    plt.clf()
    plt.title("GLCM at pi rads and len 8")
    plt.imshow(glcm_img[6][:,:,1,0])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_6_1.jpg")
    plt.clf()
    plt.title("GLCM at pi rads and len 12")
    plt.imshow(glcm_img[6][:,:,2,0])
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_6_2.jpg")
    plt.clf()
  
       
    #image 7 as described in the report
    equalized1=cv2.equalizeHist(original_img[7])
    equalized1=(ski.exposure.rescale_intensity(equalized0, out_range=(0, 15)))
    #from the report, we have the angle=3pi/4 and len=4
    #using a small delta on each side 
    ang=np.linspace(0,2*pi,4)
    length=[3,6,9]
    glcm_img.append(GLCM(equalized0, length, ang ,normed1=True,symmetric1=True))
    
    plt.title("Isometric GLCM with len 3")
    iso=0
    for i in range(len(ang)):
        iso=np.add(glcm_img[7][:,:,0,i], iso)
    
    plt.imshow(np.divide(iso,len(ang)))
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_7_0.jpg")
    plt.clf()
    
    plt.title("Isometric GLCM with len 6")
    iso=0
    for i in range(len(ang)):
        iso=np.add(glcm_img[7][:,:,1,i], iso)
    
    plt.imshow(np.divide(iso,len(ang)))
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_7_1.jpg")
    plt.clf()
    
    plt.title("Isometric GLCM with len 9")
    iso=0
    for i in range(len(ang)):
        iso=np.add(glcm_img[3][:,:,2,i], iso)
    
    plt.imshow(np.divide(iso,len(ang)))
    plt.colorbar()
    plt.savefig("report/GCLM_IMG_7_2.jpg")
    plt.clf()
   


###################
######PART 3#######
###################

def oppg3():
    inertia_attr=      [25,25]
    homogenity_attr=   [25,25]
    cluster_shade_attr=[25,25]
    inertia_img,homogenity_img,cluster_shade_img=save_features(original_img[8:], inertia_attr, homogenity_attr, 
                 cluster_shade_attr)

    return inertia_img,homogenity_img,cluster_shade_img
###################
######PART 4#######
###################

def oppg4():
    inertia_img=list(np.load('cluster_file_25_1.npy'))
    
    
    #ski.filters.try_all_threshold(inertia_img[0],figsize=(19,19),verbose=True)
    #ski.filters.try_all_threshold(inertia_img[1],figsize=(19,19),verbose=False)
    plt.imshow(inertia_img[0])
    plt.colorbar()
    plt.savefig("report/oppg4cluster0.png")
    plt.show()
    plt.imshow(inertia_img[1])
    plt.colorbar()
    plt.savefig("report/oppg4cluster1.png")
    plt.show()
    
    
    tresh=45000
    eq=eq_img(original_img)
    img0=inertia_img[0]<=tresh
    tresh=60000
    img1=inertia_img[1]<=tresh
   
    plt.imshow(np.multiply(img0,original_img[8][12:-13,12:-13]))
    plt.savefig("report/oppg4cluster0filter.png")
    plt.show()
    plt.imshow(np.multiply(img1,original_img[9][12:-13,12:-13]))
    plt.colorbar()
    plt.savefig("report/oppg4cluster1filter.png")
    plt.show()
    
   

#oppg2()
#inertia_img,homogenity_img,cluster_shade_img=oppg3()   
#np.save("inertia_file_25_1", inertia_img)
#np.save("homo_file_25_1", homogenity_img)
#np.save("cluster_file_25_1", cluster_shade_img)
oppg4()