1.
Question 1
How do you use Image Augmentation in TensorFLow

1 point

With the tf.augment API


(*)Using parameters to the ImageDataGenerator


You have to write a plugin to extend tf.layers


With the keras.augment API

2.
Question 2
If my training data only has people facing left, but I want to classify people facing right, how would I avoid overfitting?

1 point

(*)Use the ‘horizontal_flip’ parameter


Use the ‘flip’ parameter and set ‘horizontal’


Use the ‘flip’ parameter


Use the ‘flip_vertical’ parameter around the Y axis

3.
Question 3
When training with augmentation, you noticed that the training is a little slower. Why?

1 point

Because there is more data to train on


Because the training is making more mistakes


Because the augmented data is bigger


(*)Because the image processing takes cycles

4.
Question 4
What does the fill_mode parameter do?

1 point

There is no fill_mode parameter


It creates random noise in the image


(*)It attempts to recreate lost information after a transformation like a shear


It masks the background of an image

5.
Question 5
When using Image Augmentation with the ImageDataGenerator, what happens to your raw image data on-disk.

1 point

It gets overwritten, so be sure to make a backup


A copy is made and the augmentation is done on the copy


(*)Nothing, all augmentation is done in-memory


It gets deleted

6.
Question 6
How does Image Augmentation help solve overfitting?

1 point

It slows down the training process


(*)It manipulates the training set to generate more scenarios for features in the images


It manipulates the validation set to generate more scenarios for features in the images


It automatically fits features to images by finding them through image processing techniques

7.
Question 7
When using Image Augmentation my training gets...

1 point

(*)Slower


Faster


Stays the Same


Much Faster

8.
Question 8
Using Image Augmentation effectively simulates having a larger data set for training.

1 point

False


(*)True