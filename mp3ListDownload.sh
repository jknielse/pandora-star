#!/bin/bash
#this script takes exactly one argument -- a file containing a list of mp3 names
#it will download all of those mp3 names to the current directory.


ORIGINALDIR=`pwd`
SEARCHTERMLIST=`cat $1`

echo Moving to $DOWNLOADMP3DIR

cd $DOWNLOADMP3DIR

IFS='\
'

PARSEDLIST=""

for eachSearch in $SEARCHTERMLIST
do
    PARSEDLIST="$PARSEDLIST$eachSearch\~"
done

python DownloadMP3.py $PARSEDLIST

cd -

