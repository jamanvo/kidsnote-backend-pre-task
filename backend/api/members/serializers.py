from rest_framework import serializers

from apps.members.models import Contact, Label
from services.mambers.contacts import ContactService


class LabelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ("label",)


class ContactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    profile_image_url = serializers.URLField(required=False, allow_null=True)
    company = serializers.CharField(max_length=32, required=False, allow_null=True, help_text="회사")
    position = serializers.CharField(max_length=16, required=False, allow_null=True, help_text="직급")
    memo = serializers.CharField(required=False, allow_null=True, help_text="메모")
    address = serializers.CharField(required=False, allow_null=True, help_text="주소")
    birthday = serializers.DateField(required=False, allow_null=True, help_text="생일")
    website = serializers.URLField(required=False, allow_null=True, help_text="웹사이트")
    labels = LabelModelSerializer(many=True)

    class Meta:
        model = Contact
        fields = (
            "id",
            "name",
            "email",
            "phone",
            "profile_image_url",
            "company",
            "position",
            "memo",
            "address",
            "birthday",
            "website",
            "labels",
        )

    def create(self, validated_data):
        labels = validated_data.pop("labels") if "labels" in validated_data else []

        contact = super().create(validated_data)

        ContactService(contact).connect_labels(labels)

        return contact

    def update(self, instance, validated_data):
        labels = validated_data.pop("labels") if "labels" in validated_data else []

        contact = super().update(instance, validated_data)

        ContactService(contact).reconnect_labels(labels)

        return contact
