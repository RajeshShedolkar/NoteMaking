from rest_framework import serializers

from app.models import Task
from api.models import Test
from app.models import NoteMaking
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('test_id', 'note')

class NoteMakingSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteMaking
        field = ('notes_id', 'note')
