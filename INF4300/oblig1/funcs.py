#DIV Funcs
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

def make_gif(image,num_points,length):
    points=np.linspace(0,np.pi,num_points)
    glcm_img=GLCM(image, [length], points)
    for i in range(len(points)):
        plt.imshow(glcm_img[:,:,0,i])
        a="%f"%(i)
        plt.title(a,)
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
    import glob, os
    for f in glob.glob("img*.png"):
        os.remove(f)    




def GLCM(image,distances,angles,levels1=16, symmetric1=False, normed1=False):
    #calculates the grey level co-ocurtance matrix
    return skif.greycomatrix(image, distances, angles, levels=levels1, symmetric=symmetric1, normed=normed1)

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

       