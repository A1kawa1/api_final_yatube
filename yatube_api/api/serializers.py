from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from posts.models import Post, Comment, Group, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'author',
            'image',
            'group',
            'pub_date'
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description'
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        required=False,
        read_only=True
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'post',
            'text',
            'created'
        )


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = (
            'user',
            'following'
        )

    def validate(self, data):
        request = self.context.get('request')

        follow = Follow.objects.filter(
            user=request.user
        ).values_list('following', flat=True)

        following_field = get_object_or_404(
            User,
            username=data['following']
        )

        if (following_field == request.user) or (following_field.id in follow):
            raise serializers.ValidationError('не уникальная подписка')
        return data
