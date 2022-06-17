from rest_framework_nested import routers

from core.views import UserViewSet

# TODO: Correct the bad practice of todo app dependency on core app
from todo.views import TodoViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("todos", TodoViewSet, basename="todos")

urlpatterns = router.urls