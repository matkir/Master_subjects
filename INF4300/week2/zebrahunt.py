import sys  
sys.path.append('../pylibs')  


from custom import *

#ASSIGNMENT 1
im = Image.open('zebra_2.tif')
im.show()
imarray=array(im)
tmp=glcm(imarray, 255, 15, 0)
print(tmp)
plt.imshow(tmp)

plt.show()

new_img, h, new_h, s =histeq(imarray)
plt.imshow(new_img)
plt.show()