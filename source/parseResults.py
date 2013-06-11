from bs4 import BeautifulSoup
import subprocess
import re
import sys

searchFile = open('SearchResults.html', 'r')
searchResults = searchFile.read()
searchFile.close()

soup = BeautifulSoup(searchResults)

numberOfResultsString = soup.p.string

resultsRegex = re.compile('([0-9]*) mp3')
numberOfResults = resultsRegex.match(numberOfResultsString).group(1)

if numberOfResults <= 0:
    print "No results found... exiting."
    exit()
else:
    print numberOfResults + " results found."

downloadPageURL = soup.find(itemtype="http://schema.org/MusicRecording").find_all("meta")[2]['content']

devnull = open('/dev/null', 'w')
subprocess.Popen(["curl" , downloadPageURL , "-o", "DownloadPage.html"],stdout=devnull, stderr=devnull)

downloadPageFile = open('DownloadPage.html')
downloadResults = downloadPageFile.read()
downloadPageFile.close()

soup = BeautifulSoup(downloadResults)


downloadLink = soup.find("div", { "class" : "download m-bottom_20" }).a['href']

print "Downloading..."
subprocess.Popen(["wget" , "-O", sys.argv[1] + ".mp3", downloadLink], stdout=devnull, stderr=devnull).wait()
print "Done"
         
