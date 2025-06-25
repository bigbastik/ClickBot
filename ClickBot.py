from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time
import random

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--incognito")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--window-size=1280,800")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/135.0.7049.84 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)

    try:
        url = "https://lottobot.it"
        print(f"Caricamento pagina {url}...")
        driver.get(url)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Pagina caricata correttamente.")

        banner_id = "container-85f3cda6e1437d60fa91bd3f703d844e"
        container = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, banner_id))
        )
        print(f"Trovato il container del banner con id '{banner_id}'.")

        # Scrollare fino al container per assicurarsi che sia visibile
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", container)
        time.sleep(1)  # attesa per animazioni o lazy load

        # Proviamo a trovare un link cliccabile dentro il container
        clickable_elements = container.find_elements(By.CSS_SELECTOR, "a, button")
        clicked = False
        for elem in clickable_elements:
            if elem.is_displayed() and elem.is_enabled():
                try:
                    print(f"Provo a cliccare sull'elemento: tag={elem.tag_name}, testo='{elem.text[:30]}'")
                    elem.click()
                    clicked = True
                    print("Click effettuato con successo.")
                    break
                except Exception as e:
                    print(f"Click normale fallito: {e}, provo con JavaScript")
                    try:
                        driver.execute_script("arguments[0].click();", elem)
                        clicked = True
                        print("Click effettuato via JavaScript.")
                        break
                    except Exception as e2:
                        print(f"Click via JS fallito: {e2}")

        if not clicked:
            print("Nessun elemento cliccabile trovato o click fallito, provo a cliccare sul container con JS")
            try:
                driver.execute_script("arguments[0].click();", container)
                print("Click sul container via JS effettuato.")
            except Exception as e:
                print(f"Click sul container via JS fallito: {e}")

    except Exception as e:
        print("Errore durante l'esecuzione:")
        print(e)
        traceback.print_exc()

    finally:
        driver.quit()
        print("Browser chiuso.")

def intervallo_casuale(min_minutes=60, max_minutes=65):
    minuti = random.randint(min_minutes, max_minutes)
    print(f"[INFO] Prossima esecuzione tra {minuti} minuti.")
    return minuti * 60

if __name__ == "__main__":
    while True:
        try:
            print("[INFO] Avvio esecuzione script...")
            main()
            print("[INFO] Esecuzione completata con successo.")
        except Exception as e:
            print(f"[ERROR] Errore durante l'esecuzione: {e}")
        sleep_time = intervallo_casuale(60, 65)  # intervallo dinamico in minuti
        time.sleep(sleep_time)