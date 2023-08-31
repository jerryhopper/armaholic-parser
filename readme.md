

usage:

 build the image using build.sh or: 

 docker build . -t armaholic-parser

 download: https://ftp.armedassault.info/upload/Armaholic_Wayback_Archive.tar.gz
 
 unpack the contents of the armaholic_wayback_archive to ./cache


 run the desired script using run.sh or:

 docker run -it -v ${PWD}/app:/usr/src/app armaholic-parser:latest /usr/local/bin/python analyzeCache.py



dev notes:

Armaholic object definition (items with * is required.)

 - armaholic-id*

 - armaholic-section*

 - item-title*

 - item-author*

 - item-author-website

 - item-version

 - item-date*

 - item-filename*

 - item-filesize*

 - item-description

 - item-descr-images []

 - item-descr-videos []

 - item-descr-links []

 - item-descr-requirements []
 
