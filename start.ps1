#!/bin/bash
.\env\Scripts\activate.ps1
$env:FLASK_ENV = "development"
$env:FLASK_APP = "app.py"
flask run --port=2000