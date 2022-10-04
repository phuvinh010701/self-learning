1.
Question 1
Which of the following do you agree with?

	Face recognition requres K comparisons of a person's face

2.
Question 2
You want to build a system that receives a person's face picture and determines if the person is inside a workgroup. You have pictures of all the faces of the people currently in the workgroup, but some members might leave, and some new members might be added. Which of the following do you agree with?

	This can be considered a one-shot learning task
	It will be more efficient to learn a function d(img1, img2) for this task

3.
Question 3
In order to train the parameters of a face recognition system, it would be reasonable to use a training set comprising 100,000 pictures of 100,000 different persons.

	False

4.
Question 4
Triplet loss: is larger in which of the following cases?

	When the encoding of A is closer to the encoding of N than to the encoding of P
5.
Question 5
Consider the following Siamese network architecture:

	The upper and lower neural networks depicted have exactly the same parameters, but the outputs are computed independently for each image

6.
Question 6
You train a ConvNet on a dataset with 100 different classes. You wonder if you can find a hidden unit which responds strongly to pictures of cats. (I.e., a neuron so that, of all the input/training images that strongly activate that neuron, the majority are cat pictures.) You are more likely to find this unit in layer 4 of the network than in layer 1.

	True

7.
Question 7
Neural style transfer uses images Content C, Style S. The loss function used to generate image G is composed of which of the following: (Choose all that apply.)

	Jstyle that compared S and G
	Jcontent that compared C and G
8.
Question 8
In the deeper layers of a ConvNet, each channel corresponds to a different feature detector. The style matrix G^{[l]}
  measures the degree to which the activations of different feature detectors in layer ll vary (or correlate) together with each other.
	 
	 True

9.
Question 9
In neural style transfer, we can't use gradient descent since there are no trainable parameters. True/False?

	False

10.
Question 10
You are working with 3D data. The input "image" has size 32 \times 32 \times 32 \times 332×32×32×3, if you apply a convolutional layer with 16 filters of size 4 \times 4 \times 44×4×4, zero padding and stride 1. What is the size of the output volume?

	29x29x29x16

