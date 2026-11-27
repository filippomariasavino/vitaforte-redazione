# Montaggio standard VITAFORTE (dal 27/11/2026, reel C01 v4)

- `monta_reel.py`: video 1080x1920, 30 fps. Immagini in duotono del brand (inchiostro #12141B, pergamena #EDE6D6), bordi di carta tagliati, zoom lenti e lineari, stacco a ogni frase. Niente intro né outro: si parte dal gancio.
- Sottotitoli parola per parola per tutta la voce: 2-3 parole per gruppo (separate con `|` nel testo delle frasi), Lora SemiBold in maiuscolo, la parola detta si ingrandisce, parole chiave (lista KEY) in oro e più grandi; al 30% dell'altezza (più in alto se il soggetto lo richiede), fascia scura leggera dietro. VITAFORTE solo nell'ultimo secondo.
- `mixa_audio.sh`: voci F01..F08 posate sui tempi, normalizzate a -16 LUFS; musica del brand circa 13-14 dB sotto la voce, sale sul passaggio chiave, tace sull'ultima frase.

Per un reel nuovo: aggiornare in `monta_reel.py` le durate (`dur`), i gruppi di parole (`chunks`, tempi dalle pause con silencedetect), le immagini (`segs`) e le parole chiave (`KEY`); in `mixa_audio.sh` gli inizi delle frasi e la durata totale.
Cartelle attese: `src/` (F01.wav..., I1.png..., musica.mp3), `fonts/` (da media/fonts).
