import pickle
import numpy as np
import pandas as pd
from flask import Flask,render_template,request

model = pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('Prediction.html')

@app.route('/Result',methods=["POST","GET"])
def result():
    if request.method=="POST":
        Gender=request.form["Gender"]
        if Gender=="Female":
            Gender=0
        if Gender=="Male":
            Gender=1
        Age=request.form["Age"]
        Class=request.form["Class"]
        if Class=="Bussiness":
            Class=0
        if Class=="Eco":
            Class=1
        if Class=="Eco Plus":
            Class=2
        Flight_Distance = request.form[ 'Flight Distance'] 
        Inflight_wifi_service = request.form['Inflight wift service']
        Departure_Arrival_time_convenient = request.form[ 'Departure/Arrival time convenient ']
        Ease_of_Online_booking = request.form['Ease of Online booking']
        Gate_location = request.form[ 'Gate location']
        Food_and_drink = request.form[ 'Food and drink']
        Online_boarding = request.form['Online boarding']
        Seat_comfort = request.form["seat comfort"]
        Inflight_entertainment = request.form['Inflight entertainment']
        On_board_service = request.form['On-board service']
        Leg_room_service = request.form['Leg room service']
        Baggage_handling= request.form['Baggaae_ handling']    
        Checkin_service = request.form['Checkin service']
        Inflight_service = request.form['Inflight service']
        Cleanliness = request.form['Cleanliness']
        Departure_Delay_in_Minutes = request.form['Departure Delay in Minutes']
        Arrival_Delay_in_Minutes = request.form['Arrival Delay in Minutes']
        total = [Gender, Age,  Class, Flight_Distance, Inflight_wifi_service, Departure_Arrival_time_convenient, Ease_of_Online_booking, Gate_location, Food_and_drink, Online_boarding, Seat_comfort, Inflight_entertainment, On_board_service, Leg_room_service, Baggage_handling, Checkin_service, Inflight_service, Cleanliness, Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes]
        
        print(total)
        prediction = model.predict(total)
        print(prediction)
        pred = prediction[0]
        print(pred)
        
        if int(pred) == 0:
            pred = "Passengers have satisfies the Airline Service"
        else:
            pred = "Passengers have neutral or dissatisfied the Airline Service"
        print("hello",pred) 
        return render_template('Result.html', prediction_text=pred)
    

if __name__=="__main__":
  app.run(debug=False)
