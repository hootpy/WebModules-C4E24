from flask import Flask,render_template
import json
app = Flask(__name__)
with open("user.json","r") as f:
    user_list=json.load(f)

@app.route('/')
def index():
    return "Hello World"
@app.route('/user/<username>')
def user(username):
    if username in user_list:
        return render_template("username.html",
                                username = user_list[username],
                                user_url = username)
    else:
        return render_template("404.html")
if __name__ == '__main__':
  app.run(debug=True)