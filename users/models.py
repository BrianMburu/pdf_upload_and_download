from __future__ import unicode_literals
from django.db import models
from .validators import validate_file_extension
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.


'''
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.search)
    class Meta:
        verbose_name_plural = 'searches'
'''

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/',validators=[validate_file_extension],storage= RawMediaCloudinaryStorage())
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    course = models.ForeignKey('Course', related_name='books', blank=True, null=True,on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.title+"-"+self.filename

    def __unicode__(self):
        return "%s %s" % (self.title, self.author)

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

    @property
    def filename(self):
        return self.pdf.name.rsplit('/', 1)[-1]
        
    def __unicode__(self):
        return "%s %s" % (self.title, self.author)
    
class Course(models.Model):
    class Meta:
        verbose_name_plural = 'Courses'
    course_title = models.CharField('Title', max_length=100)

    def __str__(self):
        return self.course_title

