from rest_framework import serializers

from todo.models import Todo, Author


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "author", "content", "completed", "reminder", "created_at")


class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("content", "completed", "reminder")

    def create(self, validated_data):
        user = self.context["user_id"]
        (author, created) = Author.objects.get_or_create(user=user)
        return Todo.objects.create(author=author, **validated_data)
