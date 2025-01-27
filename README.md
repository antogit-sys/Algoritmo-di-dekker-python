# Algoritmo-di-dekker-python

l'Algoritmo di dekker è un approccio software per garantire la
mutua esclusione ed è stato sviluppato in 5 tentativi. Ecco
una possibile implementazione in python

## ~ Tentativo 1
prima di entrare nella sezione critica, i processi controllano uno
alla volta la variabile turno: <b>protocollo dell'iglu</b>

PRO: garantisce la mutua esclusione

CONTRO: presenza di busy wait(spreco di cpu), il più lento determina la 
velocità di entrambi (effetto convoglio),se un processo fallisce dentro
la sezione critica rimarra bloccato per sempre 

## ~ Tentativo 2
ogni processo ha un flag relativo all'utilizzo della risorsa e puo 
leggere il flag dell'altro senza modificarlo

PRO: se un processo fallisce fuori dalla sezione critica l'altro continua
a lavorare

CONTRO:
<ul>
	<li> Se un processo fallisce dentro la sezione critica o prima di
	mettere false nel suo flag allora l'altro è bloccato per sempre (livelock)</li>
	<li>presenza di Busy wait(quindi spreco della cpu)</li>
	<li> se entrambi vedono il flag dell'altro impostato a False, mettono entrambi
	il loro flag a True...quindi entrambi vanno nella sezione critica senza
	mutua esclusione(race condition)
</ul>

## ~ Tentativo 3
in questo caso con flag[0]=true indico prima di voler entrare nella
sezione critica 

PRO: la mutua esclusione è garantita

CONTRO:
<ul>
	<li> Se un processo fallisce dentro la sua sezione critica o prima di
	mettere false nel suo flag allora l'altro è bloccato per sempre (livelock)</li>
	<li>presenza di Busy wait(quindi spreco della cpu)</li>
	<li> Se entrambi settano il flag a True prima che uno dei 2 verifichi la
	condizione del while si ha lo stallo! (livelock)</li>
</ul>
