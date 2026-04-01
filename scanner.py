from nmap import nmap 
import platform
import sys
from concurrent.futures import ThreadPoolExecutor


# Inizializziamo lo scanner di nmap
nm = nmap.PortScanner()
target = ("192.168.144.1")
# Usiamo le tue porte predefinite
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 161, 389, 443, 445, 587, 993, 995, 1433, 1883, 2049, 3000, 3306, 3389, 5000, 5432, 5900, 6379, 8000, 8080, 8443, 9000, 27017]
def scan_with_nmap(port):
    # Eseguiamo una scansione specifica sulla porta
    # -sV serve per rilevare la versione del servizio
    nm.scan(target, str(port), arguments='-sV')
    # Controlliamo se la porta è aperta nei risultati
    if target in nm.all_hosts():
        if 'tcp' in nm[target] and port in nm[target]['tcp']:
            state = nm[target]['tcp'][port]['state']
            service = nm[target]['tcp'][port]['name']
            version = nm[target]['tcp'][port]['product']
            
            if state == 'open':
                print(f"[+] Porta {port}: APERTA | Servizio: {service} | Versione: {version}")

print(f"Scansione Nmap in corso su {target}...")

# Usiamo il ThreadPoolExecutor per velocizzare nmap, che è più lento di un socket puro
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(scan_with_nmap, ports)

print("\nScansione completata.")


#21 (FTP): Utilizzata per il controllo del trasferimento di file tra client e server
#22 (SSH): Accesso remoto sicuro, trasferimento file (SFTP) e port forwarding 
#23 (Telnet): Vecchio protocollo per l'accesso remoto, non sicuro perché i dati viaggiano in chiaro
#25 (SMTP): Il protocollo standard per l'invio di email tra server 
#53 (DNS): Risoluzione dei nomi di dominio (converte gli URL in indirizzi IP)
#80 (HTTP): Traffico web standard non crittografato 
#110 (POP3): Protocollo per ricevere email (scarica i messaggi dal server al client)
#135 (RPC): Utilizzata dai servizi Microsoft per la comunicazione tra processi (mapping degli endpoint)
#139 (NetBIOS): Vecchio protocollo Windows per la condivisione di file e stampanti in rete locale
#143 (IMAP): Protocollo moderno per ricevere email mantenendole sul server
#161 (SNMP): Utilizzata per il monitoraggio e la gestione di apparati di rete
#389 (LDAP): Servizio di directory per l'autenticazione utenti in rete
#443 (HTTPS): Traffico web sicuro e crittografato tramite SSL/TLS
#445 (SMB): Protocollo moderno di Windows per la condivisione di file e l'accesso alle risorse di rete
#587 (SMTP Submission): Porta moderna e sicura per l'invio di email dai client
#636 (LDAPS): Versione sicura del protocollo LDAP su SSL/TLS
#993 (IMAPS): Protocollo IMAP sicuro per la ricezione di email crittografate
#995 (POP3S): Protocollo POP3 sicuro per la ricezione di email crittografate
#1194 (OpenVPN): Porta standard per la creazione di tunnel VPN sicuri
#1433 (MSSQL): Porta predefinita per le connessioni a Microsoft SQL Server
#1883: È la porta del protocollo MQTT. Se hai lampadine smart, sensori o un server Home Assistant in rete, questa porta è quella che permette loro di comunicare.
#2049 (NFS): Utilizzata per il Network File System e condivisione file su Linux
#3000: Usata spessissimo da chi sviluppa app con React, Node.js o per pannelli di controllo come Grafana.
#3306 (MySQL): Porta predefinita per le connessioni ai database MySQL e MariaDB 
#3389 (RDP): Utilizzata dal protocollo Remote Desktop per il controllo remoto Windows
#5000: È la porta predefinita di Flask (un framework Python) e viene usata spesso dai servizi Docker o dai sistemi di controllo di macOS (AirPlay).
#5432 (PostgreSQL): Porta standard per le connessioni al database PostgreSQL
#5900 (VNC): Porta comune per il controllo remoto grafico del desktop (alternativa a RDP)
#6379 (Redis): Utilizzata per database in-memory e sistemi di caching ad alte prestazioni
#8000: Usata da Django (altro framework Python) e per server web di sviluppo generici
#8080 (HTTP Alternate): Spesso usata come porta alternativa alla 80 o per server proxy e caching 
#8443 (HTTPS Alternate): Spesso usata come porta alternativa alla 443 per servizi web sicuri
#9000: Usata spesso da Portainer (per gestire i container Docker) o da servizi PHP moderni.
#27017: Questa è la porta standard di MongoDB. È uno dei database "NoSQL" più usati al mondo. Se trovi questa porta aperta e non protetta, è un grosso rischio per la sicurezza dei dati.