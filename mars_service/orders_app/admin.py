from django.contrib import admin
from .models import Device, Customer, DeviceInField, Order


class DeviceAdmin(admin.ModelAdmin):
    """Настройка отображения модели Device в админке"""
    list_display = ('id', 'manufacturer', 'model')
    list_filter = ('manufacturer',)  # фильтр по производителю
    search_fields = ('manufacturer', 'model')  # поиск


class CustomerAdmin(admin.ModelAdmin):
    """Настройка отображения модели Customer в админке"""
    list_display = ('id', 'customer_name', 'customer_city', 'customer_address')
    search_fields = ('customer_name',)  # поиск по названию
    list_filter = ('customer_city',)  # фильтр по городу


class DeviceInFieldAdmin(admin.ModelAdmin):
    """Настройка отображения модели DeviceInField в админке"""
    list_display = ('id', 'serial_number', 'customer', 'device', 'owner_status')
    list_filter = ('owner_status', 'device__manufacturer')  # фильтр по статусу и производителю
    search_fields = ('serial_number', 'customer__customer_name')  # поиск по серийнику и клиенту
    raw_id_fields = ('customer', 'device')  # удобный поиск при большом количестве записей


class OrderAdmin(admin.ModelAdmin):
    """Настройка отображения модели Order в админке"""
    list_display = ('id', 'device', 'customer', 'order_status',
                    'created_dt', 'last_updated_dt')
    list_filter = ('order_status', 'created_dt')  # фильтры
    search_fields = ('order_description', 'device__serial_number')  # поиск
    readonly_fields = ('created_dt', 'last_updated_dt')  # только для чтения
    date_hierarchy = 'created_dt'  # навигация по датам


# Регистрация моделей в админке
admin.site.register(Device, DeviceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DeviceInField, DeviceInFieldAdmin)
admin.site.register(Order, OrderAdmin)