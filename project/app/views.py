from django.shortcuts import render
from .models import Student,Query

from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def registerdata(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        contact = request.POST.get('Contact')
        password = request.POST.get('Password')
        cpassword = request.POST.get('Cpassword')


        data = Student.objects.filter(Email=email)
        if data:
            msg = 'user already exit'
            return render(request,'register.html',{'key':msg})
        else:
            if password == cpassword:
                Student.objects.create(Name=name,
                                        Email = email,
                                        Contact = contact,
                                        Password= password)
                msg="Registration Successfully"
                
              #  For mail    
                subject='Test_mail from django server'
                message='This is demo-test mail'
                from_email='arpitkhare14@gamil.com'
                recipient_list=['arpitkhare14@gmail.com','sumitumariya11@gmail.com']
                send_mail(subject, message, from_email, recipient_list)
                # -----------------

                return render(request,'login.html',{'key':msg})
            
            else:
                msg = "Password & conformpassword not macthed"
                return render(request,'register.html',{'key':msg})

def logindata(request):
    # print(request.POST)
    email = request.POST.get('email')
    password = request.POST.get('password')
    # print(password)

    user = Student.objects.filter(Email=email)
    if user:
        data = Student.objects.get(Email = email)
        passs = data.Password
        # print(passs)
        if passs == password:
            request.session['name']=data.Name
            request.session['email']=data.Email
            request.session['contact']=data.Contact
            request.session['password']=data.Password

            Nm = request.session.get('name')
            Em = request.session.get('email')
            Cm = request.session.get('contact')
            Ps = request.session.get('password')
            context = {
                'Nm':Nm,
                'Em':Em,
                'Cm':Cm,
                'Ps':Ps
            }
            return render(request,'dashboard.html',{'context':context})
        
        else:
            msg = "Email & password not matched"
            return render(request,'login.html',{'key':msg})
    
    else:
        msg = "enter valid Email_ID"
        return render(request,'login.html',{'key':msg})

def logout(request):
    return render(request,'home.html')

def Querydata(request):
    # print(request.method)
    # print(request.POST)
    if request.method == "POST":
        email = request.POST.get('email')
        title = request.POST.get('title')
        description = request.POST.get('description')
        # print(email,title,description)
        Query.objects.create(Email=email,
                                 Title = title,
                                 discription = description)
        
        Nm = request.session.get('name')
        Em = request.session.get('email')
        Cm = request.session.get('contact')
        Ps = request.session.get('password')
        context = {
            'Nm':Nm,
            'Em':Em,
            'Cm':Cm,
            'Ps':Ps
        }
        return render(request,'dashboard.html',{'context':context})
    
def Show(request):
    # print("sumit",request.POST)
    if request.method == "POST":
        email = request.POST.get('email')
        QueryData = Query.objects.filter(Email = email)
        Nm = request.session.get('name')
        Em = request.session.get('email')
        Cm = request.session.get('contact')
        Ps = request.session.get('password')
        context = {
            'Nm':Nm,
            'Em':Em,
            'Cm':Cm,
            'Ps':Ps
        }
        return render(request,'dashboard.html',{'context':context,'QueryData':QueryData})
        
        
def delete(request,pk,ml):
        del1 = Query.objects.get(id=pk)
        del1.delete()
   
        QueryData = Query.objects.filter(Email = ml)
        data = Student.objects.get(Email= ml)
        Nm = request.session.get('name')
        Em = request.session.get('email')
        Cm = request.session.get('contact')
        Ps = request.session.get('password')
        context = {
            'Nm':Nm,
            'Em':Em,
            'Cm':Cm,
            'Ps':Ps
        }
        return render(request,'dashboard.html',{'context':context,'QueryData':QueryData})

def editpage(request,pk):
    data1 = Query.objects.get(id = pk)
    email = data1.Email
 
    Nm = request.session.get('name')
    Em = request.session.get('email')
    Cm = request.session.get('contact')
    Ps = request.session.get('password')
    context = {
        'Nm':Nm,
        'Em':Em,
        'Cm':Cm,
        'Ps':Ps
    }
    alldata = Query.objects.filter(Email = email)
    return render(request,'dashboard.html',{'key1':alldata,'context':context,'key2':data1})

def updatedata(request,pk):
    print(request.POST)
    email = request.POST.get('email')
    udata = Query.objects.get(id =pk)
    udata.Email = request.POST['email']
    udata.Title = request.POST['title']
    udata.discription = request.POST['description']
    
    udata.save()
    Nm = request.session.get('name')
    Em = request.session.get('email')
    Cm = request.session.get('contact')
    Ps = request.session.get('password')
    context = {
        'Nm':Nm,
        'Em':Em,
        'Cm':Cm,
        'Ps':Ps
    }
    alldata = Query.objects.filter(Email = email)
    return render(request,'dashboard.html',{'key1':alldata,'context':context})
