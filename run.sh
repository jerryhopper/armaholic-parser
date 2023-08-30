docker run -it -v ${PWD}/app:/usr/src/app -v ${PWD}/cache:/usr/src/app/cache armaholic-parser:latest /usr/local/bin/python analyzeCache.py $1
