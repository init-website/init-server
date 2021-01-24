"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import mysite.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mysite.views.home, name="home"),
    path('new/',mysite.views.new, name="new"),
    path('homework/',mysite.views.homework, name="homework"),
    path('homework/<int:year>/', mysite.views.homework, name="homework"),
    path('homework/<int:year>/<int:homework_id>/', mysite.views.homework_detail, name='detail'),
    path('homework/<int:year>/<int:homework_id>/submit/', mysite.views.homework_submit, name='submit'),
    path('homework/<int:year>/<int:homework_id>/result/', mysite.views.homework_result, name='result'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', mysite.views.signup, name='signup'),
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
