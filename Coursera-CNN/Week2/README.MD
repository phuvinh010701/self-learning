1.
Question 1
Which of the following do you typically see in a ConvNet? (Check all that apply.)

	FC layers in the last few layers
	Multiple CONV layers followed by a POOL layer
	
2.
Question 2
In LeNet - 5 we can see that as we get into deeper networks the number of channels increases while the height and width of the volume decreases. True/False?

	True

3.
Question 3
Based on the lectures, in the following picture, which curve corresponds to the expected behavior in theory, and which one corresponds to the behavior we get in practice? This when using plain neural networks.

	The green one depicts the results in theory, and the blue one the reality

4.
Question 4
The following equation captures the computation in a ResNet block. What goes into the two blanks above? 

	a[l] and 0, respectively

5.
Question 5
Adding a ResNet block to the end of a network makes it deeper. Which of the following is true?

	The performance of the networks doesn't get hurt since the ResNet block can easily approximate the identity funciton
	
6.
Question 6
Suppose you have an input volume of dimension n_H x n_W x n_C. Which of the following statements do you agree with? (Assume that the “1x1 convolutional layer” below always uses a stride of 1 and no padding.) 

	You can use a 1x1 convolutional layer to reduce nC but not nH and nW
	You can use a 2D pooling layer to reduce nH, nW, but not nC
	
7.
Question 7
Which of the following are true about bottleneck layers? (Check all that apply)

	By adding these layers we can reduce the computational cost in the inception modules
	The use of bottlenecks doesn't seem to hurt the performance of the network
	
8.
Question 8
When having a small training set to construct a classification model, which of the following is a strategy of transfer learning that you would use to build the model?

	Use an open-source network trained in a larger dataset freezing the layers and re-train the softmax layer
	
9.
Question 9
Which of the following are true about Depthwise-separable convolutions? (Choose all that apply)

	The pointwise convolution convolves the input volume with 1x1 filters
	The depthwise convolution convolves each channel in the input colume with a separate filter.
	
10.
Question 10
Suppose that in a MobileNet v2 Bottleneck block the input volume has shape 64 \times 64 \times 1664×64×16. If we use 3232 filters for the expansion and 1616 filters for the projection. What is the size of the input and output volume of the depthwise convolution, assuming a pad='same'?

	64x64x32 64x64x32

