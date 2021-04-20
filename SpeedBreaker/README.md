Training and Validation Images from : https://rb.gy/aecowf

Download the Trained Model (for prediction generation) from : https://rb.gy/eoylvz

Make sure you have the following installed:
1. Tensorflow
2. Matplotlib
3. Numpy
4. Pillow

Steps to get the training script running on your system:
1. Install the above mentioned libraries
2. Import the training and validation dataset from the given link
3. Update the "train_path" and "test_path" acoordingly
4. Specify where to save the model
5. Run the scipt

Steps to get the prediction script running on your system:
1. Make sure the required libraries are properly installed
2. Make sure you have the "modelTrained" folder
3. Put all the pictures (make sure they are in the JPEG format) you want to run the prediction for in a folder and provide its path in the "path_of_dir" string
4. Run the cell, the scipt should run prediction on all the images in the specified directory


About:
This is a simple speed detector model(supervised learning) trained using transfer learning(better accuracy and smaller training times) on VGG16 architecture(body), pre-weighed on the ImageNet dataset.
The Head consists of a Dropout layer(20%), and a simple dense layer with softmax for output.

Accuracy : 99% on training data and 100% on validation data (to be verified)

Real life testing : Pending

