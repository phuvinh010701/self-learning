# CNN in tensorflow

---
<pre>

/tmp/cats-v-dogs/training

/tmp/cats-v-dogs/validation

/tmp/cats-v-dogs/training/cats

/tmp/cats-v-dogs/training/dogs

/tmp/cats-v-dogs/validation/cats

/tmp/cats-v-dogs/validation/dogs
</pre>

<pre>
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1/255)

TRANING_DIR = 'path to folder training'
BATCH_SIZE = 'num image in one iteration'
CLASS_MODE = 'image mode (rgb) (grayscale/binary)'
TARGET_SIZE = 'size image (, ,)'
train_generator = train_datagen.flow_from_directory(directory=TRAINING_DIR,
                                                      batch_size=BATCH_SIZE,
                                                      class_mode=MODE,
                                                      target_size=SIZE)

## simple cnn
model = tf.keras.models.Sequential([ 
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (2,2), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
  ])

  
model.compile(optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy']) 

history = model.fit(train_generator,
                    epochs=15,
                    verbose=1,
                    validation_data=validation_generator)
<pre>