import numpy as np
import cv2

## (to install cv2 type:     pip install opencv-python )

##*************************************************************************************************

n = np.arange(27)         #creates a 1 dimentional array of numbers from 0 to 26
print (n)

x = np.arange(10.4)
print (x)


print (n.reshape(3,9))      #convert n into 2 dimentional array
print (n.reshape(3,3,3))    #convert n into 3 dimentional array

x = np.asarray([[1,2,5,6],[2,35,6,7],[5,6,7,]])           #convert a list into array
print (x)

##***************************************************************************************************

# TO load/read an image to python
# 0 after file name - means you want to read the image in gray scale.
#image_g = cv2.imread("C:\Users\DIPESH\smallgray.png",0)
#print (image_g)                 # will get a 2 dimentional array with each no. corresponding to its color

# # 1 means read the image in bgr (blue,green,red) scale.
# image_g1 = cv2.imread("C:\Users\DIPESH\smallgray.png",1)
# print image_g1                 # will get a 3 dimentional array with 1st corresponding to blue,
                                ##2nd to green & 3rd to red


# Creating images from numpy array
#cv2.imwrite("newsmallgray.png", image_g)

##******************************************************************************************************

## SLICING ARRAY:
#print (image_g[0:2,2:4])
#print (image_g[2,4])

## ITERATING through Numpy array:
# ## Method 1 : i gets the value of rows,output be will same as it is in image_p
# for i in image_g:
#     print i
#
# ## Method 2 : it transposes the array and i gets the value of columns.
# for i in image_g.T:
#     print i
#
# ## Method 3 : .flat - to get values of the array one by one then print each value individually.
# for i in image_g.flat:
#     print i

##*************************************************************************************************

## CONCATENATE ARRAYS:
## NOTE : Only arrays with the same no. of dimentions can be added.
## Horizontal concatenation - .hstack
## Can give only 1 value in hstack(), so have to create a tuple to put in 2 or more array variables to be concatenated.
#ims = np.hstack((image_g,image_g))
#print ims

## Vertical concatenation - .vstack
#imsv = np.vstack((image_g,image_g,image_g))
#print imsv

##*****************************************************************************************************

## SPLITTING ARRAYS:
#lst = np.hsplit(imsv,5)        # splits horizontally
#print lst                      # lst is a list

#lstv = np.vsplit(imsv,3)       # splits vertically
#print lstv                     # lstv is also a list