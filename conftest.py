# import pytest
#
# from datetime import datetime
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
#
#
#
# # HEADLESS = True  # режим браузера без отображения (безголовый)
# CHROME_WINDOW_SIZES = "--window-size=1920,1080"
#
# test_browser = ""
#
#
# @pytest.fixture(
#     scope="class",
#     params=[
#         "standard_user",
#     ],
# )
# def cur_login(request):
#     """Fixture"""
#     print(f"Current login - {request.param}")
#     return request.param
#
#
# @pytest.fixture(
#     scope="class",
#     params=[
#         "secret_sauce",
#     ],
# )
# def cur_password(request):
#     """Fixture"""
#     print(f"Current login - {request.param}")
#     return request.param
#
#
# def pre_go(fixture_value):
#     global test_browser
#     test_browser = fixture_value
#     return None
#
#
# @pytest.fixture(
#     scope="module",
#     params=[
#         "chrome",
#         # "firefox",
#     ],
#     autouse=True,
#     ids=pre_go,
# )
# def go(request, d):
#     """Start execution program"""
#     print(request.param)
#     # d.get(conf.URL)
#
#     yield d
#
#     d.quit()
#     print("\n*** end fixture = teardown ***\n")
#
#
# @pytest.fixture()
# def cur_time():
#     """Fixture"""
#     return str(datetime.now())
#
#
# # @pytest.fixture(scope="module")
# # # def d(browser):
# # def d():
# #     """WebDriver Initialization"""
# #     global test_browser
# #     browser = test_browser
# #     driver = None
# #     if browser == "chrome":
# #         driver = init_remote_driver_chrome()
# #     # elif browser == "firefox":
# #     #     driver = init_remote_driver_firefox()
# #     else:
# #         print('Please pass the correct browser name: {}'.format(browser))
# #         raise Exception('driver is not found')
# #     return driver
# #
# #
# # def init_remote_driver_chrome():
# #     chrome_options = webdriver.ChromeOptions()
# #     chrome_options.page_load_strategy = "eager"
# #     chrome_options.add_argument(conf.CHROME_WINDOW_SIZES)
# #
# #     # Код, отмены информационного сообщения "USB: usb_device_handle_win.cc"
# #     chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# #     chrome_options.add_argument("--accept-lang=en")
# #
# #     # безголовый режим задается переменной headless в самом начале текущего модуля
# #     if conf.HEADLESS:
# #         chrome_options.add_argument(conf.CHROMIUM_HEADLESS)
# #
# #     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# #
# #     print(driver.get_window_size())
# #     driver.implicitly_wait(4)
# #     return driver
