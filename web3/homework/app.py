from flask import Flask,render_template,request
import mlab
from models.river import River

app = Flask(__name__)
mlab.connect()
@app.route('/')
def index():
    return "Hello"
@app.route('/river/africa')
def river_africa():
    river_list = River.objects(continent='Africa')
    return render_template("river_africa.html", river_list=river_list)
@app.route('/river/samerica')
def river_samerica():
    river_list = River.objects(continent='S. America',length__lt=1000)
    return render_template('river_africa.html', river_list=river_list)
if __name__ == '__main__':
  app.run(debug=True)