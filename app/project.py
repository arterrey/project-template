"""Methods for inspecting the current project and environment. Such as settings
discovery, project path, etc.


For example, the following reads the settings from the config file ``/main/etc/debug.ini``
and the adds environment variable ``APP_MY_SETTING`` as ``my_setting``::

    >>> import os
    >>> from app.project import settings_read
    >>> os.environ["CONFIG"] = "/main/etc/debug.ini"
    >>> os.environ["APP_MY_SETTING"] = "my value"
    >>> settings = settings_read()
    >>> settings["my_setting"]
    'my value'

----
"""

import logging.config
import os
from configparser import ConfigParser
from pathlib import Path

import app
from app.const import ENVIRON_SETTINGS_PREFIX


def logging_configure() -> None:
    """Configure logging from the settings file."""
    path = settings_path_get()
    logging.config.fileConfig(path)


def settings_read(
    section: str | None = None,
    path: Path | None = None,
) -> dict[str, str]:
    """Reading settings from path and environment.

    Args:
        section (str | None): The section to read from the config file overriding
            the default section. If not given, only the default section is used.
        path (Path | None): The path to the config file. If not given, the path
            is determined using :func:`settings_path_get`.

    Returns:
        dict[str, str]: The settings.
    """
    # Read values from config file
    parser = ConfigParser()
    path = path or settings_path_get()
    parser.read(path)
    if section is None:
        settings = {**parser["DEFAULT"]}
    else:
        settings = {**parser["DEFAULT"], **parser[section]}

    # Read values from environment
    for environ_key, value in os.environ.items():
        if environ_key.startswith(ENVIRON_SETTINGS_PREFIX):
            settings_key = environ_key[len(ENVIRON_SETTINGS_PREFIX) :].lower()
            settings[settings_key] = value

    return settings


def settings_path_get() -> Path:
    """Determine and return the path to the settings file.

    Returns:
        Path: The path to the settings file.
    """
    path = os.environ.get("CONFIG") or project_path_get() / "etc" / "config.ini"
    if isinstance(path, str):
        path = Path(path)
    return path


def project_path_get() -> Path:
    """Determin and return the path to the project root directory.

    Returns:
        Path: The path to the project root directory."""
    return Path(app.__file__).resolve().parent.parent
