from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2


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
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    plt.figure(figsize=(12, 8))
    plt.pie(counts.values(), labels=hex_colors, colors=hex_colors)
    plt.savefig("color_analysis_report.png")
    print(hex_colors)
