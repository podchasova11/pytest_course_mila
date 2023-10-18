from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


@pytest.fixture()
def cur_time():
    return str(datetime.now())

@pytest.mark.autorizations
class Authorization:
    page_conditions = None

    @allure.step("Start test of button [Log in] in the Header")
    def test_01_button_login(
            self, d, cur_login):
        """
        Check: Button [Log In]
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем Aut")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.03", "Education > Menu item [Trend Trading]",
                             "01", "Testing button [Log In] in the Header")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link)

def test_auth():
    driver.get("https://www.saucedemo.com/")
    before_url = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(3)

    logout = driver.find_element(By.ID, 'about_sidebar_link')
    logout.click()
    time.sleep(1)

    after_url = driver.current_url

    assert after_url != before_url
    assert after_url == 'https://saucelabs.com/'

    driver.quit()