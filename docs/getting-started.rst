===============
Getting Started
===============

Building and Running
====================

To get started with local development. Download and install Microsoft Visual
Studio Code and the Remote Containers extension. Then open the project in
Visual Studio Code and click the "Reopen in Container" button in the bottom
right corner of the window.

Once the container is built and running, you will now have a Visual Studio code
session running inside the container. It includes the same dependencies as the
production environment plus some additional tools for development and testing.
However, the project remains to be built. To build the project, run the
following command in the terminal::

    scripts/build

INSTRUCTIONS TO RUN THE PROJECT FOR THE FIRST TIME GO HERE


What am I looking at?
=====================

This is a mono repo of a number of componnents.  The project directory is a
mixin of the following:

Python virtual environment.
    Provides an isolated python environment for the project. This is defined
    in the ``requirements.txt`` and the ``requirements-pinned.txt`` files.
    The python binary and installed scripts are available in the ``bin``.

Python package package in the ``app`` namespace.
    This is the main python package for the project configured using
    ``pyproject.toml`` to install the package directory ``app`` in the virtual
    environment. It contains the application code and the main entry points.

    In this project the package doesn't list the dependencies. Instead the
    dependencies are listed in the ``requirements.txt`` file for simplicity
    and due to the fact that this packages is not intended to be distributed.

Scripts.
    This is a collection of scripts in the folder named ``scripts`` that are
    used for various development, testing, administration and deployment tasks.

Visual Studio devcontainer workspace.
    This is defined in the ``.devcontainer`` directory. It contains the
    configuration for the Visual Studio Code devcontainer extension. Opening
    the project in Visual Studio Code will automatically build and run an
    suitable environment.

Dockerfile context.
    The ``Dockerfile`` is used to build the production docker image that is
    used to run the application in production. This is not used to build
    the devcontainer that is used by Visual Studio Code. Please see the
    ``.devcontainer`` directory for the configuration of the devcontainer.

Sphinx documentation.
    This is used to generate the documentation for the project. It is defined
    in the ``docs`` directory.

Runtime configuration.
    This is used to configure the application at runtime. It is defined in
    the ``etc`` directory. Generally configuration is loaded from ``etc/config.ini``
    or ``etc/debug.ini`` and can be overriedn by environment variables using the
    prefix ``CONFIG_``. For example, ``CONFIG_db_url`` will override the ``db_url``
    configuration option.
