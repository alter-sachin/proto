from django.db import models

# Create your models here.

class Accounts(models.Model):
    PublicKey = models.TextField(primary_key=True)
    UserName = models.CharField(max_length=200)
    Balance = models.IntegerField()
    AccountState = models.IntegerField()
    NetworkType = models.IntegerField()
    AccountType = models.IntegerField()
    LastTransactionTime = models.IntegerField()

    class Meta:
        db_table = u'Ledger'