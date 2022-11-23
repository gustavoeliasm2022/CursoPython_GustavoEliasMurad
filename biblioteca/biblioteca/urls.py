"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core.views import *

urlpatterns = (
    path('admin/', admin.site.urls),
    path('author/', AuthorView.as_view(), name='author'),
    path('author/<int:author_id>', AuthorView.as_view(), name='author'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:category_id>', CategoryView.as_view(), name='category'),
    path('book/', BookView.as_view(), name='book'),
    path('book/<int:book_id>', BookView.as_view(), name='book'),
    path('partner/', PartnerView.as_view(), name='partner'),
    path('partner/<int:partner_id>', PartnerView.as_view(), name='partner'),
    path('bookloan/', BookLoanView.as_view(), name='bookloan'),
    path('bookloan/<int:bookloan_id>', BookLoanView.as_view(), name='bookloan'),
    path('buscarautororm/', AuthorViewWithOrm.as_view(), name='author'),
    path('buscarcategoriaorm/', CatogoryViewWithOrm.as_view(), name='category'),
    path('buscarlibroorm/', BookViewWithOrm.as_view(), name='book'),
    path('buscarsocioorm/', PartnerViewWithOrm.as_view(), name='socio'),
    path('buscarprestamosorm/', BookLoanViewWithOrm.as_view(), name='status'),
    path('buscarprestamosxdniorm/', BookLoanViewDniSocioWithOrm.as_view(), name='partner'),
)
