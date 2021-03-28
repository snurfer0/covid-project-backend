from django.contrib import admin

# Register your models here.
from .models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = Test


admin.site.register(Test, TestAdmin)
