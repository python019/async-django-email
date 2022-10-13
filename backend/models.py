from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscriped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title