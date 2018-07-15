import face_recognition
import pickle
import cv2

data = pickle.loads(open("encodings.pkl", "rb").read())
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 1)
nospy = cv2.imread("no-spy.jpg")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Cam Read Error")
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            name = max(counts, key=counts.get)

        names.append(name)

    # for ((top, right, bottom, left), name) in zip(boxes, names):
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    #     y = top - 15 if top - 15 > 15 else top + 15
    #     cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    if list(filter(lambda n: n != "adam", names)):
        cv2.namedWindow("WARNING", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("WARNING", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("WARNING", nospy)
    else:
        cv2.destroyWindow("WARNING")

    # cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
