import os
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('ads.urls')),  
    path('admin/', admin.site.urls),  
    path('accounts/', include('django.contrib.auth.urls')),  
    url(r'^oauth/', include('social_django.urls', namespace='social')),  

    # Sample applications
    path('cats/', include('cats.urls')),
    path('chat/', include('chat.urls')),
    path('polls/', include('polls.urls')),


]

# Serve the favicon
urlpatterns += [
    path('favicon.ico', serve, {
        'path': 'favicon.ico',
        'document_root': os.path.join(BASE_DIR, 'home/static'),
    }
         ),
]

# Switch to social login if it is configured
try:
    from . import github_settings

    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')
