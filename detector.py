# USAGE
# python detector.py --dataset data_origin --csv db_origin.csv --report report_origin.txt

# import the necessary packages
from PIL import Image
import imagehash
import argparse
import glob2
import os
import csv


def hamming2(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to dataset of images")
ap.add_argument("-c", "--csv", required=True, help="path to CSV file for image hashes")
ap.add_argument("-r", "--report", required=True, help="path to text file for image duplicate report")
args = vars(ap.parse_args())

# open db file
db_file = open(args["csv"], "r")
reader = csv.reader(db_file)
db = {rows[0]: rows[1] for rows in reader}
# close the database
db_file.close()

# open report file
report_file = open(args["report"], "w")

# load all images in dir
candidates = list(glob2.iglob(args["dataset"] + "/*.jpg"))

while len(candidates) > 0:
    query_name = candidates[0]
    query = Image.open(query_name)
    candidates.remove(query_name)
    h = str(imagehash.dhash(query))
    filenames = {key for (key, value) in db.items() if hamming2(value, h) < 7}
    if len(filenames) > 1:
        report_file.write("\nFor image %s was founded %d images: \n" % (query_name, len(filenames) - 1))

        # loop over the images
        for filename in filenames:
            if args["dataset"] + "/" + filename != query_name:
                report_file.write(os.path.basename(query_name) + "==" + filename + "\n")
                try:
                    candidates.remove(args["dataset"] + "/" + filename)
                except ValueError:
                    pass
