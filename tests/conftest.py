import pytest
from fastapi import FastAPI

from application.app import create_app


@pytest.fixture
def app() -> FastAPI:
    app = create_app()
    return app