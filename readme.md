

usage:

 build the image using build.sh or: 

 docker build . -t armaholic-parser

 download: https://ftp.armedassault.info/upload/Armaholic_Wayback_Archive.tar.gz
 
 unpack the contents of the armaholic_wayback_archive to ./cache


 run the desired script using run.sh or:

 docker run -it -v ${PWD}/app:/usr/src/app armaholic-parser:latest /usr/local/bin/python analyzeCache.py
