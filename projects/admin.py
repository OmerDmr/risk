from django.contrib import admin
from .models import Deprem,Sel,ResponsePlan,ResponseCat



class depremAdmin(admin.ModelAdmin):

    list_display = ['id','projectName','crtDate']
    list_display_links = ['projectName']
    list_filter = ['crtDate']
    search_fields = ['projectName','summary']

    class Meta:
        model = Deprem

class selAdmin(admin.ModelAdmin):

    list_display = ['id','projectName','crtDate']
    list_display_links = ['projectName']
    list_filter = ['crtDate']
    search_fields = ['projectName','summary']

    class Meta:
        model = Sel

class responseAdmin(admin.ModelAdmin):

    list_display = ['reaction']
    list_display_links = ['reaction']
    search_fields = ['reaction']

    class Meta:
        model = ResponsePlan


class responseCatAdmin(admin.ModelAdmin):

    list_display = ['catId']
    list_display_links = ['catId']
    search_fields = ['catId']

    class Meta:
        model = ResponseCat


admin.site.register(Deprem,depremAdmin)
admin.site.register(Sel,selAdmin)
admin.site.register(ResponsePlan,responseAdmin)
admin.site.register(ResponseCat,responseCatAdmin)