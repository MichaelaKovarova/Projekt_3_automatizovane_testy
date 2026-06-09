              Automatizované testy Seznam.cz pomocí Playwright a Pytest

Projekt obsahuje automatizované UI testy webu Seznam.cz napsané v Pythonu s využitím frameworků Playwright a Pytest.

TESTY OVĚŘUJÍ:

1. Otevření domovské stránky Seznam.cz
2. Nastavení cookies
3. Přechod na službu Mapy.com
4. Vyhledávání na stránce
5. Funkčnost tlačítka pro návrat na začátek stránky (scroll up)


POŽADAVKY 
Python 3.10 nebo novější, pip


INSTALACE
1. Vytvoření virtuálního prostředí

    Windows:
python -m venv venv
venv\Scripts\activate

    Linux / macOS:
python -m venv venv
source venv/bin/activate

3. Instalace závislostí
pip install -r requirements.txt

4. Instalace prohlížečů Playwright
playwright install


SPUŠTĚNÍ
python -m pytest


POUŽITÉ TECHNOLOGIE
Python,
Pytest,
Playwright
