from rest_framework.test import APITestCase

from apps.members.models import Contact


class TestMemberCRUD(APITestCase):
    fixtures = ["fixtures/members_contact.yaml", "fixtures/members_label.yaml", "fixtures/members_contact_labels.yaml"]

    def test_create(self):
        body = {
            "name": "아무개",
            "email": "user@example.com",
            "phone": "01012341234",
            "profile_image_url": None,
            "company": "길거리",
            "position": "상무",
            "memo": "테스트",
            "address": "서울역",
            "birthday": "2025-08-08",
            "website": None,
            "labels": [{"label": "회사"}, {"label": "테스트"}],
        }

        res = self.client.post("/api/members/contacts/", data=body, format="json")
        result = res.json()

        self.assertEqual(201, res.status_code)
        self.assertEqual("아무개", result["name"])

    def test_update(self):
        body = {
            "name": "아무개",
            "email": "user@example.com",
            "phone": "01012341234",
            "profile_image_url": None,
            "company": "길거리",
            "position": "상무",
            "memo": "테스트",
            "address": "서울역",
            "birthday": "2025-08-08",
            "website": None,
            "labels": [{"label": "회사"}, {"label": "테스트"}],
        }

        res = self.client.put("/api/members/contacts/1/", data=body, format="json")
        result = res.json()

        contact = Contact.objects.get(pk=1)

        self.assertEqual(200, res.status_code)
        self.assertEqual("아무개", result["name"])
        self.assertEqual("아무개", contact.name)

    def test_retrieve(self):
        res = self.client.get("/api/members/contacts/2/", format="json")
        result = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(2, result["id"])
        self.assertEqual("박아무개", result["name"])

    def test_list_ordering_name_default_ordering(self):
        res = self.client.get("/api/members/contacts/", format="json")
        result = res.json()

        self.assertEqual(3, len(result["results"]))
        self.assertEqual(1, result["results"][0]["id"])
        self.assertEqual(2, result["results"][1]["id"])
        self.assertEqual(3, result["results"][2]["id"])

    def test_list_ordering_name_asc(self):
        res = self.client.get("/api/members/contacts/?ordering=name", format="json")
        result = res.json()

        self.assertEqual(3, len(result["results"]))
        self.assertEqual("김아무개", result["results"][0]["name"])
        self.assertEqual("박아무개", result["results"][1]["name"])
        self.assertEqual("이아무개", result["results"][2]["name"])

    def test_list_ordering_name_desc(self):
        res = self.client.get("/api/members/contacts/?ordering=-name", format="json")
        result = res.json()

        self.assertEqual(3, len(result["results"]))
        self.assertEqual("이아무개", result["results"][0]["name"])
        self.assertEqual("박아무개", result["results"][1]["name"])
        self.assertEqual("김아무개", result["results"][2]["name"])

    def test_list_ordering_email_asc(self):
        res = self.client.get("/api/members/contacts/?ordering=email", format="json")
        result = res.json()

        self.assertEqual(3, len(result["results"]))
        self.assertEqual("test1@example.com", result["results"][0]["email"])
        self.assertEqual("test2@example.com", result["results"][1]["email"])
        self.assertEqual("test3@example.com", result["results"][2]["email"])

    def test_list_ordering_email_desc(self):
        res = self.client.get("/api/members/contacts/?ordering=-email", format="json")
        result = res.json()

        self.assertEqual(3, len(result["results"]))
        self.assertEqual("test3@example.com", result["results"][0]["email"])
        self.assertEqual("test2@example.com", result["results"][1]["email"])
        self.assertEqual("test1@example.com", result["results"][2]["email"])

    def test_list_ordering_phone_asc(self):
        res = self.client.get("/api/members/contacts/?ordering=phone", format="json")
        result = res.json()

        self.assertEqual(3, len(result["results"]))
        self.assertEqual("010-1111-1111", result["results"][0]["phone"])
        self.assertEqual("010-1111-2222", result["results"][1]["phone"])
        self.assertEqual("010-1111-3333", result["results"][2]["phone"])

    def test_list_ordering_phone_desc(self):
        res = self.client.get("/api/members/contacts/?ordering=-phone", format="json")
        result = res.json()

        self.assertEqual(3, len(result["results"]))
        self.assertEqual("010-1111-3333", result["results"][0]["phone"])
        self.assertEqual("010-1111-2222", result["results"][1]["phone"])
        self.assertEqual("010-1111-1111", result["results"][2]["phone"])

    def tearDown(self):
        Contact.objects.all().delete()
