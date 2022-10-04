1.
Question 1
You are building a 3-class object classification and localization algorithm. The classes are: pedestrian (c=1), car (c=2), motorcycle (c=3). What should yy be for the image below? Remember that “?” means “don’t care”, which means that the neural network loss function won’t care what the neural network gives for that component of the output. Recall y = [p_c, b_x, b_y, b_h, b_w, c_1, c_2, c_3]

	y = [0, ?, ?, ?, ?, ?, ?, ?, ?]

2.
Question 2
You are working on a factory automation task. Your system will see a can of soft-drink coming down a conveyor belt, and you want it to take a picture and decide whether (i) there is a soft-drink can in the image, and if so (ii) its bounding box. Since the soft-drink can is round, the bounding box is always square, and the soft-drink can always appear the same size in the image. There is at most one soft-drink can in each image. Here are some typical images in your training set:

	False, we dont need bh, bw since the cans are all the same size

3.
Question 3
When building a neural network that inputs a picture of a person's face and outputs N landmarks on the face (assume that the input image contains exactly one face), which is true about \hat{y}^{(i)} 

	y^(i) has shape (2N, 1)

4.
Question 4
When training one of the object detection systems described in the lectures, you need a training set that contains many pictures of the object(s) you wish to detect. However, bounding boxes do not need to be provided in the training set, since the algorithm can learn to detect the objects by itself.

	False
	
5.
Question 5
What is the IoU between the red box and the blue box in the following figure? Assume that all the squares have the same measurements.

	3/7

6.
Question 6
Suppose you run non-max suppression on the predicted boxes nelow. The parameters you use for non-max suppression are that boxes with probability \leq 0.7≤0.7 are discarded, and the IoU threshold for deciding if two boxes overlap is 0.50.5.

After non-max suppression, only three boxes remain. True/False?
	
	True

7.
Question 7
Which of the following do you agree with about the use of anchor boxes in YOLO? Check all that apply.

	Ech object is assigned to the grid cell that contains that object's midpoint
	Ech object is assigned to an anchor box with the highest IoU inside the assigned cell

8.
Question 8
What is Semantic Segmentation?

	Locating objects in an image by predicting each pixel as to which class it belongs to

9.
Question 9
Using the concept of Transpose Convolution, fill in the values of X, Y and Z below.

(padding = 1, stride = 2)

[[1, 3], [2, 4]]
[[1, 0, 1], [0, 0, 0], [1, 0, 1]]

	X = 10, Y = 0, Z = 6



	

