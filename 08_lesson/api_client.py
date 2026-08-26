import requests


class YougileProjectsAPI:
    def __init__(self):
        self.url = "https://ru.yougile.com"  # Базовый URL Yougile API v2
        self.token = self.get_keys_list()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def get_keys_list(self):
        """Получение токена авторизации."""
        body = {
            "login": "",
            "password": ""
        }
        resp = requests.post(f"{self.url}/api-v2/auth/keys/get", json=body)
        # Защита от падения: если пришел список,
        # берем элемент [0], если словарь — ключ
        res_data = resp.json()
        if isinstance(res_data, list):
            return res_data[0]["key"]
        return res_data["key"]

    def create_project(self, title: str):
        """[POST] /api-v2/projects — Создание проекта."""
        # Передаем строго title, без лишних полей name или description
        project = {"title": title}
        resp = requests.post(f"{
            self.url}/api-v2/projects", json=project, headers=self.headers)
        return resp

    def get_project(self, project_id: str):
        """[GET] /api-v2/projects/{id} — Получение информации о проекте."""
        resp = requests.get(f"{
            self.url}/api-v2/projects/{project_id}", headers=self.headers)
        return resp

    def update_project(self, project_id: str, new_title: str):
        """[PUT] /api-v2/projects/{id} — Изменение проекта."""
        payload = {"title": new_title}
        resp = requests.put(f"{self.url}/api-v2/projects/{
            project_id}", json=payload, headers=self.headers)
        return resp
