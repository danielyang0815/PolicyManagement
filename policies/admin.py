from django.contrib import admin
from .models import Policy
from django.template.defaultfilters import register

# 修正 Django 5.x 移除 length_is 的相容性補丁
@register.filter(name='length_is')
def length_is(value, arg):
    try:
        return len(value) == int(arg)
    except:
        return False

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    # 對齊 models.py 的欄位名稱
    list_display = (
        'client_name', 
        'policy_id', 
        'policy_type', 
        'coverage_amount', 
        'start_date', 
        'status'
    )
    
    # 加入搜尋功能 (搜尋客戶姓名或保單編號)
    search_fields = ('client_name', 'policy_id')
    
    # 加入右側篩選器 (依保險種類或狀態篩選)
    list_filter = ('policy_type', 'status')
