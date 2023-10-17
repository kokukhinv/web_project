from pages.login_page import LoginPage
from pages.locators import *
from selenium.webdriver.support.select import Select


class MainPage(LoginPage):

    def open_product_card(self):
        self.browser.find_element(*MainPageLocators.BACKPACK_CARD).click()

    def should_be_cart_button(self):
        assert self.is_element_present(*MainPageLocators.CART_BUTTON)

    def change_sort_from_high_to_low(self):
        select_element = self.browser.find_element(*MainPageLocators.SORT_DROPDOWN)
        select = Select(select_element)
        select.select_by_value('hilo')

        assert self.browser.find_element(*MainPageLocators.HIGHEST_PRICE_ITEM_PRICE).text == '$49.99'

    def logout_from_burger_menu_main_page(self):
        self.browser.find_element(*MainPageLocators.LOGOUT_BUTTON).click()

    def activate_burger_menu(self):
        self.browser.find_element(*MainPageLocators.BURGER_MENU).click()
