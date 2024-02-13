from rest_framework import serializers
from .models import WalletAddress, Inscription, NFT


class WalletAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletAddress
        fields = '__all__'


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'


class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = '__all__'