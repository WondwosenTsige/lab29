from django.urls import path
from .views import AppxListView, AppxDetailView, AppxCreateView, AppxUpdateView, AppxDeleteView

urlpatterns = [
    path('', AppxListView.as_view(), name='appx_list'),
    path('<int:pk>/', AppxDetailView.as_view(), name='appx_detail'),
    path('create/', AppxCreateView.as_view(), name='appx_create'),
    path('<int:pk>/update/', AppxUpdateView.as_view(), name='appx_update'),
    path('<int:pk>/delete/', AppxDeleteView.as_view(), name='appx_delete'),
]