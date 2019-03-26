from keras import backend as K
from keras.models import Sequential
from keras.layers.core import Flatten, Dense, Dropout, Activation
from keras.optimizers import rmsprop,adam
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import Input, Dense
import os
import numpy as np
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt


# Set values

num_classes = 6
image_size = 256
nb_epoch = 20
batch_size = 8

train_data_dir = 'data/train'
validation_data_dir = 'data/validation'

nb_train_samples = 56652
nb_validation_samples = 21445

if K.image_data_format() == 'channels_first':
    input_shape = (3, image_size, image_size)
else:
    input_shape = (image_size, image_size, 3)

# Specify model

# callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5)
save_best_model = ModelCheckpoint(filepath='./result/relu+rmsprop/model/'+'model_.{epoch:02d}_{val_loss:.2f}.hdf5', verbose=1,
        monitor='val_loss')

# instantiate Sequential model
model = Sequential()

model.add(Conv2D(filters=64, kernel_size=2, strides=2, activation='relu', kernel_initializer='glorot_normal', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=2, padding='same'))

model.add(Conv2D(filters=128, kernel_size=2, strides=2, activation='relu', kernel_initializer='glorot_normal'))
model.add(MaxPooling2D(pool_size=2, padding='same'))

model.add(Conv2D(filters=256, kernel_size=2, strides=2, activation='relu', kernel_initializer='glorot_normal'))
model.add(MaxPooling2D(pool_size=2, padding='same'))

model.add(Conv2D(filters=512, kernel_size=2, strides=2, activation='relu', kernel_initializer='glorot_normal'))
model.add(MaxPooling2D(pool_size=2, padding='same'))

model.add(Flatten())
model.add(Dense(128))

model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(num_classes))
model.add(Activation('softmax'))
opt = rmsprop()

model.compile(loss='categorical_crossentropy',
             optimizer = opt,
             metrics = ['accuracy'])

# Image generators
train_datagen = ImageDataGenerator(rescale= 1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(image_size, image_size),
    classes=['antique','ballad','jazz','rap','rock','soft'],
    shuffle=True,
    batch_size=batch_size,
    class_mode='categorical'
    )

validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(image_size, image_size),
    classes=['antique','ballad','jazz','rap','rock','soft'],
    batch_size=batch_size,
    shuffle=True,
    class_mode='categorical'
    )

# Fit model
history = model.fit_generator(train_generator,
                    steps_per_epoch=(nb_train_samples // batch_size),
                    epochs=nb_epoch,
                    validation_data=validation_generator,
                    callbacks=[early_stopping,save_best_model],
                    validation_steps=(nb_validation_samples // batch_size)
                   )

# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig("./result/relu+rmsprop/relu+adam+accuracy.jpg")
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig("./result/relu+rmsprop/relu+adam+loss.jpg")
plt.show()

# Save model
model.save_weights('full_model_weights.h5')
model.save('model.h5')
