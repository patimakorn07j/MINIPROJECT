from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
from django.shortcuts import redirect, get_object_or_404
from .models import Comment  # สมมติว่าคุณมีโมเดล Comment

def index(request):
	return render(request, 'index.html')

def form(request):
	return render(request, 'form.html')

def restaurant1(request):
	comment = Comment.objects.filter(food='restaurant1')
	return render(request, 'restaurant1.html',{'comment':comment})
	
def restaurant2(request):
	comment = Comment.objects.filter(food='restaurant2')
	return render(request, 'restaurant2.html',{'comment':comment})

def restaurant3(request):
	comment = Comment.objects.filter(food='restaurant3')
	return render(request, 'restaurant3.html',{'comment':comment})

def restaurant4(request):
	comment = Comment.objects.filter(food='restaurant4')
	return render(request, 'restaurant4.html',{'comment':comment})

def restaurant5(request):
	comment = Comment.objects.filter(food='restaurant5')
	return render(request, 'restaurant5.html',{'comment':comment})

def restaurant6(request):
	comment = Comment.objects.filter(food='restaurant6')
	return render(request, 'restaurant6.html',{'comment':comment})

def restaurant7(request):
	comment = Comment.objects.filter(food='restaurant7')
	return render(request, 'restaurant7.html',{'comment':comment})

def restaurant8(request):
	comment = Comment.objects.filter(food='restaurant8')
	return render(request, 'restaurant8.html',{'comment':comment})

def restaurant9(request):
	comment = Comment.objects.filter(food='restaurant9')
	return render(request, 'restaurant9.html',{'comment':comment})

def restaurant10(request):
	comment = Comment.objects.filter(food='restaurant10')
	return render(request, 'restaurant10.html',{'comment':comment})

def allrestaurants(request):
	return render(request, 'allrestaurants.html')

def contactus(request):
	return render(request, 'contactus.html')

def login(request):
	return render(request, 'login.html')

def signup(request):
	return render(request, 'signup.html')

def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword :
        if User.objects.filter(username=username).exists():
            print('Username is already used')
            messages.success(request,'Username is already used')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            print('Email ซ้ำ')
            messages.success(request,'Email is already used')
            return redirect('/signup')
        else:
            user = User.objects.create_user(
            username = username,
            first_name = firstname,
            last_name = lastname,
            email = email,
            password = password
            )
            user.save()
            return redirect('/login')
    else:
        print('Password ไม่ตรง')
        messages.success(request,'password not match repassword')
        return redirect('/signup')
	
def loginForm(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username , password=password)
    if user is not None:
        # username pass ถูก
        auth.login(request,user)
        return redirect('/')
    else:
        print('Login bo dai')
        messages.success(request,'Invalid username or password')
        return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')

def submit_comment(request):
	comment = request.POST["comment"]
	food = request.POST["food_id"]
	newcomment = Comment.objects.create(
	user = request.user,
    content = comment,
    food = food
	)
	newcomment.save()
	return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))
