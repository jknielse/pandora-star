echo Searching for mp3s...
./searcher.sh $@ &> /dev/null
NAME=`echo $@ | sed 's/ /_/g'`
python parseResults.py $NAME
echo Cleaning up...
rm SearchResults.html &> /dev/null
rm DownloadPage.html &> /dev/null
