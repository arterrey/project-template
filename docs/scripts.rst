=======
Scripts
=======

Project scripts are locaced in the ``scripts`` directory. They are used for
verious tasks. Asside from the ``build`` script, they require the project
to be built and they are required to be run from the project root directory.

.. admonition:: Writing Scripts

    Both the devcontainer and deployment containers use the same project
    location, it is safe to set the python SH-BANG to::

      #!/main/bin/python
      
    This allows a python script to import th ``app`` package and other
    installed packages.

    If there is not need - system python or system bash is no problem.


Building
========

Scripts to build and upgrade the project.

.. describe:: build

    .. program-output:: ../scripts/build --help

Administration
==============

Scripts to administer a given dataset

Development Tools
=================

.. describe:: code-analysis

    Runs code analysis tools on the project.

.. describe:: code-fix

    Runs code fix tools on the project.

.. describe:: test

    A wrapper around zope-testrunner. It runs the unittests in the project.

.. describe:: test-integration

    A wrapper around zope-testrunner. It runs the integration tests in the
    project.

Running the Application
=======================


.. describe:: docs-serve

    Builds and serves the documentation using sphinx-autobuild
