import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginTests(unittest.TestCase):
    
    def setUp(self):
        """Configuración del entorno de prueba (Boundary Environment API 31)"""
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.app_package = ""
        options.app_activity = ""
        options.no_reset = True
        
        self.driver = webdriver.Remote("", options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def saltar_onboarding(self):
        """Función auxiliar para navegar las pantallas de bienvenida de una app limpia"""
        # 1. Clic en Omitir intro
        xpath_omitir = '//*[contains(@text, "Omitir intro")]'
        btn_omitir = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_omitir)))
        btn_omitir.click()
        
        # 2. Clic en el primer botón de Iniciar Sesión (Pantalla de la chica)
        xpath_iniciar_bienvenida = '//*[contains(@text, "Iniciar sesi")]'
        btn_iniciar_bienvenida = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_iniciar_bienvenida)))
        btn_iniciar_bienvenida.click()
        
        time.sleep(1) # Pequeña pausa para que termine la animación de transición

    def test_login_01_happy_path(self):
        """TC-002: Validar inicio de sesión exitoso (Happy Path)"""
        self.saltar_onboarding() 
        
        xpath_email = '(//android.widget.EditText)[1]'
        xpath_password = '(//android.widget.EditText)[2]'
        xpath_btn_login = '//*[contains(@text, "Iniciar")]'

        input_email = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_email)))
        input_email.click()
        input_email.clear()
        input_email.send_keys("ejemplo@gmail.com")

        input_password = self.driver.find_element(AppiumBy.XPATH, xpath_password)
        input_password.click()
        input_password.clear()
        input_password.send_keys("1350.test") 

        if self.driver.is_keyboard_shown():
            self.driver.hide_keyboard()

        btn_login = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_btn_login)))
        btn_login.click()

        # Validamos que desaparezca el botón, indicando éxito
        login_exitoso = self.wait.until(EC.invisibility_of_element((AppiumBy.XPATH, xpath_btn_login)))
        self.assertTrue(login_exitoso, "El inicio de sesión falló o la pantalla no transicionó.")


    def test_login_02_unregistered_user(self):
        """TC-003: Validar manejo de errores con usuario no registrado (Negative Test)"""
        self.saltar_onboarding() 
        
        xpath_email = '(//android.widget.EditText)[1]'
        xpath_password = '(//android.widget.EditText)[2]'
        xpath_btn_login = '//*[contains(@text, "Iniciar")]'

        input_email = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_email)))
        input_email.click()
        input_email.clear()
        input_email.send_keys("otroejemplo@gmail.com")

        input_password = self.driver.find_element(AppiumBy.XPATH, xpath_password)
        input_password.click()
        input_password.clear()
        input_password.send_keys("50502.Ejemplo") 

        if self.driver.is_keyboard_shown():
            self.driver.hide_keyboard()

        btn_login = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_btn_login)))
        btn_login.click()

         xpath_error_msg = '//*[contains(@text, "Usuario o contraseña incorrectos")]'

    def tearDown(self):
        """Limpieza de estado (Idempotencia) a nivel de OS"""
        self.driver.execute_script('mobile: clearApp', {'appId': ''})
        
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()