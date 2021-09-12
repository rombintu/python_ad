from django.contrib import admin
from .models import Host, Rule, Client, Group

admin.site.register(Host)
admin.site.register(Rule)
admin.site.register(Client)
admin.site.register(Group)

# class hostAdmin(admin.ModelAdmin):
#     list_display = ("name", "IP", "description", "type", "owner")

# class ruleAdmin(admin.ModelAdmin):
#     list_display = ("name", "IP", "description", "type", "owner")

# @admin.register(Client)
# class clientAdmin(admin.ModelAdmin):
#     list_display = ("login", "temp_password", "group", "type", "owner")

# class groupAdmin(admin.ModelAdmin):
#     list_display = ("name", "permissions")