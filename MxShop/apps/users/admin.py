from django.contrib import admin

# Register your models here.
from .models import VerifyCode, UserProfile

@admin.register(UserProfile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', "gender", "email", "birthday"]

@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'mobile', "add_time"]

admin.site.site_header = '慕学生鲜后台'
admin.site.site_title = '慕学生鲜后台'
#admin.site.index_title = '慕学生鲜后台'