"""
Class for normalizing the sliced images for the LEVIRCD dataset
"""


import numpy as np


# Class to normalize images 
class LVRCDNormal(object):
    """
    class for Normalization of images, per channel, in format CHW 
    """
    def __init__(self):
        
        # Normalization constants for image -- calculated from training images 
        # self._mean = np.array([32.539345, 38.096737, 26.94744,  71.85371])
        # self._std = np.array ([35.85937,  38.255123, 27.52351,  56.268917 ])
        
        #Normalization constants for image -- calculated from farm hand data 
        # self._mean = np.array([128.25049, 128.25049, 128.25049, 128.25049 ])
        # self._std = np.array ([25.307453, 21.081957, 20.106825, 58.384758])

        #Normalization constants for image -- calculated from farm hand + Dutch data 
        # self._mean = np.array([39.577614, 40.984497, 35.754196, 99.946236 ])
        # self._std = np.array ([54.89089,  51.707474, 46.82019,  60.879063])

        #Normalization constants for 128 X 128 image -- calculated from farm hand + Dutch data 
        # self._mean = np.array([45.45052,  46.851467, 38.638863, 73.885 ])
        # self._std = np.array ([57.32448,  57.22822,  49.759693, 71.27414])
        
        #Normalization constants for 128 X 128 image -- calculated from Dutch data 
        self._mean = np.array([35.62046,  41.339233, 32.118134, 90.02198 ])
        self._std = np.array ([45.244064, 49.484463, 34.908585, 54.91547])


        
    def __call__(self,img):

        temp = img.astype(np.float32)
        temp2 = temp.T            
        temp2 -= self._mean
        temp2 /= self._std
            
        temp = temp2.T

        return temp
        


    def restore(self,normed_img):

        d2 = normed_img.T * self._std
        d2 = d2 + self._mean
        d2 = d2.T
        d2 = np.round(d2)
        d2 = d2.astype('uint8')

        return d2 



