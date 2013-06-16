from selenium import webdriver
import selenium
import sys
from time import sleep
import subprocess

first = True
searchterms = []
for arg in sys.argv:
    if first:
        first = False
        continue
    searchterms.append(str(arg).replace('~',''))

del searchterms[-1]

driver = webdriver.Firefox()
#driver = webdriver.PhantomJS('../dependencies/phantomjs-1.9.1-linux-x86_64/bin/phantomjs')

fileMap = []

first = True
for eachTerm in searchterms:
    driver.get('http://beemp3.com/')
    sleep(2)
    try:
        driver.find_element_by_class_name('search-t').send_keys(eachTerm)
    except selenium.common.exceptions.NoSuchElementException:
        continue
    except UnicodeDecodeError:
        continue
    try:
        driver.find_element_by_id('Submit').click()
    except selenium.common.exceptions.NoSuchElementException:
        continue

    sleep(1)
    try:
        path = driver.find_element_by_class_name('song-name').find_element_by_xpath('a').get_attribute('href')
    except selenium.common.exceptions.NoSuchElementException:
        continue
    driver.get(path)
    
    try:
        firstZero = True
        while driver.find_element_by_id('cod_ck'):
            humanInput = driver.find_element_by_id('cod_ck')
            try:
                if firstZero:
                    humanInput.find_element_by_id('code_scuka').send_keys('0')
                    firstZero = False
                humanInput.find_elements_by_class_name('submit')[0].click()
                sleep(1)
            except selenium.common.exceptions.NoSuchElementException:
                break
    except selenium.common.exceptions.NoSuchElementException:
        pass
    sleep(2)

    if driver.find_elements_by_xpath("//input[@style='width:300px;']"):
        fileLink = [driver.find_elements_by_xpath("//input[@style='width:300px;']")[0].get_attribute('value'), eachTerm]
        fileMap.append(fileLink)

devnull = open ('/dev/null', 'w')


for eachFileLink in fileMap:
    result = True
    try:
        print "Attempting to download " + str(eachFileLink[1])
        result = subprocess.call(["wget",str(eachFileLink[0]),"-O",str(eachFileLink[1]) + ".mp3"],stdout = devnull, stderr = devnull)
    except error:
        pass 
    
    if result:
        print str(eachFileLink[1]) + " had a bad download link" 
    
