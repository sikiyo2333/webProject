from django.db import models

# Create your models here.


# class Subject(models.Model):
#     name = models.CharField(max_length=128, unique=True)

#     def __unicode__(self):
#         return self.name


# class Page(models.Model):
#     subject = models.ForeignKey(Subject)
#     title = models.CharField(max_length=128)
#     url = models.URLField()
#     views = models.IntegerField(default=0)

#     def __unicode__(self):
#         return self.title
