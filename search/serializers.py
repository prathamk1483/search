from rest_framework import serializers
from .models import Mentors

class MentorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Mentors 
        fields ="__all__"  
        