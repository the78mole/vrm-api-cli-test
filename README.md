# VRM API CLI Tool

Eine kleine CLI-Applikation in Python, die auf die Victron VRM-API zugreift und für alle Installationen den State of Charge (SOC) ausgibt.

## Installation

### Option 1: Installation mit `uv` (empfohlen)

```bash
# Tool global installieren
uv tool install git+https://github.com/the78mole/vrm-api-cli-test.git

# Oder lokal aus dem Repository
git clone <repository-url>
cd vrm-api-cli-test
uv tool install .
```

Nach der Installation ist das `vrm-cli` Command global verfügbar.

### Option 2: Manuelle Installation

1. Repository klonen:
```bash
git clone <repository-url>
cd vrm-api-cli-test
```

2. Python-Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

## Konfiguration

1. Umgebungsvariablen einrichten:
```bash
cp env.tmpl .env
```

2. VRM Token in `.env` eintragen:
   - Gehe zu https://vrm.victronenergy.com/
   - Erstelle ein Personal Access Token (PAT)
   - Füge den Token in die `.env` Datei ein

## Verwendung

### Nach Installation mit `uv tool install`:
```bash
vrm-cli
```

### Bei manueller Installation:
```bash
python vrm_cli.py
```

oder (wenn ausführbar):
```bash
./vrm_cli.py
```

Das Tool wird:
- Alle Installationen von deinem VRM Account abrufen
- Den aktuellen SOC (State of Charge) für jede Installation anzeigen

## Beispiel-Ausgabe

```
============================================================
Victron VRM API - State of Charge (SOC) Report
============================================================

Fetching installations...
Found 2 installation(s)

Installation: Mein Zuhause (ID: 12345)
  SOC: 85%

Installation: Wohnmobil (ID: 67890)
  SOC: 72%

============================================================
```

## Dateien

- `vrm_api_cli/` - Python Package
  - `cli.py` - Hauptlogik
  - `__init__.py` - Package Initialisierung
- `vrm_cli.py` - Wrapper für direkte Ausführung
- `pyproject.toml` - Package Konfiguration
- `requirements.txt` - Python-Abhängigkeiten
- `env.tmpl` - Vorlage für Umgebungsvariablen
- `.env` - Deine persönlichen Umgebungsvariablen (nicht im Repo)

## Hinweise

- Die `.env` Datei wird nicht ins Repository eingecheckt (siehe `.gitignore`)
- Teile deinen VRM Token niemals mit anderen
- Das Tool benötigt Python 3.8 oder höher
