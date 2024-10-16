from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Configurar las opciones del navegador
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--use-fake-ui-for-media-stream")

# Inicializar el WebDriver con las opciones configuradas
driver = webdriver.Edge(options=edge_options)

try:
    url = "http://localhost:3000/"
    num_doc = ''
    driver.get(url)
    driver.maximize_window()

    # Esperar a que el select esté disponible y seleccionar el tipo de ID
    select_tipo_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/select'))
    )
    Select(select_tipo_id).select_by_value('cc')

    # Esperar a que el input esté disponible y enviar el número de documento
    input_num_doc = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input'))
    )
    input_num_doc.send_keys(num_doc)

    # Esperar a que el botón siguiente esté disponible y hacer clic
    boton_siguiente = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/button"))
    )
    boton_siguiente.click()

    # Esperar a que el botón de foto esté disponible y hacer clic
    boton_foto = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/button"))
    )
    time.sleep(10)
    boton_foto.click()

except TimeoutException:
    print("Un elemento no se cargó a tiempo.")
finally:
    # Cerrar el navegador
    time.sleep(5)
    driver.quit()
