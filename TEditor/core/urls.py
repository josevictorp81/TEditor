from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('text-list/', views.TextListView.as_view(), name='text-list'),
    path('text-list/create/', views.TextCreateView.as_view(), name='text-create'),
    path('text-list/detail/<int:pk>/', views.TextDetailView.as_view(), name='text-detail'),
    path('text-list/update/<int:pk>/', views.TextUpdateView.as_view(), name='text-update'),
    path('text-list/delete/<int:pk>/', views.TextDeleteView.as_view(), name='text-delete'),
    path('text-list/download/<int:pk>/', views.PDFDownload.as_view(), name='text-download'),
]