#!/bin/sh

APIKEY=.
NSID=.
SECRET=.

#http://hsivonen.iki.fi/photobackup/

java -jar ./photobackup/photobackup.jar $APIKEY $NSID $SECRET ./backup
#python parsetags.py
