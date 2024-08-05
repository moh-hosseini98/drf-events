from rest_framework import serializers
from .models import Event




class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source="organizer.email")
    users = serializers.StringRelatedField(many=True)
    class Meta:
        model = Event
        fields = (
            'id','organizer','title','description','users',
            'date','location','created_at','updated_at'
        )
        extra_kwargs = {
            "organizer": {"read_only":True},
            "users": {"read_only":True},
        }

    
