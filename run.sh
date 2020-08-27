#!/bin/bash

rm -rf allure-*

if [[ -n "$(ls -A ~/.aerokube/selenoid/logs)" ]]; then
    sudo rm ~/.aerokube/selenoid/logs/*
fi
if [[ -n "$(ls -A ~/.aerokube/selenoid/video)" ]]; then
    sudo rm ~/.aerokube/selenoid/video/*
fi

pytest -v --alluredir=allure-report

allure serve allure-report
