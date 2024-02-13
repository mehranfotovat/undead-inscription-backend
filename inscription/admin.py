from django.contrib import admin
from .models import WalletAddress, Inscription, NFT


admin.site.register(WalletAddress)
admin.site.register(Inscription)
admin.site.register(NFT)
