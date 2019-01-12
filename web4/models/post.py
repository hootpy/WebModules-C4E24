from mongoengine import Document, StringField,ReferenceField

class Post(Document):
    title = StringField()
    content = StringField()
    author = ReferenceField("User")
