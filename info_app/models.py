from django.db import models


class InfoModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
