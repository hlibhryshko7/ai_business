import os
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lead

# Токены для Telegram
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def send_telegram_notification(lead):
    """Вспомогательная функция для отправки сообщения в Telegram"""
    text = (
        f"🤖 <b>Новая заявка (AI Business)</b>\n\n"
        f"<b>Имя:</b> {lead.name}\n"
        f"<b>Email:</b> {lead.email}\n"
        f"<b>Телефон:</b> {lead.phone}\n\n"
        f"<b>Задача:</b> {lead.message}"
    )
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    
    try:
        requests.post(url, data=payload, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка отправки в Telegram: {e}")

# --- КОНТРОЛЛЕРЫ СТРАНИЦ ---

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def reviews(request):
    return render(request, 'reviews.html')

def training(request):
    return render(request, 'training.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Сохраняем в БД
        new_lead = Lead.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        
        # Отправляем в ТГ, если токен изменен
        if TELEGRAM_BOT_TOKEN != 'ТВОЙ_ТОКЕН_ОТ_BOTFATHER':
            send_telegram_notification(new_lead)
            
        messages.success(request, 'Заявка успешно отправлена! Наш ИИ-ассистент скоро свяжется с вами.')
        return redirect('contact')
        
    return render(request, 'contact.html')