#!/bin/sh

#Install pyenv2.7.11 & pyenv3.6.4
pyenv install 2.7.11
pyenv install 3.6.4
sleep 10
echo "pyenv2.7.11 & pyenv3.6.4 were installed"

#Creat virtualenv python2 & python3
pyenv virtualenv 2.7.11 python2
pyenv virtualenv 3.6.4 python3
sleep 5
echo virtualenv python2 & python3 were created
