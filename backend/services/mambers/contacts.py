from django.db.models import QuerySet

from apps.members.models import Contact, Label


class ContactService:
    def __init__(self, contact: Contact):
        self.contact = contact

    def connect_labels(self, labels: list[dict]) -> None:
        label_list = self._get_or_create_labels(labels)

        for label in label_list:
            self.contact.labels.add(label)

    def reconnect_labels(self, labels: list[dict]) -> None:
        label_list = self._get_or_create_labels(labels)

        self.contact.labels.set(label_list)

    def _get_or_create_labels(self, labels: list[dict]) -> list[Label] | QuerySet:
        label_list = [label["label"] for label in labels]
        existing_label_queryset = Label.objects.filter(label__in=label_list)

        if len(label_list) == len(existing_label_queryset):
            return existing_label_queryset

        create_label_list = [
            Label(label=label)
            for label in label_list
            if label not in existing_label_queryset.values_list("label", flat=True)
        ]

        created_labels = Label.objects.bulk_create(create_label_list)

        return list(existing_label_queryset) + list(created_labels)
