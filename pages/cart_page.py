import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from loguru import logger

from base.base_class import Base


class CartPage(Base):

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

    XPATH_PRICE = "//*[@id='total-summ-place']"

    # getters

    def get_price(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_PRICE))).text
        logger.info(f'Pound price - {element}')
        return element

    # methods
    def check_price(self):
        self.assert_url("https://pitergsm.ru/personal/cart/")
        self.assert_word(self.get_price(), "169 190")
