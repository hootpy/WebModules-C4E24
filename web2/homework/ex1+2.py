from flask import Flask,render_template,request
import mlab
from mongoengine import Document,StringField
app = Flask(__name__)
class Account(Document):
    name = StringField()
    email = StringField()
    username = StringField()
    password = StringField()
@app.route('/')
def index():
    return "Hello World"

@app.route('/register')
def register():
    return render_template('ex1.html')
@app.route('/register/success',methods=['POST','GET'])

def register_success():
    if request.method == 'POST':
        infodb = Account(name=request.form['name'],email=request.form['email'],username=request.form['username'],password=request.form['password'])
    mlab.connect()
    infodb.save()
    return render_template('ex1_2.html')

if __name__ == '__main__':
  app.run(debug=True)