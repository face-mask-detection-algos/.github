import argparse
import os
import re

import pandas as pd
import cv2


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Input file, a .txt file containing the output of darknet's 'detector'")
    parser.add_argument("--output", type=str, required=True, help="Output file, a .csv containing the results of darknet rewritten for an easier bulk comparison")
    parser.add_argument("--normalize_coordinates", action="store_true", help="Normalize the coordinates to be between 0 and 1.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if os.path.dirname is not None and os.path.dirname(args.output) != "":
        os.makedirs(os.path.dirname(args.output), exist_ok=True)

    with open(args.input, "r") as f:
        lines = f.readlines()
    
    output_dict = {"image_name":[], "image_path":[], "class":[], "confidence":[], "x":[], "y":[], "w":[], "h":[]}

    imagepath_line = False
    for line in lines:
        if imagepath_line:
            if line.startswith("mask") or line.startswith("nomask"):
                fields = re.split("\W+", line)
                category = fields[0]
                confidence = fields[1]
                x = fields[3]
                y = fields[5]
                w = fields[7]
                h = fields[9]
                output_dict["image_name"].append(image_name)
                output_dict["image_path"].append(os.path.abspath(imagepath))
                output_dict["class"].append(category)
                output_dict["confidence"].append(confidence)
                if args.normalize_coordinates:
                    image = cv2.imread(imagepath)
                    height, width, _ = image.shape
                    x = float(x) / width
                    y = float(y) / height
                    w = float(w) / width
                    h = float(h) / height
                output_dict["x"].append(x)
                output_dict["y"].append(y)
                output_dict["w"].append(w)
                output_dict["h"].append(h)
            else:
                imagepath_line = False

        if "Predicted in" in line:
            imagepath_line = True
            imagepath = line.split(":")[0]
            image_name = os.path.basename(imagepath).split(".")[0]
        
    pd.DataFrame(output_dict).to_csv(args.output, index=False)
