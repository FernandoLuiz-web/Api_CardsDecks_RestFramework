from rest_framework import viewsets, serializers, response
from .models import Deck
from apps.cards.views import CardSerializer
from apps.cards.models import Card


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'


class DecksViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()


class DeckCardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    def list(self, request, decks_pk):
        cards = Card.objects.filter(deck=decks_pk)
        serializer = self.get_serializer(cards, many=True)
        return response.Response(serializer.data)