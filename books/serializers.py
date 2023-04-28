from rest_framework import serializers
from .models import Book
# Serializers define the API representation.


class BookSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'category',
                  'view_count', 'download_count', 'date_created', 'date_updated', 'status', 'picture', 'filename']
