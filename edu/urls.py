from django.urls import path
from . import views

app_name = 'edu'
urlpatterns =[path("edu/", views.post_list),

]