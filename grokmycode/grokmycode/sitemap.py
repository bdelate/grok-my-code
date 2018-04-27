from django.contrib import sitemaps
from django.urls import reverse


class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return ['core:home', 'core:portfolio', 'core:contact',
                'core:diversifyportfolio', 'core:whoknows']

    def location(self, item):
        return reverse(item)
