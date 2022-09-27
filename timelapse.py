from picamera import PiCamera
import time


interval = 1
frame = 0

camera = PiCamera()
camera.resolution = (4056, 3040)
camera.start_preview()
time.sleep(2)

while True:
    camera.capture('/home/alisson/timelapses/photos/season_%04d.jpg' % (frame))
    frame = frame + 1
    time.sleep(interval)
