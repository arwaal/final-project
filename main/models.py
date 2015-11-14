from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
# from djangoratings.fields import RatingField

# Create your models here.

class Users(models.Model):
    regular_user = models.OneToOneField(User)
    business_user = models.NullBooleanField(null=True, default=False)
    address = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    recomendation = models.ForeignKey('main.Recommendation', null=True, blank=True)

    def __unicode__ (self):
        return self.regular_user.username

class Recommendation(models.Model):
    name = models.CharField(max_length=255, null=True)
    info = models.TextField(null=True)
    map_img = models.ImageField(upload_to='maps', blank=True)
    image1 = models.ImageField(upload_to='recommendations', blank=True)
    image2 = models.ImageField(upload_to='recommendations', blank=True)
    image3 = models.ImageField(upload_to='recommendations', blank=True)
    image4 = models.ImageField(upload_to='recommendations', blank=True)
    image5 = models.ImageField(upload_to='recommendations', blank=True)
    image6 = models.ImageField(upload_to='recommendations', blank=True)
    image7 = models.ImageField(upload_to='recommendations', blank=True)
    image8 = models.ImageField(upload_to='recommendations', blank=True)
    image9 = models.ImageField(upload_to='recommendations', blank=True)
    image10 = models.ImageField(upload_to='recommendations', blank=True)
    address = models.TextField(null=True)
    mobile_number = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey('main.Category', null=True)
    up_votes = models.ManyToManyField('main.Users', related_name='up_votes')
    down_votes = models.ManyToManyField('main.Users', related_name='down_votes')
    website = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    youtube = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=150, blank=True)
    telephone = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class BusinessSubmission(models.Model):
    user = models.OneToOneField('main.Users')
    pending = models.BooleanField(default=True)
    recomendation = models.OneToOneField('main.Recommendation', null=True, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=250, unique=True)

    def __unicode__(self):
        return self.user


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    info = models.TextField(null=True)

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    # reply = models.ForeignKey('main.Comment', null=True, blank=True, related_name='+')
    recomendation = models.ForeignKey('main.Recommendation', blank=False)
    def __unicode__(self):
        return self.comment

# class RecoRate(models.Model):
#     reco = models.ForeignKey('main.Recommendation')
#     rate = models.IntegerField()

#     def __unicode__(self):
#         return self.reco
















