"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from honeypeartea import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('courses.html', views.courses, name='courses'),
    path('requirement.html', views.requirement, name='requirement'),
    path('pricing.html', views.pricing, name='pricing'),
    path('contact.html', views.contact, name='contact'),

    path('prediction.html', views.school_predict.as_view(), name='prediction'),
    path('chance.html', views.admission_chance.as_view(), name='chance'),
    path('history.html', views.history_admission.as_view(), name='history'),

    path('cma.html', views.cma_form.as_view(), name='cma'),
    path('nga.html', views.nga, name='nga'),
    path('louvre.html', views.louvre, name='louvre'),
    path('rijksmuseum.html', views.rijksmuseum, name='rijksmuseum'),
    path('random.html', views.random, name='random'),

]
