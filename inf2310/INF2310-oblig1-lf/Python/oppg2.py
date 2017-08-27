
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

'''
pad2D(img,padlengths,padtype='constant',cval=0)
Pads the image with given padlengths and given type of padding.

parameters:
    * img: image to be padded
    * padlengths: a tuple (N,M) to pad the image with N rows and M columns
    * padtype: which type of padding
    * cval: value to pad image with if padtype is constant
returns:
    * img_padded: padded image
'''
def pad2D(img,padlengths,padtype='constant',cval=0):
    pad_N = padlengths[0]
    pad_M = padlengths[1]

    half_pad_N = int((pad_N-1)/2)
    half_pad_M = int((pad_M-1)/2)

    N,M = img.shape

    #Sets values of the padded regions
    if( padtype == 'constant'):
        img_padded = np.ones((N+pad_N,M+pad_M))
        img_padded *= cval
    else:
        img_padded = np.zeros((N+pad_N,M+pad_M))

        #--- Above img ---
        img_padded[0:half_pad_N,half_pad_M:(M+half_pad_M)] = img[0:half_pad_N,:][::-1]

        #Note: [::-1] flips the image about a horizontal axis.
        #Example: A = np.array([[1,2,3],[4,5,6],[7,8,9]])
        #         A[::-1] gives [[7,8,9],[4,5,6],[1,2,3]]

        #--- Under img ---
        img_padded[(half_pad_N + N):(pad_N+N),half_pad_M:(M + half_pad_M)] = img[((N-1)-half_pad_N):N,:][::-1]

        #--- Left side to img ---
        img_padded[half_pad_N:(half_pad_N+N),0:half_pad_M] = img[:,0:half_pad_M][...,::-1]

        #Note: [...,::-1] flips the image about a vertical axis.
        #Example: A = np.array([[1,2,3],[4,5,6],[7,8,9]])
        #         A[...,::-1] gives [[3,2,1],[6,5,4],[9,8,7]]

        #--- Right side to img ---
        img_padded[half_pad_N:(half_pad_N+N),(half_pad_M+M):(M+pad_M)] = img[:,(M-1)-half_pad_M:M][...,::-1]

        #--- Corners ---
        #NW:
        img_padded[0:half_pad_N,0:half_pad_M] = img[0:half_pad_N,0:half_pad_M][::-1][...,::-1]

        #NE:
        img_padded[0:half_pad_N,(M+half_pad_M):(M+pad_M)] = img[0:half_pad_N,((M-1)-half_pad_M):M][::-1][...,::-1]

        #SW:
        img_padded[(half_pad_N + N):(N+pad_N),0:half_pad_M] = img[((N-1)-half_pad_N):N,0:half_pad_M][::-1][...,::-1]

        #SE:
        img_padded[(half_pad_N + N):(N+pad_N),(half_pad_M + M):(pad_M+M)] = img[(N-1)-half_pad_N:N,(M-1)-half_pad_M:M][::-1][...,::-1]

    #Place the original image
    img_padded[half_pad_N:(N + half_pad_N),half_pad_M:(M + half_pad_M)] = img
    return img_padded


'''
convolve2D(img,h)
Convolves a given 2D filter and image.

parameters:
    * img: image to be convolved    (could be filter aswell, if h is image)
    * h: filter to be convolved     (could be image aswell, if img is filter)
returns:
    * img_convolved: result after convlution
'''
def convolve2D(img,h):
    N,M = h.shape
    img_padded = pad2D(img,(N,M),padtype='symmetric')

    img_N, img_M = img.shape
    img_convolved = np.zeros((img_N,img_M))

    h_rotated = h[...,::-1][::-1]

    for i in range(img_N):
        for j in range(img_M):
            img_convolved[i,j] = np.sum(img_padded[i:N+i,j:M+j]*h_rotated)

    return img_convolved


'''
non_max_suppression(img_direction)
Thins out the given gradient angle image.

parameters:
    * img_grad: gradient magnitude image.
    * img_direction: the angle image. Assumed to have values 0,45,90 or 135
returns:
    * img_thinned: result after thinning
'''
def non_max_suppression(img_grad,img_direction):
    N,M = img_direction.shape

    img_thinned = np.zeros((N,M))
    for y in range(1,N-1):
        for x in range(1,M-1):
            degree = img_direction[y,x]
            a = 0; b = 0

            if degree == 0:
                a = img_grad[y-1,x]
                b = img_grad[y+1,x]
            elif degree == 45:
                a = img_grad[y+1,x+1]
                b = img_grad[y-1,x-1]
            elif degree == 135:
                a = img_grad[y-1,x+1]
                b = img_grad[y+1,x-1]
            else:
                a = img_grad[y,x-1]
                b = img_grad[y,x+1]

            if ( img_grad[y,x] > a and img_grad[y,x] > b):
                img_thinned[y,x] = img_grad[y,x]

    return img_thinned


'''
hysteresis(img_thinned,tw,ts)
Tracks strong edges.

parameters:
    * img_thinned: thinned gradient angle image
    * tw: threshold for weak edges
    * ts: threshold for strong edges
returns:
    * img_strong: image where the strong edges are marked
'''
def hysteresis(img_thinned,tw,ts):
    N,M = img_thinned.shape

    img_strong = np.copy(img_thinned)
    img_strong[np.where(img_thinned > ts)] = 255

    img_hyst = np.copy(img_strong)
    marked = 1
    while(marked > 0):
        marked = 0
        for y in range(1,N):
            for x in range(1,M):

                if (tw < img_strong[y,x] < ts):

                    #Using 4-connected neighbourhood. Could also use 8
                    num_strong = np.sum(img_strong[y-1:y+1,x-1:x+1] == 255)

                    if (num_strong > 0):
                        img_hyst[y,x] = 255
                        marked += 1

        img_strong = np.copy(img_hyst)

    #Get rid of weak edges
    img_strong[np.where(img_strong != 255)] = 0
    return img_strong

if __name__ == '__main__':

    img = cv2.imread('../houses.png',cv2.IMREAD_GRAYSCALE)
    N = 11
    sigma = 2

    NN = int((N-1)/2)


    H = 1/(2*np.pi*sigma**2)*np.array([ [np.exp(-((x*x + y*y)/(2*sigma**2))) for x in range(-NN,NN+1)] \
                                        for y in range(-NN,NN+1)])
    H=np.array([[1,1,1],[1,1,1],[1,1,1]])/9.
    img_gauss =img# convolve2D(img,H)
    
    test=np.fft.fft2(img)
    plt.imshow(np.log(np.abs(np.fft.fftshift(test))**2))
    for i in test:
        for j in i:
            if np.abs(j) > 1e+04:
                i=0
    test=np.fft.fftn(test)
    plt.imshow(np.abs(test))
    a=input()
    sobel = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    img_gx = convolve2D(img_gauss,sobel)
    img_gy = convolve2D(img_gauss,sobel.T)


    img_grad = np.sqrt(img_gx*img_gx + img_gy*img_gy)

    img_direction = np.arctan2(img_gy,img_gx)
    img_direction = np.mod((np.round(img_direction*180/(np.pi*45))*45),180)

    img_thinned = non_max_suppression(img_grad,img_direction)

    # Remember to have values between 0 and 255 such that hysteresis gives desired results
    img_thinned = ((img_thinned- np.min(img_thinned))*255)/(np.max(img_thinned) - np.min(img_thinned))

    img_hyst = hysteresis(img_thinned, 30,60)

    plt.imshow(img_hyst,cmap ='gray',interpolation='none')
    plt.show()
