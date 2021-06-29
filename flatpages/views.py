from django.views.generic.base import TemplateView


class AuthorPage(TemplateView):
    template_name = 'flatpages/about.html'
    extra_context = {
        'author': True,
        'title': 'Evan Vilagov',
        'content_title': 'About author',
        'links': {
            'Github': 'https://www.github.com/vilagov/',
            'Linkedin': 'https://www.linkedin.com/in/vilagov/',
            'Instagram': 'https://www.instagram.com/evan.vilagov/',
            'Facebook': 'https://www.facebook.com/vilagov/vilagov',
        },
        'email': 'evan.vilagov@gmail.com',
        'text_ru': 'Информация об авторе на русском.',
        'text_en': 'Information about author in English',
    }


class TechPage(TemplateView):
    template_name = 'flatpages/about.html'
    extra_context = {
        'title': 'Stack used',
        'content_title': 'Список использованных технологий',
        'links': {
            'Python 3': '#',
            'Django 3.1': '#',
            'Django REST Framework 3': '#',
            'PostgreSQL': '#',
        },
    }
