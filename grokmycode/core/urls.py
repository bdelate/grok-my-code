from django.urls import path
from .views import (Home, Portfolio, Contact,
                    DiversifyPortfolio, Kanban, WhoKnows)

app_name = 'core'

urlpatterns = [
    path('',
         Home.as_view(),
         name='home'),
    path('portfolio/',
         Portfolio.as_view(),
         name='portfolio'),
    path('contact/',
         Contact.as_view(),
         name='contact'),
    path('portfolio/diversifyportfolio/',
         DiversifyPortfolio.as_view(),
         name='diversifyportfolio'),
    path('portfolio/kanban/',
         Kanban.as_view(),
         name='kanban'),
    path('portfolio/whoknows/',
         WhoKnows.as_view(),
         name='whoknows'),
]
