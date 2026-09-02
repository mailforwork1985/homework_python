# Lesson 10 — PageObject + Allure (SauceDemo)

Автотест для магазина SauceDemo с применением паттерна Page Object
и генерацией Allure-отчётов. Браузер — Firefox.

## Структура проекта

```
lesson_10/
├── pages/
│   └── shop_page.py        # Page Object: MainShopPage и CartPage
├── tests/
│   └── test_sauce_shop.py  # Тест с Allure-шагами и декораторами
├── conftest.py             # Фикстура WebDriver (Firefox)
├── requirements.txt        # Зависимости
└── readme.md
```

## Установка

1. Установить Python 3.10+.

2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Убедиться, что в системе установлен Mozilla Firefox
   (Selenium Manager скачает GeckoDriver автоматически).

## Запуск тестов

### Обычный запуск

```bash
pytest tests/test_sauce_shop.py
```

### Запуск с формированием Allure-отчёта

```bash
pytest tests/test_sauce_shop.py --alluredir=allure-results
```

После выполнения в папке `allure-results/` появятся файлы с результатами.

## Просмотр отчёта

### Локальный сервер Allure

```bash
allure serve allure-results
```

Allure поднимёт локальный веб-сервер и откроет отчёт в браузере.

### Статический HTML-отчёт

```bash
allure generate allure-results -o allure-report --clean
```

Откройте файл `allure-report/index.html` в браузере.

## Примечание

- Папки `allure-results/` и `allure-report/` в репозиторий не пушить
  (добавить в `.gitignore` или оставить пустыми).
- В тесте используется фиксированный набор товаров и ожидаемая сумма $58.29.