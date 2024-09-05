from rest_framework import serializers

from workout_app.blog.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('title', 'intro', 'text')
