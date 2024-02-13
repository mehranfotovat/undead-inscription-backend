from django.db import models

from django.db import models

class WalletAddress(models.Model):
    address = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.address

class Inscription(models.Model):
    wallet = models.ForeignKey(WalletAddress, on_delete=models.CASCADE, related_name='inscriptions')

    def __str__(self):
        return f'Inscription {self.pk} for {self.wallet.address}'

class NFT(models.Model):
    nft_address = models.CharField(max_length=255, unique=True)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE, related_name='nfts')

    def __str__(self):
        return self.nft_address
