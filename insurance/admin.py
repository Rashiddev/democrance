from django.contrib import admin

from insurance.models import Customer, Policy


class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ('first_name', 'last_name', 'dob')
    fields = ('first_name', 'last_name', 'dob')
    can_delete = True


class PolicyAdmin(admin.ModelAdmin):
    model = Policy
    list_display = ('type', 'premium', 'cover', 'customer')
    fields = ('type', 'premium', 'cover', 'customer')
    can_delete = True


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Policy, PolicyAdmin)