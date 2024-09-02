"""
URL configuration for info_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import HomeView, PublicationDetailView, CreatePublicationCommentView, HomesearchView, \
    contact_client_view
from info_core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    ]
urlpatterns += i18n_patterns(
    path('home/', HomeView.as_view(), name='home'),
    path('home/search/', HomesearchView.as_view(), name='home-search-url'),
    path('contact/', contact_client_view, name='contact_list'),
    path('contact/contact_client/', contact_client_view, name='contact_client'),
    path('publication-detail/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('publication-detail/<int:pk>/create-comment/', CreatePublicationCommentView.as_view())
)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)