# Real-Time Object Tracker

A simple Python program that uses the webcam to track an object in real time.

First, the program shows the first webcam frame and lets the user select an object using a bounding box. The selected object is then tracked using the CSRT tracker from OpenCV.

## How It Works

1. Open the webcam.
2. Take the first frame.
3. Select the object with the mouse.
4. Start the CSRT tracker.
5. Read new frames from the webcam.
6. Update the object's position.
7. Draw a box around the object.
8. Press `q` to stop the program.

CSRT is used because it usually gives better tracking results when the object changes size or moves compared with some faster trackers.

The program also checks both common OpenCV tracker locations:

```python
cv2.TrackerCSRT_create()
```

and, if needed:

```python
cv2.legacy.TrackerCSRT_create()
```

This can help when using different OpenCV versions.

## Requirements

* Python 3.7 or newer
* A webcam
* `opencv-contrib-python`

Install OpenCV with:

```bash
pip install opencv-contrib-python
```

## Run the Program

```bash
python tracker.py
```

A window will open with the webcam.

Select the object you want to track and press **Enter** or **Space**.

The program will then follow the object and draw a rectangle around it.

Press **q** to close the program.

## Troubleshooting

### CSRT tracker not found

If you get:

```text
AttributeError: module 'cv2' has no attribute 'TrackerCSRT_create'
```

make sure you installed the contrib version:

```bash
pip uninstall opencv-python
pip install opencv-contrib-python
```

### Camera does not open

Check that:

* The webcam is connected.
* Another program isn't already using it.
* Camera permission is enabled for your Python/IDE.

## Project

This project is a basic example of real-time object tracking using OpenCV.
