from rest_framework import serializers
from .models import AddItems

class ItemSerializers(serializers.ModelSerializer):
	class Meta:
		model=AddItems
		fields=['Item_id','ItemName','Description','Quantity']
