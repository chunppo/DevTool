from django.db import models

class Album(models.Model):
    albumid = models.CharField(max_length=30,  default='aa')
    title = models.CharField(max_length=30,  default='bb')
    artistid = models.CharField(max_length=30,  default='cc')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def __unicode__(self):
        return self.name

class Book(models.Model):
    bName        = models.CharField(max_length=30,  default='book_name')
    bPrice       = models.IntegerField(default='12000')
    bAuthor      = models.CharField(max_length=30,  default='ABC')
    bISBN        = models.CharField(max_length=30,  default='ISBN')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def __unicode__(self):
        return self.name
