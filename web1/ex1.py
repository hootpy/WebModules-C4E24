from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hello World</h1>"
@app.route("/add/<int:num1>/<int:num2>")
def add(num1,num2):
    n = num1 + num2
    return str(n)

if __name__ == '__main__':
  app.run(debug=True)