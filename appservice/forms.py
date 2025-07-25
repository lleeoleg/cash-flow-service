from django import forms
from .models import CashFlow, Status, Type, Category, SubCategory


class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select', 'id': 'id_type'}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'id_category'}),
            'subcategory': forms.Select(attrs={'class': 'form-select', 'id': 'id_subcategory'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is None:
            raise forms.ValidationError("Сумма обязательна для заполнения.")
        if amount <= 0:
            raise forms.ValidationError("Сумма должна быть больше нуля.")
        return amount

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('type'):
            self.add_error('type', "Тип обязателен.")
        if not cleaned_data.get('category'):
            self.add_error('category', "Категория обязательна.")
        if not cleaned_data.get('subcategory'):
            self.add_error('subcategory', "Подкатегория обязательна.")

# Основные формы
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']





# Форма для управления и редактирования статусов
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название статуса'
            }),
        }
        labels = {
            'name': 'Название статуса',
        }

# Форма для управления и редактирования типов
class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название типа'
            }),
        }
        labels = {
            'name': 'Название типа',
        }

# Форма для управления и редактирования категорий
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['type', 'name']
        widgets = {
            'type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название категории'
            }),
        }
        labels = {
            'type': 'Тип',
            'name': 'Название категории',
        }
        
# Форма для управления и редактирования подкатегорий
class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'name']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название подкатегории'
            }),
        }
        labels = {
            'category': 'Категория',
            'name': 'Название подкатегории',
        }