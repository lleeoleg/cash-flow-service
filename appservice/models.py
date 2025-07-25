from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
    
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name

class CashFlow(models.Model):
    # Добавил функционал для поддерживания валидации данных
    created_at = models.DateField(auto_now_add=True)
    date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    comment = models.TextField(blank=True, null=True)
    

    class Meta:
        verbose_name = "Денежная операция"
        verbose_name_plural = "Денежные операции"

    def __str__(self):
        return f"{self.type.name} - {self.amount} on {self.date}"
