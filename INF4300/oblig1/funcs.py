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


def save_features(original_img,inertia_attr,homogenity_attr,cluster_shade_attr): 
    inertia_img=[]
    homogenity_img=[]
    cluster_shade_img=[]
    import time
    for i in enumerate(original_img):
        start_time = time.time()
        a=sliding_window(i[1],inertia_attr[i[0]],inertia)
        b=sliding_window(i[1],homogenity_attr[i[0]],homogenity)
        c=sliding_window(i[1],cluster_shade_attr[i[0]],cluster_shade)
        inertia_img.append(a)
        homogenity_img.append(b)
        cluster_shade_img.append(c)
        
        print("--- %s seconds ---" % (time.time() - start_time))
    
        plt.imshow(a)
        plt.savefig('report/inertia%s.png'%(i[0]))
        plt.clf()
        plt.imshow(b)
        plt.savefig('report/homogenity%s.png'%(i[0]))
        plt.clf()
        plt.imshow(c)
        plt.savefig('report/cluster_shade%s.png'%(i[0]))
        plt.clf()
    
    return inertia_img,homogenity_img,cluster_shade_img       



def eq_img(original_img,plotting=False):    
    #equalized img with 16 greysacles
    equalized_img=[]
    for i in original_img:
            equalized_img.append(ski.exposure.rescale_intensity(cv2.equalizeHist(i), out_range=(0, 15)))
    
    if plotting:
        plot_imglist(equalized_img,sub=True)
    return equalized_img


def homogenity(p):
        rows,cols=p.shape
        a=np.fromfunction(lambda x, y: 1/(1+(x-y)**2) , (rows, cols), dtype=int)
        return np.sum(np.multiply(a,p))
        
    
def inertia(p):
    rows,cols=p.shape
    a=np.fromfunction(lambda x, y:(x-y)**2 , (rows, cols), dtype=int)
    return np.sum(np.multiply(a,p))
   
def cluster_shade(p):
    rows,cols=p.shape
    
    def u_x(rows,cols,p):
        
        return np.fromfunction(lambda  i,j : i*np.sum(p[i,:]) , (rows,1), dtype=int)
    
    def u_y(rows,cols,p):
        return np.fromfunction(lambda  j,i : j*np.sum(p[:,j]) , (cols,1), dtype=int)
    
    a=np.fromfunction(lambda x, y:x+y , (rows, cols), dtype=int)
    b=u_x(rows,cols,p)
    c=u_y(rows,cols,p)
    d=np.add(a, b)
    d=np.add(d,c)
    d=np.power(d, 3)
    return np.sum(np.multiply(d,p))
    
@jit
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
            p=GLCM(inarray_16[w[0]:w[1],w[2]:w[3]], [3], [0], symmetric1=True, normed1=True)
            p=p[:,:,0,0] #gets only the first gclm
            newarray[i[0]][j[0]]=f(p)
    
    return newarray[0+s+1:A-s,0+s+1:B-s]    
