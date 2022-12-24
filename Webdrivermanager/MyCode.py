from webdrivermanager.chrome import ChromeDriverManager
from webdrivermanager.gecko import GeckoDriverManager


def get_driver_path_with_browser(browser_name):
    if browser_name.lower() == 'chrome':
        driver_path = ChromeDriverManager().install()
    elif browser_name.lower() == 'firefox':
        driver_path = GeckoDriverManager().install()
    print(driver_path)
    return driver_path
