from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('detail/<int:chemistry_id>', views.detail, name='detail'),
    path('edit/<int:chemistry_id>', views.edit_form, name='edit'),
    path('editsave', views.edit_save, name='editsave'),
    path('delete/<int:chemistry_id>', views.delete, name='delete'),
]