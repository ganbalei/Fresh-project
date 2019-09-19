from django.contrib import admin

# Register your models here.
from .models import UserFav, UserLeavingMessage, UserAddress

@admin.register(UserFav)
class UserFavAdmin(admin.ModelAdmin):
    list_display = ['user', 'goods', "add_time"]

@admin.register(UserLeavingMessage)
class UserLeavingMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message_type', "message", "add_time"]

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ["signer_name", "signer_mobile", "district", "address"]
