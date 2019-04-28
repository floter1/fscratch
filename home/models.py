from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


# Create your models here.


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
    
class Articles(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=250)
    writer = models.CharField(max_length=250)
    points = models.FloatField(null=True, blank=True, default=0.0)
    like = models.FloatField(null=True, blank=True, default=0.0)

class Comment(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    like = models.FloatField(null=True, blank=True, default=0.0)
    points = models.FloatField(null=True, blank=True, default=0.0)
    author = models.CharField(max_length=250)
    commentor = models.CharField(max_length=250)
    
class Bsell(models.Model):
    user_name = models.CharField(max_length=250)
    owner = models.CharField(max_length=250, default="admin")
    coins = models.FloatField(null=True, blank=True, default=0.0)
    price = models.FloatField(null=True, blank=True, default=1.0)
    
class Members(models.Model):
	user_name = models.CharField(max_length=250)
	age = models.IntegerField(null=True, blank=True, default=18)
	phone = models.CharField(max_length=250)
	upline = models.CharField(max_length=250)
	tin = models.CharField(max_length=250)
	points = models.FloatField(null=True, blank=True, default=0.0)
	money = models.FloatField(null=True, blank=True, default=0.0)
	photo = models.ImageField(upload_to='avatar', default='avatars/default/default.jpg')
	    