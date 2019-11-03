from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('services', views.ServicestsView.as_view(), name='services'),
    path('products', views.ProductsView.as_view(), name='products'),
    path('cake/<int:pk>', views.CakeDetailView.as_view(), name='cake'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
