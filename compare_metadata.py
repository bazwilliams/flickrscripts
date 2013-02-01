import fnmatch;
import os;
import pyexiv2;
import datetime;

photoDir = "./compares/"

#create a string with name, description and keywords (without fromflickr)
#check dictionary for key with datestring, if not present:
#	store datestring with compound string
#else compare value with compound string - if different then print the filename and metadata

allmetadata = dict()

def parseMetadata(filename):
        metadata = pyexiv2.ImageMetadata(filename)
        metadata.read()

	name = os.path.basename(filename)
	name = os.path.splitext(name)[0]
	key = 'Iptc.Application2.ObjectName'
	if key in metadata:
		tag = metadata[key]
		name = tag.raw_value[0];

	description = ""
	key = 'Exif.Image.ImageDescription'
	if key in metadata:
		tag = metadata[key]
		description = tag.raw_value;

	keywords = []
	key = 'Iptc.Application2.Keywords'
	if key in metadata:
		tag = metadata[key]
		keywords = tag.raw_value;
		if 'fromflickr' in keywords:
			keywords.remove('fromflickr')

	key = 'Exif.Image.DateTime'
	date= metadata[key].value;

	key = 'Exif.Photo.DateTimeOriginal'
	if key in metadata:
		tag = metadata[key]
		date = tag.value;
	
	compound_string = '%s|%s|%s' % (name, description, keywords)
	metadatakey = '%s' % date.strftime('%Y%m%d%H%M%S')
	if metadatakey in allmetadata:
		if compound_string != allmetadata[metadatakey]:
			print '%s: %s [DIFFERS] (%s)' % (metadatakey, filename, compound_string)
		else:
			print '%s: %s [OK] (%s)' % (metadatakey, filename, compound_string)
	else:
		allmetadata[metadatakey] = compound_string
		print '%s: %s [ADDED] (%s)' % (metadatakey, filename, compound_string)

for filename in os.listdir(photoDir):
	f = os.path.join(photoDir,filename)
	parseMetadata(f)
