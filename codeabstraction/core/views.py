from django.views.generic import TemplateView


class Home(TemplateView):

    template_name = 'core/index.html'
    extra_context = {'active_link': 'about'}
