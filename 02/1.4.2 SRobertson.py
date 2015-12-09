# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # “as” lets us use standard abbreviations
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
filename2 = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)
img2 = plt.imread(filename2)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
fig2, ax2 = plt.subplots(1, 5)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
for i in range(0,5):
    ax2[i].imshow(img2, interpolation='none')
# Show the figure on the screen
fig.show()
fig2.show()

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img)
ax[1].imshow(img, interpolation='none') # Override the default
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
ax[1].set_title('asdasd')
# Show the figure on the screen
fig.show()
cDir = os.path.dirname(os.path.abspath(__file__))
fName = os.path.join(cDir, 'cat1-a.gif')
imgArr = plt.imread(fName)
figure, axes = plt.subplots(1,3)

axes[0].imshow(imgArr, interpolation = 'none')
axes[0].set_xlim(20,30)
axes[0].set_ylim(20,30)
axes[1].imshow(imgArr, interpolation = 'none')
axes[1].set_xlim(50,60)
axes[1].set_ylim(55,65)
axes[2].imshow(imgArr, interpolation = 'none')
axes[2].set_xlim(38,48)
axes[2].set_ylim(40,50)
figure.show()