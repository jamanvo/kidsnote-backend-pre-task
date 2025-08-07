from django.db import models


class Label(models.Model):
    label = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=36, verbose_name="이름")
    email = models.EmailField(verbose_name="이메일")
    phone = models.CharField(max_length=20, verbose_name="전화번호")

    profile_image_url = models.URLField(null=True)
    company = models.CharField(max_length=100, null=True, verbose_name="회사")
    position = models.CharField(max_length=100, null=True, verbose_name="직책")
    memo = models.TextField(null=True, verbose_name="메모")
    address = models.TextField(null=True, verbose_name="주소")
    birthday = models.DateField(null=True, verbose_name="생일")
    website = models.CharField(max_length=256, null=True, verbose_name="웹사이트")

    labels = models.ManyToManyField(Label, related_name="contacts")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = (
            models.Index(fields=("name",)),
            models.Index(fields=("email",)),
            models.Index(fields=("phone",)),
        )
        ordering = ("id",)
