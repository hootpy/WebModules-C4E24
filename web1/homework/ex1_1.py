from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"
@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    bmi = weight/((height/100)**2)
    if bmi < 16:
        return "You are severely underweight" + " and your BMI index is: " + str(round(bmi,1))
    elif bmi >= 16 and bmi <18.5:
        return "You are underweight" + " and your BMI index is: " + str(round(bmi,1))
    elif bmi >= 18.5 and bmi < 25:
        return "You are normal" + " and your BMI index is: " + str(round(bmi,1))
    elif bmi >= 25 and bmi <30:
        return "You are overweight" + " and your BMI index is: " + str(round(bmi,1))
    else:
        return "You are obese" + " and your BMI index is: " + str(round(bmi,1))

if __name__ == '__main__':
  app.run(debug=True)