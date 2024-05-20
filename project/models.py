from django.db import models



class Post(models.Model):
    text = models.TextField(max_length=256)
    image = models.ImageField(upload_to='images', blank=True)
    link = models.URLField(blank=True)
    pub_date = models.DateTimeField("date published")
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.text

class Tag(models.Model):
    text = models.TextField(max_length=256)

    def __str__(self):
        return self.text


