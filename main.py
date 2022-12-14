from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
import numpy as np

def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation=cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0] * modified_img.shape[1], 3)
    return modified_img

def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color

def color_analysis(img, num_of_colors: int = 5):
    clf = KMeans(n_clusters=num_of_colors)
    clf.fit(img)
    center_colors = clf.cluster_centers_.round().astype('int')
    counts = Counter(clf.labels_)

    unique, counts2 = np.unique(clf.labels_, return_counts=True)
    counts_percent_rounded = (counts2 / counts2.sum() * 100).round(2)

    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    # TODO somehow we need to attach hex colot to it's percentage (representation size in the pic)
    result = np.column_stack((unique, counts_percent_rounded))
    return hex_colors, result

def img_to_result(image_path, num_colors):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    modified_image = prep_image(image)
    result = color_analysis(modified_image, num_colors)

    return result

if __name__ == "__main__":
    image_path = "data/interiers/inter_1.jpg"
    num_colors = 3

    result = img_to_result(image_path, num_colors)