from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.models import User
from policies import views


def home(request):
    return HttpResponse("""
        <body style='font-family:sans-serif; text-align:center; padding-top:100px; background:#f0f2f5;'>
            <h1 style='color:#1a73e8; font-size: 3em;'>🛡️ 智能保單管理系統</h1>
            <p style='font-size: 1.2em; color: #555;'>您的專屬期末專案開發環境</p>
            <hr style='width: 50%; border: 1px solid #ddd; margin: 30px auto;'>
            <div style='margin: 20px;'>
                <a href='/admin' style='display:inline-block; padding:15px 30px; background:#1a73e8; color:white; text-decoration:none; border-radius:5px; font-weight:bold;'>進入後台管理資料</a>
            </div>
            <div style='margin-top:50px; color:#888;'>製作人：您的姓名</div>
        </body>
    """)

def setup_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', '密碼123')
        return HttpResponse("雲端管理員建立成功！帳號: admin / 密碼: 密碼123")
    return HttpResponse("帳號已經存在囉！")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),              
    path('setup/', setup_admin), 
    path('', views.policy_search, name='home'),
]
