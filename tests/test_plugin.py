
from django.test import TestCase, Client


class ColabAudienciasPluginPluginTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_true(self):
        assert True
