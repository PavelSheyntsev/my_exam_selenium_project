import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.mac_book_page import MacBookPage
from pages.mac_book_pro_page import MacBookProPage
from pages.main_page import MainPage
from pages.pound_page import PoundPage


def test_buy_mac_pro(set_up):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    main_page = MainPage(driver)
    main_page.select_mac_menu()

    mac_page = MacBookPage(driver)
    mac_page.select_mac_pro()

    mac_pro_page = MacBookProPage(driver)
    mac_pro_page.select_options()

    pound_page = PoundPage(driver)
    pound_page.add_poud_to_cart()

    driver.quit()
