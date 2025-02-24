from django.db import models


class Payment(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    order = models.OneToOneField("orders.Order", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=[("pending", "Pending"), ("completed", "Completed")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
