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