from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
  c= {
    "name": "AQUAMAN",
    "company": "DC Comic",
    "image": "https://m.media-amazon.com/images/M/MV5BOTk5ODg0OTU5M15BMl5BanBnXkFtZTgwMDQ3MDY3NjM@._V1_.jpg",
    "ability_list" : ["Speed","Strength","Reflexes"]}
  return render_template("index.html",
                          character = c)
@app.route("/hi/<name>")
def say_hi(name):
    print(name)
    return "Hi " + name

if __name__ == '__main__':
  app.run(debug=True)
