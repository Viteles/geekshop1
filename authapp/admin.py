from django.contrib import admin
from.models import ShopUser
from basketapp.models import Basket


class BasketInline(admin.TabularInline):
    model = Basket
    fields = 'product', 'quantity'
    extra = 1


@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    search_fields = 'username', 'category__name',
    list_filter = 'is_active',
    inlines = BasketInline,

