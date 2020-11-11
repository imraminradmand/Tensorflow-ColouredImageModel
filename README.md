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

<img width="559" alt="Screen Shot 2020-11-10 at 11 23 09 PM" src="https://user-images.githubusercontent.com/69999501/98777160-7984e900-23ad-11eb-9544-9318867bf701.png">

Info on this model can be found at: https://www.cs.toronto.edu/~kriz/cifar.html

# The model
In this model I have decided to try and do the same thing I did in my greyscale model except with coloured image and images of actual things rather than numbers.
CIFAR10 was my best bet since it gave me a variety of images in different categories to work with and they were actually coloured so it was something new to try.
Process was very similar to the greyscale model so I was able to get it done fairly quickly since I had figured the greyscale one out earlier.

# Metrics of the model

Below you can see the graphs of loss, and acuracy. Followed with a confusion matrix and a heamap to show us where the model lacked. (Model confuses dogs with cats sometimes)
Acurracy is fairly good sitting at a 65%, considering the model has a 1/10 chance of getting the image category right.

<img width="400" alt="Screen Shot 2020-11-10 at 11 12 17 PM" src="https://user-images.githubusercontent.com/69999501/98777129-70941780-23ad-11eb-9d98-0d1efd59a267.png">
<img width="399" alt="Screen Shot 2020-11-10 at 11 12 24 PM" src="https://user-images.githubusercontent.com/69999501/98777134-71c54480-23ad-11eb-826f-023d6764e8f2.png">
<img width="455" alt="Screen Shot 2020-11-10 at 11 13 28 PM" src="https://user-images.githubusercontent.com/69999501/98777137-72f67180-23ad-11eb-8148-21a9b978d666.png">
<img width="560" alt="Screen Shot 2020-11-10 at 11 18 57 PM" src="https://user-images.githubusercontent.com/69999501/98777138-738f0800-23ad-11eb-8070-931bc5bd259a.png">



# Model results
Here you can see that I chose a random index for my test set to pass in to see if the model will actually perform. 
The index I chose turned out to be a car, which the model does a very good job at predicting considering there is also a truck category in the CIFAR10 dataset
I then plotted the data at that index so I know what I'm looking for.
The model predicted the image to be in category at index 1 which would be a car, and thats what the plot is showing so model predicted right, and I didn't just wait 20 minutes for my model to train for nothing :)

<img width="503" alt="Screen Shot 2020-11-10 at 11 22 31 PM" src="https://user-images.githubusercontent.com/69999501/98777170-80136080-23ad-11eb-8d9c-a1c4b970040e.png">
<img width="437" alt="Screen Shot 2020-11-10 at 11 22 38 PM" src="https://user-images.githubusercontent.com/69999501/98777171-80abf700-23ad-11eb-976d-e2aace817aa9.png">

