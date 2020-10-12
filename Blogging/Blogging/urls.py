"""Blogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including Nikita choudhary is inviting you to a scheduled Zoom meeting.

Topic: Day 20 PyDjango
Time: Sep 12, 2020 06:30 PM

Join Zoom Meeting
https://zoom.us/j/6529354974?pwd=WmhkMmFOV3FGVkV6ZHRFcUV1amVyUT09

Meeting ID: 652 935 4974
Passcode: happinessanother URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blog.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',FirstPage),
    path('SecondPage/',SecondPage,name = 'second'),
    path('temp/',HtmlPage),
    path('allstudent/',Allstudent,name = "alls"),
    path('singledata/',getdata),
    path("details/<int:sid>/",StudentDetail,name='sdetail'),
    path('addition/<int:num1>/<int:num2>/',Add,name ='Add'),

    path('All_category/',AdminPanel,name = 'allc'),
    path('cat_detail/<int:cid>/', Category_detail, name="cdetail"),
    path('testfile/',test,name = 'test'),
    path('dynamic_fun/<int:num>',test1,name = 'test1'),
    path('add_form/',HtmlForm,name='form'),
    path('add_category/',AddCategory,name ='add_cat'),
    path('add_blog/',AddBlog,name ='add_blog'),
    path('Login/', LoginForm, name='login'),
    path('home/', Home, name='home'),
    path('UserPanel', Userpanel, name='upanel'),
    path('logout/', LogoutUser, name='logout'),
     path('Signup/', Signup, name='signup'),
    path('Edit_blog/<int:bid>/', Edit_blog, name='edit_b'),
path('delete_blog/<int:bid>/', DeleteData, name='delete_b'),

################# New URLs ######################
path('', NewHome, name='newhome'),
path('about/', AboutUs, name='about'),
path('allblog/', AllBlogs, name='blogs'),
path('contact/', ContactUs, name='contact'),
path('blog_detail/<int:bid>/', Newblogdetail, name="bdetail"),
path('blog_comment/<int:bid>/', AddComment, name="comment"),
path('blog_like/<int:bid>/', LikeTheBlog, name="like"),
path('UserPanel', Userpanel, name='upanel'),

]+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)

