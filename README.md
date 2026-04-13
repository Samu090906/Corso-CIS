🛡️ Descrizione dello Script
Questo script è un Network Scanner multithread basato sulla libreria python-nmap. A differenza di un semplice scanner di socket, questo strumento si interfaccia direttamente con l'engine di Nmap, permettendo non solo di vedere se una porta è aperta, ma anche di identificare quale servizio ci sta girando e la relativa versione.

L'uso del ThreadPoolExecutor permette di interrogare più porte contemporaneamente, abbattendo i tempi di attesa tipici delle scansioni sequenziali di Nmap.

⚙️ Come funziona (Passo dopo passo)
	1	Input del Target: Lo script richiede l'indirizzo IP (o l'hostname) della macchina da analizzare.
	
	2	Definizione del Target List: Viene utilizzata una lista predefinita di 25 porte comuni (HTTP, SSH, FTP, Database, ecc.).
	
	3	Inizializzazione Nmap: Viene creato un oggetto PortScanner(). Questo funge da "ponte" tra Python e l'eseguibile Nmap installato nel sistema.
	
	4	Esecuzione Multithread:
	
	◦	Lo script lancia 5 "lavoratori" (threads) contemporaneamente.
	
	◦	Ogni thread prende una porta dalla lista e chiama la funzione scan_with_nmap.
	
	5	Analisi del Servizio (-sV): Per ogni porta, viene eseguito il comando nm.scan con l'argomento -sV. Questo invia dei pacchetti specifici (probes) per forzare il servizio a rispondere con il proprio nome e numero di versione (Service Version Detection).
	
	6	Parsing dei Risultati: Se la porta risulta open, lo script estrae dal report di Nmap il nome del servizio (es. Apache) e la versione (es. 2.4.41) e li stampa a video.

🚀 Come farlo funzionare
Per eseguire correttamente questo script, devi soddisfare alcuni requisiti di sistema:
1. Installare Nmap (Il software)
Lo script è un'interfaccia; ha bisogno che il software Nmap sia installato sul tuo sistema operativo.

	•	Linux (Debian/Ubuntu): sudo apt install nmap

	•	Windows: Scarica l'installer dal sito ufficiale nmap.org.
	
	•	macOS: brew install nmap

3. Installare la libreria Python
Devi installare il wrapper Python per Nmap tramite terminale:
Bash
pip install python-nmap

4. Esecuzione
Salva il codice in un file (es. scanner.py) e avvialo:
Bash

python scanner.py
Nota: Su alcuni sistemi, per ottenere risultati più precisi o per scansioni che richiedono privilegi (come gli SYN scan), potrebbe essere necessario eseguire lo script come amministratore/root (sudo).

🔍 Cosa può fare questo script

	•	Service Fingerprinting: Non ti dice solo "la porta 80 è aperta", ma ti dice "c'è un server Nginx versione 1.18".

	•	Vulnerability Assessment Preliminare: Conoscere la versione esatta di un servizio permette di cercare rapidamente se quel software è affetto da vulnerabilità note (CVE).

	•	Velocità Ottimizzata: Grazie al multithreading, la scansione è molto più rapida rispetto a un comando Nmap standard eseguito su una singola porta alla volta.
	
	•	Monitoraggio Asset: Può essere usato per controllare rapidamente se su un server aziendale sono stati aperti servizi non autorizzati (es. un database esposto esternamente).


