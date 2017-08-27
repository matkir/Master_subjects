import matplotlib.pyplot as plt
import numpy as np
import cv2

'''
to_8bits_values(img)
Ensures that the range of values in img are in [0,255] using linear transformation.
Converts the transformed image to type uint8.

parameters:
    * img: image
returns:
    * img_within_range: image wheras the values between 0 and 255 and of type uint8
'''
def to_8bits_values(img): #Gives same result as cv2.convertScaleAbs(img)
    img_within_range = np.round(((img - np.min(img))*255)/(np.max(img) - np.min(img)));
    return img_within_range


'''
standarize_contrast(img,mean,sigma)
Uses a linear transform to ensure that the image has the given mean and standarddeviation

parameters:
    * img: image
    * mean: desired meanvalue
    * sigma: desired standarddeviation
returns:
    * image with the desired meanvalue and standarddeviation
'''
def standarize_contrast(img,mean,sigma):
    N,M = img.shape

    mean_img = np.sum(img)/(N*M)
    sigma_img = np.sqrt(np.sum((img-mean_img)**2)/(N*M))

    return mean + (img-mean_img)*(sigma/sigma_img)


'''
forward_map(N_old,M_old,N_new,M_new,img,transform_matrix)
Maps the given image using forwardmapping.

parameters:
    * N_old: Number of rows in the image to be mapped
    * M_old: Number of columns in the image to be mapped
    * N_new: Number of rows in the resulting image
    * M_new: Number of columns in the resulting image
    * img: image to be mapped
    * tranform_matrix: matrix containing the transform coefficients
returns:
    * forward_map: result after forwardmapping the image
'''
def forward_map(N_old,M_old,N_new,M_new,img,transform_matrix):

    forward_map = np.zeros((N_new,M_new))
    for y in range(N_old):
        for x in range(M_old):
            new_coord = np.rint(np.dot(transform_matrix,np.array([[x],[y],[1.]]))).astype(int)

            #Alternatively, one could write out the explicit result after matrix multiplication
            #which can be found in slide 5 about geometric operations

            x_ = new_coord[0]
            y_ = new_coord[1]
            if (0 <= x_ < M_new and 0 <= y_ < N_new):
                forward_map[y_,x_] = img[y,x]

    return forward_map


'''
backward_map(N_old,M_old,N_new,M_new,img,tranform_matrix,interpolation = 'nearest neighbour')
Maps the given image using backwardmapping and a specified interpolation.

parameters:
    * N_old: Number of rows in the image to be mapped
    * M_old: Number of columns in the image to be mapped
    * N_new: Number of rows in the resulting image
    * M_new: Number of columns in the resulting image
    * img: image to be mapped
    * tranform_matrix: matrix containing the transform coefficients (not inversed)
    * interpolation: type of interpolation
returns:
    * backward_mapped: result after the backwardmapping and interpolation of image
'''
def backward_map(N,M,N_new,M_new,img,tranform_matrix,interpolation = 'nearest neighbour'):
    inv_transform_matrix = np.linalg.inv(tranform_matrix)
    backward_mapped = np.zeros((N_new,M_new))
    for y_ in range(N_new):
        for x_ in range(M_new):

            new_coord = np.dot(inv_transform_matrix,np.vstack((x_,y_,1.)))

            #Alternatively, one could calculate how to find the coordinates (y,x) as functions of (y_,x_).
            #By some rearranging of the equations we get
            #y = (a0*y_ - b0*x_ + a2*b0 - a0*b2)/(a0*b1 - b0*a1)
            #x = (x_ - a2 -a1*y)/a0

            y = new_coord[1,0]
            x = new_coord[0,0]
            if(interpolation == 'nearest neighbour'):
                backward_mapped[y_,x_] = 0 if (not (0 <= x < M and 0 <= y < N)) else img[int(round(y)),int(round(x))]

            elif(interpolation == 'bilinear'):
                x0,y0 = np.floor([x,y]).astype(int)
                x1,y1 = np.ceil([x,y]).astype(int)

                if ( (0 <= x0 and x1 < M ) and (0 <= y0 and y1 < N) ):

                    dx = x - x0
                    dy = y - y0

                    #Used the definition of the interpolation from slide 19 about geometric operations.
                    #The coordinates x and y has been interchanged here compared to the slide.

                    p = img[y0,x0] + (img[y1,x0] - img[y0,x0])*dy
                    q = img[y0,x1] + (img[y1,x1] - img[y0,x1])*dy

                    backward_mapped[y_,x_] =  p + (q-p)*dx

    return backward_mapped

if __name__ == '__main__':
    img = cv2.imread('../portrett.png',cv2.IMREAD_GRAYSCALE)

    plt.figure()
    plt.imshow(img,cmap='gray',vmin=0,vmax=255)
    plt.title("Original image")

    sigma = 64.
    mean = 127.
    img_standarized = to_8bits_values(standarize_contrast(img,mean,sigma))

    plt.figure()
    plt.imshow(img_standarized,cmap='gray',vmin=0,vmax=255)
    plt.title("After standarized mean and standarddeviation")


    mask = cv2.imread('../geometrimaske.png',cv2.IMREAD_GRAYSCALE)
    #plt.figure()
    #plt.imshow(mask,cmap='gray',vmin=0,vmax=255)
    #plt.title("Mask")

    #Manually chosen points by looking at the image of the mask
    #Left eye:              (173, 258)
    #Right eye:             (343, 259)
    #Midpoint at the mouth: (254, 439)
    points_mask = np.array([(173,258),(343,259),(254,439)])

    #Manually chosen points by looking at the portrait of SYLVESTER STALLONE
    #Left eye:              (84,88)
    #Right eye:             (119,68)
    #Midpoint at the mouth: (128,109)
    points_img = np.array([(84,88),(119,68),(128,109)]) #.reshape((3,1))

    coordinate_matrix = np.append(points_img,np.ones((3,1)),axis=1)

    #Along x-axis (horizontal axis)
    a = np.linalg.solve(coordinate_matrix,points_mask[:,0])

    #One could also use the method of minimizing the mean square error as
    #described in slide 28 about geometric operations

    #Along y-axis (vertical axis)
    b = np.linalg.solve(coordinate_matrix,points_mask[:,1])

    A = np.zeros((3,3))
    A[0] = a.T
    A[1] = b.T
    A[2] = [0,0,1.]

    N,M = img.shape
    N_mask,M_mask = mask.shape
    img_forward_mapped = forward_map(N,M,N_mask,M_mask,img_standarized,A)

    plt.figure()
    plt.imshow(img_forward_mapped,cmap='gray',vmin=0,vmax=255)
    plt.title("Result after forwardmapping")

    img_backward_mapped_nearest = backward_map(N,M,N_mask,M_mask,img_standarized,A)

    plt.figure()
    plt.imshow(img_backward_mapped_nearest,cmap='gray',vmin=0,vmax=255)
    plt.title("Result after backwardmapping using nearest neighbour interpolation")

    img_backward_mapped_bilin = backward_map(N,M,N_mask,M_mask,img_standarized,A,interpolation='bilinear')

    plt.figure()
    plt.imshow(img_backward_mapped_bilin,cmap='gray',vmin=0,vmax=255)
    plt.title("Result after backwardmapping using bilinear interpolation")


    plt.show()
