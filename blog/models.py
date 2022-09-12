from enum import auto
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        if (self.name == "---------"):
            return "Non Categorized"
        return self.name 

    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('allposts')

class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField(null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="profile_pics/")
    website_url = models.CharField(max_length=255,null=True,blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    instagram_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    pinterest_url = models.CharField(max_length=255,null=True,blank=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('allposts')

class Post(models.Model):
    title = models.CharField(max_length=255)         # Title of blog
    title_tag = models.CharField(max_length=255)     # Title of blog post to be shown in head
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    body = RichTextField(blank=True,null=True)
    snippet = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author) # self.author is an object and it is to be converted into string
    
    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('allposts')

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True,default="")
    body = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)