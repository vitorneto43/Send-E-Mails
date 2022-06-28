import yagmail
from datetime import datetime


contatos = [('Libia', 'libiaferraz@yahoo.com.br', '15/06'),
            ('Leda', 'aedaveiga@gmail.com', '10/08'),
            ('Paulo', 'paulocesar5583@gmail.com', '12/02'),
            ('Vitor', 'vitor_veiga@yahoo.com.br', '31/10'),
            ('Marcos', 'mafveiga@hotmail.com', '01/10')
            ]

dataAtual = datetime.now().strftime('%d/%m')

emailServer = yagmail.SMTP('wneto3110@gmail.com', 'libiaferraz1506')
for nome in contatos:
    if nome[2] == dataAtual:
        emailServer.send(nome[1], subject = 'Feliz Aniversário', contents = "Olá," + nome[0]+"! Feliz Aniversário!")
        
        