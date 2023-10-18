
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialization driver
driver = webdriver.Chrome

def test_login_form():



    driver.get("https://www.saucedemo.com/")
    login_form = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
    login_form.send_keys("standard_user")
    password_form = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
    password_form.send_keys("secret_sauce")
    submit_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    submit_button.click()


    time.sleep(5)
assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()

  def test_add_to_cart():


      driver.get("https://www.saucedemo.com/")
      login_form = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
      login_form.send_keys("standard_user")
      password_form = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
      password_form.send_keys("secret_sauce")
      submit_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
      submit_button.click()

      item_in_cart = driver.find_element(By.XPATH, 'a[@class="shopping_cart_link"]')
      item_in_cart.click()
      button_add_to_cart = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]')
      button_add_to_cart.click()
      time.sleep(5)

      button_cart = webdriver.Chrome.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
      button_cart.click()


time.sleep(5)
assert driver.current_url == "https://www.saucedemo.com/inventory.html"

driver.quit()










