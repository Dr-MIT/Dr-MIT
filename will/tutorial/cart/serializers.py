from rest_framework import serializers

from.models import Cart

class CartSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('item', 'title')

