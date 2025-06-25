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

## Requisiti

- Python 3.9+
- Google Chrome versione 135 (o compatibile)
- ChromeDriver versione corrispondente a Chrome

## Installazione

1. Clona il repository
2. Installa le dipendenze con:

```bash
pip install -r requirements.txt
