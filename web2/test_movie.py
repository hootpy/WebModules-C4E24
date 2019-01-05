#connect to database
import mlab
from mongoengine import Document, StringField, IntField
mlab.connect()


#define model
class Movie(Document):
    title = StringField()
    image = StringField()
    link = StringField()
    rate = IntField()

movie_list = Movie.objects(rate__gte=7,title__icontains="strange") #lazy loading
for m in movie_list:
    print(m.title , m.rate)
# #create data
# m = Movie(title="Guardians of the Galaxy",
#         image="https://m.media-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_SY1000_CR0,0,674,1000_AL_.jpg",
#         link="https://www.imdb.com/title/tt2015381",
#         rate=5)

# m.save()