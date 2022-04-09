from django.contrib import admin
from django.urls import path
from main.views import index, blog, posting, new_post, remove_post, edit, update
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', posting, name='posting'),
    path('blog/new_post/', new_post, name='new_post'),
    path('blog/<int:pk>/edit/', edit, name='edit'),
    path('blog/<int:pk>/update/', update, name='update'),
    path('blog/<int:pk>/remove/', remove_post, name='remove_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
