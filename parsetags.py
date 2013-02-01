from lxml import etree
import fnmatch;
import os;
import os, re
import flickr;

targetTagDir = "./tags"
targetSetDir = "./sets"
metaDir = "./flickr/backup/metadata/"
photoDir = "./flickr/backup/photos/"

_split = re.compile(r'[\0%s]' % re.escape(''.join(
    [os.path.sep, os.path.altsep or ''])))

def secure_filename(path):
    return _split.sub('', path)

f = flickr.flickr(metaDir)

for id in f.getIds():
	print "%s" % (id)
	print "Filename   : %s" % (f.getFilename(id))
	print "Taken      : %s" % (f.getCaptureTime(id))
	print "Title      : %s" % (f.getTitle(id))
	print "Description: %s" % (f.getDescription(id))
	print "Keywords   : %s" % (f.getKeywords(id))

for photoselement in doc.getroot().iterchildren("photos"):
	for element in photoselement.iterchildren("photo"):
		idstring = element.get("id")
		originalstring = element.get("originalsecret")
		filetype = element.get("originalformat")
		phototypes[idstring] = filetype

		filename = idstring + "_" + originalstring+"_o." + filetype
		originalFile = os.path.join(photoDir,filename)
		photomap[idstring] = originalFile

		name = ""
		for nameElement in element.iterchildren(tag="title"):
			name = nameElement.text

		uniqueName = (name + "_" + idstring + "." + filetype).encode(_CHARSET)

		for tagElement in element.iter("tag"):
			tag = tagElement.get("raw").encode(_CHARSET)

			tagDir = os.path.join(targetTagDir,tag)
			if not os.path.exists(tagDir):
				os.makedirs(tagDir)

			secureName = secure_filename(uniqueName)
			targetFile = os.path.join(tagDir,secureName)

			if not os.path.lexists(targetFile):
				print "%s -> %s" % (originalFile, targetFile)
			os.symlink(originalFile, targetFile)

for photosetselement in doc.getroot().iterchildren("photosets"):
	for element in photosetselement.iterchildren("photoset"):
		setname = ""
		for nameElement in element.iterchildren("title"):
			setname = nameElement.text

		setDir = os.path.join(targetSetDir,setname.encode(_CHARSET))
		if not os.path.exists(setDir):
			os.makedirs(setDir)
	
		index = 0
		for photoElement in element.iterchildren("photo"):
			title = photoElement.get("title")
			photoid = photoElement.get("id")
			filetype = phototypes[photoid]
			uniqueName = (("%03d " % index) + title + " (" + photoid + ")." + filetype).encode(_CHARSET)
			targetFile = os.path.join(setDir,uniqueName)
			index+=1

			if not os.path.lexists(targetFile):
				originalFile = photomap[photoid]
				print "%s -> %s" % (originalFile, targetFile)
				os.symlink(originalFile, targetFile)
