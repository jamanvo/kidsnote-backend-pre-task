from rest_framework.routers import DefaultRouter

from api.members.views import ContactViewSet

router = DefaultRouter()

router.register("contacts", ContactViewSet, basename="contacts")

urlpatterns = router.urls
