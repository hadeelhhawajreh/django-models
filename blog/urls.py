from django.urls import path,include
from .views import HomeView,DetalisView
urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('<int:pk>/', DetalisView.as_view(),name='details')
]
