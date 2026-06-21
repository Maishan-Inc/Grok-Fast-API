import os
import pathlib
import sys
import types
import unittest
from unittest.mock import patch


_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _package(name: str, path: pathlib.Path) -> types.ModuleType:
    module = types.ModuleType(name)
    module.__path__ = [str(path)]
    return module


def _load_module(module_name: str, file_path: pathlib.Path):
    import importlib.util

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _load_account_factory():
    with patch.dict(
        sys.modules,
        {
            "app": _package("app", _ROOT / "app"),
            "app.control": _package("app.control", _ROOT / "app/control"),
            "app.control.account": _package("app.control.account", _ROOT / "app/control/account"),
            "app.control.account.backends": _package(
                "app.control.account.backends",
                _ROOT / "app/control/account/backends",
            ),
            "app.control.account.repository": types.SimpleNamespace(AccountRepository=object),
        },
    ):
        return _load_module(
            "app.control.account.backends.factory",
            _ROOT / "app/control/account/backends/factory.py",
        )


def _load_config_factory():
    with patch.dict(
        sys.modules,
        {
            "app": _package("app", _ROOT / "app"),
            "app.platform": _package("app.platform", _ROOT / "app/platform"),
            "app.platform.config": _package("app.platform.config", _ROOT / "app/platform/config"),
            "app.platform.config.backends": _package(
                "app.platform.config.backends",
                _ROOT / "app/platform/config/backends",
            ),
        },
    ):
        return _load_module(
            "app.platform.config.backends.factory",
            _ROOT / "app/platform/config/backends/factory.py",
        )


class StorageDefaultsTests(unittest.TestCase):
    def test_account_storage_defaults_to_postgresql(self):
        factory = _load_account_factory()
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(factory.get_repository_backend(), "postgresql")

    def test_config_storage_follows_postgresql_default(self):
        factory = _load_config_factory()
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(factory.get_config_backend_name(), "postgresql")


if __name__ == "__main__":
    unittest.main()
