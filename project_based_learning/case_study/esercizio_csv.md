# Esercizio: Riconciliazione Anagrafica Dipendenti

## Scenario
****
Lavori nel team **Data Governance** di *Industrie Digitali S.p.A.*, un'azienda con circa 1.000 dipendenti distribuiti su diverse sedi italiane.

L'azienda utilizza tre sistemi informativi diversi, ognuno gestito da un reparto differente, che mantengono ciascuno una propria anagrafica dei dipendenti:

1. **sistema_hr.csv** — Esportazione dal gestionale Risorse Umane, utilizzato dall'ufficio del personale per contratti, assunzioni e gestione organizzativa.
2. **gestionale_paghe.csv** — Esportazione dal sistema paghe, utilizzato dall'ufficio Amministrazione e Finanza per stipendi e cedolini.
3. **anagrafica_aziendale.csv** — Esportazione dal registro aziendale centrale, utilizzato dalla Direzione Generale per reportistica e comunicazioni interne.

Nel tempo, a causa di inserimenti manuali, migrazioni e disallineamenti tra i reparti, i tre sistemi si sono **desincronizzati**: non tutti i dipendenti sono presenti in tutti e tre i file, e ogni sistema adotta formati e convenzioni proprie.

La Direzione ti chiede di fare una **riconciliazione completa** per capire lo stato reale dell'anagrafica.

---

## Obiettivi

### 1. Caricare correttamente i tre file
Ogni file ha un formato diverso. Prima di qualsiasi analisi devi capire e gestire le differenze di:
- separatore (quale carattere separa le colonne?)
- formato delle date
- formato dello stipendio (decimali, arrotondamenti)
- struttura del nome (una colonna o due? in che ordine?)
- codice identificativo del dipendente (quale prefisso? quale formato?)
- lingua e stile delle intestazioni

### 2. Identificare una chiave di collegamento
I tre file non usano lo stesso codice dipendente. Trova un campo presente in tutti e tre i file che possa fungere da **chiave univoca di join** per collegare i record tra loro.

### 3. Costruire l'anagrafica completa
Partendo dai tre file, costruisci un unico DataFrame con tutti i 1.000 dipendenti, senza duplicati.

### 4. Individuare i disallineamenti
Rispondi a queste domande:

- Quanti dipendenti sono presenti in **tutti e tre** i file?
- Quanti dipendenti **mancano** da ciascun file? Quali sono?
- Ci sono dipendenti presenti in **uno solo** dei tre file?
- Ci sono dipendenti presenti in **esattamente due** file? Se sì, in quale combinazione?

### 5. Produrre un report di sintesi
Genera un output chiaro (tabella, DataFrame o file) che riassuma per ciascun dipendente in quali sistemi è presente e in quali è assente.

---

## Suggerimenti

- Inizia aprendo ciascun file con un editor di testo (o con `head` da terminale) per osservare il formato **prima** di scrivere codice.
- La funzione `pd.read_csv()` accetta il parametro `sep` per specificare il separatore.
- Le operazioni sugli insiemi (`set`, intersezione, differenza, unione) sono molto utili per questo tipo di analisi.
- Ragiona su quale campo è davvero **univoco e coerente** tra i tre file: non tutti lo sono.
- Attenzione: uno dei file non ha il telefono. Non è un errore, è una caratteristica del sistema da cui proviene.

---

## Consegna

Produci un notebook (`.ipynb`) o uno script (`.py`) che:

1. Carica i tre file in tre DataFrame separati.
2. Individua la chiave di collegamento tra i file.
3. Calcola e stampa il numero di dipendenti per ciascuna delle seguenti categorie:
   - presenti in tutti e tre i file
   - mancanti da ciascun file (con elenco)
   - presenti in uno solo dei file
   - presenti in esattamente due file
4. (Facoltativo) Produce un file CSV finale con l'anagrafica completa e una colonna che indica la presenza in ciascun sistema (es. `presente_hr`, `presente_paghe`, `presente_anagrafica`).

Buon lavoro!
