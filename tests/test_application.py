import pytest
from application import create_app

class TestApplication():
    @pytest.fixture
    def app():
        app = create_app('config.MockConfig')
        return app.test_client()