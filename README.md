# alphabet-recognition-based-music-player
The repository is of a project of deep learning based on convolutional neural networks for alphabet recognition. 
This is a tkinter based GUI application with CNN network for alphabet recognition and help in the game of ANTAKSHARI

DATASET
The dataset comprises of around 13-15 thousand images of handrwritten capital english alphabets obtained from Kaggle. The data is available in csv format.

FLOW OF FILES
1. 01-csv_to_images: the csv file of images is converted to images for convnet
2. 02-create_model: code for creating the CNN model
3. 03-load_model: The model is loaded and tested 
4. 04-paintApp: a tkinter gui is created for creating a paint window to let the user draw                 alphabet of their choice
5. 05-music_player: another tkinter based gui for selection of song from offline playlist of 		    the user starting from the painted alphabet
6. 06-alphabet_recognition: It is the combined code for all the above mentioned codes.

