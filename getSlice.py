from PIL import Image
import requests
import os
import numpy as np
import threading  
import time  

image_size = 256
num_classes = 6
DEFAULT_IMG_SIZE = 256
DATA_DIR = './sliced_img/'

# helper function - gets dimensions of the spectrogram
def get_spect_dims(input_img):
    img_width, img_height = input_img.size
    return img_width, img_height

# helper function - calculates the number of slices available from the full size spectrogram
def get_num_slices(img_width):
    n_slices = img_width // DEFAULT_IMG_SIZE
    return n_slices

# helper function - returns a list of coordinates/dimensions where to split the spectrogram
def get_slice_dims(input_img):
    img_width, img_height = get_spect_dims(input_img)
    num_slices = get_num_slices(img_width)
    unused_size = img_width - (num_slices * DEFAULT_IMG_SIZE)
    start_px = 0 + unused_size
    image_dims = []
    for i in range(num_slices):
        img_width = DEFAULT_IMG_SIZE
        image_dims.append((start_px, start_px + DEFAULT_IMG_SIZE))
        start_px += DEFAULT_IMG_SIZE
    return image_dims

# slices the spectrogram into individual sample images
def slice_spect(path, input_file, name):
    input_file_cleaned = input_file.replace('.png','')
    img = Image.open(path+input_file)
    dims = get_slice_dims(img)
    counter = 0
    for dim in dims:
        counter_formatted = str(counter).zfill(3)
        img_name = '{}_{}.png'.format(input_file_cleaned, counter_formatted)
        start_width = dim[0]
        end_width = dim[1]
        sliced_img = img.crop((start_width, 0, end_width, DEFAULT_IMG_SIZE))
        sliced_img.save(DATA_DIR + name + '/'+ img_name)
        counter += 1


class SliceTor(threading.Thread): #The Convertor class is derived from the class threading.Thread  
    def __init__(self, num, interval, names):  
        threading.Thread.__init__(self)  
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False
        self.names = names  
   
    def run(self): #Overwrite run() method, put what you want the thread do here 
        counter = 0 
        while not self.thread_stop:
            for name in self.names:
                path='./image/'+name+'/'
                files = os.listdir(path)
                for file in files:
                    print(file)
                    counter += 1
                    if counter>=len(slef.names)*len(files):
                        self.thread_stop = True
                    # strero=>mono
                    slice_spect(path, file, name)
            time.sleep(self.interval)  
    def stop(self):  
        self.thread_stop = True  
         
   
def test():
    names1 = ['antique','jazz']
    names2 = ['ballad','soft']
    names3 = ['rap','rock']

    thread1 = SliceTor(1, 0.1, names1)  
    thread2 = SliceTor(2, 0.1, names2)
    thread3 = SliceTor(3, 0.1, names3)
    thread1.start()  
    thread2.start()
    thread3.start()
    print("finished!!!!!!!!!!!!!!!!!!")

if __name__ == '__main__':
    test()

