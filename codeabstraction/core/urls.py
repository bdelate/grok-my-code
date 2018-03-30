from django.urls import path
from .views import Home, Portfolio

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('portfolio/', Portfolio.as_view(), name='portfolio'),
]
