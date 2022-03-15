from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from .models import Commands, CustomersContact, Categories, Product
# Register your models here.





#admin.site.register(Commands)
admin.site.register(Categories)

class AdminUrlMixin(object):

    def get_admin_url(self, obj):

        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse("admin:store_%s_change" % (
            content_type.model),
            args=(obj.id,))



class BookingInline(admin.TabularInline):

    model = Commands
    readonly_fields = ['created_at', 'customers', 'product', 'contacted']
    fieldsets = [
        (None, {'fields': ['contacted', 'product']})
    ]
    extra = 0
    verbose_name = 'Réservation'
    verbose_name_plural = 'Réservations'

    def has_add_permission(self, request):
        # Fonction permettant de restraindre la possibilité
        # a l'utilisateur de pas ajouter les reservation.
        return False

@admin.register(CustomersContact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline, ]

    search_fields = ['name']

    def has_add_permission(self, request):
        return False


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass




@admin.register(Commands)
class BookingAdmin(admin.ModelAdmin, AdminUrlMixin):
    readonly_fields = ['created_at', 'customers', 'product_link', 'contacted']
    list_filter = ['created_at', 'contacted']

    def has_add_permission(self, request):
        # Fonction permettant de restraindre la possibilité
        # a l'utilisateur de pas ajouter les reservation.

        return False

    def product_link(self, booking):
        url = self.get_admin_url(booking.product)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.product.name))