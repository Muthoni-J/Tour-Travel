from django.contrib import admin
from .models import Destination,Detailed_desc, agent_detail,customer_detail,Cards,NetBanking,Transactions
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

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ("amount","transaction_type","transaction_charge","transaction_cost","status")
    search_fields = ("amount","transaction_type",)
admin.site.register(Transactions,TransactionsAdmin)

# class CardSAdmin(admin.ModelAdmin):
#     list_display = ("signature","date_issued","card_status","CVV_security_code","account")
#     search_fields = ("signature","date_issued",)
# admin.site.register(Cards,CardSAdmin)

# class ThirdpartyAdmin(admin.ModelAdmin):
#     list_display = ("email","phone_number","is_active","currency","transaction_cost","account")
#     search_fields = ("email","phone_number",)
# admin.site.register(Thirdparty,ThirdpartyAdmin)

# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ("message","data_created","image","receipt","is_active")
#     search_fields = ("message","data_created",)
# admin.site.register(Notification,NotificationAdmin)




