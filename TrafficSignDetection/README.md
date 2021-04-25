# Traffic-Sign-Detection
Road Sign Detection using Neural Network

Dataset from: https://bitbucket.org/jadslim/german-traffic-signs

## Description:
Fine tuning model

- Accuracy is not as high as we would like
- Our network seems to be overfitting our training data

## To improve accuracy
- Decrease the learning rate allowing the model to learn more slowly but more effectively we increased (changing Adam(lr = 0.01 TO 0.001)
- Increased number of filters in our convolutional layers from 30 to 60 and 15 to 30 
 as well as number of convolutional layers to allow for more eddective feature extraction
- Added a dropout layer to prevent overfitting of our data 

- Validation must be lesser than training data in graph for loss
- Validation must be higher than training data in graph for accuracy

## Another technique to improve model training process
- Data Augmentation (useful because it allows our model to look at each image)
