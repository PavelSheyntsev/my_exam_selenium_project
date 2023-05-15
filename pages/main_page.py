from datetime import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from loguru import logger

from base.base_class import Base


class MainPage(Base):
    logger.add(f"logs/logs-{datetime.now().date()}.log")

    url = 'https://pitergsm.ru/'

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

    XPATH_MAC = "//a[@class='sh-menu__link imac']"

    # getters

    def get_mac_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_MAC)))

    # actions

    def click_mac_button(self):
        self.highlight(self.get_mac_button())
        self.get_mac_button().click()
        logger.info("Click mac button")

    # methods

    def select_mac_menu(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_mac_button()
        self.get_screenshot()
        self.assert_url("https://pitergsm.ru/catalog/tablets-and-laptops/mac/")
