# Автоматизация тестирования Web UI OpenCart

Проектная работа по курсу Python QA Engineer.

## Используемые технологии
* Python + pytest
* Docker
* Selenoid
* Allure

## Подготовка тестового окружения

1. Установить и активировать виртуальной окружение Python 3.8, установить зависимости:
    ```bash
    sudo apt install python3.8-venv && \
    mkdir venv && \
    python3.8 -m venv venv && \
    source venv/bin/activate && \
    pip install --upgrade pip setuptools && \
    pip install -r requirements.txt
    ```
2. [Установить Docker](https://docs.docker.com/engine/install/ubuntu/).
3. [Установить и запустить Selenoid](https://aerokube.com/selenoid/latest/#_quick_start_guide).
    ```bash
    cm selenoid update
    cm selenoid-ui update
    ```
4. [Установить Allure](https://docs.qameta.io/allure/#_installing_a_commandline).

## Тестирование и отчеты

1. Запустить тесты:
    ```bash
    pytest -v --alluredir=allure-reports
    ```
2. Сгенерировать отчет и показать его в браузере:
    ```bash
    allure serve allure-reports
    ```