from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,ProjectViewSet,CommentViewSet,TaskAssignmentViewSet


router = DefaultRouter()

router.register(r"task", TaskViewSet, basename="task"),
router.register(r"projects", ProjectViewSet,basename ="project" ),
router.register(r"comments", CommentViewSet,basename="comments"),
router.register(r"taskassignment", TaskAssignmentViewSet,basename=" taskassignment" )


urlpatterns = router.urls