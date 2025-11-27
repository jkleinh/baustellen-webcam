# webcam_dummy.py

import time
from datetime import datetime
from pathlib import Path
from ftplib import FTP

from PIL import Image, ImageFilter
#Hier ein kommentar!
import config


def ensure_dirs():
    config.BASE_DIR.mkdir(parents=True, exist_ok=True)
    config.ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)


def make_archive_image(dummy_source: Path) -> Path:
    """Dummybild ins Archiv kopieren (als wäre es ein Kamera-Shot)."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target = config.ARCHIVE_DIR / f"baustelle_{timestamp}.jpg"
    img = Image.open(dummy_source)
    img.save(target, quality=90)
    return target


def apply_blur_region(path: Path):
    """Festen Bildbereich blurren (Simu Kindergarten)."""
    x, y, w, h = config.BLUR_REGION
    if w <= 0 or h <= 0:
        return

    img = Image.open(path)
    box = (x, y, x + w, y + h)
    region = img.crop(box)
    region = region.filter(ImageFilter.GaussianBlur(radius=25))
    img.paste(region, box)
    img.save(path, quality=90)


def save_live_image(archive_file: Path):
    """Archivbild als current.jpg speichern."""
    img = Image.open(archive_file)
    img.save(config.LIVE_IMAGE, quality=85)


def upload_via_ftp(local_file: Path):
    """current.jpg per FTP hochladen (wenn aktiviert)."""
    if not config.FTP_ENABLED:
        return

    try:
        with FTP(config.FTP_HOST, timeout=20) as ftp:
            ftp.login(config.FTP_USER, config.FTP_PASSWORD)
            with open(local_file, "rb") as f:
                ftp.storbinary(f"STOR " + config.FTP_REMOTE_PATH, f)
        print(f"[FTP] Upload ok: {config.FTP_REMOTE_PATH}")
    except Exception as e:
        print(f"[FTP] Fehler: {e}")


def main_loop():
    dummy_source = Path("/home/jan/baustellen-webcam/test_dummy.jpg")
    if not dummy_source.exists():
        raise FileNotFoundError(f"Dummybild nicht gefunden: {dummy_source}")

    ensure_dirs()
    print("Dummy-Webcam-Loop gestartet. Strg+C zum Beenden.")

    while True:
        start = time.time()
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            print(f"[{ts}] Neuer Durchlauf...")

            archive_file = make_archive_image(dummy_source)
            apply_blur_region(archive_file)
            save_live_image(archive_file)
            upload_via_ftp(config.LIVE_IMAGE)

            print(f"[{ts}] Fertig: {archive_file.name}")
        except KeyboardInterrupt:
            print("Beendet durch Benutzer.")
            break
        except Exception as e:
            print(f"[{ts}] Fehler: {e}")

        elapsed = time.time() - start
        sleep_time = max(0, config.INTERVAL_SECONDS - elapsed)
        time.sleep(sleep_time)


if __name__ == "__main__":
    main_loop()
