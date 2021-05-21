from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('text-list/', views.TextListView.as_view(), name='text-list'),
    path('text-create/', views.TextCreateView.as_view(), name='text-create'),
    path('text-detail/<int:pk>/', views.TextDetailView.as_view(), name='text-detail'),
    path('text-update/<int:pk>/', views.TextUpdateView.as_view(), name='text-update'),
    path('text-delete/<int:pk>/', views.TextDeleteView.as_view(), name='text-delete'),
    path('text-download/<int:pk>/', views.PDFDownload.as_view(), name='text-download'),
]