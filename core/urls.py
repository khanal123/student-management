"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from users.views import SocialloginUserRole

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # urls for course app
    path("", include('course.urls', namespace="course")),
    
    # urls for account app
    path("users/", include('users.urls', namespace="users")),

    # urls for notice app
    path("notice/", include('notice.urls', namespace='notice')),

    # urls for event app
    path("event/", include('event.urls', namespace='event')),

    # urls for social login
    path('accounts/', include('allauth.urls')),
    path('accounts/user/role', SocialloginUserRole.as_view(), name="userroledit"),

    # urls for api
    path('api/', include('api.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
