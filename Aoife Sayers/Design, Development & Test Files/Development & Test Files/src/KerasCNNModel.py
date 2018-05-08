''''''''''''''''''''''''''
# Title: Multi label classifier from scratch
#Author: https://gist.github.com/fchollet Fchollet
# Site owner gist.github.com
# Date: March 4 2017
# Code Version: f35fbc80e066a49d65f1688a7e99f069
# Availability https://gist.github.com/fchollet/f35fbc80e066a49d65f1688a7e99f069
#Modified - train and test data directories, train and test samples etc.
#
''''''''''''''''''''''''''
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

trainData = '../../fingerprintsdataset/train/'
testData = '../../fingerprintsdataset/test/'
nb_train_samples = 2800
nb_validation_samples = 1200
epochs = 50
batch_size = 16
#img width x height x 3 rgb channels
input_shape = (32, 32, 3)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    trainData,
    target_size=(32, 32),
    batch_size=batch_size,
    class_mode='binary')

trainGenerator = test_datagen.flow_from_directory(
    testData,
    target_size=(32, 32),
    batch_size=batch_size,
    class_mode='binary')

model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=trainGenerator,
    validation_steps=nb_validation_samples // batch_size)

model.save_weights('model_weights.h5')
model.save('model_keras.h5')