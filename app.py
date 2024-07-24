from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
            form_data = request.form.to_dict()  # Get all form data as a dictionary


            location = form_data.get("location")
            rainfall = float(form_data.get("rainfall"))
            evaporation = float(form_data.get("evaporation"))
            sunshine = float(form_data.get("sunshine"))
            windgustdir = form_data.get("windGustDir")
            windgustspeed = float(form_data.get("windGustSpeed"))
            winddir9am = form_data.get("windDir9am")
            winddir3pm = form_data.get("windDir3pm")
            windspeed9am = float(form_data.get("windSpeed9am"))
            windspeed3pm = float(form_data.get("windSpeed3pm"))
            humidity9am = float(form_data.get("humidity9am"))
            humidity3pm = float(form_data.get("humidity3pm"))
            pressure9am = float(form_data.get("pressure9am"))
            pressure3pm = float(form_data.get("pressure3pm"))
            cloud9am = float(form_data.get("cloud9am"))
            cloud3pm = float(form_data.get("cloud3pm"))
            temp9am = float(form_data.get("temp9am"))
            temp3pm = float(form_data.get("temp3pm"))
            avg_temp = float(form_data.get("avgTemp"))
            day = form_data.get("day")
            rain_today = form_data.get("rainToday")
            year = int(form_data.get("year"))
            month = form_data.get("Month")

            month_dict = {
                "january": 1, "february": 2, "march": 3, "april": 4, "may": 5,
                "june": 6, "july": 7, "august": 8, "september": 9, "october": 10,
                "november": 11, "december": 12
            }

            if month.lower() in month_dict:
                month = month_dict[month.lower()]
            else:
                raise ValueError("Invalid month name")

            weekdays = {
                "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4,
                "friday": 5, "saturday": 6, "sunday": 7
            }

            if day.lower() in weekdays:
                day = weekdays[day.lower()]
            else:
                raise ValueError("Invalid day name")

            month_sin = np.sin(2 * np.pi * month / 12)
            month_cos = np.cos(2 * np.pi * month / 12)
            day_sin = np.sin(2 * np.pi * day / 7)
            day_cos = np.cos(2 * np.pi * day / 7)

            values = [
                location, rainfall, evaporation, sunshine, windgustdir, windgustspeed,
                winddir9am, winddir3pm, windspeed9am, windspeed3pm, humidity9am, humidity3pm,
                pressure9am, pressure3pm, cloud9am, cloud3pm, temp9am, temp3pm, rain_today,
                year, month_sin, month_cos, day_sin, day_cos, avg_temp
            ]

            object_cols = ['location', 'windgustdir', 'winddir9am', 'winddir3pm', 'rain_today']
            num_cols = [
                'rainfall', 'evaporation', 'sunshine', 'windgustspeed', 'windspeed9am', 'windspeed3pm',
                'humidity9am', 'humidity3pm', 'pressure9am', 'pressure3pm', 'cloud9am', 'cloud3pm',
                'temp9am', 'temp3pm', 'year', 'month_sin', 'month_cos', 'day_sin', 'day_cos', 'avg_temp'
            ]
            if(rain_today.lower()=="yes"):
                rain_today=1
            else:
                rain_today=0    

            data_dict = {
            'Location': location,
            'Rainfall': rainfall,
            'Evaporation': evaporation,
            'Sunshine': sunshine,
            'WindGustDir': windgustdir,
            'WindGustSpeed': windgustspeed,
            'WindDir9am': winddir9am,
            'WindDir3pm': winddir3pm,
            'WindSpeed9am': windspeed9am,
            'WindSpeed3pm': windspeed3pm,
            'Humidity9am': humidity9am,
            'Humidity3pm': humidity3pm,
            'Pressure9am': pressure9am,
            'Pressure3pm': pressure3pm,
            'Cloud9am': cloud9am,
            'Cloud3pm': cloud3pm,
            'Temp9am': temp9am,
            'Temp3pm': temp3pm,
            'RainToday': rain_today,
            'year': year,
            'month_sin': month_sin,
            'month_cos': month_cos,
            'day_sin': day_sin,
            'day_cos': day_cos,
            'Avg_temp': avg_temp
        }
        

            df = pd.DataFrame([data_dict])
            with open("preprocessor.pkl", "rb") as f:
                preprocessor = pickle.load(f)

            X = preprocessor.transform(df)
            model = load_model("modelrain_final.keras")
            prediction = model.predict(X)
            prediction = "There will be RainFall Tomorrow" if prediction[0][0] >= 0.5 else "There will Not Be Rainfall Tomorrow"
        
            return render_template("index2.html", prediction=prediction)

     
if __name__ == "__main__":
    app.run(debug=True)
