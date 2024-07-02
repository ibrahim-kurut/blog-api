from rest_framework import serializers

from .models import Category, Post

# create category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id",)


# create post serializer

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id", "created_date", "updated_date",)

    # show category name in post 
    category_name = serializers.SerializerMethodField()
    def get_category_name(self, obj):
            return obj.category.name

