"""project_impact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from core import views as core_views

urlpatterns = [
    # Index
    path('', core_views.index, name='index'), 
    path('', RedirectView.as_view(url='/index/', permanent=True)),
    
    # How to Give Back to Foster Community
    path('giveback/', core_views.give_back, name='give_back'),
    
    # Blog List and Blog Detail
    path('blog/', core_views.BlogPostListView.as_view(), name='blog'),
    path('blog/<int:pk>', core_views.BlogPostDetailView.as_view(), name='blog-detail'),

    # Resource List and Resource Detail
    path('resource/', core_views.ResourceListView.as_view(), name='resource'),
    path('resource/<int:pk>', core_views.ResourceDetailView.as_view(), name='resource-detail'),


    # Django Registration Redux
    path('accounts/', include('registration.backends.admin_approval.urls')),
    path('admin/', admin.site.urls),

    # Forms
    path('newblog/', core_views.add_new_blog, name='add_new_blog'),
]

# Django Debug Toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
