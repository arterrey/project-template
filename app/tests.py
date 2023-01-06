"""Test suites for the app package.

There are two suites of tests, unit tests and integration tests.

Unit Tests
==========

These are tests that can without integrating with external
services, such as a database. These tests are discovered with the pattern
``*_test.py``.

Example ``my_test.py``::

    from unittest import TestCase

    class MyTest(TestCase):
        def test_something(self):
            self.assertTrue(True)

Integration Tests
=================

These are tests that require the presence of docker
and create integration layers, such as database and cache. These tests are
discovered with the pattern ``*_inttest.py``. Integration tests require
specifying a testing layer on the ``TestCase`` class.

Example ``my_inttest.py``::

    from unittest import TestCase
    from app.testing.layers.registry import RegistryLayer

    class MyIntegrationTest(TestCase):
        layer = RegistryLayer

        def test_something(self):
            registry = self.layer["registry"]
            with registry.session_begin() as session:
                result = session.execute("SELECT 1").scalar()
                assert result == 1

----
"""
import unittest

import app.project


def test_suite():
    """The default test suite. Discover tests with the pattern ``*_test.py``
    These are unit tests.

    Returns:
        A test suite of unit tests."""
    cases = _test_suite_test_cases()
    return unittest.TestSuite([cases])


def integration_test_suite():
    """Return a testsuite of integrated tests with the pattern ``*_inttest.py``

    Returns:
        A testsuite of integration tests.
    """
    cases = _test_suite_test_cases(pattern="*_inttest.py")
    return unittest.TestSuite([cases])


def _test_suite_test_cases(pattern="*_test.py"):
    top_level_dir = str(app.project.project_path_get())
    return unittest.TestLoader().discover(
        top_level_dir,
        pattern=pattern,
        top_level_dir=top_level_dir,
    )
