from django.contrib import admin
from .models import Policy
from django.template.defaultfilters import register

# 修正 Django 5.2 移除 length_is 的相容性問題
@register.filter(name='length_is')
def length_is(value, arg):
    try:
        return len(value) == int(arg)
    except:
        return False

# 最簡化版設定，只顯示 ID，確保絕對不會報錯
@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')
