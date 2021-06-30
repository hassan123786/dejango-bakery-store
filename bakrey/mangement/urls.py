from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products, name="products"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name="blog"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('terms/', views.terms, name="terms"),
    path('product-details/', views.productdetails, name="product-details"),
    path('blog-details/', views.blogdetails, name="blog-details"),
    path('login/', views.logins, name="login"),
    path('signup/', views.signup, name="signup"),
]