from django.urls import path
from main_page.views import index, cars_list, car_single, about, service, contact, pricing

app_name = 'main_page'



urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('pricing/', pricing, name='pricing'),
    path('cars/', cars_list, name='cars_list'),
    path('cars/<int:id>/', car_single, name='car_single'),
    ]