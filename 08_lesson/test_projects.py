import pytest
import uuid
from api_client import YougileProjectsAPI


@pytest.fixture(scope="session")
def api():
    """Фикстура инициализации API клиента."""
    return YougileProjectsAPI()


@pytest.fixture()
def temp_project(api):
    """Фикстура для фонового создания проекта (для тестов GET и PUT)."""
    unique_title = f"Autotest Project {uuid.uuid4().hex[:6]}"
    resp = api.create_project(unique_title)
    assert resp.status_code == 201, f"Фоновое создание проекта завершилось ошибкой: {resp.text}"
    project_id = resp.json()["id"]
    yield project_id
    # Здесь можно было бы добавить
    # шаг удаления (Teardown), если API это поддерживает

    # === 1. ТЕСТЫ НА МЕТОД [POST] /api-v2/projects ===


def test_create_project_positive(api):
    """Позитивный тест: Создание проекта с валидным title."""
    unique_title = f"New Project {uuid.uuid4().hex[:6]}"
    response = api.create_project(unique_title)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_empty_title(api):
    """Негативный тест: Создание проекта с пустым title."""
    response = api.create_project("")

    # API должно вернуть 400 Bad Request на пустое обязательное поле
    assert response.status_code == 400


# === 2. ТЕСТЫ НА МЕТОД [GET] /api-v2/projects/{id} ===

def test_get_project_positive(api, temp_project):
    """Позитивный тест: Получение существующего проекта по ID."""
    response = api.get_project(temp_project)

    assert response.status_code == 200
    assert response.json()["id"] == temp_project


def test_get_project_negative_invalid_id(api):
    """Негативный тест: Получение проекта по несуществующему ID."""
    fake_id = str(uuid.uuid4())
    response = api.get_project(fake_id)

    # Ожидаем 404 Not Found или 400 в зависимости от логики Yougile
    assert response.status_code in [404, 400]


# === 3. ТЕСТЫ НА МЕТОД [PUT] /api-v2/projects/{id} ===

def test_update_project_positive(api, temp_project):
    """Позитивный тест: Изменение названия существующего проекта."""
    updated_title = f"Updated Project {uuid.uuid4().hex[:6]}"
    response = api.update_project(temp_project, updated_title)
    assert response.status_code == 200
    # Дополнительно проверяем через GET, что имя реально изменилось
    get_resp = api.get_project(temp_project)
    assert get_resp.json()["title"] == updated_title


def test_update_project_negative_non_existent(api):
    """Негативный тест: Попытка изменить несуществующий проект."""
    fake_id = str(uuid.uuid4())
    response = api.update_project(fake_id, "New Title")
    assert response.status_code in [404, 400]
