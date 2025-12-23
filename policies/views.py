from django.shortcuts import render
from .models import Policy
from django.contrib.auth.decorators import login_required

@login_required
def policy_search(request):
    # 取得使用者輸入的關鍵字
    query = request.GET.get('q', '')
    
    # 複雜邏輯處理：如果有人搜尋，就過濾資料；否則顯示全部
    if query:
        # 搜尋客戶姓名或保單編號
        results = Policy.objects.filter(client_name__icontains=query) | \
                  Policy.objects.filter(policy_id__icontains=query)
    else:
        results = Policy.objects.all()
        
    return render(request, 'policies/index.html', {
        'policies': results,
        'query': query
    })
