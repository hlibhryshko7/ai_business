from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    # Колонки, которые будут видны в общем списке
    list_display = ('name', 'email', 'phone', 'status', 'created_at')
    
    # Боковая панель для фильтрации
    list_filter = ('status', 'created_at')
    
    # Поля, по которым будет работать строка поиска
    search_fields = ('name', 'email', 'phone', 'message')
    
    # Позволяет менеджеру менять статус заявки прямо в списке, не заходя внутрь
    list_editable = ('status',) 
    
    # Защита от редактирования даты создания
    readonly_fields = ('created_at',)