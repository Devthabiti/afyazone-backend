from django.contrib import admin
from .models import ClientProfile,Transactions

# Register your models here.
admin.site.register(ClientProfile)
#admin.site.register(Transactions)


class TransactionAdmin(admin.ModelAdmin):
    # Specify which fields to display in the list view
    list_display = ('doctor', 'order_id','amount','status')
    
    # Add filters to the sidebar
    list_filter = ('status','doctor',)
    
    # Add search functionality
    search_fields = ('id','status',)
    
    # Optionally, you can specify the default ordering
    ordering = ('doctor',)  # Orders by `created_at` in descending order

# Register the model and the custom admin class
admin.site.register(Transactions, TransactionAdmin)