from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from projects.models import Deprem,Sel
from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import template
from django.contrib.auth.models import Group




def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('accounts:home')

    return render(request, "accounts/form.html", {"form": form, 'title':'Sign In'})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('accounts:home')
    return render(request, "accounts/form.html", {"form": form, 'title': 'Sign Up'})

def updateProfile(request):
    if request.user.is_authenticated:
        user = request.user
        form = RegisterForm(request.POST or None,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect('accounts:home')
        return render(request, "accounts/form.html", {"form": form, 'title': 'Update User Information'})
    else:
        return render(request, 'accounts/notLogin.html')

def viewProfile(request):
    if request.user.is_authenticated:
        user = request.user
        deprems = user.deprems.all()
        sels = user.sels.all()


        context = {
            'user': user,
            'prjDpr': deprems,
            'prjSel': sels,
        }

        return render(request, 'accounts/viewUser.html', context)
    else:
        return render(request, 'accounts/notLogin.html')

def firstPage(request):
    form1 = LoginForm(request.POST or None)
    form2 = RegisterForm(request.POST or None)
    if form1.is_valid():
        username = form1.cleaned_data.get('username')
        password = form1.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('accounts:home')

    if form2.is_valid():
        user = form2.save(commit=False)
        password = form2.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('accounts:home')

    return render(request, "accounts/firstPage.html", {'form1': form1, 'form2':form2, 'title': 'Welcome'})


def logout_view(request):
    logout(request)
    return redirect('firstPage')


def homeView(request):

    if request.user.is_authenticated:

        user = request.user


        projectsDeprem = Deprem.objects.order_by('-crtDate')
        projectsSel = Sel.objects.order_by('-crtDate')


        prjDpr = []
        i = 0
        for prj in projectsDeprem:
            if i< 7:
                prjDpr.append(prj)
            i = i+1

        prjSel = []
        i = 0
        for prj in projectsSel:
            if i < 7:
                prjSel.append(prj)
            i = i + 1

        context = {
            'prjDpr': prjDpr,
            'prjSel': prjSel
        }
        return render(request, 'home/home.html', context)
    else:
        return render(request, 'accounts/notLogin.html')



#####
#####
#####
######

## Turkish ###


def login_viewTr(request):
    form = LoginFormTr(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('accounts:homeTr')

    return render(request, "accounts/Turkish/formTr.html", {"form": form, 'title':'Giriş Yap'})

def register_viewTr(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('accounts:homeTr')
    return render(request, "accounts/Turkish/formTr.html", {"form": form, 'title': 'Kayıt Ol'})

def updateProfileTr(request):
    if request.user.is_authenticated:
        user = request.user
        form = RegisterForm(request.POST or None,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect('accounts:homeTr')
        return render(request, "accounts/Turkish/formTr.html", {"form": form, 'title': 'Bilgileri Güncelle'})
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')

def viewProfileTr(request):
    if request.user.is_authenticated:
        user = request.user
        deprems = user.deprems.all()
        sels = user.sels.all()


        context = {
            'user': user,
            'prjDpr': deprems,
            'prjSel': sels,
        }

        return render(request, 'accounts/Turkish/viewUserTr.html', context)
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')

def firstPageTr(request):
    form1 = LoginFormTr(request.POST or None)
    form2 = RegisterFormTr(request.POST or None)
    if form1.is_valid():
        username = form1.cleaned_data.get('username')
        password = form1.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('accounts:homeTr')

    if form2.is_valid():
        user = form2.save(commit=False)
        password = form2.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('accounts:homeTr')

    return render(request, "accounts/Turkish/firstPageTr.html", {'form1': form1, 'form2':form2, 'title': 'Hoşgeldiniz'})



def logout_viewTr(request):
    logout(request)
    return redirect('firstPageTr')


def homeViewTr(request):

    if request.user.is_authenticated:

        user = request.user


        projectsDeprem = Deprem.objects.order_by('-crtDate')
        projectsSel = Sel.objects.order_by('-crtDate')


        prjDpr = []
        i = 0
        for prj in projectsDeprem:
            if i< 7:
                prjDpr.append(prj)
            i = i+1

        prjSel = []
        i = 0
        for prj in projectsSel:
            if i < 7:
                prjSel.append(prj)
            i = i + 1

        context = {
            'prjDpr': prjDpr,
            'prjSel': prjSel
        }
        return render(request, 'home/Turkish/homeTr.html', context)
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')





