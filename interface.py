import tkinter as tk
import time
import random
import nxppy
import ndef

'''
Funzioni per lettura badge e scansione codice
'''

def code_finder(ndef_string,len_code):
	index = ndef_string.index('Text',17)
	code_start = index+6
	code_end = index+6+len_code
	code = ndef_string[code_start:code_end]
	return code

def reader():
	code = ""
	detected = False
	try:
		# Select tag
		uid = mifare.select()
		# Read NDEF data
		ndef_data = mifare.read_ndef()
		# Parse NDEF data
		ndef_records = list(ndef.message_decoder(ndef_data))
		print(ndef_records)
		stringa = str(ndef_records[0])
		code = code_finder(stringa,5)
		if code != "":
			detected = True
		print(code)
		current_time = time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
		print(current_time)
		if code not in registro:
			registro[code] = current_time
	except nxppy.SelectError:
		# SelectError is raised if no card is in the field.
		pass

	print(registro)
	return detected

'''
Inizializzazipone finestra
'''
window = tk.Tk()
window.geometry("800x800")
window.title("Hello Tkinter")
window.resizable(False,False)
window.configure(background="white")

'''
Variabili globali
'''
#text1 = "Appoggia badge al lettore!"
#text2 = "Timbratura effettuata"
#counter = 0

mifare = nxppy.Mifare() #istanza del reader
registro = {} #dizionario che contiene i valori registrati

''' ESEMPIO DI UTILIZZO
def task():
	global text1
	global text2
	global counter
	label1 = tk.Label(window,text=text1,fg="black")
	label2 = tk.Label(window,text=text2,fg="white")
	label1.grid(row=0,column=0)
	label2.grid(row=0,column=1)
	if counter % 2 == 0:
		#mostro text1
		label1.config(fg="black")
		label2.config(fg="white")
	else:
		#mostro text2
		label1.config(fg="white")
		label2.config(fg="black")
	
	counter += 1	
	window.after(3000,task)
'''

def tk_nfc_read():
	# istanza base di tkinter (manca settare le dimensioni e la posizione centrale del label)
	text_waiting = "Appoggiare badge sul lettore..."
	text_succeed = "Ingresso confermato!"
	label = tk.Label(window,text=text_waiting,fg="black",bg="white")
	label.grid(row=0,column=0)

	# lettura badge
	global mifare
	global registro
	detected = reader() #True se rileva un badge
	if detected is True:
		label.config(text=text_succeed) #aggiorno il testo

	# invio via ftp dei risultati

	#routine after
	window.after(3000,tk_nfc_read)




if __name__ == '__main__':
    window.after(1000,tk_nfc_read)
	window.mainloop()