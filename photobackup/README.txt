=Photo and Metadata Backup for Flickr 1.0=

This is a photo and *metadata* backup utility for Flickr. The metadata is
written is an XML file whose format is an aggregation of the response data 
from the Flickr API.

There is no restore utility. That's up to you. I don't need one yet.

Author: Henri Sivonen, hsivonen@iki.fi

==Usage==

java -jar photobackup.jar apikey nsid secret backupdirectory

Running the app again creates a new metadata dump and updates the photo dupm 
by downloading only new photos.

apikey is a Flickr API key. See http://www.flickr.com/services/api/keys/

nsid is your numeric Flickr user id. See e.g.
http://www.flickr.com/services/api/explore/?method=flickr.contacts.getList
(on the right)

secret is the "shared secret" associated with your API key.
See http://www.flickr.com/services/api/keys/

backupdirectory is the directory you want the backup to written in.

==Backup Format==

The metadata backup file consists of an XML file whose root element is <rsp>.
The root has two children: <photosets> and <photos>. 

The children of <photosets> correspond to the response of the 
flickr.photosets.getPhotos API call with the response of 
flickr.photosets.comments.getList added as a child.

The children of <photos> correspond to the response flickr.photos.getInfo 
except the <comments> element is replaced with the response of 
flickr.photos.comments.getList.

The photos are named id_originalsecret_o.format.

==Licensing==

The classes in com.aetrion.* are from Flickrj.
See flicrkj.LICENSE.txt for license.

The classes in nu.validator.* are from Validator.nu utilities. 
See validatornu-utils.LICENSE.txt for license.

The classes in org.apache.* are from the Xalan Serializer utilities. 
See serializer.LICENSE.txt for license and serializer.NOTICE.txt for required notice.

The classes in fi.hsivonen.* are original to this program except portions of the 
fi.hsivonen.photobackup.FlickrEntityResolver and fi.hsivonen.photobackup.Main which 
derived from Flickrj and its sample code.
See photobackup.LICENSE.txt for license of the original code and 
flicrkj.LICENSE.txt for license of the portions derived from Flickrj.

==Notices==

   Flickr is a trademark and service mark Yahoo! Inc.

   This product includes software developed by Aetrion LLC.

   This product includes software developed by IBM Corporation (http://www.ibm.com)
   and The Apache Software Foundation (http://www.apache.org/).

   Portions of this software was originally based on the following:
     - software copyright (c) 1999-2002, Lotus Development Corporation.,
       http://www.lotus.com.
     - software copyright (c) 2001-2002, Sun Microsystems.,
       http://www.sun.com.
     - software copyright (c) 2003, IBM Corporation., http://www.ibm.com.
