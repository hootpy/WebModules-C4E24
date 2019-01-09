from flask import Flask,render_template,request
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
@app.route('/characters/<fid>')
def character_detail(fid):
    character = Character.objects(fid=fid).first()
    return render_template('character.html',character=character)

if __name__ == '__main__':
  app.run(debug=True)