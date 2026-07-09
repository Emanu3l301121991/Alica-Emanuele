# Alica & Emanuele — Sito delle foto del matrimonio

Sito elegante dove gli invitati **vedono e scaricano** le foto. È un sito statico (gratis, veloce),
con queste novità:

- **Le foto compaiono da sole**: basta metterle nella cartella `photos/` su GitHub, senza scrivere nessun elenco.
- **Immagine di copertina** all'inizio (`cover.jpg`).
- **Due lingue**: Italiano / Tedesco, con il pulsante IT / DE in alto.
- **Ottimizzato per il cellulare**: galleria a griglia, foto a tutto schermo, swipe con il dito.

## File nella cartella
- `index.html` — il sito
- `cover.jpg` — immagine di copertina (sostituitela con la vostra)
- `ridimensiona-foto.py` — script per alleggerire le 500 foto prima di caricarle
- `photos/` — le foto (dentro ci sono 3 esempi)
- `photos.json` — serve solo per l'anteprima locale, online si ignora

---

## PASSO 1 — Alleggerire le foto (importante!)
500 foto originali pesano diversi GB e superano i limiti di GitHub.
Prima vanno rimpicciolite (restano bellissime, ma leggere): da MB a ~300–600 KB l'una.

Modo semplice, senza programmare — scegliete uno:
- **Windows:** installate *Microsoft PowerToys* (gratis) → poi clic destro sulle foto selezionate → **Ridimensiona immagini** → scegliete ~2000 px.
- **Mac:** aprite le foto in *Anteprima* → selezionatele → menu *Strumenti → Regola dimensioni* → 2000 px lato lungo → esporta in JPEG.

Modo con lo script (fa tutto in automatico):
1. Installate Python da https://www.python.org (spuntate "Add to PATH").
2. Nella cartella, aprite il Terminale ed eseguite `pip install pillow`.
3. Mettete tutte le foto originali in una cartella `originali/` accanto allo script.
4. Eseguite `python ridimensiona-foto.py` → le foto pronte finiscono in `photos/`.

## PASSO 2 — Impostare il vostro repository
Aprite `index.html` con un editor di testo e, in cima, modificate **solo** queste righe:

```js
const CONFIG = {
  user:   "vostro-username-github",   // il vostro nome utente GitHub
  repo:   "foto-matrimonio",          // il nome del repository
  branch: "main",
  folder: "photos",
  cover:  "cover.jpg",
  data:   "13 Settembre 2025"         // la vostra data (appare sotto i nomi)
};
```

## PASSO 3 — Pubblicare su GitHub Pages (gratis)
1. Su https://github.com create un repository **Public** con lo stesso nome messo in `repo`.
2. Caricate: `index.html`, `cover.jpg` e la cartella `photos/` (**Add file → Upload files → Commit**).
3. Aprite **Settings → Pages**, alla voce *Branch* scegliete `main` e `/ (root)`, poi **Save**.
4. Dopo ~1 minuto avrete il link pubblico, es. `https://vostro-username.github.io/foto-matrimonio/`.
5. Inviatelo agli invitati. Fatto!

## Aggiungere altre foto (in qualsiasi momento)
Caricate le nuove immagini nella cartella `photos/` del repository e **Commit**.
Compaiono sul sito **da sole**, senza toccare altro.

---

## Note utili
- Gli invitati possono solo guardare e scaricare: non possono modificare o cancellare nulla.
- Il pulsante **"Scarica tutte"** crea un unico file `.zip` con tutte le foto.
- Nomi delle foto: evitate spazi e accenti (es. `cerimonia-01.jpg`), così vanno sempre bene.
- Il sito ordina le foto per nome: numeratele (01, 02, 03…) per avere l'ordine che volete.
