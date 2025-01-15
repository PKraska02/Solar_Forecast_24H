# Solar_Forecast_24H
# Table of Content
- [Introduction](#Introduction)
- [Instalation](#Instalation)
- [Configuration](#Configuration)
- [Important notes](#Important-notes)

# Introduction
![Example prediction plot](Images/Image1.PNG)
Home Assistant Extension to forecast PV electricity production the next day.
It allows us to easily check the predicted production of our photovoltaic panels.

# Instalation
In order for the charts to function correctly, the components listed need to be downloaded:
- UI Lovelace Minimalist
- apexchart-card
These components can be downloaded via [HACS]("https://hacs.xyz")
In addition, the Terminal & SSH add-on must be downloaded.

**Steps to be taken during installation:**
- Add project folder to /homeassistant folder,
- Open Terminal
- sudo apt install dos2unix
- cd /homeassistant/SolarForecast_24H
- dos2unix forecast_setup.sh
- dos2unix run_forecast.sh
- run forecast_setup.sh
- run run_forecast.sh

# Configuration
**Step 1. Add .env file**
.env file is neccessary for the integration to work properly.
.env must contain 5 elements:
'''
LATITUDE = xx.xx
LONGITUDE = xx.xx
POWER = x.xx
HA_URL = http://homeassistant.local:8123
HA_TOKEN = xxxxxxxx
'''
