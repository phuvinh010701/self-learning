1.
Question 1
What do you think applying this filter to a grayscale image will do?

    Detect horizontal edges.

2.
Question 2
Suppose your input is a 300 by 300 color (RGB) image, and you are not using a convolutional network. If the first hidden layer has 100 neurons, each one fully connected to the input, how many parameters does this hidden layer have (including the bias parameters)?

    27,000,100

3.
Question 3
Suppose your input is a 256 by 256 color (RGB) image, and you use a convolutional layer with 128 filters that are each 7\times 77×7. How many parameters does this hidden layer have (including the bias parameters)?

    18944

4.
Question 4
You have an input volume that is 121 \times 121 \times 16121×121×16, and convolve it with 32 filters of 4 \times 44×4, using a stride of 3 and no padding. What is the output volume?

    40x40x32

5.
Question 5
You have an input volume that is 15x15x8, and pad it using “pad=2”. What is the dimension of the resulting volume (after padding)?

    19x19x8

Question 6
You have an input volume that is 63x63x16, and convolve it with 32 filters that are each 7x7, and stride of 1. You want to use a “same” convolution. What is the padding?

    3 (63 - 7 + 1) / 2

7.
Question 7
You have an input volume that is 128x128x12, and apply max pooling with a stride of 4 and a filter size of 4. What is the output volume?

    32x32x12 

8.
Question 8
Which of the following are hyperparameters of the pooling layers? (Choose all that apply)

    max or average
    stride

9.
Question 9
Which of the following are true about convolutional layers? (Check all that apply)

    Convolutional layers provide sparsity of connections
    It allows a feature detector to be used in multiple locations throughout the whole input volume

10.
Question 10
The following image depicts the result of a convolution at the right when using a stride of 1 and the filter is shown right next.

    It depends on the pixels enclosed by the green square