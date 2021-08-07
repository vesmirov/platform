from django.conf import settings
from django.conf.urls import handler404, handler500, handler403
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

handler404 = 'blog.errors.page_not_found'  # noqa: F811
handler500 = 'blog.errors.server_error'  # noqa: F811
handler403 = 'blog.errors.forbidden'  # noqa: F811

urlpatterns = [
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('flatpages.urls')),
    path('me/', RedirectView.as_view(url=reverse_lazy('author'),
                                     permanent=True))
]

urlpatterns += [
    path('api/', include('api.urls')),
    path('notes/', include('notes.urls', namespace='notes')),
    path('', include('posts.urls', namespace='posts')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
