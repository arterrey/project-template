import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest import TestCase
from unittest.mock import patch

from .project import (
    logging_configure,
    project_path_get,
    settings_path_get,
    settings_read,
)


class ProjectTest(TestCase):
    def test_project_path_get(self):
        # This basicly tests that we are working in the container.
        path = project_path_get()
        self.assertEqual(path, Path("/main"))

    def test_settings_path_get(self):
        saved_config = os.environ.get("CONFIG")

        if "CONFIG" in os.environ:
            del os.environ["CONFIG"]
        path = settings_path_get()
        self.assertEqual(path, Path("/main/etc/config.ini"))

        os.environ["CONFIG"] = "/path/to/custom.ini"
        self.assertEqual(settings_path_get(), Path("/path/to/custom.ini"))

        # Put it all back together again
        os.environ["CONFIG"] = saved_config

    def test_settings_read(self):
        with NamedTemporaryFile() as f:
            f.write(b"[DEFAULT]\nval0 = 0\nval1 = a\n[section]\nval1 = b\nval2 = c\n")
            f.flush()

            settings = settings_read(path=Path(f.name))
            self.assertEqual(settings["val0"], "0")
            self.assertEqual(settings["val1"], "a")
            self.assertNotIn("val2", settings)

            settings = settings_read(path=Path(f.name), section="section")
            self.assertEqual(settings["val0"], "0")
            self.assertEqual(settings["val1"], "b")
            self.assertEqual(settings["val2"], "c")import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest import TestCase
from unittest.mock import patch

from .project import (
    logging_configure,
    project_path_get,
    settings_path_get,
    settings_read,
)


class ProjectTest(TestCase):
    def test_project_path_get(self):
        # This basicly tests that we are working in the container.
        path = project_path_get()
        self.assertEqual(path, Path("/main"))

    def test_settings_path_get(self):
        saved_config = os.environ.get("CONFIG")

        if "CONFIG" in os.environ:
            del os.environ["CONFIG"]
        path = settings_path_get()
        self.assertEqual(path, Path("/main/etc/config.ini"))

        os.environ["CONFIG"] = "/path/to/custom.ini"
        self.assertEqual(settings_path_get(), Path("/path/to/custom.ini"))

        # Put it all back together again
        os.environ["CONFIG"] = saved_config

    def test_settings_read(self):
        with NamedTemporaryFile() as f:
            f.write(b"[DEFAULT]\nval0 = 0\nval1 = a\n[section]\nval1 = b\nval2 = c\n")
            f.flush()

            settings = settings_read(path=Path(f.name))
            self.assertEqual(settings["val0"], "0")
            self.assertEqual(settings["val1"], "a")
            self.assertNotIn("val2", settings)

            settings = settings_read(path=Path(f.name), section="section")
            self.assertEqual(settings["val0"], "0")
            self.assertEqual(settings["val1"], "b")
            self.assertEqual(settings["val2"], "c")

            os.environ["APP_VAL0"] = "x"
            settings = settings_read(path=Path(f.name), section="section")
            self.assertEqual(settings["val0"], "x")

    @patch("app.project.logging")
    def test_logging_configure(self, logging):
        logging_configure()
        logging.config.fileConfig.assert_called_once_with(settings_path_get())


    @patch("app.project.logging")
    def test_logging_configure(self, logging):
        logging_configure()
        logging.config.fileConfig.assert_called_once_with(settings_path_get())
