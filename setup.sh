#!/bin/bash
pip install virtualenv
virtualenv env
pip install -r ./requirements.txt
$env:FLASK_ENV = "development"
$env:FLASK_APP = "app.py"
