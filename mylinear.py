#This is the file that we will create. It contains the necessary code to display our desired results.
# import class Flask, apscheduler and other necessary libraries.
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from sklearn import datasets, linear_model, preprocessing
from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
import sys

# Initialization of the different components that we will need.
data = None
regressor = None

def create_model():
    global regressor
    global data

    
    #Reset Values
    data = None
    regressor = None
    data_from_set = pd.read_csv('pmdata/BeijingPM.csv')
    
    data = data_from_set
    np.nan_to_num(data)
    # dataset = dataset[isnan(dataset)]
    data[data.notnull()]
    data = data.dropna()
    X = data[['year', 'month','hour', 'DEWP', 'HUMI']]
    y = data[['TEMP']]
    
    # Create linear regressor object
    regressor = linear_model.LinearRegression()
    
    # Train the model using the training sets
    regressor.fit(X, y)
    # return get_future_pred()
    
# Once the dataset has been applied to the model, we will return the prediction for today.
def get_future_pred(year, month, hour, DEWP, HUMI):
    global data
    print("hej Christian", file=sys.stderr)
    print(type(year), file=sys.stderr)
    year = int(year)
    month = int(month)
    hour = int(hour)
    DEWP = float(DEWP)
    HUMI = float(HUMI)
    print(type(year), file=sys.stderr)
    
    y_future = regressor.predict([[year, month, hour, DEWP, HUMI]])
    r2_score = regressor.score(data[['year', 'month', 'hour', 'DEWP', 'HUMI']], data[['TEMP']])
    
    return y_future[0][0], data.shape[0], r2_score

# create an instance (our app)
app = Flask(__name__)

# Routes for our app.
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', form=None)

@app.route('/prediction', methods=['POST'])
def prediction():
    year = request.form['year']
    month = request.form['month']
    hour = request.form['hour']
    DEWP = request.form['DEWP']
    HUMI = request.form['HUMI']
    create_model()
    y_future, dataAmount, r2_score = get_future_pred(year, month, hour, DEWP, HUMI)
    return render_template('result.html', year=year, 
                           month=month, 
                           hour=hour, 
                           DEWP=DEWP, 
                           HUMI=HUMI, 
                           y_future=y_future, 
                           dataAmount=dataAmount, 
                           r2_score=r2_score)

#@app.route('/result/<symbol>&<y_today>&<dataAmount>&<r2_score>', methods=['GET', 'POST'])
#def result_new(symbol, y_today, dataAmount, r2_score):
#    app.logger.info('result: ' + cur_symbol)
#    return render_template('result.html',symbol=symbol, y_today=y_today, dataAmount=dataAmount, r2_score=r2_score)

@app.route('/result', methods=['POST'])
def result():
    global cur_symbol
    y_future,dataAmount, r2_score = get_future_pred()
    return render_template('result.html', y_future=y_future, dataAmount=dataAmount, r2_score=r2_score)
    
if __name__ == '__main__':
    app.run(debug=True)