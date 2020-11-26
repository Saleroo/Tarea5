import getpass, imaplib, email
import pprint
from email.header import decode_header  #servira para leer el encabezado del correo electronico
import webbrowser
import os
import csv
import re # importando el modulo de regex de python
message_id_list=[]
correo=[]
expr_regular=[]
fecha=[]

def  obtener_ids( name, password):
    #--crea conexion--
    mail=imaplib.IMAP4_SSL('imap.gmail.com')
    #--inicia sesion--
    mail.login( name , password )
    print("En la cuenta de correo electrónico, accediendo a ", name ,"\n")

    #--lee en la categoria inbox de gmail--
    mail.select('INBOX') 
   
    #--obtener las ids de los mensajes con remitente edufindme--
    typ, data = mail.search(None,'(FROM "edufindme")')
    ids = data[0]
    id_list = ids.split()

    for i in range( len(id_list) ):
        id_list[i]= int(id_list[i])
    id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

    #--verificar si cuenta con el minimo de 20 mensajes de el mismo emisor--
    if(len(id_list)>=20):
        print("=========================================================")
        print("Se encontraron ",len(id_list), "mensajes de este emisor" )
        print("=========================================================")
    
    else:
        print("=========================================================")
        print("Se encontraron ",len(id_list),"mensajes de este emisor, por lo que no es suficiente (deben ser minimo 20)")
        print("=========================================================")
        exit(-1)
    


    for i in id_list:
        res, msg_data = mail.fetch( str(i), '(RFC822)') #fetch obtiene apartir la conexion el mensaje i. RFC822 = estandar que pide todas las partes de un correo
        for respuesta in msg_data:
            if isinstance(respuesta, tuple): #si la respuesta es una tupla
                #--obtener el contenido--
                msg_data = email.message_from_bytes(respuesta[1])

                #--decodificar el contenido--
                subject = decode_header(msg_data["Subject"])[0][0] #asunto del mensaje
                if isinstance(subject, bytes):
                    #--convertir a string--
                    subject = subject.decode("utf-8")

                #--emisor de el correo--
                from_ = msg_data.get("From")

                #--Message-ID--
                message_id = msg_data.get('Message-ID')

                #--Guardar en un archivo los msg id--
                archivo = open("message_id.txt","a")
                message_id=message_id.replace('<','')
                message_id=message_id.replace('>','')
                message_id_list.append(message_id)
                archivo.write( message_id + '\n')
                archivo.close()


                print("Asunto: ", subject)
                print("Enviado desde: ", from_)
                print("Message-ID: ", message_id)
                print("=========================================================")

    #-- cerrar sesion--
    mail.close()
    mail.logout()

def importar():
    print("Importando el archivo csv con las expresiones regulares...")

    with open('regular.csv') as f:
        reader = csv.reader(f) #itera linea por linea el archivo csv
        for row in reader:
            correo.append(row[0])
            expr_regular.append(row[1])
            fecha.append(row[2])
            print("mail: ", row[0])
            print("--------------------")
            print("expresion regular: ", row[1])
            print("--------------------")
            print("fecha: ", row[2])
            print("=========================================================")


