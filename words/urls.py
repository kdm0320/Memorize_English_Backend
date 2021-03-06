from rest_framework.routers import DefaultRouter
from . import views


app_name = "words"


router = DefaultRouter()
router.register("", views.WordViewSet)

urlpatterns = router.urls
