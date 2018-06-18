from tkinter import *
from rsa_enc import encrypt
from rsa_dec import decrypt
from rsa_genkey import generisi_kljuceve

class RSAGraphicInterface:
	def __init__(self, master):
		self.master = master
		master.title("RSA Algoritam")
		master.geometry('640x480')

		self.genkey_button = Button(master, text="Generisi kljuceve", command=self.get_kljucevi)
		self.genkey_button.grid(column=0, row=0)

		self.privkey_input = Text(master, height=8, width=60)
		self.pk_lbl = Label(master, text="Privatni kljuc: ")
		self.pk_lbl.grid(column=0, row=1)
		self.privkey_input.grid(column=1, row=1)

		self.publkey_input = Text(master, height=8, width=60)
		self.pubk_lbl = Label(master, text="Javni kljuc: ")
		self.pubk_lbl.grid(column=0, row=2)
		self.publkey_input.grid(column=1, row=2)

		self.m_lbl = Label(master, text="String za enkripciju/dekripciju: ")
		self.m_lbl.grid(column=0, row=3)
		self.m_input = Text(master, height=5, width=60)
		self.m_input.grid(column=1, row=3)

		self.enkript_button = Button(master, text="Enkriptuj javnim klucem: ", command=self.enkriptuj)
		self.enkript_button.grid(column=0, row=4)

		self.dekript_button = Button(master, text="Dekriptuj privatnim kljucem", command=self.dekriptuj)
		self.dekript_button.grid(column=1, row=4)

		self.c_lbl = Label(master, text="Rezultat: ")
		self.c_lbl.grid(column=0, row=5)
		self.c_input = Text(master, height=5, width=60)
		self.c_input.grid(column=1, row=5)

		self.close_button = Button(master, text="Close", command=master.quit)
	
	def get_kljucevi(self):

		self.private_key, self.public_key = generisi_kljuceve()

		self.privkey_input.config(state = NORMAL)
		self.privkey_input.delete(1.0, END);
		self.privkey_input.insert(END, "Privatni kljuc d \n\n{}\n\nModuo N\n\n{}".format(self.private_key[0], self.private_key[1]) );
		self.privkey_input.config(state = DISABLED)
		
		self.publkey_input.config(state = NORMAL)
		self.publkey_input.delete(1.0, END);
		self.publkey_input.insert(END, "Javni eksponent e \n\n{}\n\nModuo N\n\n{}".format(self.public_key[0], self.public_key[1]) );
		self.publkey_input.config(state = DISABLED)

	
	def enkriptuj(self):

		m = self.m_input.get(1.0, END).strip()
		c = encrypt(m, self.public_key)

		self.c_input.delete(1.0, END)
		self.c_input.insert(END, c)
	

	def dekriptuj(self):

		m = self.m_input.get(1.0, END).strip()
		c = decrypt(m, self.private_key)

		self.c_input.delete(1.0, END)
		self.c_input.insert(END, c)

root = Tk()
my_gui = RSAGraphicInterface(root)
root.mainloop()