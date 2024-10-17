from rest_framework.views import APIView
from .serializers import ItemSerializers
from rest_framework.permissions import IsAuthenticated
from .models import AddItems
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class Item(APIView):
	permission_classes = [IsAuthenticated]
	def post(self, request):
		try:
			serializer=ItemSerializers(data=request.data)
			serializer.is_valid(raise_exception=True)
			serializer.save()
			return Response(serializer.data)
		except:
			return Response("Data is already present",status=status.HTTP_400_DATA_EXISTS)
	def get(self,request):
		try:
			item=request.query_params.get('Item_id')
			Items=AddItems.objects.get(Item_id=item)
			serializer=ItemSerializers(Items)
			return Response(serializer.data)
		except:
			return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
	def put(self, request):
		try:			
			item=request.query_params.get('Item_id')
			Items=AddItems.objects.get(Item_id=item)
			serializer=ItemSerializers(Items,data=request.data)
			serializer.is_valid(raise_exception=True)
			serializer.save()
			return Response(serializer.data)
		except:
			return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
	def delete(self, request):
		try:
			item=request.query_params.get('Item_id')
			Items=AddItems.objects.get(Item_id=item)
			Items.delete()
			return Response("Data deleted")
		except:
			return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
