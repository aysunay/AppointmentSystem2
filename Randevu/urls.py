from django.contrib import admin
from django.urls import path
from Randevu.views import home  # ✅ Giriş sayfası için fonksiyonu içe aktardık

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # 🎯 Ana sayfa burada tanımlandı
]