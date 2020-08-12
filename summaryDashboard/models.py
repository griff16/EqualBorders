from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    date = models.DateTimeField(default=None, blank=True, null=True)
    link = models.TextField(default=None, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title

# Table for colleges
class College(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    link = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name + '  , ' + self.code + '  , ' + str(self.link)


