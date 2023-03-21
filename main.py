import json
import sys
import opencv

with open('lists.json') as f:
    data = json.load(f)

img = opencv.imread(data["cats"][1]["sitting"], opencv.IMREAD_ANYCOLOR)
opencv.imread("Marta", img)
