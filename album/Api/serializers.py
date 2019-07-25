from rest_framework import serializers
from album.models import Contact


class ContactSerializer(serializers.ModelSerializer):

	class Meta:
		model=Contact
		fields=['pk','first_name','last_name','location','photo','created']