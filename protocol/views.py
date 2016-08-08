from django.shortcuts import render

# Create your views here.
import json
from models import *
from django.http import HttpResponse
def sachin(request):
    #user = request.GET["user"]
    temp = Accounts.objects.filter(UserName=user)
    data=[]
    for i in temp:
        temp_dict={}
        #import pdb; pdb.set_trace()
        temp_dict["PublicKey"] = unicode(str(i.PublicKey), errors='ignore')
        temp_dict["balance"] = i.Balance
        temp_dict["UserName"] = i.UserName
        temp_dict["AccountState"] = i.AccountState
        temp_dict["NetworkType"] = i.NetworkType
        temp_dict["Last_time"] = i.LastTransactionTime
        temp_dict["account_type"] = i.AccountType
        data.append(temp_dict)

    return HttpResponse(json.dumps(data))