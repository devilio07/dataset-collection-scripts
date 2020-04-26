import cv2
import os
import sys
import argparse
from imutils.video import VideoStream
import time

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--feature", required=True,
    help="To tell the finger count in words")
ap.add_argument("-i", "--count", required=True,
    help="# of images to be captured.")
ap.add_argument("-o", "--output", required=True,
    help="Path to the output directory")

args = vars(ap.parse_args())

try:
    Label_name = args["feature"]
    num_samples = int(args["count"])
    data_set_dir = args["output"]
except:
    print("Arguments missing.")
    exit(-1)

IMAGE_CLASS_PATH = os.path.join(data_set_dir,Label_name)
try:
    os.mkdir(IMAGE_CLASS_PATH)
except FileExistsError:
    print("{} directory already exists".format(IMAGE_CLASS_PATH))
    print("Images gathered will be saved here.")

print("[INFO] starting video stream ...")
vs = VideoStream(src=0).start()
# Warming up the camera with some delay
time.sleep(2.0)
total_count = 0
start = False

while True:
    frame = vs.read()
    orig = frame.copy()

    if total_count == num_samples:
        break

    cv2.rectangle(frame, (100,100), (100+256, 100+256), (255,0,0), 2)
    
    
    key = cv2.waitKey(1) & 0xFF 

    if key == ord("s"):
        start = True

    elif key == ord("q"):
        break

    if start:
        roi = frame[100:356, 100:356]
        save_path = os.path.join(IMAGE_CLASS_PATH, "{}.png".format(total_count))
        cv2.imwrite(save_path, roi)
        total_count += 1
        time.sleep(0.01)

    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(frame, "Collecting {}".format(total_count), (98,98), font, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)

print("[INFO] {} images stored".format(total_count))
print("[INFO] cleaning up......")

cv2.destroyAllWindows()
vs.stop()
