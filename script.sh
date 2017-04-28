#!/bin/bash
# Install requirements
echo '*** Installing pip requirements ***'
sudo pip install -U -r requirements.txt

# Run pytest
echo '*** Running tests ***'
py.test --cov==src

# Run the program
echo '*** Start program ***'
python src/interpreter.py