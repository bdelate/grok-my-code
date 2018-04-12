from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException


class Home(TemplateView):

    template_name = 'core/index.html'
    extra_context = {'active_link': 'about'}


class Portfolio(TemplateView):

    template_name = 'core/portfolio.html'
    extra_context = {'active_link': 'portfolio'}


class Contact(FormView):

    form_class = ContactForm
    template_name = 'core/contact.html'
    extra_context = {'active_link': 'contact'}

    def form_valid(self, form):
        message = 'Sender email: {}\n\n{}'.format(
            form.cleaned_data.get('email'),
            form.cleaned_data.get('message'))
        try:
            send_mail(subject='Email from Grok My Code',
                      message=message,
                      from_email=settings.DEFAULT_FROM_EMAIL,
                      recipient_list=[settings.DEFAULT_FROM_EMAIL])
        except SMTPException:
            self.extra_context['email_result'] = 'error'
        else:
            self.extra_context['email_result'] = 'success'
        return render(self.request,
                      'core/contact_done.html',
                      self.get_context_data())


class DiversifyPortfolio(TemplateView):

    template_name = 'core/diversifyportfolio.html'


class WhoKnows(TemplateView):

    template_name = 'core/whoknows.html'
