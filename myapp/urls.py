from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.index, name='index'),
   path('about-us', views.about, name='about'),
   path('products', views.products, name='products'),
   path('services', views.services, name='services'),
   path('product/<str:slug>', views.product_details, name='product_detail'),
   path('service/<str:slug>', views.service_details, name='service_detail'),
   path('message', views.message, name='message'),
   path('blogs', views.blogs, name='blogs'),
   path('blog/<str:slug>', views.blog_details, name='blog_details'),
   path('jobs', views.jobs, name='jobs'),
   path('careers/<str:id>/', views.careers, name='career'),
   path('contact', views.contact, name='contact'),
   path('portfolio', views.portfolio, name='projects'),
   path('subscribe', views.subscribe, name='subscribe'),
   path('jobs', views.jobs, name='jobs'),
   path('careers', views.careers, name='careers'),
   path('faqs', views.faqs, name='faqs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
