import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage.feature as skif
from matplotlib import animation
#import seaborn
plot1=False
plot2=False



def GLCM(image,distances,angles):
    #calculates the grey level co-ocurtance matrix
    return skif.greycomatrix(image, distances, angles, levels=None, symmetric=False, normed=False)

def plot_imglist(img,sub=False):
    if sub:
        plt.subplot(221),plt.imshow(img[0],cmap = 'gray')
        plt.title('Img1'), plt.xticks([]), plt.yticks([])
        plt.subplot(222),plt.imshow(img[1],cmap = 'gray')
        plt.title('Img2'), plt.xticks([]), plt.yticks([])
        plt.subplot(223),plt.imshow(img[2],cmap = 'gray')
        plt.title('Img3'), plt.xticks([]), plt.yticks([])
        plt.subplot(224),plt.imshow(img[3],cmap = 'gray')
        plt.title('Img4'), plt.xticks([]), plt.yticks([])
        plt.show()
        plt.subplot(221),plt.imshow(img[4],cmap = 'gray')
        plt.title('Img5'), plt.xticks([]), plt.yticks([])
        plt.subplot(222),plt.imshow(img[5],cmap = 'gray')
        plt.title('Img6'), plt.xticks([]), plt.yticks([])
        plt.subplot(223),plt.imshow(img[6],cmap = 'gray')
        plt.title('Img7'), plt.xticks([]), plt.yticks([])
        plt.subplot(224),plt.imshow(img[7],cmap = 'gray')
        plt.title('Img8'), plt.xticks([]), plt.yticks([])
        plt.show()
    else:
        plt.subplot(121),plt.imshow(img[8],cmap = 'gray')
        plt.title('Img1'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img[9],cmap = 'gray')
        plt.title('Img2'), plt.xticks([]), plt.yticks([])
        plt.show()

        

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


"""
EQ IMG
"""
equalized_img=[]
for i in original_img:
        equalized_img.append(cv2.equalizeHist(i))
plot_imglist(equalized_img,sub=True)

"""
GLCM IMG
"""
glcm_img=[]
megapic=np.linspace(0,2*np.pi,50)
for i in equalized_img:
        glcm_img.append(GLCM(i, [6], megapic))

def make_gif(img_number):
    for i in range(len(megapic)):
        plt.imshow(glcm_img[img_number][:,:,0,i])
        a="%f"%(i/50*2*np.pi)
        plt.title(a)
        plt.savefig('img%.2d.png'%(i))
        plt.clf()
    import glob
    filenames=glob.glob('img*')
    f=sorted(filenames)
    g=f[:-2]
    filenames=g
    import imageio
    with imageio.get_writer('movie.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
make_gif(4)