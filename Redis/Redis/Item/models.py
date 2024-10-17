from django.db import models


# Create your models here.
class AddItems(models.Model):
	Item_id=models.AutoField(primary_key=True)
	ItemName=models.CharField(max_length=255, unique=True)
	Description=models.TextField()
	Quantity=models.IntegerField()