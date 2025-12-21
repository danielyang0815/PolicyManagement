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
    # 列表顯示欄位
    list_display = ('customer_name', 'policy_number', 'insurance_type', 'insurance_amount', 'status')
    # 加入搜尋框
    search_fields = ('customer_name', 'policy_number')
    # 加入右側篩選器
    list_filter = ('insurance_type', 'status')
