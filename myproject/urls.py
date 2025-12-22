from django.contrib import admin
from django.urls import path
from policies import views  # 保留這行，這是連結 policies/views.py 的橋樑

urlpatterns = [
    # 1. 管理後台 (Jazzmin 介面)
    path('admin/', admin.site.urls),
    
    # 2. 你的手寫前端首頁 (這就是老師要看的 90 分成果！)
    # 它會執行 views.py 裡的 policy_search，並套用 index.html 模板
    path('', views.policy_search, name='home'),
]
