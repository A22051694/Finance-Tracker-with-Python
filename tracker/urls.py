from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracker/', views.tracker_view, name='tracker'),
    path('export/', views.export_csv, name='export_csv'),
    path('import/', views.import_csv, name='import_csv'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),


]
