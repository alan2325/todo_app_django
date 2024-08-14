from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('add',views.add),
    path('view',views.view),
    path('edit/<std>',views.edit),
    path('delete/<ID>',views.delete)
]