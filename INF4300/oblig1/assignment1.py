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
img0shape=img0.shape
img1shape=img1.shape


if plot1:
    plt.subplot(121),plt.imshow(img0,cmap = 'gray')
    plt.title('Original Image1'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img1,cmap = 'gray')
    plt.title('Original Image2'), plt.xticks([]), plt.yticks([])
    plt.show()

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

original_img=[subimg00,subimg01,subimg02,subimg03,subimg10,subimg11,subimg12,subimg13,img0,img1]
#original_img is now on the sape over
for i in enumerate(original_img):
    break
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
  
   


"""
EQ IMG
"""
"""
equalized_img=[]
for i in original_img:
        equalized_img.append(ski.exposure.rescale_intensity(i, out_range=(0, 15)))
        #equalized_img.append(cv2.equalizeHist(i))

plot_imglist(equalized_img,sub=True)
"""



###################
######PART 2#######
###################

"""
GLCM IMG
"""
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

#@jit
def homogenity(p):
    rows,cols=p.shape
    a=np.fromfunction(lambda x, y: 1/(1+(x-y)**2) , (rows, cols), dtype=float)
    return np.sum(np.multiply(a,p))
    

def inertia(p):
    rows,cols=p.shape
    a=np.fromfunction(lambda x, y:(x-y)**2 , (rows, cols), dtype=float)
    return np.sum(np.multiply(a,p))
   
def cluster_shade(p):
    rows,cols=p.shape
    
    def u_x(i):
        return np.fromfunction(lambda  j : j*i*p[i,j] , (rows), dtype=float)
    
    def u_y(j):
        return np.fromfunction(lambda  i : j*i*p[i,j] , (cols), dtype=float)
    
    a=np.fromfunction(lambda x, y:x+y , (rows, cols), dtype=float)
    b=np.fromfunction(u_x(rows) , (rows, cols), dtype=float)
    c=np.fromfunction(u_y(cols) , (rows, cols), dtype=float)
    d=np.add(a, b)
    d=np.add(d,c)
    d=d**3
    return np.sum(np.multiply(d,p))
    



def sliding_window(inarray,size,f):
    equalized0=cv2.equalizeHist(inarray)
    inarray_16=(ski.exposure.rescale_intensity(equalized0, out_range=(0, 15)))
    s=int((size-1)/2)
    newarray=np.zeros(inarray.shape)
    A,B=np.shape(inarray)
    
    for i in enumerate(inarray):
        if i[0]+s >= A or i[0]-s <= 0:
            continue
        for j in enumerate(i[1]):
            if j[0]+s >= B or j[0]-s <= 0:
                continue
            
            
            w=[i[0]-s,i[0]+s,j[0]-s,j[0]+s]
            p=GLCM(inarray_16[w[0]:w[1],w[2]:w[3]], [3], [pi], symmetric1=True, normed1=True)
            p=p[:,:,0,0] #gets only the first gclm
            plass=f(p)
            newarray[i[0]][j[0]]=plass
    
    return newarray[0+s+1:A-s,0+s+1:B-s]    


import time
start_time = time.time()
a=sliding_window(original_img[-2],10,cluster_shade)
print("--- %s seconds ---" % (time.time() - start_time))
plt.imshow(a)
plt.show()


#make_gif(equalized_img[2],20,10)