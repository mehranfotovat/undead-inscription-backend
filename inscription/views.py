from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WalletAddress, Inscription, NFT
from .serializers import WalletAddressSerializer, InscriptionSerializer, NFTSerializer
import json


class AddressInscriptionApiView(APIView):
    def get(self, request, wallet_address):
        wallet = WalletAddress.objects.filter(address=wallet_address)
        if wallet.exists():
            nfts = NFT.objects.filter(inscription__wallet=wallet[0])
            serializer = NFTSerializer(nfts, many=True)
            # this case doesnt happen unless you add a address manually.
            if len(serializer.data) == 0:
                return Response({'address': "no nfts!"})
            return Response({'address': serializer.data})
        return Response({'address': "no address!"})
    

class NftInscriptionApiView(APIView):
    def post(self, request):
        wallet_address = request.data.get('wallet_address')
        nft_addresses = json.loads(request.data.get('nft_addresses', []))
        print(wallet_address)
        print(nft_addresses)
        wallet = WalletAddress.objects.filter(address=wallet_address)
        if wallet.exists():
            inscription = Inscription.objects.create(wallet=wallet[0])
            for nft_address in nft_addresses:
                try:
                    NFT.objects.create(nft_address=nft_address, inscription=inscription)
                    print(f"created {nft_address}")
                except:
                    print(f"already exist: {nft_address}")
            return Response({'address': inscription})
        else:
            for nft_address in nft_addresses:
                nft = NFT.objects.filter(nft_address=nft_address)
                if nft.exists():
                    return Response({'Err': "An NFT already exist in DB!"})
            wallet = WalletAddress.objects.create(address=wallet_address)
            inscription = Inscription.objects.create(wallet=wallet)
            for nft_address in nft_addresses:
                try:
                    NFT.objects.create(nft_address=nft_address, inscription=inscription)
                    print(f"created {nft_address}")
                except:
                    print(f"already exist: {nft_address}")
            inscription = InscriptionSerializer(inscription).data
            return Response({'address': inscription})
