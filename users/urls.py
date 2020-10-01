from django.urls import path

from .views import home_view, signup_view, dashboard_view, about_view,faq_view
from .views import course_view,book_list,upload_book,delete_book,BookListView,UploadBookView
app_name = "users"

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='sign-up'),
    path('dashboard/', dashboard_view, name='dashboard'),
    #path('new_search/',search_view,name='new_search'),
    path('aboutus/',about_view,name='aboutus'),
    path('faqs/',faq_view,name='faqs'),
    path('course/',course_view,name='course'),
    

]
