from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_pesquisar_custumer_service():

    def setup_method(self):
        # Configuração do driver antes de cada teste
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:automationName": "uiautomator2",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        })

        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


    def test_pesquisar_custumer_service_valido(self):

        menu4 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Browse menu Tab 4 of 4")
        menu4.click()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Customer Service\")")))

        select_custumer_service = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Customer Service\")")
        select_custumer_service.click()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME,"android.widget.EditText")))

        pesquisar = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
        pesquisar.click()

        pesquisar.send_keys("Where's My Stuff?")
        self.driver.press_keycode(66)

        assert WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Help Search Results\")")))


    def test_pesquisar_custumer_service_invalido(self):

        texto = 'No results match your search for "produts" in Amazon.com Help.'

        menu4 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Browse menu Tab 4 of 4")
        menu4.click()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("cs")')))

        select_custumer_service = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().text(\"Customer Service\")")
        select_custumer_service.click()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText")))

        pesquisar = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
        pesquisar.click()

        pesquisar.send_keys("produts")
        self.driver.press_keycode(66)

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.webkit.WebView[@text="Amazon"]/android.view.View/android.view.View/android.widget.TextView')))

        resultado_pesquisa_invalida = self.driver.find_element(AppiumBy.XPATH, '//android.webkit.WebView[@text="Amazon"]/android.view.View/android.view.View/android.widget.TextView').text

        assert texto == resultado_pesquisa_invalida