from flask import Flask,render_template,request,redirect,session
from models.character import Character
from models.user import User
from models.post import Post
import mlab

mlab.connect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "very secret"


@app.route('/characters')
def characters():
    if "token" in session:
        character_list = Character.objects()
        return  render_template('characters.html',character_list=character_list)
    else:
        return redirect("/login?next=characters")


@app.route('/add_character', methods=['GET','POST'])
def add_character():
    if request.method == 'GET':
        return render_template('character_form.html')
    elif request.method == 'POST':
        new_character = Character(name = request.form['name'],
                                image=request.form['image'],
                                rate=request.form['rate'],
                                fid=request.form['fid'])
        new_character.save()
        return "gotcha"


@app.route('/character/<fid>')
def character_detail(fid):
    character = Character.objects(fid=fid).first()
    return render_template('character.html',character=character)


@app.route('/character/<fid>/update',methods=['GET','POST'])
def character_update(fid):
    if request.method == 'GET':
        character = Character.objects(fid=fid).first()
        return render_template('character_update.html',character=character)
    elif request.method == 'POST':
        character = Character.objects(fid=fid).first()
        character.update(name=request.form['name'],image=request.form['image'],rate=request.form['rate'])
        return redirect("/characters")


@app.route('/character/<fid>/delete',methods=['GET','POST'])
def character_delete(fid):
    if request.method == 'GET':
        return render_template('character_delete.html')
    elif request.method == 'POST':
        character = Character.objects(fid=fid).first()
        character.delete()
        return redirect("/characters")

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login_form.html')
    elif request.method == 'POST':
        form = request.form
        username = form["username"]
        password = form['password']
        found_user = User.objects(username=username).first()
        if found_user is None:
            return "User not found"
        else:
            if password != found_user.password:
                return "Invalid password"
            else:
                session["token"] = username
                next = request.args.get('next')
                if next is None or next == '':
                    return 'login successfully'
                else:
                    return redirect("/"+ next)

@app.route('/logout')
def logout():
    del session['token']
    return redirect("/login")


# @app.route('/posts')
# def posts():
#     if 'token' not in session:
#         return redirect('/login?next=posts')
#     else:
#         posts = Post.objects(author=session['token'])
#         for post in posts:
#             print(post.title)
#         return "Hello"






if __name__ == '__main__':
  app.run(debug=True)


