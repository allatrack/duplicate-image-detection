# USAGE
# python gather2.py --input data

# import the necessary packages
import argparse
import shutil
import glob2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="input directory of images")
args = vars(ap.parse_args())

# loop over the input images
for imagePath in glob2.iglob(args["input"] + "/*.jpg"):
    if "origin" in imagePath:
        shutil.copy(imagePath, args["input"] + "_origin" + "/" + os.path.basename(imagePath))
    if "quadratic" in imagePath:
        shutil.copy(imagePath, args["input"] + "_quadratic" + "/" + os.path.basename(imagePath))
