from django.db import models

class User(models.Model):
    pass

#user can have multiple posts, but post can only have one user. one to many relationship


#The related_name attribute specifies the name of the reverse relation from the User model back to your model.
# If you don't specify a related_name, Django automatically creates one using the name of your model with the suffix _set, for instance User.map_set.all().
# If you do specify, e.g. related_name=maps on the User model, User.map_set will still work, but the User.maps. syntax is obviously a bit cleaner and less clunky; so for example, if you had a user object current_user, you could use current_user.maps.all() to get all instances of your Map model that have a relation to current_user.

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="posts") #so heree I want to be able to refer to user.posts to see these
    

#one single comment can go on one post and a post can have multiple comments
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

