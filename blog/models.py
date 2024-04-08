from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    author = models.CharField(max_length=12)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class About(TimeStampedModel):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='about')
    profession = models.CharField(max_length=212)
    project_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    phone = models.CharField(max_length=212)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name

