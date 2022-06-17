from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Todo
from .serializers import CreateTodoSerializer, TodoSerializer


class TodoViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete", "head", "options"]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CreateTodoSerializer(
            data=request.data, context={"user_id": self.request.user.id}
        )
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(instance=todo)
        return Response(data=serializer.data)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateTodoSerializer
        return TodoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Todo.objects.all()
        return Todo.objects.filter(author__user=user)

    @action(detail=False, methods=["GET"])
    def completed(self, request):
        completed_tasks = Todo.objects.filter(completed=True).all()
        serializer = TodoSerializer(completed_tasks, many=True)
        return Response(serializer.data)
