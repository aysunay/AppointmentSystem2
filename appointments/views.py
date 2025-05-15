from django.shortcuts import render
from django.http import HttpResponse

def appointment_list(request):
    return HttpResponse("<h1>Randevu Listesi</h1><p>Burada randevular listelenecek.</p>")

def create_appointment(request):
    return HttpResponse("<h1>Yeni Randevu Oluştur</h1><p>Burada randevu ekleme formu olacak.</p>") 
def appointment_list(request):
    return HttpResponse("<h1>Randevu Listesi</h1><p>Burada randevular listelenecek.</p>")

def create_appointment(request):
    return HttpResponse("<h1>Yeni Randevu Oluştur</h1><p>Burada randevu ekleme formu olacak.</p>")
def home(request):
    return render(request, 'home.html')
