import glob
import time
import cv2
import numpy as np
from PIL import Image
from scipy import ndimage
from scipy import misc


images = []
labels = []

start = time.time()
dsDir = "../../NISTSpecialDatabase4GrayScaleImagesofFIGS/sd04/png_txt/figs_"
y = 0
for x in range(0,8): # Directories /figs_0 to 7
    for img in glob.glob(dsDir + str(x) + "/*.png"):
        n = misc.imread(img)
        featurevector = np.array(n)
        images.append(featurevector)
        labels.append(y)
        y+=1
end = time.time()

# using two numpy arrays
#features, labels = (np.random.sample((100,2)), np.random.sample((100,1)))
#dataset = tf.data.Dataset.from_tensor_slices((features,labels))
print('Finished reading in all pngs. It took ' + str(end - start) + ' seconds')
