from rest_framework import routers
from comment.viewsets import CommentViewSet

from core.post.viewsets import PostViewSet
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet


router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


# ##################################################################### #
# ################### USER                       ###################### #
# ##################################################################### #

router.register(r'user', UserViewSet, basename='user')

# ##################################################################### #
# ################### POST                       ###################### #
# ##################################################################### #

router.register(r'post', PostViewSet, basename='post')

posts_router = routers.NestedSimpleRouter(router,r'post', lookup='post')

posts_router.register(r'comment', CommentViewSet,basename='post-comment')

# NestedSimpleRouter is a sub-class of the SimpleRouter class, which takes initialization
# parameters, such as parent_router – router –parent_prefix – r'post' – and
# the lookup – post. The lookup is the regex variable that matches an instance of the parent
# resource – PostViewSet.

urlpatterns = [
    *router.urls,
    *posts_router.urls
]