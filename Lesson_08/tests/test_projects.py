import pytest
import json
from pages.projects_page import ProjectsPage


class TestProjects:
    """Тесты для методов работы с проектами"""

    # Позитивные тесты

    def test_create_project_positive(self, base_url, auth_headers, cleanup_project):
        """Позитивный тест создания проекта"""
        projects_page = ProjectsPage(base_url, auth_headers)

        project_data = {
            "title": "Test Project Positive",
            "description": "This is a test project for positive case",
            "companyId": "9347006b-dc75-4550-97d5-3008ba00d4a0"
        }

        response = projects_page.create_project(project_data)

        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["title"] == project_data["title"]

        # Сохраняем ID для очистки
        cleanup_project.append(response.json()["id"])

    def test_get_project_positive(self, base_url, auth_headers, cleanup_project):
        """Позитивный тест получения проекта"""
        projects_page = ProjectsPage(base_url, auth_headers)

        # Сначала создаем проект
        project_data = {
            "title": "Test Project for Get",
            "description": "Project for get test",
            "companyId": "your_company_id_here"
        }

        create_response = projects_page.create_project(project_data)
        project_id = create_response.json()["id"]
        cleanup_project.append(project_id)

        # Получаем проект
        response = projects_page.get_project(project_id)

        assert response.status_code == 200
        assert response.json()["id"] == project_id
        assert response.json()["title"] == project_data["title"]

    def test_update_project_positive(self, base_url, auth_headers, cleanup_project):
        """Позитивный тест обновления проекта"""
        projects_page = ProjectsPage(base_url, auth_headers)

        # Сначала создаем проект
        project_data = {
            "title": "Test Project for Update",
            "description": "Project for update test",
            "companyId": "9347006b-dc75-4550-97d5-3008ba00d4a0"
        }

        create_response = projects_page.create_project(project_data)
        project_id = create_response.json()["id"]
        cleanup_project.append(project_id)

        # Обновляем проект
        update_data = {
            "title": "Updated Test Project",
            "description": "Updated description"
        }

        response = projects_page.update_project(project_id, update_data)

        assert response.status_code == 200
        assert response.json()["title"] == update_data["title"]
        assert response.json()["description"] == update_data["description"]

    # Негативные тесты

    def test_create_project_negative_missing_required(self, base_url, auth_headers):
        """Негативный тест создания проекта без обязательных полей"""
        projects_page = ProjectsPage(base_url, auth_headers)

        # Отсутствует обязательное поле title
        project_data = {
            "description": "Project without title",
            "companyId": "9347006b-dc75-4550-97d5-3008ba00d4a0"
        }

        response = projects_page.create_project(project_data)

        # Ожидаем ошибку валидации
        assert response.status_code in [400, 422]

    def test_get_project_negative_not_found(self, base_url, auth_headers):
        """Негативный тест получения несуществующего проекта"""
        projects_page = ProjectsPage(base_url, auth_headers)

        # Пытаемся получить проект с несуществующим ID
        response = projects_page.get_project("non_existing_id_12345")

        assert response.status_code == 404

    def test_update_project_negative_invalid_data(self, base_url, auth_headers, cleanup_project):
        """Негативный тест обновления проекта с невалидными данными"""
        projects_page = ProjectsPage(base_url, auth_headers)

        # Сначала создаем проект
        project_data = {
            "title": "Test Project for Negative Update",
            "companyId": "9347006b-dc75-4550-97d5-3008ba00d4a0"
        }

        create_response = projects_page.create_project(project_data)
        project_id = create_response.json()["id"]
        cleanup_project.append(project_id)

        # Пытаемся обновить с невалидными данными (пустой title)
        update_data = {
            "title": "",  # Пустой title недопустим
            "description": "Updated description"
        }

        response = projects_page.update_project(project_id, update_data)

        # Ожидаем ошибку валидации
        assert response.status_code in [400, 422]

    def test_create_project_negative_unauthorized(self, base_url):
        """Негативный тест создания проекта без авторизации"""
        projects_page = ProjectsPage(base_url, {"Authorization": "Bearer invalid_token"})

        project_data = {
            "title": "Test Project Unauthorized",
            "companyId": "9347006b-dc75-4550-97d5-3008ba00d4a0"
        }

        response = projects_page.create_project(project_data)

        assert response.status_code == 401