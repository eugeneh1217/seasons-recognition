from data import data
import InputData

from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.resnet50 import ResNet50
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, InputLayer
from keras.models import Sequential
from keras import optimizers
import keras

IMG_HEIGHT, IMG_WIDTH = (300, 300)

input_data = InputData(data).resize((IMG_HEIGHT, IMG_WIDTH)).split(.7)

# data generators that augments data live
training_data_gen = ImageDataGenerator(rescale=1./255, zoom_range=0.3, rotation_range=50, width_shift_range=0.2,
                                             height_shift_range=0.2, shear_range=0.2, horizontal_flip=True,
                                             fill_mode='nearest')
testing_data_gen = ImageDataGenerator(rescale=1./255)

# one-hot encoding for non-binary classification
for label_index in range(len(input_data.train_y)):
    hot_encoding = [0] * len(data.categories)
    hot_encoding[data.categories.index(input_data.train_y[label_index])] = 1
    input_data.train_y[label_index] = list(hot_encoding)

# set up generators with encodings
train_generator = training_data_gen.flow(input_data.train_x, train_labels_enc, batch_size=30)
test_generator = testing_data_gen.flow(input_data.test_x, test_labels_enc, batch_size=30)

# build model
resnet50 = ResNet50(include_top=False, weights='imagnet', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3))
resnet = Model(resnet.input, output=keras.layers.Flatten() (resnet.layers[-1].output))

for layers in resnet.layers:
    layer.trainable = False

# resnet.summary()

model = Sequential()

model.add(resnet)
model.add(Dense(512, activation='relu', input_dim=(IMG_HEIGHT, IMG_WIDTH)))
model.add(Dropout(0.3))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(4, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=2e-5), metrics=['accuracy'])

# train model

history = model.fit_generator(train_generator,
                              steps_per_epoch=100,
                              epochs=100,
                              test_data=test_generator,
                              validation_steps=50,
                              verbose=1)

model.save('weather_recog_weights.h5')
