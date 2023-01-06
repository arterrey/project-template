"""The application registry is an object that is used to manage and maintain a set
of global objects and methods that are available to the application. It is
designed to be configured during process startup and live for the duration of
the process.

A simple useage of the registry in the context of a script or a HTTP view might be::

    >>> from app.registry import Registry
    >>> registry = Registry()

----

"""
from .project import settings_read


class Registry:
    """A bag of global objects and methods.  Configured using
    :func:`app.project.settings_read`

    This registry is a subclass of the Pyramid Registry. Since, it is reasonably
    generic and can be used when it comes to configuring a HTTP server.
    """

    settings: dict[str, str]
    """Application settings used to configure this registry"""

    def __init__(self):
        super().__init__()
        self.settings = settings_read()
