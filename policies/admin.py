from django.contrib import admin
from .models import Policy
from django.template.defaultfilters import register

# 修正 Django 5.x 移除 length_is 的問題
@register.filter(name='length_is')
def length_is(value, arg):
    try:
        return len(value) == int(arg)
    except:
        return False

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    # 這是對應你的 models.py (image_53bfcc.png) 的正確欄位
    list_display = (
        'client_name', 
        'policy_id', 
        'policy_type', 
        'coverage_amount', 
        'status'
    )
    
    # 確保搜尋欄位也對齊模型名稱
    search_fields = ('client_name', 'policy_id')
    
    # 確保篩選器也對齊模型名稱
    list_filter = ('policy_type', 'status')
