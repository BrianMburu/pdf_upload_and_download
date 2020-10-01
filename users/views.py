from __future__ import unicode_literals
import requests
from django.shortcuts import render, redirect,get_object_or_404,Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from django.views import generic
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.db import transaction

from .forms import SignUpForm,BookForm,SearchBookForm,CourseProfileForm
from .models import Book,Course
from profiles.models import Profile
from search_views.views import SearchListView
from search_views.filters import BaseFilter

# This the get book function to obey DRY rule
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')

    if request.method == "POST":
        form = SignUpForm(request.POST)
        course_form = CourseProfileForm(request.POST)
        if form.is_valid() and course_form.is_valid():
            user = form.save()
            profile = course_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('users:dashboard')
        else:
            messages.error(request, 'Correct the errors below')
    else:
        form = SignUpForm()
        course_form = CourseProfileForm()

    context = {'form':form,'course_form':course_form}
    return render(request, 'app/signup.html',context)


@login_required
def dashboard_view(request):
    username = request.user.username
    user = get_object_or_404(User, username=username)
    if request.user.username != user.username:
        raise Http404
    course = user.profile.course
    books = Book.objects.filter(course__course_title = course)
    context = {'books':books,'course':course}
    return render(request,'app/dashboard.html',context)
	


def home_view(request):
    profile = Profile.objects.all()
    book = Book.objects.order_by('-pub_date')
    books = []
    for i in book and range(10):
        if i >= len(book): break
        books.append(book[i])
    context = {'books':books,'profile':profile}
    return render(request, 'app/index.html',context)
    
def about_view(request):
	return render(request,'app/about.html')

def faq_view(request):
	return render(request,'app/faq.html')
    
@login_required   
def course_view(request):
    username = request.user.username
    user = get_object_or_404(User, username=username)
    if request.user.username != user.username:
        raise Http404
    course = user.profile.course
    books = Book.objects.filter(course__course_title = course)
    if user.profile.course == "Available Courses":
        books = books.order_by('-pub_date')
    else:
        books =books.filter(course__course_title = course)
    context = {'books':books,'course':course}
    return render(request,'app/dashboard.html',context)


def book_list(request):
        books = Book.objects.all()
        return render(request, 'app/book_list.html', {
            'books': books
        })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'app/upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

class BookListView(ListView):
    model = Book
    template_name = 'app/class_book_list.html'
    context_object_name = 'books'
    

class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'app/upload_book.html'

class BookFilter(BaseFilter):
    search_fields = {
        "search_name" : ["title","author"],
    }
class BookSearchView(SearchListView):
    model = Book
    template_name = "app/search_list.html"

    form_class = SearchBookForm
    filter_class = BookFilter