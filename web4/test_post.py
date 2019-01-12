import mlab
from models.user import User
from models.post import Post
mlab.connect()

# a_random_user = User.objects(username='vietnam').first()

# if a_random_user is None:
#     print("User not found")
# else:
#     new_post = Post(title='My post 3',
#                     content="Hello guys again",
#                     author=a_random_user)
#     new_post.save()
#     print("Done")


# Post => author
# for post in Post.objects():
#     print(post.title, 'by',post.author.username)


# Author => Post
user = User.objects(username='hola123').first()
posts = Post.objects(author=user)
for post in posts:
    print(post.title)
