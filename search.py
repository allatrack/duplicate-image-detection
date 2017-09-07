# USAGE
# python search.py --dataset images --csv db.csv --query selected_images/images/image_0001.jpg

# import the necessary packages
from PIL import Image
import imagehash
import argparse
import csv

hex2bin_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111",
}


def hamming2(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    sb1 = "".join(hex2bin_map[i] for i in s1)
    sb2 = "".join(hex2bin_map[i] for i in s2)
    return sum(c1 != c2 for c1, c2 in zip(sb1, sb2))


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to dataset of images")
ap.add_argument("-c", "--csv", required=True, help="path to CSV file for image hashes")
ap.add_argument("-q", "--query", required=True, help="path to the query image")
args = vars(ap.parse_args())

# open db file
db_file = open(args["csv"], "r")
reader = csv.reader(db_file)
db = {rows[0]: (rows[1], rows[2], rows[3]) for rows in reader}
print hamming2('f10708142f58b413', 'f680002cf7f8871f')
exit()
# close the database
db_file.close()

# load the query image, compute the difference image hash, and
# and grab the images from the database that have the same hash
# value
query = Image.open(args["query"])
width, height = query.size
h = str(imagehash.dhash(query))
left_area = (0, 0, width / 2, height)
right_area = (width / 2, 0, width, height)
image_left_part = query.crop(left_area)
image_right_part = query.crop(right_area)
hl = str(imagehash.dhash(image_left_part))
hr = str(imagehash.dhash(image_right_part))
filenames = {key for (key, value) in db.items()
             if ((hamming2(value[0], h) < 9) or (hamming2(value[1], hl) < 9) or (hamming2(value[2], hr) < 9))}

print "Found %d images" % (len(filenames))

# loop over the images
for filename in filenames:
    image = Image.open(args["dataset"] + "/" + filename)
    image.show()
