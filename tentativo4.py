import threading
import time
import sys

# Variabili condivise
counter = 0  # Contatore inizializzato a 0
flag = [False, False]  # flag[0] e flag[1] per i processi 0 e 1

def main():
	print("***************************************************")
	print("sia p1 che p0 mettono il loro flag a true")
	print("naturalmente nello stesso istante,quindi stallo")
	print("***************************************************\n")

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
	
	return 0

# Sezione critica per il processo 0
def process_0():
	global counter, flag
	for _ in range(10):
		flag[0]=True
		while flag[1]:  # Se il processo 1 sta cercando di entrare
			flag[0]=False
			time.sleep(1)
			flag[0]=True

		# Sezione critica
		print(f"Processo 0 entra nella sezione critica. Counter = {counter}")
		counter += 1
		time.sleep(0.1)  # Simula il lavoro nella sezione critica
		
		# Uscita dalla sezione critica
		flag[0] = False  # Indico che sono uscito dalla sezione critica

# Sezione critica per il processo 1
def process_1():
	global counter, flag  
	for _ in range(10):
		flag[1]=True
		while flag[0]:  # Se il processo 0 sta cercando di entrare
			flag[1]=False
			time.sleep(1)
			flag[1]=True
       
		# Sezione critica
		print(f"Processo 1 entra nella sezione critica. Counter = {counter}")
		counter += 1
		time.sleep(0.1)  # Simula il lavoro nella sezione critica
		
		# Uscita dalla sezione critica
		flag[1] = False  # Indico che sono uscito dalla sezione critica

if __name__ == '__main__':
	sys.exit(main())
