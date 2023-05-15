import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from loguru import logger

from base.base_class import Base


class PoundPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # highlight elements

    def highlight(self, element):
        driver = self.driver
        effect_time = 0.3
        colors = ["red", "skyblue", "lightgreen"]
        border = 4

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)

        original_style = element.get_attribute('style')
        for color in colors:
            apply_style("border: {0}px solid {1};".format(border, color))
            time.sleep(effect_time)
        apply_style(original_style)

    # locators

    XPATH_BUY_BUTTON_1 = "/html/body/div[1]/main/div/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/a[2]"
    XPATH_BUY_BUTTON_2 = "//*[@id='bx_basketFKauiIproducts']/div[3]/a[1]"

    # getters

    def get_buy_button_1(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_BUY_BUTTON_1)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_buy_button_2(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_BUY_BUTTON_2)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    # actions
    def click_buy_button_1(self):
        self.highlight(self.get_buy_button_1())
        self.get_buy_button_1().click()
        logger.info("Click RAM checkbox")

    def click_buy_button_2(self):
        self.highlight(self.get_buy_button_2())
        self.get_buy_button_2().click()
        logger.info("Click RAM checkbox")

    # methods
    def add_poud_to_cart(self):
        self.click_buy_button_1()
        self.click_buy_button_2()
        self.assert_url("https://pitergsm.ru/personal/cart/")
