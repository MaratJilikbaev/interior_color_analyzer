import cv2
import numpy as np
import matplotlib.pyplot as plt


def extract_colors(image_name, num_colors, image_path='data/interiors/'):
    # Load the image
    image = cv2.imread(image_path + image_name)
    # Convert the image to the LAB color space
    image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)
    # Convert the pixels to floating point values
    pixels = np.float32(pixels)
    # Apply K-Means clustering to identify the dominant colors
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, palette = cv2.kmeans(pixels, num_colors, None, criteria, 10, flags)
    # Convert the palette values back to 8-bit integers
    palette = np.uint8(palette)
    # Convert the palette values back to the BGR color space
    bgr_palette = []
    for color in palette:
        lab_image = np.uint8([[color]])
        bgr_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)
        bgr_palette.append(bgr_image[0][0])
    bgr_palette = np.array(bgr_palette)
    # Calculate the percentage of each color
    color_counts = np.unique(labels, return_counts=True)[1]
    color_percentages = (color_counts / pixels.shape[0]) * 100
    return bgr_palette, color_percentages


def create_pie_chart(colors, percentages, filename):
    fig, ax = plt.subplots()
    ax.pie(percentages, colors=colors / 255.0)
    plt.savefig(filename)


if __name__ == "__main__":
    print('ok')
