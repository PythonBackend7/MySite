from django.urls import path
from .views import (home_page, about_page, contact_page, blog_page, post_detail)


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('blog/', blog_page, name='posts'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]