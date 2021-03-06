from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('text-list/', views.TextListView.as_view(), name='text-list'),
    path('text-list/create/', views.text_create, name='text-create'),
    path('text-list/<int:pk>/', views.TextDetailView.as_view(), name='text-detail'),
    path('text-list/<int:pk>/update/', views.TextUpdateView.as_view(), name='text-update'),
    path('text-list/<int:pk>/delete/', views.TextDeleteView.as_view(), name='text-delete'),
    path('text-list/<int:pk>/download/', views.PDFDownload.as_view(), name='text-download'),
]