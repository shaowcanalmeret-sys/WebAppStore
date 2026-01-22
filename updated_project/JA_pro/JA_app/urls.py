from django.urls import path
from . import views

urlpatterns = [


path('', views.page, name="home"),

path('add_to_cart/<int:offer_id>/', views.add_to_cart, name='add_to_cart'),

path('about/', views.about, name="about"),

path('offers/', views.offers, name="offers"),

path('add_offer/', views.add_offer, name="add_offer"),

path('edit_offer/<int:of_id>/', views.edit_offer, name='edit_offer'),

path('delete_offer/<int:of_id>/', views.delete_offer, name='delete_offer'),

path('products/', views.products, name='products'),

path('add_product/', views.add_products, name="add_product"),

path('edit_product/<int:prod_id>/', views.edit_product, name="edit_product"),

path('delete_product/<int:prod_id>/', views.delete_product, name="delete_product"),

path('category/', views.category, name="category"),

path('add_category/', views.add_category, name="add_category"),

path('edit_category/<int:cate_id>/', views.edit_category, name="edit_category"),

path('delete_category/<int:cate_id>/', views.delete_category, name='delete_category'),

path('contact/', views.contact, name="contact"),

path('signUp/', views.signUp, name="signUp"),

path('login/', views.loginUser, name="login"),

path('logout/', views.logoutUser, name="logout")


]
