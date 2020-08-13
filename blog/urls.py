from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', views.all_blog, name='all_blog'),

    path('<int:bid>/', views.view_blog, name='view_blog')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)