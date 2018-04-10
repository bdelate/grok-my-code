from django.views.generic import TemplateView


class Home(TemplateView):

    template_name = 'core/index.html'
    extra_context = {'active_link': 'about'}


class Portfolio(TemplateView):

    template_name = 'core/portfolio.html'
    extra_context = {'active_link': 'portfolio'}


class DiversifyPortfolio(TemplateView):

    template_name = 'core/diversifyportfolio.html'


class WhoKnows(TemplateView):

    template_name = 'core/whoknows.html'
