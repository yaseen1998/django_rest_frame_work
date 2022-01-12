from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

class ReviewSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ('watchlist_app',)
class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    reviews = ReviewSerailizer(many= True,read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id','storyline','title']
        # exclude =['active'] # except 
    

class StreamPlatformSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="platform_detail")
    platform = WatchListSerializer(many=True,read_only=True)
    # platform = serializers.StringRelatedField(many= True)
    # platform = serializers.PrimaryKeyRelatedField(many= True,read_only=True)
    # platform = serializers.HyperlinkedIdentityField(many= True,read_only=True,view_name='platform_detail')
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'


    # def get_len_name(self,object):
    #     length = len(object.name)
    #     return length
        
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('name and description should be different')
    #     else:
    #         return data

    
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('name is too short')
    #     else:
    #         return value
        

# def description_length(value):
#     if len(value) < 10:
#         raise serializers.ValidationError('description is too short')
#     else:
#         return value
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_length])
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movies.objects.create(**validated_data)
    
#     def update(self,instace,validated_data):
#         instace.name = validated_data.get('name',instace.name)
#         instace.description = validated_data.get('description',instace.description)
#         instace.active = validated_data.get('active',instace.active)
#         instace.save()
#         return instace
    
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('name and description should be different')
#         else:
#             return data

    
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError('name is too short')
#         else:
#             return value
        