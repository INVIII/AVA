Training and Validation Images from : https://drive.google.com/drive/folders/1dZbepocmH1wPpyQaOM2FCfAhuI26qU8l?usp=sharing
Download the Trained Model (for prediction generation) from : https://drive.google.com/drive/folders/1j3SoDdOdQE_VER9D29gqv4ZYyh9c0ijW?usp=sharing

Make sure you have the following installed:
1. Tensorflow
2. Matplotlib
3. Numpy
4. Pillow

About:
This is a simple speed detector model(supervised learning) trained using transfer learning(better accuracy and smaller training times) on VGG16 architecture(body), pre-weighed on the ImageNet dataset.
The Head consists of a Dropout layer(20%), and a simple dense layer with softmax for output.

Accuracy : 99% on training data and 100% on validation data (to be verified)

Real life testing : Pending
