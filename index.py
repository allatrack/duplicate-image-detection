# USAGE
# python index.py --dataset images --csv db.csv

# import the necessary packages
from PIL import Image
import imagehash
import argparse
import glob

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset of images")
ap.add_argument("-c", "--csv", required=True, help="path to CSV file for image hashes")
args = vars(ap.parse_args())

# open db file for writing
db = open(args["csv"], "w")

# loop over the image dataset
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # load the image and compute the difference hash
    image = Image.open(imagePath)
    width, height = image.size
    h = str(imagehash.dhash(image))
    left_area = (0, 0, width / 2, height)
    right_area = (width / 2, 0, width, height)
    image_left_part = image.crop(left_area)
    image_right_part = image.crop(right_area)
    hl = str(imagehash.dhash(image_left_part))
    hr = str(imagehash.dhash(image_right_part))

    # extract the filename from the path and update the database
    # using the hash as the key and the filename append to the
    # list of values
    filename = imagePath[imagePath.rfind("/") + 1:]
    db.write("%s,%s,%s,%s\n" % (filename, h, hl, hr))

# close the csv database
db.close()
