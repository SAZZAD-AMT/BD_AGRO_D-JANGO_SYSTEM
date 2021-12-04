from django.db import models
from user.models import User


class PaperModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
