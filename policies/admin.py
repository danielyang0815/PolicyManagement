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
    # 這是對齊 image_53bfcc.png 中定義的正確欄位名稱
    list_display = (
        'client_name',      # 不是 customer_name
        'policy_id',        # 不是 policy_number
        'policy_type',      # 不是 insurance_type
        'coverage_amount',   # 不是 insurance_amount
        'start_date', 
        'status'
    )
    
    # 加入搜尋功能 (依據 client_name 或 policy_id)
    search_fields = ('client_name', 'policy_id')
    
    # 加入右側篩選器
    list_filter = ('policy_type', 'status')
