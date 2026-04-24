from django.db import models

class Lead(models.Model):
    # Варианты статусов для удобного управления заявками
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
    )

    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='new', 
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']  # Новые заявки всегда будут сверху

    def __str__(self):
        return f"{self.name} - {self.email}"