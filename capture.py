# import the necessary packages
import cv2
import os

name = input("Please enter ID: ")
cam = cv2.VideoCapture(0)
total = 0

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("k"):
        p = os.path.sep.join(["dataset/", name, "{}.png".format(
            str(total).zfill(5))])
        if not os.path.isdir("dataset/" + name):
            os.mkdir("dataset/" + name)
        cv2.imwrite(p, frame)
        print(p)
        total += 1

    # if the `q` key was pressed, break from the loop
    elif key == ord("q"):
        break
