# VITAFORTE – Voce narrante

Scelta da Filippo il 27/11/2026 (sostituisce Thomas di Horacle/ElevenLabs).

- **Servizio:** Gemini TTS, tramite Composio (strumento `GEMINI_GENERATE_CONTENT`)
- **Modello:** `gemini-2.5-flash-preview-tts`
- **Voce:** `Iapetus`
- **Istruzione di stile** (da mettere prima del testo, uguale ogni volta):

```
Leggi in italiano, con voce profonda e autorevole, ritmo scorrevole e deciso, un po' più veloce del normale, come la voce di un reel sui social, senza pause lunghe: 
```

- **Uscita:** audio PCM 24 kHz mono, da convertire in WAV/MP3 per il montaggio.
- **Ritmo di riferimento:** circa 2,7 parole al secondo (frase di prova di 19 parole = 7 secondi).
  Per un reel di 30–40 secondi: testo di circa 80–105 parole.

Nota: la voce può cambiare a periodi; tenerne una sola per periodo e aggiornare questo file.
