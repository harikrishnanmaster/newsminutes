from django.contrib import admin
from django.urls import path, include
urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include("news.urls")),
]
urlpatterns += patterns('',
    (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)