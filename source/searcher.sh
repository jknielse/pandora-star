#!/bin/bash
#this script just does a search on searchmp3.mobi for the song name:

PAGE=`echo $@ | sed 's/\\ /-/g'`
QUERY=`echo $@ | sed 's/\\ /+/g'`
curl "searchmp3.mobi/mp3/$PAGE" -o SearchResults.html
