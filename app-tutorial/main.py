import numpy as np
import cv2
from waggle.data.vision import Camera


def compute_mean_color(image):
    return np.mean(image, (0, 1)).astype(float)


def main():
    # open camera and take snapshot
    with Camera() as camera:
        snapshot = camera.snapshot()

    # compute mean color
    mean_color = compute_mean_color(snapshot.data)

    # print mean color
    print(mean_color)


if __name__ == "__main__":
    main()