from pathlib import Path

# Basis-Pfade
BASE_DIR = Path("/home/jan/baustellen-webcam_data")
ARCHIVE_DIR = BASE_DIR / "archive"
LIVE_IMAGE = BASE_DIR / "current.jpg"

# Intervall in Sekunden (Standard: 10 Minuten = 600)
INTERVAL_SECONDS = 600

# Blur-Bereich (x, y, breite, höhe) – Beispielwerte.
# Für echte Nutzung im Bild ermitteln und in config.py anpassen.
BLUR_REGION = (0, 0, 0, 0)

# FTP-Konfiguration – NUR in config.py mit echten Daten befüllen!
FTP_ENABLED = False
FTP_HOST = "ftp.example.com"
FTP_USER = "ftpuser"
FTP_PASSWORD = "ftppass"
FTP_REMOTE_PATH = "/pfad/zu/current.jpg"
