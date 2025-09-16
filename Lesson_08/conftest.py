import pytest
import requests
from config import Config


@pytest.fixture(scope="session")
def auth_headers():

    return {
        "Authorization": f"Bearer {"H6HngIA816fpIhY7tBvWx/it3YbVvEt/33Sk8afA39MCR9a"}",
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="session")
def base_url():

    return Config.BASE_URL


@pytest.fixture
def cleanup_project(auth_headers, base_url):
    
    created_projects = []

    yield created_projects

    # Очистка после выполнения тестов
    for project_id in created_projects:
        try:
            response = requests.delete(
                f"{base_url}/projects/{project_id}",
                headers=auth_headers
            )
        except:
            pass