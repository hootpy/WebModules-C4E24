import mlab
from models.character import Character
mlab.connect()

#update
#1.1 read data
character = Character.objects(fid='tt1477834').first()
# character.update(inc__rate=1)
# #1.2 Update data

#delete
#2.1 Read data
#2.2 Delete data

character.delete()