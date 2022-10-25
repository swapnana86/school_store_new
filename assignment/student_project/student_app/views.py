# from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import StudentCreationForm
from .models import Course, Userdata as UserdataModel


# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['c_password']

        details = User.objects.create_user(username, password, c_password)

        details.save()
        messages.success(request, 'Your account has been created Successfully')
        return redirect('signin')
    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(username=username, password=password)
        print('Hiiii')
        if auth_user is not None:
            auth_login(request, auth_user)
            student_info = UserdataModel.objects.filter(user_id=auth_user.id).all()
            print(student_info)
            if not student_info.exists():
                print('hii')
                return redirect('student_create')
            else:
                return render(request, 'students/student_info.html', {'student_info': student_info})

        else:
            messages.error(request, 'Wrong Credentials')
            return render(request, 'login.html')

    return render(request, 'login.html')


# @login_required
def student_create_view(request):
    form = StudentCreationForm()

    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
    if form.is_valid():
        s = form.save()
        return redirect('student_info', id=s.id)
    else:
        print("NOT VAAALID")

    return render(request, 'students/home.html', {'form': form})


def student_info(request, id):
    print(id)
    student_info = UserdataModel.objects.filter(id=id).all()
    print(student_info)

    return render(request, 'students/student_info.html', {'student_info': student_info})


# AJAX
def load_course(request):
    # print("AJAX CALLEDDDDDDD")
    dept_id = request.GET.get('dept_id')
    # print(dept_id)
    courses = Course.objects.filter(dept_id=dept_id).all()
    # print(courses)
    return render(request, 'drop_down/course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(course.values('id', 'name')), safe=False)


def logout(request):
    auth_logout(request)
    return redirect('/')
