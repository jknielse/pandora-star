#!/bin/bash
#setup.sh - this is a default setup script to make the process of making these
#           for other applications easier.

. ~/.libs/colours

function setup {
       
    bldylw
    echo "    Installing beautiful soup and selenium"
    sudo pip install BeautifulSoup
    sudo pip install selenium
    bldgrn
    echo "    Done"

    bldylw
    echo "    Creating script aliases"
    echo "export DOWNLOADMP3DIR='`pwd`/source'" >> ~/.bashrc
    echo "alias downloadmp3list='`pwd`/mp3ListDownload.sh'" >> ~/.bashrc
    bldgrn
    echo "    Done"



    #after everything else, this is probably the last step.
    bldylw
    echo "    Updating installation status"
    echo 0 > ./installation_status
    bldgrn
    echo "    Done"
    bldgrn
    echo "Installation Successful"
}


bldylw
echo -n "Installing "
bldblu
cat ./program_name
if [[ -e ./installation_status ]]
then
    if [[ `cat ./installation_status` == "0" ]]
    then
        bldylw
        echo "    Program aready installed"
        bldgrn
        echo "Installation Successful"
    else
        setup
    fi
else
    setup
fi
txtrst
