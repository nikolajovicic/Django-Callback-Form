from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter

from .models import SupportRequest

class ArchivedFilter(SimpleListFilter):
    title = _('Archived')

    parameter_name = 'archived'

    def lookups(self, request, model_admin):
        return (
            (None, _('No')),
            ('yes', _('Yes')),
            ('all', _('All')),
        )

    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value == 'yes':
            return queryset.filter(archived=True)
        elif self.value == 'no':
            return queryset.filter(archived=False)
        elif self.value == 'all':
            return queryset.filter(archived__in=[True,False])
        elif self.value() == None:
            return queryset.filter(archived=False)

class SupportRequestAdmin(admin.ModelAdmin):
    fields = ('subject','sender_name','email','phone_number','problem_description','company_name','callback_date_time','comment','archived')
    list_display = ['pub_date','sender_name','subject','callback_date_time']
    #list_editable = ['sender_name','subject','callback_date_time']
    sortable_by = ['pub_date','sender_name','subject','callback_date_time']
    list_filter = [ArchivedFilter]
    readonly_fields = ['subject','sender_name','email','phone_number','company_name','callback_date_time','pub_date','callback_date','callback_time','problem_description']
    

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(SupportRequest, SupportRequestAdmin)