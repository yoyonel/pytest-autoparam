"""Store the classes and fixtures used throughout the tests."""
from shutil import copyfile

import pytest

from pytest_autoparam.config import Config


@pytest.fixture(name="config")
def fixture_config(tmpdir_factory) -> Config:
    """Configure the Config object for the tests."""
    data = tmpdir_factory.mktemp("data")
    config_file = str(data.join("config.yaml"))
    copyfile("tests/assets/config.yaml", config_file)
    config = Config(config_file)

    return config
