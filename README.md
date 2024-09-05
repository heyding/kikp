# WebApp - Kicker Interactive Kaderplaner


Dies ist eine Webanwendung, die mit Flask entwickelt wurde. Diese Anleitung beschreibt, wie Sie die Anwendung lokal auf Ihrem Rechner starten können.

## Voraussetzungen

Stellen Sie sicher, dass die folgenden Softwarekomponenten auf Ihrem Rechner installiert sind:

- Python 3.6 oder höher
- pip (Python Paketmanager)
- virtualenv (optional, aber empfohlen)

## Installation

1. **Repository klonen**:

   ```sh
   git clone https://github.com/heyding/kikp.git
   cd kikp
   ```

2. **Virtuelle Umgebung erstellen und aktivieren (optional, aber empfohlen)**:

    ```
    python -m venv venv
    source venv/bin/activate  
    
    # Auf Windows: venv\Scripts\activate
    ```

3. **Abhängigkeiten installieren**:

    ```
    pip install -r requirements.txt
    ```

4. **Umgebungsvariablen konfigurieren**:

    Erstellen Sie eine .env-Datei im Stammverzeichnis des Projekts und fügen Sie die folgenden Zeilen hinzu:

    ```
    FLASK_ENV=development
    ```

## Daten vorbereiten

Stellen Sie sicher, dass die Datei "data/2024_25_merged_players.json" im richtigen Verzeichnis vorhanden ist. Diese Datei enthält die Daten, die von der Anwendung verwendet werden.

1. **Flask-Anwendung starten**:

    ```
    flask run
    ```

    Die Anwendung wird standardmäßig unter http://127.0.0.1:5000/ verfügbar sein.

## Verwendung

Öffnen Sie Ihren Webbrowser und navigieren Sie zu http://127.0.0.1:5000/, um die Anwendung zu verwenden.

## Deployment

Für das Deployment in einer Produktionsumgebung setzen Sie die Umgebungsvariable FLASK_ENV auf production und verwenden Sie einen WSGI-Server wie Gunicorn:

```
export FLASK_ENV=production
gunicorn -c gunicorn_config.py app:app
```

## Fehlerbehebung

Falls Sie auf Probleme stoßen, überprüfen Sie die folgenden Punkte:

- Stellen Sie sicher, dass alle Abhängigkeiten korrekt installiert sind.
- Überprüfen Sie, ob die Datei data/2024_25_merged_players.json vorhanden ist und die richtigen Daten enthält.
- Stellen Sie sicher, dass die Umgebungsvariablen korrekt gesetzt sind.