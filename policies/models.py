from django.db import models

class Policy(models.Model):
    # 對應期中提案的保單欄位
    client_name = models.CharField(max_length=100, verbose_name="客戶姓名")
    policy_id = models.CharField(max_length=50, unique=True, verbose_name="保單編號")
    policy_type = models.CharField(max_length=100, verbose_name="保險種類")
    coverage_amount = models.IntegerField(verbose_name="保險金額")
    start_date = models.DateField(verbose_name="投保日期")
    expiry_date = models.DateField(verbose_name="到期日期")
    premium = models.IntegerField(verbose_name="保費")
    status = models.CharField(max_length=20, default="有效", verbose_name="狀態")

    def __str__(self):
        return f"{self.client_name} - {self.policy_id}"