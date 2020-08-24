from time import sleep

import allure
import pytest


class TestMainPage:

    @pytest.mark.parametrize(
        argnames="currency",
        argvalues=[("EUR", "€"), ("GBP", "£"), ("USD", "$")],
        ids=["Set currency: €", "Set currency: £", "Set currency: $"]
    )
    @allure.title("Check new currency has been applied")
    @allure.story("Main page")
    def test_change_currency(self, main_page, currency):
        with allure.step("Set new currency"):
            main_page.change_currency(new_currency=currency[0])
        sleep(3)
        with allure.step("Check new currency has been applied"):
            assert main_page.get_current_currency() == currency[1]
    #

    @allure.title("Check My Account links")
    @allure.story("Main page")
    def test_open_my_account_dropdown(self, main_page):
        with allure.step("Open My Account dropdown list"):
            main_page.open_my_account_dropdown()
        with allure.step("Check Register and Login links"):
            assert main_page.find_element(locator=main_page.A_REGISTER)
            assert main_page.find_element(locator=main_page.A_LOGIN)
    #

    @allure.title("Check product added to cart")
    @allure.story("Main page")
    def test_product_added_to_cart(self, main_page):
        with allure.step("Check cart is empty"):
            assert main_page.is_cart_empty()
        with allure.step("Click add to cart button"):
            main_page.add_to_cart()
        with allure.step("Check product added to cart"):
            main_page.check_product_added_to_cart()
#
