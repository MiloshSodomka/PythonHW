import requests
from config import Config


class ProjectsPage:
    def __init__(self, base_url, auth_headers):
        self.base_url = base_url
        self.auth_headers = auth_headers

    def create_project(self, project_data):
        """POST /api-v2/projects - создание проекта"""
        url = f"{self.base_url}/projects"
        response = requests.post(
            url,
            json=project_data,
            headers=self.auth_headers
        )
        return response

    def get_project(self, project_id):
        """GET /api-v2/projects/{id} - получение проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.auth_headers)
        return response

    def update_project(self, project_id, update_data):
        """PUT /api-v2/projects/{id} - обновление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(
            url,
            json=update_data,
            headers=self.auth_headers
        )
        return response

    def delete_project(self, project_id):
        """DELETE /api-v2/projects/{id} - удаление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.delete(url, headers=self.auth_headers)
        return response