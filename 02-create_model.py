from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Classifier
classifier = Sequential()


# Step 1 - Concolutional
classifier.add(Convolution2D(32,3,3, input_shape = (28,28,3), activation='relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))

# Adding a second convolutional layer
classifier.add(Convolution2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
 
# Adding a third convolutional layer
classifier.add(Convolution2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim = 128 , activation='relu'))
classifier.add(Dense(output_dim = 26, activation='softmax'))

# Compiling CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fitting CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.5,
                                   horizontal_flip = False)
 
training_set = train_datagen.flow_from_directory('data',
                                                 target_size = (28, 28),
                                                 batch_size = 50,
                                                 class_mode = 'categorical')



classifier.fit_generator(training_set,
                         samples_per_epoch = 351451,
                         nb_epoch = 30,
                         steps_per_epoch = 20)
classifier.save("model.h5")