"""myssite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from login import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('marker', views.markerView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^maps/', views.dashboard),
    url(r'^', include(router.urls)),
    url(r'^view', views.listView),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/token/', TokenObtainPairView.as_view()),
    url(r'^api/token/refresh', TokenRefreshView.as_view()),
]
