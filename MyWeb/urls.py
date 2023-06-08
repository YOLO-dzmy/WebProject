from django.urls import path
from . import views

# MyWeb urls
urlpatterns = [
    path('', views.list),
    path('update', views.check),
    path("<int:id>", views.num)
]
