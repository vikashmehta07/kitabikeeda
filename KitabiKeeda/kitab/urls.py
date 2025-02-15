from django.urls import path
from . import views
# from .views import upload_pdf, search_pdf

urlpatterns = [
    path('',views.home, name='home'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('search/', views.search_pdf, name='search_pdf'),
]