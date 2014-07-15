#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
#Script by David Isztl & Michel Basili based on original ssllogmux python decompiler

# Librerie per il corretto funzionamento
import urllib

def analizza(t):
    pezzi = t.split(" ")
    tipo = pezzi[0]
    tipoc = 0
    cont1 = 0
    cont3 = 0
    
    #Tipi di log conosciuti
    if tipo == "sshd_connection_start_3":                               #sshd_connection_start_3
        print "!----------------Connection requeset...."
        tipoc = 1
    elif tipo == "auth_info_3":                                         #auth_info_3
        print "!----------------Connection allowed/denyed..."
        tipoc = 2
    elif tipo == "channel_data_client_3" or "channel_data_server_3":    #channel_data_client_3 channel_data_server_3
        tipoc = 3

    for item in pezzi:
        element = item.split("=")
        if len(element) == 2:
            type = element[0]
            # Type contiene il nome del pezzo di log es. port=22 la porta sara' 22 e il nome port
            if type == "uristring":
                val = urllib.unquote_plus(str(element[1]))
                if tipoc == 1:
                    if cont1 > 0 and cont1 <> 2:
                        print val
                    cont1 += 1
                elif tipoc == 2:
                    if cont1 > 0:
                        print val
                    cont1 += 1
                elif tipoc == 3:
                    if cont3 == 2:
                        print val
                    cont3 += 1
            if type == "addr":
                 if tipoc == 1:
                     print "Address:", element[1]
            if type == "port":
                 if tipoc == 1:
                     print "Port:", element[1]

#Leggi tutto il file di log
f = open('ssllogmux.log') # Directory log
for line in iter(f):
    analizza(line) # Dai la riga del log alla funzione che lo analizzera'
f.close()
