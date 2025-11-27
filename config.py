# config.py
from pathlib import Path

# Basis-Pfade
BASE_DIR = Path("/home/jan/baustellen-webcam_data")
ARCHIVE_DIR = BASE_DIR / "archive"
LIVE_IMAGE = BASE_DIR / "current.jpg"

# Testintervall: 60 Sekunden (später 600 für 10 Minuten)
INTERVAL_SECONDS = 60

# Blur-Bereich (x, y, breite, höhe) – Beispielwerte,
# einfach mal irgendwo ins Bild „reinhauen“ zum Testen
BLUR_REGION = (500, 300, 800, 400)

# FTP-Konfiguration
FTP_ENABLED = True
FTP_HOST = "DEIN_FTP_SERVER"
FTP_USER = "DEIN_USER"
FTP_PASSWORD = "DEIN_PASSWORT"
FTP_REMOTE_PATH = "/pfad/auf/dem/server/current.jpg"
