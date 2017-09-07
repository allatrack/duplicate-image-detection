Image Perceptual Hash
=========

> A perceptual hash is a fingerprint of a multimedia file derived from various features from its content. Unlike cryptographic hash functions which rely on the avalanche effect of small changes in input leading to drastic changes in the output, perceptual hashes are "close" to one another if the features are similar.

Equal images will not always have a distance of 0, so you will need to decide at which distance you will evaluate images as equal. For the image set that I tested, a max distance of 5 was acceptable. But this will depend on the implementation, the images and the number of images. For example; when comparing a small set of images, a lower maximum distances should be acceptable as the chances of false positives are quite low. If however you are comparing a large amount of images, 5 might already be too much.
