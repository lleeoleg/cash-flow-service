from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import *
from .forms import CashFlowForm, StatusForm, TypeForm, CategoryForm, SubCategoryForm
from django.http import JsonResponse
from django import forms

# Основные представления для денежных операций

class CashFlowListView(ListView):
    model = CashFlow
    template_name = 'cashflow/index.html'
    context_object_name = 'records'

    def get_queryset(self):
        queryset = CashFlow.objects.select_related('status', 'type', 'category', 'subcategory')
        status = self.request.GET.get('status')
        type_ = self.request.GET.get('type')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        if status:
            queryset = queryset.filter(status__id=status)
        if type_:
            queryset = queryset.filter(type__id=type_)
        if category:
            queryset = queryset.filter(category__id=category)
        if subcategory:
            queryset = queryset.filter(subcategory__id=subcategory)
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context


class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cashflow/form.html'
    success_url = reverse_lazy('cashflow:index')

class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cashflow/form.html'
    success_url = reverse_lazy('cashflow:index')

class CashFlowDeleteView(DeleteView):
    model = CashFlow
    template_name = 'cashflow/confirm_delete.html'
    success_url = reverse_lazy('cashflow:index')
    

# AJAX-запросы для загрузки категорий и подкатегорий
    
    
def ajax_load_categories(request):
    type_id = request.GET.get('type')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def ajax_load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

    
    
# Панель управления

class ManagePanelView(TemplateView):
    template_name = 'manage/manage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context

# Панель управления для статусов

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'manage/create_status.html'
    success_url = reverse_lazy('cashflow:manage_panel')

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'manage/update_status.html'
    success_url = reverse_lazy('cashflow:manage_panel')

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'manage/confirm_delete_status.html'
    success_url = reverse_lazy('cashflow:manage_panel')
    
    
# Панель управления для типов


class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'manage/create_type.html'
    success_url = reverse_lazy('cashflow:manage_panel')

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'manage/update_type.html'
    success_url = reverse_lazy('cashflow:manage_panel')

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'manage/confirm_delete_type.html'
    success_url = reverse_lazy('cashflow:manage_panel')
    
# Панель управления для категорий
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'manage/create_category.html'
    success_url = reverse_lazy('cashflow:manage_panel')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'manage/update_category.html'
    success_url = reverse_lazy('cashflow:manage_panel')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'manage/confirm_delete_category.html'
    success_url = reverse_lazy('cashflow:manage_panel')
    
    
# Панель управления для подкатегорий
class SubCategoryCreateView(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'manage/create_subcategory.html'
    success_url = reverse_lazy('cashflow:manage_panel')

class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'manage/update_subcategory.html'
    success_url = reverse_lazy('cashflow:manage_panel')

class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = 'manage/confirm_delete_subcategory.html'
    success_url = reverse_lazy('cashflow:manage_panel')