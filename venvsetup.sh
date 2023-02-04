#!/bin/bash
# presetting the activate function
activate () {
    source $PWD/venv/bin/activate
}

# check if python3 exists
if ! [[ $(python3 --version) =~ ^Python\ 3* ]]
then
    exit;
fi
# set up current working directory
PWD=$(pwd)

# check if virtual environment exists
if ! [[ -d "venv" ]]
then
    # if virtual environment doesn't exist, build virtual environment
    python3 -m venv venv;
fi

# give execute permision to activate file
chmod +x $PWD/venv/bin/activate;

# runs the activate script
activate;

# upgrades pip
pip install --upgrade pip;

# installs requirements
pip install -r requirements.txt;

# curls api to apioutputs
if [[ ! -f apioutputs.json ]];
then
    curl https://ucsc.cc/api -o apioutputs.json
fi