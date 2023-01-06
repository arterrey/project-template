from unittest import TestCase
from unittest.mock import patch

from .registry import Registry


class RegistryTest(TestCase):
    @patch("app.registry.settings_read")
    def test_registry(self, settings_read):
        settings_read.return_value = {"foo": "bar"}
        registry = Registry()
        self.assertEqual(registry.settings, {"foo": "bar"})
