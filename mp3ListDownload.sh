#!/bin/bash
#this script takes exactly one argument -- a file containing a list of mp3 names
#it will download all of those mp3 names to the current directory.


ORIGINALDIR=`pwd`
SEARCHTERMLIST=`cat $1`

echo Moving to $DOWNLOADMP3DIR

cd $DOWNLOADMP3DIR

IFS='\
'

for eachSearch in $SEARCHTERMLIST
do
    echo Downloading mp3 for search terms: "$eachSearch"
    ./download.sh "$eachSearch"
    mv ./Result.mp3 "$ORIGINALDIR/$eachSearch.mp3"
done

cd -

