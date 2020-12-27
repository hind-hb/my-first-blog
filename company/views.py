
from  django.views.decorators.csrf import csrf_exempt
from company.models import Company , Department ,Employee , User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from operator import itemgetter
from django.db import connection

# Create your views here.
def home(request):
    return render(request,'base.html')
def index(request):
    return render(request,'index.html')
def pagehome(request):
    return render(request,'pagehome.html')

def signup(request):
    if request.method=='POST':
        user = User()
        user.fname.request.POST['fname']
        user.lname.request.POST['lname']
        user.email.request.POST['email']
        user.password.request.POST['password']
        user.repassword.request.POST['repassword']
        if user.password != user.repassword :
            return redirect('signup')
        elif user.fname=="" or user.password=="":
             messages.info(request ,'some fields are empty')
             return redirect('signup')
        else:
            user.save()

    return render (request,'signup.html')

def signin(request):
    con = connection.connect(name='db.sqlite3')
    cursor=con.cursor('email')
    con2 = connection.connect['db.sqlite3']
    cursor2 = con.execute('password')
    sqlcommand='select email from User'
    sqlcommand2 = 'select password from User'
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e=[]
    p=[]
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res=list(map(itemgetter(0),e))
    res2 = list(map(itemgetter(0), p))
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password ']
        i=1
        k=len(res)
        while i <k:
            if res[i]==email and res2[i]==password:
                return render(request,'base.html',{'email':email})
                break
            i+1
        else:
            messages.info(request,'check username or password')
            return redirect('signin')

    return render (request,'signin.html')

def add_employee(request):
  content=request.POST['content']
  Employee.objects.create(text=content)
  return HttpResponseRedirect("/")









