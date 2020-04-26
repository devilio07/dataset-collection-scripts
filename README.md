# Some of my personal Data collection scripts for Computer Vision with DL

For training any Deep Learning model an architrcture is indeed important.But what holds the equal necessity is the Data you're going to train upon.

Recently I was working upon ResNe50 a deep 50 layer Residual Network for learning hand gestures.
Now since I didn't want to grab images from the internet, I decided to collect my own.

So I just decided to create my own Python Script and OpenCV to collect some data.

dataset_collection_gestures.py is an fully automated data collection script. Just make sure you've a working Web-Cam.

## Before you jump in:
  1. Script is to collect images of a gesture you make by your hand (you can use it for anything).
  2. feaure : basically name of the directory that will be containing all the images.
  3. count : #of images you want to capture.
  4. output : path for the output to be saved.
  5. Images inside the given blue box only will be captured.
  6. Image size is 256 x 256 pixels. (you can change occording to you)
  7. Time delay between consecutive images can be set manually.
  
## How to Use:
  In the Terminal or Command prompt (depending upon the OS you're using.)
  Type : 
    python dataset_collection_gestures.py --feature <name of the gesture you'll make to be captured> --count <#of images you       want to capture> --output <where you want to save the output folder>
