"""
            A3 More Libraris [Basic]

            Created on 2020.May.27

    This Is the first part of RoboCup SimPlus Simulation Tutorial
    For working with this simulator you need basic knowledge about python programming
    In this session we practice some fun trick in python and introducing a few essential libraries
    If you are familiar with following python concepts.

    List of Tutorial Materials:
        ## 1. Numpy
        ## 2. OpenCV
        ## 3. RCJRVision
        ## 4. GRPC
"""

################################
## 1. Numpy
################################
"""
Numpy is the core library for scientific computing in Python. 
It provides a high-performance multidimensional array object, 
and tools for working with these arrays. 

## Arrays
    A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers.
    The number of dimensions is the rank of the array;
    The shape of an array is a tuple of integers giving the size of the array along each dimension.

    We can initialize numpy arrays from nested Python lists, and access elements using square brackets:
"""
import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
print(type(a))  # Prints "<class 'numpy.ndarray'>"
print(a.shape)  # Prints "(3,)"
print(a[0], a[1], a[2])  # Prints "1 2 3"
a[0] = 5  # Change an element of the array
print(a)  # Prints "[5, 2, 3]"

b = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 2 array
print(b.shape)  # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])  # Prints "1 2 4"

# Numpy also provides many functions to create arrays:

import numpy as np

a = np.zeros((2, 2))  # Create an array of all zeros
print(a)  # Prints "[[ 0.  0.]
#          [ 0.  0.]]"

b = np.ones((1, 2))  # Create an array of all ones
print(b)  # Prints "[[ 1.  1.]]"

c = np.full((2, 2), 7)  # Create a constant array
print(c)  # Prints "[[ 7.  7.]
#          [ 7.  7.]]"

d = np.eye(2)  # Create a 2x2 identity matrix
print(d)  # Prints "[[ 1.  0.]
#          [ 0.  1.]]"

e = np.random.random((2, 2))  # Create an array filled with random values
print(e)  # Might print "[[ 0.91940167  0.08143941]
#               [ 0.68744134  0.87236687]]"
"""                             
Array indexing

Numpy offers several ways to index into arrays.
Slicing: Similar to Python lists, numpy arrays can be sliced.
Since arrays may be multidimensional, you must specify a slice for each dimension of the array:
"""
import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])  # Prints "2"
b[0, 0] = 77  # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])  # Prints "77"

###
# You can also mix integer indexing with slice indexing.
# However, doing so will yield an array of lower rank than the original array.
# Note that this is quite different from the way that MATLAB handles array slicing:
###

import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1, :]  # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)  # Prints "[[ 2]
#          [ 6]
#          [10]] (3, 1)"
###
# Integer array indexing:
# When you index into numpy arrays using slicing,
# the resulting array view will always be a subarray of the original array.
# In contrast, integer array indexing allows you to construct arbitrary arrays using the data from another array.
# Here is an example:
####
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"

# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"

###
# One useful trick with integer array indexing is selecting or mutating one element from each row of a matrix:
###
import numpy as np

# Create a new array from which we will select elements
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(a)  # prints "array([[ 1,  2,  3],
#                [ 4,  5,  6],
#                [ 7,  8,  9],
#                [10, 11, 12]])"

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10

print(a)  # prints "array([[11,  2,  3],
#                [ 4,  5, 16],
#                [17,  8,  9],
#                [10, 21, 12]])
###
# Boolean array indexing:
# Boolean array indexing lets you pick out arbitrary elements of an array.
# Frequently this type of indexing is used to select the elements of an array that satisfy some condition.
# Here is an example:
###
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])

bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
# this returns a numpy array of Booleans of the same
# shape as a, where each slot of bool_idx tells
# whether that element of a is > 2.

print(bool_idx)  # Prints "[[False False]
#          [ True  True]
#          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print(a[a > 2])  # Prints "[3 4 5 6]"

###
# Datatypes
#
# Every numpy array is a grid of elements of the same type.
# Numpy provides a large set of numeric datatypes that you can use to construct arrays.
# Numpy tries to guess a datatype when you create an array,
# but functions that construct arrays usually also include an optional argument to explicitly specify the datatype.
# Here is an example:
###
import numpy as np

x = np.array([1, 2])  # Let numpy choose the datatype
print(x.dtype)  # Prints "int64"

x = np.array([1.0, 2.0])  # Let numpy choose the datatype
print(x.dtype)  # Prints "float64"

x = np.array([1, 2], dtype=np.int64)  # Force a particular datatype
print(x.dtype)  # Prints "int64"

###
# Array math
#
# Basic mathematical functions operate elementwise on arrays,
# and are available both as operator overloads and as functions in the numpy module:
###
import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

###
# We instead use the dot function to compute inner products of vectors,
# to multiply a vector by a matrix, and to multiply matrices.
# dot is available both as a function in the numpy module and as an instance method of array objects:
###
import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))

###
# Numpy provides many useful functions for performing computations on arrays; one of the most useful is sum:
###
import numpy as np

