from rest_framework_simplejwt.token_blacklist import models, admin


class CustomOutstandingTokenAdmin(admin.OutstandingTokenAdmin):
    
    def has_delete_permission(self, *args, **kwargs):
        return True # or whatever logic you want

from django.contrib import admin
from accounts.models import ModuleAccess, TempStorage, User, ActivationOtp, StoreBankDetail, StoreProfile
from django.contrib.auth.models import Permission

# Register your models here.

class BankDetailAdmin(admin.StackedInline):
    model = StoreBankDetail

@admin.register(StoreProfile)
class StoreProfileAdmin(admin.ModelAdmin):
    inlines = [BankDetailAdmin,]
    
    
class StoreLinkInline(admin.StackedInline):
    model = StoreProfile
    show_change_link = True
    
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "role", "is_active", "is_admin"]
    list_editable = ["role", "is_active", "is_admin"]
    inlines = [ StoreLinkInline]
    
    
admin.site.register(ActivationOtp)
admin.site.unregister(models.OutstandingToken)
admin.site.register(models.OutstandingToken, CustomOutstandingTokenAdmin)
admin.site.register([ StoreBankDetail])
admin.site.register([Permission, ModuleAccess,TempStorage])