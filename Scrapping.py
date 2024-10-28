from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Configura el WebDriver (ajusta la ruta del WebDriver si es necesario)
driver = webdriver.Chrome()
driver.get("http://butedock.com/cgs/rank.php")

# Cambiar "Show Peeling Information" a False
peel_false_radio = driver.find_element(By.XPATH, '//input[@name="show_peel" and @value="no_peel"]')
peel_false_radio.click()

# Cambiar "Show Grip Type" a True
grip_true_radio = driver.find_element(By.XPATH, '//input[@name="show_grip" and @value="grip"]')
grip_true_radio.click()

# Seleccionar el año 2023
year_select = Select(driver.find_element(By.NAME, "year"))
year_select.select_by_visible_text("2023")

# Cambiar "Min Games" a 1
min_games_input = driver.find_element(By.NAME, "games")
min_games_input.clear()
min_games_input.send_keys("1")

# Cambiar "Min Grade" a 1000
min_grade_input = driver.find_element(By.NAME, "grade")
min_grade_input.clear()
min_grade_input.send_keys("1000")

# Espera un momento para asegurarse de que los cambios se registran
time.sleep(1)

# Encuentra y haz clic en el botón "Submit"
submit_button = driver.find_element(By.XPATH, '//input[@type="submit" and @value="Submit"]')
submit_button.click()

# Espera a que la nueva página cargue completamente
time.sleep(3)  # Ajusta el tiempo según la velocidad de carga de la página

# Extrae la información de la tabla
rows = driver.find_elements(By.XPATH, '//table//tr')
data = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    cell_data = [cell.text for cell in cells]
    if cell_data:  # Evita filas vacías
        data.append(cell_data)

# Convertir a un DataFrame (opcional)
import pandas as pd
column_names = ["Num", "Name", "Country", "DGrade", "pdt", "Games", "Wins", "%wins", "Grip", "Last"]
df = pd.DataFrame(data,columns = column_names)
print(df)
df.to_csv("CroquetGC.csv",index=False)

# Cierra el navegador
driver.quit()
