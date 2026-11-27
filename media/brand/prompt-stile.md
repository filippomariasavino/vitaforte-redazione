# VITAFORTE – Prompt di stile per generatori di immagini

Versione del 27/11/2026 (approvata da Filippo). Sostituisce la versione seppia.

## Le 4 regole dello stile
1. **Porta e sigla**: incisione molto dettagliata (tipo Gustave Doré).
2. **Immagini dei contenuti**: incisione SEMPLIFICATA: linee nere marcate, poco tratteggio, contrasto forte, un solo soggetto chiaro, zone vuote per il testo.
3. **Colore**: inchiostro NERO su carta antica chiara (avorio leggero). Niente seppia, niente marrone, niente colori.
4. **Luce**: UNA sola fonte di luce visibile (candela, porta aperta, finestra, lanterna, raggio dall'alto); il resto in penombra.

Altre regole: nessuna scritta nell'immagine; niente volti realistici di persone vere di oggi (figure di spalle, in ombra o lontane); formato verticale 9:16; a tutta pagina, senza cornice.

Generatore: Gemini via Composio, modello `gemini-2.5-flash-image`, `aspect_ratio` 9:16 (circa 4 centesimi a immagine). Le immagini si salvano su Drive in Progetti Claude/VF_Social/01_Immagini.

---

## 1. Blocco STILE – CONTENUTI (in fondo a ogni prompt di contenuto)

```
simplified antique engraving, bold clean black ink lines, minimal sparse hatching, strong contrast, large flat areas of black and of light paper, black ink on slightly aged off-white paper, black and white, neutral grayscale, no sepia, no brown, no color, one single visible light source, the rest in deep shadow, faces not visible, vertical 9:16, full bleed edge to edge, no border, no frame, no rounded corners, no text, no letters, no watermark, no signature
```

Modello di prompt:
```
[SOGGETTO], simple composition with one clear subject, large calm empty area for text in the [upper/lower] half, [STILE CONTENUTI]
```
Esempio approvato (VF_studioso_semplificato_prova1.png):
```
An old scholar seen from behind, sitting at a wooden desk, reading a large open ancient book by the light of a single candle, simple composition with one clear subject in the lower half, large calm empty dark wall in the upper half, [STILE CONTENUTI]
```

## 2. Blocco STILE – PORTA E SIGLA (dettagliato)

```
antique copperplate engraving in the style of Gustave Doré, fine black ink cross-hatching and stippling on slightly aged off-white paper, black and white, neutral grayscale, no sepia, no brown, no color tint, only a very faint antique paper tone, deep chiaroscuro with one single light source, highly detailed, perfectly centered and symmetrical, vertical 9:16, full bleed edge to edge, no border, no frame, no rounded corners, no text, no letters, no watermark, no signature, no modern elements
```

Porta socchiusa approvata (VF_porta_socchiusa_prova2_bn.png):
```
A monumental gothic cathedral portal seen from the front, heavy wooden double doors half open, a blade of bright light pouring out onto the stone steps, pointed arch with stone tracery and pinnacles, dark ribbed vault above, [STILE PORTA]
```
Varianti: porta chiusa con una linea di luce tra i battenti; porta spalancata sulla luce.

## 3. Pendolo – simbolo che ritorna
```
A single brass pendulum hanging from a thin chain, perfectly still and vertical, centered, a soft halo of light behind it, plain empty paper background, emblem, [STILE CONTENUTI]
```

## 4. Negative prompt (solo dove c'è il campo apposito)
```
sepia, brown, color, color photograph, 3D render, CGI, cartoon, anime, flat vector, neon, modern objects, text, letters, logo, watermark, signature, frame, border, rounded corners, blurry, multiple light sources, realistic modern faces
```
