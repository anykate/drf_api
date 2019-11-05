from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('api/', views.api_index_view, name='api_index'),
    path('api/', views.APIIndexView.as_view(), name='api_index'),
]
