"""
This file is loaded by pytest to configure the test environments, set up fixtures, etc.

@see https://docs.pytest.org/en/latest/example/simple.html

Some example packages you might want to consider loading/configuring here are:

- https://github.com/jamielennox/requests-mock/
- https://github.com/joke2k/faker/


"""

from _pytest.config import Config as PytestConfig

# CHANGEME: This is a good place to call any sort of methods you might have to
#           initialize or configure things like logging.


def _pytest_configure(ptconfig: PytestConfig) -> None:
    """
    Update/override pytest config.  This separate function exists so we can override the
    pytest hookspec that requires the parameter be named 'config', which of course
    conflicts with our own config variable name.
    """
    if not ptconfig.option.markexpr:
        ptconfig.option.markexpr = ""

    # CHANGME: all of this...

    # For example, you could detect running tests in your dev environment and silence
    # some noisy logs.
    #
    # if DETECT_IS_DEV_MODE:
    #     # These logging namespaces are VERY noisy in debug mode, so let's disable them
    #     # for local tests. Devs can temporarily comment out this section if the debug
    #     # data is helpful for tracking down specific errors.
    #     for noisy_log in ("urllib3", "faker"):
    #         logger = logging.getLogger(noisy_log)
    #         logger.setLevel(logging.INFO)
    #
    # Or tell pytest to exclude certain tests marked as "devonly" that won't run in
    # your actual test environment.
    #
    # else:
    #     if ptconfig.option.markexpr:
    #         ptconfig.option.markexpr += " and "
    #     ptconfig.option.markexpr += "not devonly"


def pytest_configure(config: PytestConfig) -> None:
    """
    Update/override pytest config

    Annoying that this requires use of the 'config' parameter name that overrides our
    own package global var so we have to create a separate function in order to access
    both.
    """
    return _pytest_configure(config)
