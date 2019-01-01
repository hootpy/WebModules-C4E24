from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"
@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    bmi = round(weight/((height/100)**2),1)
    return render_template("ex1.html",
                            bmi=bmi)
  

if __name__ == '__main__':
  app.run(debug=True)