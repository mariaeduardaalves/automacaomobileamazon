import time

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_pesquisar_produto():

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


    def test_pesquisar_produto_valido(self):
        # As pesquisa válidas devem exibir o botão de filtros

        campo_pesquisa1 = self.driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/chrome_search_hint_view")
        campo_pesquisa1.click()
        time.sleep(3)
        #WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,"com.amazon.mShop.android.shopping:id/rs_search_src_text")))
        campo_pesquisa2 = self.driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/rs_search_src_text")
        campo_pesquisa2.send_keys("Sapato feminino")

        sugestao1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"sapato feminino\").instance(0)")
        sugestao1.click()
        sugestao1.click()

        assert WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AppiumBy.XPATH,"//android.widget.Button[@text='Filters']" )))


    def test_pesquisar_produto_invalido(self):
        # As pesquisa inválidas não devem exibir o botão de filtros e é exibida uma mensgem

        msgEsperada = "Check each product page for other buying options."

        campo_pesquisa1 = self.driver.find_element(by=AppiumBy.ID,value="com.amazon.mShop.android.shopping:id/chrome_search_hint_view")
        campo_pesquisa1.click()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AppiumBy.ID,"com.amazon.mShop.android.shopping:id/rs_search_src_text")))

        campo_pesquisa2 = self.driver.find_element(by=AppiumBy.ID,value="com.amazon.mShop.android.shopping:id/rs_search_src_text")
        campo_pesquisa2.send_keys("B0BQZJ6HYY")

        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((AppiumBy.ID, "com.amazon.mShop.android.shopping:id/rs_search_src_text"),"B0BQZJ6HYY"))
        self.driver.press_keycode(66)

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Check each product page for other buying options.\")")))

        msg = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Check each product page for other buying options.\")")
        msg = msg.text

        assert msgEsperada == msg
