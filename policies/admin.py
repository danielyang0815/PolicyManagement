from django.contrib import admin
from .models import Policy

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    # 1. 列表頁面要顯示哪些欄位
    list_display = ('customer_name', 'policy_number', 'insurance_type', 'insurance_amount', 'start_date')
    
    # 2. 加入搜尋框 (可以搜尋姓名或保單編號)
    search_fields = ('customer_name', 'policy_number')
    
    # 3. 加入右側篩選欄 (依保險種類或狀態篩選)
    list_filter = ('insurance_type', 'status')
