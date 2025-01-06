#!/bin/bash


cd /homeassistant/Solar_Forecast_24H

echo "Uruchamianie skryptu $(date)" >> /homeassitant/run_forecast.log
source .venv/bin/activate

python3 main.py > /homeassistant/run_forecast_data.log

deactivate