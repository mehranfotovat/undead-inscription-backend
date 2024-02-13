from django.urls import path
from.views import AddressInscriptionApiView, NftInscriptionApiView

urlpatterns = [
    path('address/<str:wallet_address>/', AddressInscriptionApiView.as_view()),
    path('nfts/', NftInscriptionApiView.as_view()),
]