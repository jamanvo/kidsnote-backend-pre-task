from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.members.serializers import ContactSerializer
from apps.members.models import Contact


class ContactViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.prefetch_related("labels").all()

    filter_backends = (OrderingFilter,)
    ordering_fields = ("name", "email", "phone")
    ordering = "id"

    http_method_names = ["get", "post", "put", "head", "options"]

    @extend_schema(
        summary="새로운 연락처 생성",
        request=ContactSerializer,
        responses=ContactSerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="개별 연락처 업데이트",
        request=ContactSerializer,
        responses=ContactSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="연락처 목록",
        request=ContactSerializer,
        responses=ContactSerializer,
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="연락처 상세",
        request=ContactSerializer,
        responses=ContactSerializer,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
