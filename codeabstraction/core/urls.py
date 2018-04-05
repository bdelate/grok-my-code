from django.urls import path
from .views import Home, Portfolio, WhoKnows

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('portfolio/', Portfolio.as_view(), name='portfolio'),
    path('portfolio/whoknows/', WhoKnows.as_view(), name='whoknows'),
]
