              Automatizované testy Seznam.cz pomocí Playwright a Pytest

Projekt obsahuje automatizované UI testy webu Seznam.cz napsané v Pythonu s využitím frameworků Playwright a Pytest.

TESTY OVĚŘUJÍ:

1. Otevření domovské stránky Seznam.cz
2. Nastavení cookies
3. Otevření okna pro přihlášení do emailu 
4. Přechod na službu Mapy.com
5. Vyhledávání na stránce
   


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
