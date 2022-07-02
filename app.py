from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import json
import pandas as pd


app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.get('/')
def index():
    return render_template('index.html', data = [])


@app.get('/health')
def health():
    return json.dumps({"Status": True}), 200, {"ContentType":"application/json"}


@app.get('/search')
def search():
    if request.method == 'GET':
        try:
            df_seats = pd.read_csv('seats.csv')
            q = request.args.get('q')

            df_seats['Names'] = df_seats['Names'].str.lower()

            df_loc = df_seats.query(f'Names.str.contains("{q.lower()}")', engine='python')
        
            return render_template('index.html', data = df_loc)
        except:
            app.logger.error('An error occured while searching for guest')