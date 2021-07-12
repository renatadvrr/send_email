import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#acessar gmail
smtp_host = 'smtp.gmail.com'
smtp_port = 587
username = ''
passaword = ''


# Criando servidor
print('Criando servidor...')
server = smtplib.SMTP(smtp_host, smtp_port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(username, passaword)

lista_cadastro = {
"cadastro1" : {
    "nome": "",
    "email": ""
},
"cadastro2" : {
    "nome": "",
    "email": ""
},
"cadastro3" : {
    "nome": "",
    "email": ""
}
}
for x in lista_cadastro:
    salvando_email = lista_cadastro[x].get("email")
    nome = lista_cadastro[x].get("nome")

    # Criando mensagem 
    message_html = '''
    <html>
    <head></head>
    <body>
        <p>Olá, {name}!<br>
        oi bonitinho<br>
        vamos ver boruto! <br>
        Aqui vai um <a href="http://www.python.org">link</a> 
        que talvez você goste.
        </p>
    </body>
    </html>
    '''.format(name=nome)
    email_msg = MIMEMultipart()

    print('Criando mensagem...')
    email_msg['From'] = username
    email_msg['To'] = salvando_email
    email_msg['Subject'] = 'Teste py'
    print('peraí...')

    email_msg.attach(MIMEText(message_html, 'html'))
    print(email_msg['From'], email_msg['To'])
    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    print('Mensagem enviada!')

server.quit()