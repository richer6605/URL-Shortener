from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:mapping_string>', views.redirectToOrigin, name='redirect'),
    path('new/<path:original_url>', views.createMapping, name='mapping'),
]