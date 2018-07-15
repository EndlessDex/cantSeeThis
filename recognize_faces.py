import os
import pickle
import time

import cv2
import face_recognition
import numpy as np
from imutils import paths


def capture_faces():
    name = input("Please enter ID: ")
    cam = cv2.VideoCapture(0)
    total = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        # Convert opencv format (BGR) to dlib format (RGB)
        rgb_small_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb_small_frame)

        for top, right, bottom, left in boxes:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

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


def encode_faces():
    # Get all images in dataset
    image_paths = list(paths.list_images("dataset"))

    known_encodings = list()
    known_names = list()
    for i, image_path in enumerate(image_paths):
        print("[INFO] processing image {}/{}".format(i + 1, len(image_paths)))
        name = image_path.split(os.path.sep)[-2]

        # load the input image and convert it from BGR (OpenCV ordering) to dlib ordering (RGB)
        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(name)

    data = {"encodings": known_encodings, "names": known_names}
    with open("encodings.pkl", "wb") as f:
        f.write(pickle.dumps(data))


def recognize_faces(scale, show=False, block=True):
    data = pickle.loads(open("encodings.pkl", "rb").read())
    cam = cv2.VideoCapture(0)
    nospy = cv2.imread("no-spy.jpg")

    while True:
        start_time = time.time()
        ret, frame = cam.read()
        if not ret:
            print("Cam Read Error")
            break

        # Resize for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=scale, fy=scale)

        # Convert opencv format (BGR) to dlib format (RGB)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Get face encodings
        boxes = face_recognition.face_locations(rgb_small_frame)
        encodings = face_recognition.face_encodings(rgb_small_frame, boxes)

        names = list()
        for encoding in encodings:
            matches = np.array(face_recognition.compare_faces(data["encodings"], encoding))
            name = "Unknown"

            if any(matches):
                counts = {}
                for idx in [i for (i, b) in enumerate(matches) if b]:
                    name = data["names"][idx]
                    counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)
            names.append(name)

        if show:
            for ((top, right, bottom, left), name) in zip(boxes, names):
                top = int(top / scale)
                right = int(right / scale)
                bottom = int(bottom / scale)
                left = int(left / scale)
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
            cv2.imshow("Frame", frame)

        if block:
            if list(filter(lambda n: n == "00001", names)):
                cv2.namedWindow("WARNING", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("WARNING", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("WARNING", nospy)
            else:
                cv2.destroyWindow("WARNING")

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

        time.sleep(max(0.0, 1.0 - (time.time() - start_time)))

if __name__ == '__main__':
    # capture_faces()
    # encode_faces()
    recognize_faces(0.5)
