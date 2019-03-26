from keras import backend as K
from keras.models import load_model
from keras.models import Model
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import os
import glob
import numpy as np
import pickle

# DATA_DIR = 'prediction/'
image_size = 256

if K.image_data_format() == 'channels_first':
    input_shape = (3, image_size, image_size)
else:
    input_shape = (image_size, image_size, 3)

model = load_model('music_classify.hdf5')
print(model.summary())
new_model = Model(inputs=model.input, outputs=model.get_layer('dense_1').output)
print(new_model.summary())
new_model.save('music_feature_extractor.hdf5')
# model.layers.pop() doesn't work here
# model.layers.pop()
# model.layers.pop()
# model.layers.pop()
# model.layers.pop()
# new_output = model.layers[-1].output
# feature_vec_model = Model(model.input, new_output)
# feature_vec_model.save('music_feature_extractor.hdf5')