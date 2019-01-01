from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/about-me")
def aboutme():
    am= {"name": "Hien",
    "work": "Student",
    "school": "FTU",
    "hobbies": "Video game"
    }
    return render_template("ex1_study.html",
                            aboutme = am)
@app.route("/school")
def school():
    return redirect("http://techkids.vn", code= 302)                           

if __name__ == '__main__':
  app.run(debug=True)