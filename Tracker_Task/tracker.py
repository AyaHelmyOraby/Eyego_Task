import cv2

Live_video = cv2.VideoCapture(0)

if not Live_video.isOpened():
    raise IOError("Live video is not opened")

tracker_window = "Live tracker"
cv2.namedWindow(tracker_window)

well, frame = Live_video.read()

select_box = cv2.selectROI(tracker_window, frame, fromCenter=False)

Live_Tracker = cv2.TrackerCSRT_create()
Live_Tracker.init(frame, select_box)

while True:
    well, frame = Live_video.read()

    if not well:
        break

    well, select_box = Live_Tracker.update(frame)

    if well:
        x, y, width, height = map(int, select_box)

        cv2.rectangle(
            frame,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            3
        )

    else:
        cv2.putText(
            frame,
            "Tracker lost",
            (50, 80),
            0.75,
            (0, 0, 255),
            3
        )

    cv2.imshow(tracker_window, frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

Live_video.release()
cv2.destroyAllWindows()