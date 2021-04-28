from django.urls import path
from public_view import views
app_name ='public_view'
urlpatterns = [
    path('about-page', views.about, name='about'),
    path('detail-page/<int:team_id>/', views.team_detail, name='team_detail'),
    path('agent-page', views.agent, name='agent'),
    path('rent-page', views.rent, name='rent'),
    path('requests-page', views.request, name='request'),
    path('property-details/<slug:slug>/', views.property_details, name='property_details'),
    path('buy-page', views.buy, name='buy'),
    path('register-page', views.register, name='register'),
    path('login-page', views.login, name='login'),
]
