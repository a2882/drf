from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.validators import ValidationError
from .models import Product
from .validators import validate_title


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="products-detail",lookup_field = 'pk')
    title = serializers.CharField(validators=[validate_title])


    class Meta:
        model = Product
        fields = [
            'edit_url',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value
#this def for validate particular instance we can use it on any instance

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('products-edit',kwargs={'pk':obj.pk},request=request)
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()