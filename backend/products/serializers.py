from rest_framework import serializers
from .models import Category, Comment, Product


# class CategorySerializer(serializers.Serializer):
#     slug = serializers.SlugField(allow_unicode=True)
#     name = serializers.CharField(max_length=10)

#     def create(self, validated_data):
#         obj = Category.objects.create(
#             slug=validated_data['slug'], name=validated_data['name'])
#         return obj

#     def update(self, instance, validated_data):
#         instance.slug = validated_data['slug']
#         instance.name = validated_data['name']
#         instance.save()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('slug', 'name','id')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug' ,read_only=True)
    class Meta:
        model = Product
        fields = ('slug', 'name', 'description',
                  'price', 'discount', 'category')


class ProductDetailsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('slug', 'name', 'description',
                  'price', 'discount', 'category', 'comments')
