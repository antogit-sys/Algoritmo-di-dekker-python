import threading
import time

# Variabili condivise
counter = 0  # Inizialmente il contatore è 0
turn = 0  # Inizialmente il turno è per il processo 0

# Sezione critica per il processo 0
def process_0():
	global counter, turn  
	for _ in range(10):
		# Processo 0: Segnala intenzione di entrare nella sezione critica
		while turn != 0:
			pass  # Busy wait
			
		# Sezione critica
		print(f"Processo 0 entra nella sezione critica. Counter = {counter}")
		counter += 1
		time.sleep(0.1)  # Simula lavoro nella sezione critica
		
		# Uscita dalla sezione critica
		turn = 1  # Passa il turno al processo 1

# Sezione critica per il processo 1
def process_1():
	global counter, turn 
	for _ in range(10):
		# Processo 1: Segnala intenzione di entrare nella sezione critica
		while turn != 1:
			pass  # Busy wait
		
		# Sezione critica
		print(f"Processo 1 entra nella sezione critica. Counter = {counter}")
		counter += 1
		time.sleep(0.1)  # Simula lavoro nella sezione critica
		
		# Uscita dalla sezione critica
		turn = 0  # Passa il turno al processo 0

# Creazione dei thread per i due processi
t0 = threading.Thread(target=process_0)
t1 = threading.Thread(target=process_1)

# Avvio dei thread
t0.start()
t1.start()

# Attendere che entrambi i thread finiscano
t0.join()
t1.join()

# Risultato finale
print(f"Counter finale: {counter}")
