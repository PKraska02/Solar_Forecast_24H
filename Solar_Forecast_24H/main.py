from weather_data_preparation import prepare_weather_data
from generate_prediction import generate_prediction
from plots_prediction import sent_data_to_plot
import pandas as pd

if __name__ == '__main__':
    df = prepare_weather_data()
    prediction = generate_prediction(df)
    print(prediction)
    sent_data_to_plot(prediction)