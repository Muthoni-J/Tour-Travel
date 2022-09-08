from django.contrib import admin
from .models import Destination,Detailed_desc, agent_detail,customer_detail,Cards,NetBanking
# Register your models here.

class DestinationAdmin(admin.ModelAdmin):
    list_display = ("id","country","number")
    search_fields = ("id","country",) 
admin.site.register(Destination,DestinationAdmin)

class Detailed_descAdmin(admin.ModelAdmin):
    list_display = ("country","price",)
    search_fields = ("country","price",) 
admin.site.register(Detailed_desc,Detailed_descAdmin)

class Customer_detailAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","age","username",)
    search_fields = ("first_name","last_name",) 
admin.site.register(customer_detail,Customer_detailAdmin)

class Agent_detailAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","username",)
    search_fields = ("first_name","last_name",) 
admin.site.register(agent_detail,Agent_detailAdmin)

# class TransactionsAdmin(admin.ModelAdmin):
#     list_display = ("amount","transaction_type","transaction_charge","transaction_cost","status")
#     search_fields = ("amount","transaction_type",)
# admin.site.register(Transactions,TransactionsAdmin)

class CardsAdmin(admin.ModelAdmin):
    list_display = ("Card_number","email","Ex_Year","CVV","Ex_Year")
    search_fields = ("Card_number","email",)
admin.site.register(Cards,CardsAdmin)

class NetBankingAdmin(admin.ModelAdmin):
    list_display = ("Username","Password")
    search_fields = ("Username","Password",)
admin.site.register(NetBanking,NetBankingAdmin)







