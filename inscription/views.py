from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WalletAddress, Inscription, NFT
from .serializers import WalletAddressSerializer, InscriptionSerializer, NFTSerializer


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
        nft_addresses = request.data.get('nft_addresses', [])
        print(wallet_address)
        print(nft_addresses)
        # print(wallet_address)
        # wallet = WalletAddress.objects.filter(address=wallet_address)
        # if wallet.exists():
        #     # print(nft_addresses)
        #     pass
        # else:
        return Response({'address': "no address!"})