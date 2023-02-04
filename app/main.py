import sys
from utils.primary_color_extractor import create_pie_chart, extract_colors


if __name__ == "__main__":
    sys.path.append("/home/mjilikbaev/pet_projects/interior_color_analyzer/app")
    colors, percentages = extract_colors('inter_2.jpg', 4)
    print(colors)
    print(percentages)
    create_pie_chart(colors, percentages, 'test_colors2.png')
