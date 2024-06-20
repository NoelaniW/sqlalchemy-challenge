# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlit:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

precipitation_dict = [{"date": "prcp"}]

stations =[{"station: 'USC00519281'},
                {"station": 'USC00519397'},
                {"station": 'USC00513117'},
                {"station": 'USC00519523'},
                {"station": 'USC00516128'},
                {"station": 'USC00514830'},
                {"station": 'USC00511918'},
                {"station": 'USC00517948'},
                {"station": 'USC00518838'}]

temp_list = 
#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
   return "<h1>Hawaii Weather!!<h1>"

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations", methods=['GET'])
def station_list():
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def temperature():
    recent_temp_date = session.query(measurement.date).order_by(measurement.date.desc()).filter(measurement.station == 'USC00519281').first()
    start = dt.date(2017, 8,18)-dt.timedelta(days=365)

    temp_data = session.query(measurement.station, measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').all()
    temp_df = pd.DataFrame(temp_data, columns=['Station', 'Date', 'Temperature'])
    temp_df['Date'] = pd.to_datetime(temp_df['Date'])
    temp_year_sort = (temp_df['Date'] > '2016-08-23')
    temp_plot_df = temp_df.loc[temp_year_sort]

    temps = []
    for result in temp_plot_df:
        temps.append({
            "Date": result.date,
            "Temperature": result.tobs
        })
    session.close()

    return jsonify(temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        start = datetime.strptime(start, "%Y-%m-%d")
        end = datetime.strptime(end, "%Y-%m-%d") 
        results = session.query(*sel).filter(Measurement.date >= start).all()

    session.close()

    list(np.ravel(results))

    return jsonify(results)










if __name__ == "__main__":
    app.run(debug=True)