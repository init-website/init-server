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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import mysite.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mysite.views.home, name="home"),

    path('homework/',mysite.views.homework, name="homework"),
    path('homework/<int:year>/', mysite.views.homework_list, name="homework_list"),
    path('homework/<int:year>/<int:homework_id>/', mysite.views.homework_detail, name='homework_detail'),
    path('homework/<int:year>/<int:homework_id>/submit/', mysite.views.homework_submit, name='homework_submit'),
    path('homework/<int:year>/<int:homework_id>/result/', mysite.views.homework_result, name='homework_result'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', mysite.views.signup, name='signup'),
    path('accounts/update/', mysite.views.update, name='update'),
    path('accounts/password/', mysite.views.change_password, name='change_password'),
    path('accounts/profile/', mysite.views.get_profile, name='get_profile'),
    path('accounts/profile/update/', mysite.views.update_profile, name='update_profile'),

    path('projects/',mysite.views.projects, name='projects'),
    path('projects/<int:pk>/',mysite.views.project_detail, name='project_detail'),
    path('projects/project_new/', mysite.views.project_new, name='project_new'),
    path('blog/<int:pk>/delete/', mysite.views.project_delete, name='project_delete'),
    path('blog/<int:post_id>/update', mysite.views.project_update, name='project_update'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
