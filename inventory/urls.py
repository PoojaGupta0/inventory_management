from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('inventory/', TemplateView.as_view(template_name="inventory/inventory.html"), name='inventory'),
    path('inventory/<int:pk>', views.InventoryDetailView.as_view(), name='inventory_detail'),
]