x = np.array([[1, 2], [3, 4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

###
# Apart from computing mathematical functions using arrays,
# we frequently need to reshape or otherwise manipulate data in arrays.
# The simplest example of this type of operation is transposing a matrix; to transpose a matrix,
# simply use the T attribute of an array object:
###
import numpy as np

x = np.array([[1, 2], [3, 4]])
print(x)  # Prints "[[1 2]
#          [3 4]]"
print(x.T)  # Prints "[[1 3]
#          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1, 2, 3])
print(v)  # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"

################################
## 2. OpenCV
################################
# OpenCV is one the greated libraries for machine vision,
# Although we can not cover all concepts of this library here
# But we trying to show you basic operation and most useful functions in this project

import cv2
import numpy
import matplotlib.pyplot as plt

# Core Functions
img = cv2.imread('img/vision.png')  # Read image file

plt.subplot(111), plt.imshow(img, cmap='gray'), plt.title('Vision')  # Plot the Image
plt.show()  # Show the plotter window (You should see the image in a new window now)

# You can access a pixel value by its row and column coordinates. For BGR image,
# it returns an array of Blue, Green, Red values.
# For grayscale image, just corresponding intensity is returned.
px = img[100, 100]
print(px)  # => [105 105 105]
# accessing only blue pixel
blue = img[100, 100, 0]
print(blue)  # => 105

# You can modify the pixel values the same way.
img[100, 100] = [255, 255, 255]
print(img[100, 100])  # => [255 255 255]

### NOTICE
##
# Numpy is a optimized library for fast array calculations.
# So simply accessing each and every pixel values and modifying it will be very slow and it is discouraged.
##
###

### NOTICE
##
# Above mentioned method is normally used for selecting a region of array,
# say first 5 rows and last 3 columns like that. For individual pixel access,
# Numpy array methods, array.item() and array.itemset() is considered to be better.
# But it always returns a scalar.
#
# So if you want to access all B,G,R values,
# you need to call array.item() separately for all.
##
###

### Better pixel accessing and editing method :
## accessing RED value
img.item(10, 10, 2)  # => 167

## modifying RED value
img.itemset((10, 10, 2), 100)
img.item(10, 10, 2)  # => 100

### Accessing Image Properties
## Image properties include number of rows, columns and channels, type of image data, number of pixels etc.
## Shape of image is accessed by img.shape. It returns a tuple of number of rows, columns and channels (if image is color):
print(img.shape)

# Total number of pixels is accessed by img.size:
print(img.size)

# Image datatype is obtained by img.dtype:
print(img.dtype)

### Image ROI
# Sometimes, you will have to play with certain region of images.
# For eye detection in images,
# first perform face detection over the image until the face is found,
# then search within the face region for eyes.
# This approach improves accuracy (because eyes are always on faces :D ) 
# and performance (because we search for a small area).

## ROI is again obtained using Numpy indexing.
## Here I am selecting the ball and copying it to another region in the image:
box = img[250:750, 100:600]
img[250:750, 650:1150] = box

# Check the results below:
plt.subplot(111), plt.imshow(img, cmap='gray'), plt.title('ROI')  # Plot the Image
plt.show()  # Show the plotter window (You should see the image in a new window now)

"""    Image ROI    """

### Splitting and Merging Image Channels
# The B,G,R channels of an image can be split into their individual planes when needed.
# Then, the individual channels can be merged back together to form a BGR image again.
# This can be performed by:
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

## Or ##
b = img[:, :, 0]

# Suppose, you want to make all the red pixels to zero,
# you need not split like this and put it equal to zero.
# You can simply use Numpy indexing which is faster.
img[:, :, 2] = 0

#### Warning ####
# `cv2.split()` is a costly operation (in terms of time),
# so only use it if necessary.
# Numpy indexing is much more efficient and should be used if possible.

### Making Borders for Images (Padding)
# If you want to create a border around the image,
# something like a photo frame, you can use cv2.copyMakeBorder() function.
# But it has more applications for convolution operation, zero padding etc.
# This function takes following arguments:

# src - input image
# top, bottom, left, right - border width in number of pixels in corresponding directions
#
# borderType - Flag defining what kind of border to be added. It can be following types:
#         cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
#         cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
#         cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
#         cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
#         cv2.BORDER_WRAP - Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg
#
# value - Color of border if border type is cv2.BORDER_CONSTANT

# Below is a sample code demonstrating all these border types for better understanding:

BLUE = [255, 0, 0]
img1 = cv2.imread('img/rc.jpeg')

replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()

################################
## 3. RCJRVision
################################
# One of the best modules that been desinged and used in many robocup competition.
# It is now specially tuned for RoboCup Rescue Simulatiuon
# you can detect all letters and signs with three simple step
from RCJRVision import RCJRVision  # Import module

my_vision = RCJRVision.HSUVision()  # Instantiate
letter, center = my_vision.find_HSU(img)  # Call the function
################################
## 4. GRPC (Optional)
################################
# Actually, You don't need this part for development, only for those who are more interested
# As you may know all programs for this leagues are communicating via network.
# For this communication we need to standardize some protocol and messaging system
# It has been done with low-latency and performance in mind so we choose GRPC
# The best practice for this modules are **client.py** and **server.py** in this project.
