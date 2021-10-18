from django.urls import path
from .import views
urlpatterns = [
    path('', views.home,name="task-home"),
    # path('result',views.home,name="task-result")
    
]