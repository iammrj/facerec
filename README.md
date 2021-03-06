facerec
=======

Python based framework for OpenCV's Fisher faces

Example
========

 - Train the recognizer, predict few results and save data

``` python

from facerec import FaceRecognizer, ImageSet, LabelSet, concatenate

recognizer = FaceRecognizer()
img1 = ImageSet("Female_faces")
label1 = LabelSet("Female", img1)
img2 = ImageSet("Male_faces")
label2 = LabelSet("Male", img2)

imgs = concatenate(img1, img2)
labels = concatenate(label1, label2)
recognizer.train(imgs, labels)

img = ImageSet("Test_images")
print recognizer.predict(img)
recognizer.save("gender.xml")
```
 - Load data and predict.

``` python
recognizer = FaceRecognizer()
recognizer.load("gender.xml")
img = ImageSet("Test_images")
print recognizer.predict(img)
```
 - Crop faces from the image (multiple faces in one image support added)

``` python

imgs = ImageSet("images with faces")
faces = imgs.cropFaces("cascadefile.xml")
# or
# faces = imgs.cropFaces() # to use the default cascade file included
# faces is ImageSet object
faces.show()
```
 -  Show Images

``` python
img = ImageSet("image_folder/")
img.show(delay=500) # This uses default opencv display.
# delay is in milliseconds
```