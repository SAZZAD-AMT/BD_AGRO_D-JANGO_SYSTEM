from django.db import models
from django.shortcuts import reverse
from user.models import User


class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Absolute URL for Post"""
        return reverse("blog_details", kwargs={"blog_id": self.id})

class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
