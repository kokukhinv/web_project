from pages.login_page import LoginPage
from pages.main_page import MainPage
from data_generator import *

login_page_link = 'https://www.saucedemo.com/'


def test_login_with_correct_credentials(browser):
    data = get_right_login_data()
    page = LoginPage(browser, login_page_link, 5)
    page.open()
    page.fill_out_login_form(**data)


def test_login_with_incorrect_credentials(browser):
    data = get_wrong_login_data()
    page = LoginPage(browser, login_page_link, 5)
    page.open()
    page.fill_out_login_form(**data)
    page.should_be_warning_message()


def test_open_product_card_backpack(browser):
    data = get_right_login_data()
    page = MainPage(browser, login_page_link, 5)
    page.open()
    page.fill_out_login_form(**data)
    page.open_product_card()


def test_sort_items_from_high_to_low(browser):
    data = get_right_login_data()
    page = MainPage(browser, login_page_link, 5)
    page.open()
    page.fill_out_login_form(**data)
    page.change_sort_from_high_to_low()


def test_logout_from_main_page(browser):
    data = get_right_login_data()
    page = MainPage(browser, login_page_link, 5)
    page.open()
    page.fill_out_login_form(**data)
    page.activate_burger_menu()
    page.logout_from_burger_menu_main_page()
    page.should_be_login_form()
