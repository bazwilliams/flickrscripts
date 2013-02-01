from lxml import etree
import fnmatch;
import os;
import pyexiv2;
import datetime;
import flickr;

metaDir = "./photos/flickr/backup/metadata/"
photoDir = "./photos/flickr/backup/photos/"

f = flickr.flickr(metaDir)

def mergeMetadata(metadata, flickrid):
        name = f.getTitle(id)
	key = 'Iptc.Application2.ObjectName'
	metadata[key] = pyexiv2.IptcTag(key, [name])

        description = f.getDescription(id)
	key = 'Exif.Image.ImageDescription'
	metadata[key] = pyexiv2.ExifTag(key, description)

        keywords = f.getKeywords(id)
	key = 'Iptc.Application2.Keywords'
	metadata[key] = pyexiv2.IptcTag(key, ["fromflickr"] + keywords)

        date = f.getCaptureTime(id)
	key = 'Exif.Photo.DateTimeOriginal'
	metadata[key] = pyexiv2.ExifTag(key,date)
	key = 'Exif.Image.DateTime'
	metadata[key] = pyexiv2.ExifTag(key,date)

for id in f.getIds():
	filename = f.getFilename(id)
	originalFile = os.path.join(photoDir,filename)

	if os.path.isfile(originalFile):
		print originalFile
        	metadata = pyexiv2.ImageMetadata(originalFile)
        	metadata.read()
		mergeMetadata(metadata, id)
		metadata.write()

