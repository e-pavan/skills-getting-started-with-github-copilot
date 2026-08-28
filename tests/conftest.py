from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    # Arrange: create a reusable HTTP client for API tests.
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange: snapshot initial in-memory data for test isolation.
    original_activities = deepcopy(app_module.activities)

    yield

    # Assert cleanup: restore the baseline state after each test.
    app_module.activities.clear()
    app_module.activities.update(deepcopy(original_activities))
