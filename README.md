# Tensorflow-ColouredImageModel

# DataSet
In this model I have used the CIFAR10 dataset for coloured images to create my model
Model has 10 categoreis and each category has 10 different images, of the same object or animal, in it.

- airplane : 0
- automobile : 1
- bird : 2
- cat : 3
- deer : 4
- dog : 5
- frog : 6
- horse : 7
- ship : 8
- truck : 9

image

Info on this model can be found at: https://www.cs.toronto.edu/~kriz/cifar.html

# The model
In this model I have decided to try and do the same thing I did in my greyscale model except with coloured image and images of actual things rather than numbers.
CIFAR10 was my best bet since it gave me a variety of images in different categories to work with and they were actually coloured so it was something new to try.
Process was very similar to the greyscale model so I was able to get it done fairly quickly since I had figured the greyscale one out earlier.

# Metrics of the model

Below you can see the graphs of loss, and acuracy. Followed with a confusion matrix and a heamap to show us where the model lacked.
Acurracy is fairly good sitting at a 65%, considering the model has a 1/10 chance of getting the image category right.




# Model results
Here you can see that I chose a random index for my test set to pass in to see if the model will actually perform. 
The index I chose turned out to be a car, which the model does a very good job at predicting considering there is also a truck category in the CIFAR10 dataset
I then plotted the data at that index so I know what I'm looking for.
The model predicted the image to be in category at index 1 which would be a car, and thats what the plot is showing so model predicted right, and I didn't just wait 20 minutes for my model to train for nothing :)


