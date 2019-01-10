from flask import Flask,render_template,request,redirect
from models.character import Character
import mlab
mlab.connect()
app = Flask(__name__)

@app.route('/characters')
def characters():
    character_list = Character.objects()
    return  render_template('characters.html',character_list=character_list)
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
if __name__ == '__main__':
  app.run(debug=True)