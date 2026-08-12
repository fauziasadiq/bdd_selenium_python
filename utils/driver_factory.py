
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def create_driver(browser, headless=False):
    if browser.lower() == "chrome":
        options = Options()
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False  # Disable leak detection
        })
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")

        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    raise Exception(f"Browser {browser} not supported")
