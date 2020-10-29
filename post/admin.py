from django.contrib import admin
from .models import Post,SiteSetting,Kategori,reports,bilgilendirme,Comment
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display = ("id","title","content","publising_date")
    list_display_links = ("id","title","content")

class kategoriAdmin(admin.ModelAdmin):
    list_display = ("id","kategoriad")
    list_display_links = ("id","kategoriad")

class settingAdmin(admin.ModelAdmin):
    list_display = ("id","SiteTitle")
    list_display_links=("id","SiteTitle")

class reportsAdmin(admin.ModelAdmin):
    list_display = ("name","title")
    list_display_links = ("name","title")

class bilgilendirmeAdmin(admin.ModelAdmin):
    list_display = ("id","yazi")
    list_display_links = ("yazi",)

class commentAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_display_links = ("id","name")

admin.site.register(SiteSetting,settingAdmin)
admin.site.register(Post,postAdmin)
admin.site.register(Kategori,kategoriAdmin)
admin.site.register(reports,reportsAdmin)
admin.site.register(bilgilendirme,bilgilendirmeAdmin)
admin.site.register(Comment,commentAdmin)