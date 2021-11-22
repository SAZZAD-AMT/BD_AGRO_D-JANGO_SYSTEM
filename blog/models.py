from django.db import models
from user.models import User


class BlogPost(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    desciptions = models.TextField()
    location = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to="blog-image", null=True, blank=True)
    image2 = models.ImageField(upload_to="blog-image", null=True, blank=True)
    image3 = models.ImageField(upload_to="blog-image", null=True, blank=True)
    image4 = models.ImageField(upload_to="blog-image", null=True, blank=True)
    add_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.desciptions+' - '+self.user.username




class Comments(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    add_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment+' - '+self.user.username