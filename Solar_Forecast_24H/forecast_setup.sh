#!/bin/bash

apk add python3
apk add py3-pip

cd /homeassistant/Solar_Forecast_24H
python3 -m venv .venv --system-side-packages

source .venv/bin/activate
python3 -m pip install -r requieremnts.txt
deactivate