# tests/conftest.py
import pytest
import os
from app import app as flask_app

# Workaround for Windows "Can't pickle local object" error
import multiprocessing
if os.name == 'nt':
    multiprocessing.set_start_method('spawn', force=True)


@pytest.fixture(scope='session')
def app():
    return flask_app


@pytest.fixture
def client(app):
    return app.test_client()
