# WEB UI OpenCart Testing Automation

Design work on the course of Python Qa Engineer.

## Used technologies
* Python + Pytest
* Docker
* Selenoid
* Allure.

## Preparing a test environment

1. Install and activate the Python 3.8 virtual environment, establish dependencies:
    `` `bash
    Sudo Apt Install Python3.8-Venv && \
    mkdir venv && \
    Python3.8 -m Venv Venv && \
    SOURCE VENV / BIN / ACTIVATE && \
    Pip Install --Upgrade Pip SetupTools && \
    Pip Install -R Requirements.txt
    `` ``
2. [Install Docker] (https://docs.docker.com/engine/install/ubuntu/).
3. [Install and run Selenoid] (https://aerokube.com/selenoid/lateest/#_quick_start_guide).
    `` `bash
    CM Selenoid Update.
    CM SELENOID-UI UPDATE
    `` ``
4. [Install Allure] (https://docs.qameta.io/allure/#_installing_a_commandline).

## Testing and Reports

1. Run tests:
    `` `bash
    pytest -v --alluredir = allure-reports
    `` ``
2. Generate a report and show it in the browser:
    `` `bash
    Allure Serve Allure-Reports
    `` ``
    
