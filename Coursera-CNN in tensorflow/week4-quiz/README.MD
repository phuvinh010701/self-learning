1.
Question 1
The diagram for traditional programming had Rules and Data In, but what came out?

1 point

(*)Answers


Binary


Machine Learning


Bugs

2.
Question 2
Why does the DNN for Fashion MNIST have 10 output neurons?

1 point

To make it train 10x faster


To make it classify 10x faster


Purely Arbitrary


(*)The dataset has 10 classes

3.
Question 3
What is a Convolution? 

1 point

A technique to make images smaller


A technique to make images larger


(*)A technique to extract features from an image


A technique to remove unwanted images

4.
Question 4
Applying Convolutions on top of a DNN will have what impact on training?

1 point

It will be slower


It will be faster


There will be no impact


(*)It depends on many factors. It might make your training faster or slower, and a poorly designed Convolutional layer may even be less efficient than a plain DNN!

5.
Question 5
What method on an ImageGenerator is used to normalize the image? 

1 point

normalize


flatten


rezize()


(*)rescale

6.
Question 6
When using Image Augmentation with the ImageDataGenerator, what happens to your raw image data on-disk.

1 point

A copy will be made, and the copies are augmented


A copy will be made, and the originals will be augmented


(*)Nothing


The images will be edited on disk, so be sure to have a backup

7.
Question 7
Can you use Image augmentation with Transfer Learning? 

1 point

No - because the layers are frozen so they can't be augmented


(*)Yes. It's pre-trained layers that are frozen. So you can augment your images as you train the bottom layers of the DNN with them

8.
Question 8
When training for multiple classes what is the Class Mode for Image Augmentation?

1 point

class_mode='multiple'


class_mode='non_binary'


(*)class_mode='categorical'


class_mode='all'