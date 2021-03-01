from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PollViewSet, QuestionViewSet, VoteViewSet

router_v1 = DefaultRouter()
router_v1.register(r'questions', QuestionViewSet, basename='questions')
router_v1.register(r'polls', PollViewSet, basename='polls')
router_v1.register(r'votes', VoteViewSet, basename='votes')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
