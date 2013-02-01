from lxml import etree
import fnmatch;
import os;
import datetime;

_CHARSET = "utf-8"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class flickr:
	def __init__(self,metaDir):
		self.filenames = dict()
		self.titles = dict()
		self.descriptions = dict()
		self.keywords = dict()
		self.capturetimes = dict()

		latestMetadataFile = self.getMetadataFile(metaDir)
		self.parseMetadata(latestMetadataFile)

	def getMetadataFile(self,metaDir):
		latestmetadatafile = ""
		age = 0
		for f in os.listdir(metaDir):
			metadatafile = os.path.join(metaDir, f)
			modDate = os.path.getctime(metadatafile)
			if modDate > age:
				age = modDate
				latestmetadatafile = metadatafile
		return latestmetadatafile;
	
	def parseMetadata(self,metadatafile):
		print "Latest Metadata: %s" % metadatafile
		doc = etree.parse(metadatafile)
		for photoselement in doc.getroot().iterchildren("photos"):
			for element in photoselement.iterchildren("photo"):
				idstring = element.get("id")

				originalstring = element.get("originalsecret")
				filetype = element.get("originalformat")
				filename = idstring + "_" + originalstring+"_o." + filetype
				self.filenames[idstring] = filename

				name = ""
				for nameElement in element.iterchildren(tag="title"):
					name = nameElement.text.encode(_CHARSET)
				self.titles[idstring] = name

				description = ""
				for descriptionElement in element.iterchildren(tag="description"):
					descriptionText = descriptionElement.text
					if (descriptionText != None):
						description = descriptionText.encode(_CHARSET)
				self.descriptions[idstring] = description
	
				tags = []
				for tagElement in element.iter("tag"):
					tag = tagElement.get("raw").encode(_CHARSET)
					tags = tags + [tag]
				self.keywords[idstring] = tags

				for datesElement in element.iterchildren(tag="dates"):
					taken = datesElement.get("taken").encode(_CHARSET)
					date = datetime.datetime.strptime(taken, _DATE_FORMAT)
				self.capturetimes[idstring] = date



	def getIds(self):
		return self.filenames.iterkeys()

	def getFilename(self,id):
		return self.filenames[id]

	def getTitle(self,id):
		return self.titles[id]

	def getDescription(self,id):
		return self.descriptions[id]

	def getKeywords(self,id):
		return self.keywords[id]

	def getCaptureTime(self,id):
		return self.capturetimes[id]
