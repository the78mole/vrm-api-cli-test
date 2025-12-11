# VRM API CLI Tool

Eine kleine CLI-Applikation in Python, die auf die Victron VRM-API zugreift und für alle Installationen den State of Charge (SOC) ausgibt.

## Installation

1. Repository klonen:
```bash
git clone <repository-url>
cd vrm-api-cli-test
```

2. Python-Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

3. Umgebungsvariablen einrichten:
```bash
cp env.tmpl .env
```

4. VRM Token in `.env` eintragen:
   - Gehe zu https://vrm.victronenergy.com/
   - Erstelle ein Personal Access Token (PAT)
   - Füge den Token in die `.env` Datei ein

## Verwendung

Führe das CLI-Tool aus:
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

- `vrm_cli.py` - Hauptanwendung
- `requirements.txt` - Python-Abhängigkeiten
- `env.tmpl` - Vorlage für Umgebungsvariablen
- `.env` - Deine persönlichen Umgebungsvariablen (nicht im Repo)

## Hinweise

- Die `.env` Datei wird nicht ins Repository eingecheckt (siehe `.gitignore`)
- Teile deinen VRM Token niemals mit anderen
