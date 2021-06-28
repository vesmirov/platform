from django.views.generic.base import TemplateView


class AuthorPage(TemplateView):
    template_name = 'flatpages/about.html'
    extra_context = {
        'page': 'author',
        'title': 'Evan Vilagov',
        'content_title': 'About author',
        'github': 'vilagov',
        'instagram': 'evan.vilagov/',
        'linkedin': 'vilagov',
        'facebook': 'vilagov',
        'email': 'evan.vilagov@gmail.com',
        'text_ru': '',
        'text_en': '',
    }


class TechPage(TemplateView):
    template_name = 'flatpages/about.html'
    extra_context = {
        'page': 'tech',
        'title': 'Used technologies',
        'content_title': 'Список использованных технологий',
        'content': [
            'Python 3',
            'Django 3.1',
            'Django REST Framework 3',
            'PostgreSQL',
        ],
    }
