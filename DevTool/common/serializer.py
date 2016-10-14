from django.core.serializers.json import Serializer

class ResultSerializer(Serializer):
    def get_dump_object(self, obj):
        data = self._current
        return data