def detectar(name,password):
    #--crea conexion--
    mail=imaplib.IMAP4_SSL('imap.gmail.com')
    #--inicia sesion--
    mail.login( name , password )
    print("En la cuenta de correo electrónico, accediendo a ", name ,"\n")

    #--lee en la categoria inbox de gmail--
    mail.select('INBOX') 

    while(True):
        print(correo)
        opcion=input("elegir el correo que decea detectar algun intento de pishing o si desea salir escriba(salir): ")

        if(opcion == "edufindme@edufindme.com"):
            #--obtener las ids de los mensajes con remitente edufindme--
            typ, data = mail.search(None,'(FROM "edufindme@edufindme.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            print("=========================================================")
            print("Se encontraron ",len(id_list), "mensajes de este emisor" )
            print("=========================================================")


            for i in id_list:
                res, msg_data = mail.fetch( str(i), '(RFC822)') #fetch obtiene apartir la conexion el mensaje i. RFC822 = estandar que pide todas las partes de un correo
                for respuesta in msg_data:
                    if isinstance(respuesta, tuple): #si la respuesta es una tupla
                        #--obtener el contenido--
                        msg_data = email.message_from_bytes(respuesta[1])

                        #--decodificar el contenido--
                        subject = decode_header(msg_data["Subject"])[0][0] #asunto del mensaje
                        if isinstance(subject, bytes):
                            #--convertir a string--
                            subject = subject.decode("utf-8")

                        #--emisor de el correo--
                        from_ = msg_data.get("From")

                        #--Message-ID--
                        message_id = msg_data.get('Message-ID')

                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')

                        # --Validando la el Message-ID--
                        id_re = re.compile(expr_regular[0]) #tipo de expresion regrular del id
                        if (id_re.search(message_id) == None):
                            print("WARNING ESTE CORREO PODRIA SER FALSO!!!")
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("=========================================================")


                        else:
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("=========================================================") 

        elif(opcion == "noreply@steampowered.com"):
            #--obtener las ids de los mensajes con remitente steam--
            typ, data = mail.search(None,'(FROM "noreply@steampowered.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            print("=========================================================")
            print("Se encontraron ",len(id_list), "mensajes de este emisor" )
            print("=========================================================")


            for i in id_list:
                res, msg_data = mail.fetch( str(i), '(RFC822)') #fetch obtiene apartir la conexion el mensaje i. RFC822 = estandar que pide todas las partes de un correo
                for respuesta in msg_data:
                    if isinstance(respuesta, tuple): #si la respuesta es una tupla
                        #--obtener el contenido--
                        msg_data = email.message_from_bytes(respuesta[1])

                        #--decodificar el contenido--
                        subject = decode_header(msg_data["Subject"])[0][0] #asunto del mensaje
                        if isinstance(subject, bytes):
                            #--convertir a string--
                            subject = subject.decode("utf-8")

                        #--emisor de el correo--
                        from_ = msg_data.get("From")

                        #--Message-ID--
                        message_id = msg_data.get('Message-ID')


                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')
                        # --Validando la el Message-ID--
                        id_re = re.compile(expr_regular[1]) #tipo de expresion regrular del id
                        if (id_re.search(message_id) == None):
                            print("WARNING ESTE CORREO PODRIA SER FALSO!!!")
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("=========================================================")


                        else:
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("=========================================================")


        elif(opcion == "no-reply@twitch.tv"):
            #--obtener las ids de los mensajes con remitente twitch--
            typ, data = mail.search(None,'(FROM "no-reply@twitch.tv")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            print("=========================================================")
            print("Se encontraron ",len(id_list), "mensajes de este emisor" )
            print("=========================================================")


            for i in id_list:
                res, msg_data = mail.fetch( str(i), '(RFC822)') #fetch obtiene apartir la conexion el mensaje i. RFC822 = estandar que pide todas las partes de un correo
                for respuesta in msg_data:
                    if isinstance(respuesta, tuple): #si la respuesta es una tupla
                        #--obtener el contenido--
                        msg_data = email.message_from_bytes(respuesta[1])

                        #--decodificar el contenido--
                        subject = decode_header(msg_data["Subject"])[0][0] #asunto del mensaje
                        if isinstance(subject, bytes):
                            #--convertir a string--
                            subject = subject.decode("utf-8")

                        #--emisor de el correo--
                        from_ = msg_data.get("From")

                        #--Message-ID--
                        message_id = msg_data.get('Message-ID')

                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')
                        # --Validando la el Message-ID--
                        id_re = re.compile(expr_regular[2]) #tipo de expresion regrular del id
                        if (id_re.search(message_id) == None):
                            print("WARNING ESTE CORREO PODRIA SER FALSO!!!")
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("=========================================================")


                        else:
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("=========================================================")

        elif(opcion == "salir"):
            break





    #-- cerrar sesion--
    mail.close()
    mail.logout()


if __name__ == '__main__':

    #--datos de usuario--
    email_address = input('Enter your email: ')
    print("Username: %s" % ( email_address ))
    obtener_ids( email_address, getpass.getpass())
    print('------------------------')
    os.system("PAUSE")
    print('------------------------')
    importar()
    print('------------------------')
    os.system("PAUSE")
    print('------------------------')
    #--datos de usuario para deteccion--
    email_address = input('Enter your email: ')
    print("Username: %s" % ( email_address ))
    detectar(email_address,getpass.getpass())

