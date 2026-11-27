# VITAFORTE – Prompt di stile per generatori di immagini

Stile di riferimento: le clip `sigla_incisione_master.mp4` e `sigla_zoom.mp4`
(incisione antica a inchiostro seppia su pergamena, luce calda al centro).

Regole:
- I prompt sono in inglese: quasi tutti i generatori rendono meglio così.
- Nessuna scritta dentro l'immagine: titoli e "VITAFORTE" si aggiungono solo al montaggio.
- Niente volti realistici di persone vere di oggi: figure di spalle, in ombra o lontane.
- Formato verticale 9:16.

---

## 1. Blocco STILE (da incollare in fondo a ogni prompt)

```
antique copperplate engraving, fine cross-hatching and stippling, sepia brown ink on aged cream parchment, almost monochrome warm palette, one single warm golden light source, deep chiaroscuro, highly detailed, 17th-century etching, perfectly centered symmetrical composition, vertical 9:16, no text, no letters, no watermark, no signature, no modern elements
```

## 2. Negative prompt (solo dove c'è il campo apposito)

```
color photograph, 3D render, CGI, cartoon, anime, flat vector, neon, saturated colors, modern objects, text, letters, logo, watermark, signature, frame border, blurry, asymmetry, distorted architecture, realistic modern faces
```

---

## 3. Porta – il gancio di entrata e uscita (SENZA pendolo)

**3a. Porta chiusa (inizio dell'intro / fine dell'outro)**
```
A monumental gothic cathedral portal seen from the front, heavy wooden double doors closed, iron studs and ornate hinges, pointed arch with stone tracery and pinnacles, ribbed vault above, wide stone steps in the foreground, a thin line of warm light glowing through the gap between the doors, [STILE]
```

**3b. Porta socchiusa**
```
A monumental gothic cathedral portal seen from the front, heavy wooden double doors half open, a blade of warm golden light pouring out onto the stone steps, pointed arch with stone tracery and pinnacles, ribbed vault above, [STILE]
```

**3c. Porta spalancata sulla luce (fine dell'intro / inizio dell'outro)**
```
Close view through wide open gothic wooden doors, the doorway filled with radiant warm light drawn as fine engraved rays, the dark doors framing the light on both sides, stone threshold at the bottom, [STILE]
```

## 4. Pendolo – il simbolo che ritorna

**4a. Emblema (da usare piccolo nelle grafiche)**
```
A single brass pendulum hanging from a thin chain, perfectly still and vertical, centered, a soft halo of warm light behind it, plain aged parchment background, emblem, [STILE]
```

**4b. Pendolo nella luce (chiusura alternativa)**
```
A brass pendulum hanging perfectly still in the center of a radiant gothic doorway full of warm light, engraved light rays, dark stone arch framing the scene, [STILE]
```

## 5. Scena per i contenuti (modello)

Sostituisci [SOGGETTO] con la scena del reel.
```
[SOGGETTO], figures seen from behind or in deep shadow, faces not visible, [STILE]
```
Esempio:
```
An old scholar seen from behind reading a large open book by candlelight in a stone library, figures seen from behind or in deep shadow, faces not visible, [STILE]
```

---

## Come provarli
- Gemini, Bing Image Creator, Firefly: incolla il prompt intero, con lo STILE al posto di [STILE]. Il negative prompt non serve.
- Ideogram, Leonardo: incolla il prompt e metti il negative nel suo campo.
- Midjourney: aggiungi in fondo `--ar 9:16 --style raw --no text, letters, color, 3d`.
- Per confrontare i generatori usa sempre lo **stesso prompt** (consigliato: 3b) e valuta: somiglianza con le sigle, simmetria, assenza di scritte, qualità delle linee incise.
