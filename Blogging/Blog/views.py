from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
# Create your views here.

def FirstPage(request):
    name = "vaishnavi"
    return HttpResponse("<h1>Welcome " + name + "</h1>")


def SecondPage(request):
    return HttpResponse("<h1>Welcome to TechSim+</h1>")

def HtmlPage(request):
    slist = ["swagat","Parth","Pragya","Vaishnavi","Chandan"]
    d = {"sdata":slist}
    return render(request, 'index.html',d)


def Allstudent(request):
    data = Student.objects.all() # list of objects[]
    d = {"studentdata":data}
    return render(request,'students.html',d)

def getdata(request):
    data = Student.objects.get(id=3) # single object

    filterdata = Student.objects.filter(branch = "CS")# [] List of objects
    lastob = Student.objects.filter(branch = "CS").last()
    fristob = Student.objects.filter(branch = "CS").first()
    print("filterdata:.....",filterdata)
    d = {"student":data,"filterdata":filterdata}
    return render(request,'single.html',d)

def Add(request,num1,num2):
    print(num1,num2)
    output = num1 + num2
    return HttpResponse("<h1>Output: "+str(output)+"</h1>")

def StudentDetail(request,sid):
    data = Student.objects.get(id = sid)
    d = {"student":data}
    return render(request,'details.html',d)




def test(request):
    return render(request,'test.html')

def test1(request,num):
    num = num + 10
    d = {"num":num}
    return render(request,'test1.html',d)


def HtmlForm(request):
    output = None
    if request.method == "POST":
        d = request.POST
        print(d['num1'])
        print(d['num2'])
        a = int(d['num1'])
        b = int(d['num2'])
        output = a + b
    dic = {"op":output}

    return render(request,'hform.html',dic)


from datetime import date

from django.contrib.auth import authenticate,login,logout

### Project Structure
def Home(request):
    allcat = Category.objects.all()
    d = {"allcat":allcat}
    return render(request,'home.html',d)


# If SuperUser
def AdminPanel(request):
    allcat = Category.objects.all()
    d = {"allcat":allcat}
    return render(request,'allcat.html',d)


def AddCategory(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        dic = request.POST
        c = dic['cname']
        Category.objects.create(name = c)
        return redirect('allc')

    return render(request,'add_cat.html')


def Category_detail(request,cid):
    catdata = Category.objects.get(id = cid)
    blogs = BlogModel.objects.filter(cat = catdata)
    d = {"blogs":blogs}
    return render(request,'cat_details.html',d)

# Normal User



def AddBlog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    allcategory = Category.objects.all()
    d = {"allcategory":allcategory}
    if request.method == "POST":
        dic = request.POST
        catid = dic['cat']
        catdata = Category.objects.get(id = catid)
        bname = dic['bname']
        st = dic['short']
        long = dic['long']
        img = request.FILES['img']
        #img_post = dic['img']
        #print(img,img_post)
        td = date.today()
        userdata = request.user
        BlogModel.objects.create(usr = userdata,
                                 cat = catdata,
                                 title = bname,
                                 sdes = st,
                                 long_des =long,
                                 image = img,
                                 date = td)
        return redirect('cdetail',catid)

    return render(request,'add_blog.html',d)



# Logout

def LogoutUser(request):
    logout(request)
    return redirect('newhome')

# SignUp

def Signup(request):
    error = False
    if request.method == "POST":
        d = request.POST
        full = d['fname'].split()
        first = full[0]
        last = full[1]
        mob = d['mob']
        em = d['email']
        u = d['uname']
        p = d['pwd']
        i = request.FILES['img']
        user = User.objects.filter(username = u)
        if user:
            error = True
        else:
            userdata = User.objects.create_user(username=u,password=p,
                                     email=em,first_name = first,
                                     last_name = last)
            UserDetail.objects.create(usr = userdata,image = i,mobile= mob)
            return redirect('login')


    dic = {"error":error}
    return render(request,'signup.html',dic)


def Edit_blog(request,bid):
    blogdata = BlogModel.objects.get(id = bid)
    allcategory = Category.objects.all()
    if request.method == "POST":
        dic = request.POST
        catid = dic['cat']
        t = dic['bname']
        s = dic['short']
        l = dic['long']


        file = request.FILES
        if len(file) != 0:
            i = request.FILES['img']
            blogdata.image = i
            blogdata.save()
        '''try:
            i = request.FILES['img']
            blogdata.image = i
            blogdata.save()
        except:
            pass'''


        catdata = Category.objects.get(id = catid)
        blogdata.title = t
        blogdata.sdes = s
        blogdata.long_des = l

        blogdata.cat = catdata
        blogdata.save()
    d = {"blogdata":blogdata,"allcategory":allcategory}
    return render(request,'blog_edit.html',d)


def DeleteData(request,bid):
    blogdata = BlogModel.objects.get(id=bid)
    blogdata.delete()
    return redirect('upanel')





###################### New Front End ########################

def NewHome(request):
    allblog = BlogModel.objects.all()
    bigblog = allblog[len(allblog)-1]
    #allblog = allblog[::-1] negative indexing is not allowed
    last_four_blog = allblog[:4]
    d = {"bigblog":bigblog,"last_four_blog":last_four_blog}
    return render(request,'newtemp/index.html',d)


def AboutUs(request):
    return render(request, 'newtemp/about.html')

def AllBlogs(request):
    blogs = BlogModel.objects.all()
    d = {"blogs":blogs}
    return render(request,'newtemp/allblog.html',d)

def ContactUs(request):
    return render(request, 'newtemp/contact.html')


def Newblogdetail(request,bid):
    data = BlogModel.objects.get(id = bid)
    userdata = UserDetail.objects.filter(usr = data.usr).first()
    comments = UserComment.objects.filter(blog = data)
    n = comments.count()
    d = {"detail":data,"userdata":userdata,"count":n}
    return render(request,'newtemp/single.html',d)


def AddComment(request,bid):
    if not request.user.is_authenticated:
        return redirect('login')
    blogdata = BlogModel.objects.get(id = bid)
    usr = request.user
    td = date.today()
    msg = request.POST['msg']
    UserComment.objects.create(usr = usr,blog = blogdata,date = td,msg = msg)
    return redirect('bdetail',bid)


def LikeTheBlog(request,bid):
    blogdata = BlogModel.objects.get(id=bid)
    user = request.user
    data = LikeBlog.objects.filter(blog = blogdata,usr = user)
    if not data:
        LikeBlog.objects.create(blog = blogdata,usr = request.user)
    else:
        data.delete()

    return redirect('bdetail',bid)


def Userpanel(request):
    if not request.user.is_authenticated:
        return redirect('login')
    userblogs = BlogModel.objects.filter(usr = request.user)
    userdata = UserDetail.objects.get(usr = request.user)
    d = {"blogs":userblogs,"userdata":userdata}

    return render(request, 'newtemp/userpanel.html',d)

def LoginForm(request):
    if request.method == "POST":
        dic = request.POST
        u = dic['user']
        p = dic['pwd']
        user = authenticate(username = u,password = p)
        if user:
            login(request,user)
            if request.user.is_staff:
                 return redirect('allc')
            return redirect('newhome')
        else:
            return HttpResponse("User Not Found")

    return render(request,'newtemp/login.html')





