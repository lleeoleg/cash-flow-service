from django.urls import path
from .views import *

app_name = 'cashflow'

urlpatterns = [
    # Основные URL для денежных операций и их CRUD
    path('', CashFlowListView.as_view(), name='index'),
    path('create/', CashFlowCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CashFlowUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', CashFlowDeleteView.as_view(), name='delete'),
    path('ajax/load-categories/', ajax_load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', ajax_load_subcategories, name='ajax_load_subcategories'),
    
    # Панель управления
    path('manage/', ManagePanelView.as_view(), name='manage_panel'),
    
    # CRUD для статусов
    path('manage/status/create/', StatusCreateView.as_view(), name='status_create'),
    path('manage/status/update/<int:pk>/', StatusUpdateView.as_view(), name='status_update'),
    path('manage/status/delete/<int:pk>/', StatusDeleteView.as_view(), name='status_delete'),


    # CRUD для типов
    path('manage/type/create/', TypeCreateView.as_view(), name='create_type'),
    path('manage/type/update/<int:pk>/', TypeUpdateView.as_view(), name='update_type'),
    path('manage/type/delete/<int:pk>/', TypeDeleteView.as_view(), name='delete_type'),
    
    #CRUD для категорий
    path('manage/category/create/', CategoryCreateView.as_view(), name='create_category'),
    path('manage/category/update/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('manage/category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    
    
    #CRUD для подкатегорий
    path('manage/subcategory/create/', SubCategoryCreateView.as_view(), name='create_subcategory'),
    path('manage/subcategory/update/<int:pk>/', SubCategoryUpdateView.as_view(), name='update_subcategory'),
    path('manage/subcategory/delete/<int:pk>/', SubCategoryDeleteView.as_view(), name='delete_subcategory'),
]
