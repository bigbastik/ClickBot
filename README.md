# ClickBot Selenium Automation

Script Python per l'automazione del click su un banner pubblicitario presente nel sito [https://lottobot.it](https://lottobot.it) utilizzando Selenium WebDriver con Chrome in modalità headless.

## Scopo didattico

Questo progetto è realizzato esclusivamente a scopo didattico per mostrare come:

- utilizzare Selenium per interagire con elementi web dinamici;
- gestire click su elementi non sempre facilmente cliccabili;
- eseguire script a intervalli temporali dinamici casuali;
- gestire errori e garantire la continuità dell'esecuzione.

## Funzionamento

- Lo script apre la pagina, individua il banner tramite ID.
- Prova a cliccare su elementi interni cliccabili (link o bottoni).
- In caso di insuccesso tenta il click tramite JavaScript sul container.
- Ripete l'esecuzione a intervalli casuali tra 60 e 65 minuti (configurabile).

## Requisiti di sistema

Il requirements.txt elenca solo i pacchetti Python, ma per eseguire correttamente il tuo script serve anche:

Python 3.9 o superiore
Se non presente nella macchina:

sudo apt update
sudo apt install python3 python3-pip

Google Chrome (versione 135 o compatibile)
Se non presente:

# Su Debian/Ubuntu
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

ChromeDriver corrispondente alla versione di Chrome
Se non presente:

# Esempio: ChromeDriver 135
wget https://storage.googleapis.com/chrome-for-testing-public/135.0.7049.84/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

 ## Come installare tutto

Una volta preparato l’ambiente, basterà:

pip install -r requirements.txt

