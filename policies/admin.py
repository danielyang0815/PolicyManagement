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
    # 這裡只放 Django 預設一定有的欄位來測試，確保不會噴 E108 錯誤
    # 如果你之後在 models.py 定義了新的欄位，再回來這裡加
    list_display = ('id', '__str__') 
    
    # 暫時註解掉搜尋與篩選，等網站變綠燈再加
    # search_fields = ('id',)
