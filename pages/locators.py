from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, '//*[@id="login_button_container"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    WARNING_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')


class MainPageLocators:
    BACKPACK_CARD = (By.XPATH, '//*[@id="item_4_title_link"]')
    BACKPACK_ADD_TO_CART = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    CART_BUTTON = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    SORT_DROPDOWN = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    HIGHEST_PRICE_ITEM_PRICE = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    BURGER_MENU = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
