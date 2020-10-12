from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Student(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    mobile = models.CharField(max_length=13,null=True)
    address = models.TextField(null=True)
    branch = models.CharField(max_length=50,default="CS")
    roll_no = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name


class BlogModel(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    sdes = models.TextField(null=True)
    long_des = models.TextField(null=True)
    date = models.DateField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.title + " -- " + self.cat.name

class LikeBlog(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, null=True)



class UserDetail(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=100,null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.usr.first_name

class UserComment(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE,null=True)
    msg = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.usr.first_name + '--' + self.blog.title















