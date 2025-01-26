# Algoritmo-di-dekker-python

l'Algoritmo di dekker è un approccio software per garantire la
mutua esclusione ed è stato sviluppato in 5 tentativi. Ecco
una possibile implementazione in python

## ~ tentativo 1
prima di entrare nella sezione critica, i processi controllano uno
alla volta la variabile turno: <b>protocollo dell'iglu</b>

PRO: garantisce la mutua esclusione

CONTRO: presenza di busy wait(spreco di cpu), il più lento determina la 
velocità di entrambi (effetto convoglio),se un processo fallisce dentro
la sezione critica rimarra bloccato per sempre 
