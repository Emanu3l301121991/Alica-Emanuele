#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ridimensiona e alleggerisce le foto per il sito del matrimonio.

A cosa serve:
  500 foto originali possono pesare diversi GB e superare i limiti di GitHub.
  Questo script crea copie piu' leggere (lato lungo 2000px, qualita' 82%):
  di solito ogni foto passa da alcuni MB a circa 300-600 KB.
  500 foto -> di solito 150-350 MB in totale, comode su GitHub.

Come si usa (una volta sola serve installare Pillow):
  1) Installare Python da https://www.python.org (spuntare "Add to PATH").
  2) Aprire il Prompt/Terminale nella cartella di questo file ed eseguire:
        pip install pillow
  3) Mettere TUTTE le foto originali in una cartella chiamata "originali"
     (accanto a questo script), poi eseguire:
        python ridimensiona-foto.py
  4) Le foto pronte finiscono nella cartella "photos".
     Caricate SOLO la cartella "photos" (e cover.jpg, index.html) su GitHub.

Opzioni (facoltative):
  python ridimensiona-foto.py --input MIA_CARTELLA --output photos --max 2000 --quality 82
"""

import argparse, os, sys
try:
    from PIL import Image, ImageOps
except ImportError:
    print("Manca la libreria Pillow. Installala con:  pip install pillow")
    sys.exit(1)

ESTENSIONI = (".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp", ".heic")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="originali", help="cartella con le foto originali")
    ap.add_argument("--output", default="photos", help="cartella di destinazione")
    ap.add_argument("--max", type=int, default=2000, help="lato lungo massimo in pixel")
    ap.add_argument("--quality", type=int, default=82, help="qualita' JPEG 1-100")
    a = ap.parse_args()

    if not os.path.isdir(a.input):
        print(f'Cartella "{a.input}" non trovata. Mettici dentro le foto originali e riprova.')
        sys.exit(1)
    os.makedirs(a.output, exist_ok=True)

    files = [f for f in sorted(os.listdir(a.input)) if f.lower().endswith(ESTENSIONI)]
    if not files:
        print(f'Nessuna immagine trovata in "{a.input}".')
        sys.exit(1)

    print(f"Trovate {len(files)} foto. Elaboro...\n")
    tot_in = tot_out = ok = 0
    for i, name in enumerate(files, 1):
        src = os.path.join(a.input, name)
        base = os.path.splitext(name)[0]
        dst = os.path.join(a.output, base + ".jpg")
        try:
            im = Image.open(src)
            im = ImageOps.exif_transpose(im)      # raddrizza secondo l'orientamento della foto
            im = im.convert("RGB")
            im.thumbnail((a.max, a.max), Image.LANCZOS)
            im.save(dst, "JPEG", quality=a.quality, optimize=True, progressive=True)
            si = os.path.getsize(src); so = os.path.getsize(dst)
            tot_in += si; tot_out += so; ok += 1
            print(f"[{i}/{len(files)}] {name}  {si//1024} KB -> {so//1024} KB")
        except Exception as e:
            print(f"[{i}/{len(files)}] SALTATA {name}: {e}")

    mb = lambda b: b / (1024*1024)
    print("\n--- Fatto ---")
    print(f"Foto elaborate: {ok}/{len(files)}")
    print(f"Peso totale: {mb(tot_in):.0f} MB -> {mb(tot_out):.0f} MB")
    print(f'Le foto pronte sono nella cartella "{a.output}". Ora caricatela su GitHub.')

if __name__ == "__main__":
    main()
