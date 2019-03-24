#importing the libraries

from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils import build_montages
from imutils import paths
import numpy as np
import argparse
import random
import cv2


# load the pre-trained network
print("[INFO] loading pre-trained network...")
model = load_model("saved.model")
results=[]
def detect(gray,frame):
    
    image = cv2.resize(frame, (64, 64))
    image = image.astype("float") / 255.0
    # order channel dimensions (channels-first or channels-last)
    # depending on our Keras backend, then add a batch dimension to
    # the image
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # make predictions on the input image
    pred = model.predict(image)
    pred = pred.argmax(axis=1)[0]

    # an index of zero is the 'cracks' label while an index of
    # one is the 'uncracks' label
    label = "uncracks" if pred == 0 else "crack"
    color = (255, 0, 255) if pred == 0 else (255, 255, 0)

    # resize our original input (so we can better visualize it) and
    # then draw the label on the image
    orig = cv2.resize(frame, (1024, 1024))
    cv2.putText(orig, label, (3, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8,color, 2)

    return orig

cap=cv2.VideoCapture("http://192.168.43.1:8080/video")
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    # show the output montage
    #montage = build_montages(results, (1024, 1024), (1, 1))[0]
    #cv2.imshow("Results", montage)
    cv2.imshow("results",canvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyallwindows()


"""
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to out input directory of images")
ap.add_argument("-m", "--model", required=True,
	help="path to pre-trained model")
args = vars(ap.parse_args())

# load the pre-trained network
print("[INFO] loading pre-trained network...")
model = load_model(args["model"])

# grab all image paths in the input directory and randomly sample them
#imagePaths = list(paths.list_images(args["images"]))
#random.shuffle(imagePaths)
#imagePaths = imagePaths[:16]

# initialize our list of results
results = []
for p in imagePaths:
    # load our original input image
    orig = cv2.imread(p)

    # pre-process our image by converting it from BGR to RGB channel
    # ordering (since our Keras mdoel was trained on RGB ordering),
    # resize it to 64x64 pixels, and then scale the pixel intensities
    # to the range [0, 1]
    image = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (64, 64))
    image = image.astype("float") / 255.0
    # order channel dimensions (channels-first or channels-last)
    # depending on our Keras backend, then add a batch dimension to
    # the image
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # make predictions on the input image
    pred = model.predict(image)
    pred = pred.argmax(axis=1)[0]

    # an index of zero is the 'cracks' label while an index of
    # one is the 'uncracks' label
    label = "cracks" if pred == 0 else "uncracks"
    color = (255, 0, 255) if pred == 0 else (255, 255, 0)

    # resize our original input (so we can better visualize it) and
    # then draw the label on the image
    orig = cv2.resize(orig, (128, 128))
    cv2.putText(orig, label, (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,color, 2)

    # add the output image to our list of results
    results.append(orig)
# create a montage using 128x128 "tiles" with 4 rows and 4 columns
montage = build_montages(results, (128, 128), (4, 4))[0]
"""
