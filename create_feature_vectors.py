from keras import backend as K
from keras.models import load_model
from keras.models import Model
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import os
import glob
import numpy as np
import pickle

image_size = 256
names = ['antique','ballad','jazz','rap','rock','soft']
cates = ['train', 'validation', 'test']
DATA_DIR = './data/train/antique/'

if K.image_data_format() == 'channels_first':
    input_shape = (3, image_size, image_size)
else:
    input_shape = (image_size, image_size, 3)

feature_vec_model = load_model('music_feature_extractor.hdf5')
for cate in cates:
    for name in names:
        spect_files = glob.glob('.\\data\\'+cate+'\\'+name+'\\'+'*.png')
        for file in spect_files:
            img = load_img('{}'.format(file), target_size=(256, 256))
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255
            
            feature_vec = feature_vec_model.predict(img_array)
            
            s = file
            s = s.replace('.png','')
            print(s)
            s = s.split('\\')[-1]
            print(s)
            file_info = s
            
            out_file_name = '{}.npy'.format(file_info)
            out_file_dir = 'feature_vec_arrays_single_file'
            out_file_path = '{}/{}'.format(out_file_dir, out_file_name)
            
            np.save(out_file_path, feature_vec)