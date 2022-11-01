from rest_framework import serializers
from articles.models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.author.email
    
    class Meta:
        model = Comment
        exclude = ("article",)



class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    likes = serializers.StringRelatedField(many=True)
    
    def get_author(self, obj):
        return obj.author.email
    
    class Meta:
        model = Article
        fields = '__all__'
        
        
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "image", "content")       
        
        
class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.author.email
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comments_count(self, obj):
        return obj.comments.count()
    
    class Meta:
        model = Article
        fields = ("pk", "title", "image", "updated_at", "author", "likes_count", "comments_count")
        
        
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)    