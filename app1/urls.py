from django.urls import path

#from app1 import views
from . import views
urlpatterns = [
    path('index',views.index,name="index_page"),
    path('home',views.home,name="home_page"),
    path('delete/<rid>',views.delete),
    path('addition/<x1>/<x2>',views.addition),
    path('blogform',views.postblog),
    path('contact',views.contact),
    path('placement',views.placement),
    path('create',views.create),
    path('store',views.store)
]
