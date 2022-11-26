from django.views.generic.base import TemplateView

from .texts import TEXT_RU, TEXT_EN


class AuthorPage(TemplateView):
    """About author page"""

    template_name = 'flatpages/about.html'
    extra_context = {
        'author': True,
        'title': 'Evan Vesmirov',
        'content_title': 'About author',
        'links': {
            'Github': 'https://www.github.com/vesmirov/',
            'Linkedin': 'https://www.linkedin.com/in/vesmirov/',
            'Instagram': 'https://www.instagram.com/evan.vesmirov/',
            'Facebook': 'https://www.facebook.com/vesmirov/',
        },
        'email': 'evan.vesmirov@gmail.com',
        'text_ru': TEXT_RU,
        'text_en': TEXT_EN,
    }


class TechPage(TemplateView):
    """Project stack page"""

    template_name = 'flatpages/about.html'
    extra_context = {
        'title': 'Stack',
        'content_title': 'Список использованных технологий',
        'links': {
            'Python 3.9.2': 'https://www.python.org/downloads/release/python-392/',  # noqa
            'Django 3.2.4': 'https://docs.djangoproject.com/en/3.2/releases/3.2.4/', # noqa
            'Bootsrap 5': 'https://getbootstrap.com/docs/5.0/getting-started/introduction/',  # noqa 
            'Gunicorn 20.1': 'https://gunicorn.org/',
            'Nginx': 'https://nginx.org/',
            'PostgreSQL': 'https://www.postgresql.org/',
        },
    }
