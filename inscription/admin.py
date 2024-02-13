from django.contrib import admin
from .models import WalletAddress, Inscription, NFT


admin.site.register(WalletAddress)

class NFTInline(admin.TabularInline):  # Using TabularInline for a tabular layout
    model = NFT
    can_delete = False  # Prevents deletion of NFT entries
    readonly_fields = ('nft_address',)  # Makes the fields read-only. Add more fields as needed.
    extra = 0  # No extra blank forms

    def has_add_permission(self, request, obj=None):
        # Prevents adding new NFTs from the Inscription admin page
        return False

class InscriptionAdmin(admin.ModelAdmin):
    inlines = [NFTInline]

admin.site.register(Inscription, InscriptionAdmin) 
admin.site.register(NFT)
