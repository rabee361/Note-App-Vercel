from rest_framework.serializers import ModelSerializer , SerializerMethodField
from base.models import *
 
class NoteSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Note
        fields = '__all__'

    def get_user(self,obj):
        return obj.user.username
