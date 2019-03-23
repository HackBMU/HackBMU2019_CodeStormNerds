<h1 align="center">Crack Seals</h1>

This is an initiative to deal with problems caused by road cracks .

<h5>General Overview</h5>
This involves detection of cracks on the road and giving the notifications to the user
on the basis of detection of holes whether the person has to drive slow or not.Not only this 
we are also embedding the location of the potholes in the maps so that other users may get notified for the precautions

<h4>Procedure</h4>
<h6>Step 1.</h6>
Our first step involves detection of certain portholes on the road.This module detect the portholes which comprises
of basic substeps.
	Step 1.1
		This steps involves taking of dataset of images which basically are training and testing images so as
		to predict the accuracy of the model which involves classification of certain images by separating the 
		sets so for classification we uses a library named as keras which is a mathematical computation library
	
	Step 1.2 
		We are increasing our images by augmenting the images by changing the shapes of images and based on that 
		giving our model a base to train on more images and then based on the classification of our model we are 
		classifying the images of cracks or non cracks images.So as to train our model perfectly so that it does
		not gets overfitted.
	Step 1.3
		Then after that for the classification purpose we are creating the convolution layers.Then after general steps 
		of pooling of an images followed neural network then feeding that network into sigmoid function so as to separate
		our dataset and then on the basis of that we are fitting our model to certain images based on their train and test
		then we build our model based on the pixels. So we use SGD optimiser to optimise our model and then calculating the 
		losses
		![alt text](  https://www.google.com/imgres?imgurl=https%3A%2F%2Fadeshpande3.github.io%2Fassets%2FCover.png&imgrefurl=https%3A%2F%2Fadeshpande3.github.io%2FA-Beginner%2527s-Guide-To-Understanding-Convolutional-Neural-Networks%2F&docid=kx37uOScobcsjM&tbnid=5MXH4b48-olmkM%3A&vet=10ahUKEwjH0N6ks5jhAhVk73MBHawxCVEQMwhZKAAwAA..i&w=1000&h=341&client=ubuntu&bih=639&biw=1366&q=convolution%20networks&ved=0ahUKEwjH0N6ks5jhAhVk73MBHawxCVEQMwhZKAAwAA&iact=mrc&uact=8)
		
<h6>Step 2</h6>
Our Second step inolves knowing our location so as to notify the users based on the detection of portholes as thereby giving the location of certain
portholes for prevention of another users.

<h6>Step 3</h6>
Embedding it into maps API so as to give another user preference or accesibilty that he should be safe while going from that road

<h4>Advantages</h4>
	1. Before crossing the roads we can finds the crack on that and thereby recommending users to go for the safer path.
	2. It's advantages outlies for the blind people and thereby premeasuring the safe path to follow through
	3. Notifies the governement to seal that particular hole so that they can fill that particular road
	4. Reduces Road Accidents

<h4>Future Scope</h4>
In the future, we plan to conduct a survey on the different techniques available for invasive method-based crack detection as this works presents an extensive study over the noninvasive methods of crack detection.Also, Keeping in mind the loss and ill-effects of this never ending problem we are aiming to work hard and more sincerely in order to get guidance by experienced communities which in future would help us to expand the domain of our knowledge in the same field.  

	 		
 
