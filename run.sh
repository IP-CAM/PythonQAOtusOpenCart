#!/bin/bash

rm -rf allure-*

sudo rm ~/.aerokube/selenoid/logs/*
sudo rm ~/.aerokube/selenoid/video/*

pytest -v --alluredir=allure-report

allure serve allure-report

