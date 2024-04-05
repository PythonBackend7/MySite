from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    author = models.CharField(max_length=12)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class About(models.Model):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='about')
    profession = models.CharField(max_length=212)
    project_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    phone = models.CharField(max_length=212)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
