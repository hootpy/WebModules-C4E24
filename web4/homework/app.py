from flask import Flask,render_template,request
from mongoengine import Document,StringField,IntField
import mlab
import json
app = Flask(__name__)
mlab.connect()

class Bike(Document):
    model = StringField()
    daily_fee = IntField()
    image = StringField()
    year = IntField() 

@app.route('/')
def index():
    return "Hello"

@app.route('/new_bike', methods = ['GET','POST'])
def new_bike():
    if request.method == 'GET':
        return render_template('bike.html')
    elif request.method == 'POST':
        new_rent = Bike(
            request.form['model'],
            request.form['daily_fee'],
            request.form['image'],
            request.form['year']
        )
        new_rent.save()
        return render_template('rent_submitted.html')



  

if __name__ == '__main__':
  app.run(debug=True)