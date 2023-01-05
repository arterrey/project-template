=====================
Runtime Configuration
=====================

Runtime configuration are the configurable inputs to the application that
are not fixed by the codebase.

Approach
========

Most python utility scripts are configured via a configuration file in the
ConfigParser format. Therfore, this project uses a common configuration file
across a number of utilities as long as there is no conflict in section naming.

The project comes with two configuration sets, a default one that is used
for deployments and a "debug" configuration set that is used for local
development and is not to be used in a deployment.

The "debug" configuration set generally features configuration optimizes
for clarity and debugability. Where as the default configuration optimizes for
performance and security.

The configuration sets are locataed in the directory ``etc``. The default
default being ``etc/default.cfg`` and the debug configuration being
``etc/debug.cfg``.

They mixin the following configurations:

* `Python logging module <https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig>`_


App Entrypoint Configuration
============================

The application is simerly configured via either the default or debug
configuration sets.  Configuration keys are overriden in the following order:

1. Configuration keys in the section ``[DEFAULT]``

2. Configuration keys in the section ``[app:<entry_point_name>]``

3. Environment variables prefixed with ``CONFIG_``

For example::

    [DEFAULT]
    db_url = postgresql://user:password@localhost:5432/db
    email_noreply = noreply@example.com

    [app:web]
    cookie_secret = 1234

    [app:worker]
    backend_timeout = 120

Both ``web`` and ``worker`` entry points will have the ``db_url`` and
``email_noreply`` configuration keys set to the values in the ``[DEFAULT]``
section. However, the ``cookie_secret`` configuration key will be set to
``1234`` for the ``web`` entry point and ``backend_timeout`` will be set to
``120`` for the ``worker`` entry point.

In a specific deployment the admin may need to override the ``db_url`` and he
may do so by setting the environment variable ``CONFIG_db_url``.

