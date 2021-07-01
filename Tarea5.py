import getpass, imaplib, email
import pprint
from email.header import decode_header  #servira para leer el encabezado del correo electronico
import webbrowser
import os
import csv
import re # importando el modulo de regex de python
from re import X
from subseq_tree import gen_tree, tree_to_regex, tree_to_HTML






correo=['udiegoportales@difusion.udp.cl','edufindme@edufindme.com','no-reply@accounts.google.com','no-reply@dropbox.com','notifications@instructure.com']
expr_regular=[]


def extract(strs):
    """ (The main function)
    Takes a list of strings and generates a RegEx that matches similar strings.
    """
    tree = gen_tree(strs)

    return tree_to_regex(tree)

def extract_HTML(strs):
    tree = gen_tree(strs)
    return tree_to_HTML(tree)

def  obtener_ids( name, password):
    #--crea conexion--
    mail=imaplib.IMAP4_SSL('imap.gmail.com')
    #--inicia sesion--
    mail.login( name , password )
    print("En la cuenta de correo electrónico, accediendo a ", name ,"\n")

    #--lee en la categoria inbox de gmail--
    mail.select('INBOX') 
   
    #--obtener las ids de los mensajes con remitente eligido:--
    while(True):
        print(correo)
        opcion=input("elegir el correo que decea obtener su informacion o si desea salir escriba(salir): ")
        if(opcion == "udiegoportales@difusion.udp.cl"):
            typ, data = mail.search(None,'(FROM "udiegoportales@difusion.udp.cl")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            #--verificar si cuenta con el minimo de 40 mensajes de el mismo emisor--
            if(len(id_list)>=40):
                print("=========================================================")
                print("Se encontraron ",len(id_list), "mensajes de este emisor" )
                os.system("PAUSE")
                print("=========================================================")
            
            else:
                print("=========================================================")
                print("Se encontraron ",len(id_list),"mensajes de este emisor, por lo que no es suficiente (deben ser minimo 40)")
                print("=========================================================")
                exit(-1)
            


            for i in id_list:
                res, msg_data = mail.fetch( str(i), '(RFC822)') #fetch obtiene apartir la conexion el mensaje i. RFC822 = estandar que pide todas las partes de un correo
                for respuesta in msg_data:
                    if isinstance(respuesta, tuple): #si la respuesta es una tupla
                        #--obtener el contenido del header--
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
                        #--Guardar en un archivo.txt los msg id--
                        archivo = open("message_id_udiegoportales.txt","a")
                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')

                        archivo.write( message_id + '\n')
                        archivo.close()


                        #--Receiver1--
                        message_receiver1=msg_data.get('Received')

                        #--UTC--
                        UTC=msg_data.get('Date')


                        print("Asunto: ", subject)
                        print("Enviado desde: ", from_)
                        print("Message-ID: ", message_id)
                        print("Received: ", message_receiver1)
                        print("UTC: ", UTC)
                        print("=========================================================")

        if(opcion == "edufindme@edufindme.com"):
            typ, data = mail.search(None,'(FROM "edufindme@edufindme.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            #--verificar si cuenta con el minimo de 40 mensajes de el mismo emisor--
            if(len(id_list)>=40):
                print("=========================================================")
                print("Se encontraron ",len(id_list), "mensajes de este emisor" )
                os.system("PAUSE")
                print("=========================================================")
            
            else:
                print("=========================================================")
                print("Se encontraron ",len(id_list),"mensajes de este emisor, por lo que no es suficiente (deben ser minimo 40)")
                print("=========================================================")
                exit(-1)
            


            for i in id_list:
                res, msg_data = mail.fetch( str(i), '(RFC822)') #fetch obtiene apartir la conexion el mensaje i. RFC822 = estandar que pide todas las partes de un correo
                for respuesta in msg_data:
                    if isinstance(respuesta, tuple): #si la respuesta es una tupla
                        #--obtener el contenido del header--
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
                        #--Guardar en un archivo.txt los msg id--
                        archivo = open("message_id_edufindme.txt","a")
                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')

                        archivo.write( message_id + '\n')
                        archivo.close()


                        #--Receiver1--
                        message_receiver1=msg_data.get('Received')

                        #--UTC--
                        UTC=msg_data.get('Date')


                        print("Asunto: ", subject)
                        print("Enviado desde: ", from_)
                        print("Message-ID: ", message_id)
                        print("Received: ", message_receiver1)
                        print("UTC: ", UTC)
                        print("=========================================================")

        if(opcion == "no-reply@accounts.google.com"):
            typ, data = mail.search(None,'(FROM "no-reply@accounts.google.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            #--verificar si cuenta con el minimo de 40 mensajes de el mismo emisor--
            if(len(id_list)>=40):
                print("=========================================================")
                print("Se encontraron ",len(id_list), "mensajes de este emisor" )
                os.system("PAUSE")
                print("=========================================================")
            
            else:
                print("=========================================================")
                print("Se encontraron ",len(id_list),"mensajes de este emisor, por lo que no es suficiente (deben ser minimo 40)")
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
                        #--Guardar en un archivo.txt los msg id--
                        archivo = open("message_id_google.txt","a")
                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')

                        archivo.write( message_id + '\n')
                        archivo.close()


                        #--Receiver--
                        message_receiver1=msg_data.get('Received')

                        #--UTC--
                        UTC=msg_data.get('Date')


                        print("Asunto: ", subject)
                        print("Enviado desde: ", from_)
                        print("Message-ID: ", message_id)
                        print("Received: ", message_receiver1)
                        print("UTC: ", UTC)
                        print("=========================================================")

        if(opcion == "no-reply@dropbox.com"):
            typ, data = mail.search(None,'(FROM "no-reply@dropbox.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            #--verificar si cuenta con el minimo de 40 mensajes de el mismo emisor--
            if(len(id_list)>=40):
                print("=========================================================")
                print("Se encontraron ",len(id_list), "mensajes de este emisor" )
                os.system("PAUSE")
                print("=========================================================")
            
            else:
                print("=========================================================")
                print("Se encontraron ",len(id_list),"mensajes de este emisor, por lo que no es suficiente (deben ser minimo 40)")
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
                        #--Guardar en un archivo.txt los msg id--
                        archivo = open("message_id_dropbox.txt","a")
                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')

                        archivo.write( message_id + '\n')
                        archivo.close()

                        #--Receiver--
                        message_receiver1=msg_data.get('Received')

                        #--UTC--
                        UTC=msg_data.get('Date')


                        print("Asunto: ", subject)
                        print("Enviado desde: ", from_)
                        print("Message-ID: ", message_id)
                        print("Received: ", message_receiver1)
                        print("UTC: ", UTC)
                        print("=========================================================")


        if(opcion == "notifications@instructure.com"):
            typ, data = mail.search(None,'(FROM "notifications@instructure.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            #--verificar si cuenta con el minimo de 40 mensajes de el mismo emisor--
            if(len(id_list)>=40):
                print("=========================================================")
                print("Se encontraron ",len(id_list), "mensajes de este emisor" )
                os.system("PAUSE")
                print("=========================================================")
            
            else:
                print("=========================================================")
                print("Se encontraron ",len(id_list),"mensajes de este emisor, por lo que no es suficiente (deben ser minimo 40)")
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
                        #--Guardar en un archivo.txt los msg id--
                        archivo = open("message_id_instructure.txt","a")
                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')

                        archivo.write( message_id + '\n')
                        archivo.close()

                        #--Receiver--
                        message_receiver1=msg_data.get('Received')

                        #--UTC--
                        UTC=msg_data.get('Date')


                        print("Asunto: ", subject)
                        print("Enviado desde: ", from_)
                        print("Message-ID: ", message_id)
                        print("Received: ", message_receiver1)
                        print("UTC: ", UTC)
                        print("=========================================================")



                
        if(opcion == "salir"):
            break


    #-- cerrar sesion--
    mail.close()
    mail.logout()


def regex():
    mssg_id=[]
    print("===================================================")
    print("Obtener el Regex de: udiegoportales@difusion.udp.cl")

    archivo = open("message_id_udiegoportales.txt", "r") 
    for linea in archivo:
        mssg_id.append(linea)
    archivo.close()
    regx1=extract(mssg_id)
    regx1=regx1.rstrip(regx1[-1])
    regx1=regx1.rstrip(regx1[-1])
    expr_regular.append(regx1)
    print(regx1)

    print("===================================================")   
    print("Obtener el Regex de: edufindme@edufindme.com")

    archivo = open("message_id_edufindme.txt", "r")
    mssg_id=[]
    for linea in archivo:
        mssg_id.append(linea)
    archivo.close()
    regx2=extract(mssg_id)
    regx2=regx2.rstrip(regx2[-1])
    regx2=regx2.rstrip(regx2[-1])
    expr_regular.append(regx2)
    print(regx2)

    print("===================================================")  
    print("Obtener el Regex de: no-reply@accounts.google.com")

    archivo = open("message_id_google.txt", "r")
    mssg_id=[]
    for linea in archivo:
        mssg_id.append(linea)
    archivo.close()
    regx3=extract(mssg_id)
    regx3=regx3.rstrip(regx3[-1])
    regx3=regx3.rstrip(regx3[-1])
    expr_regular.append(regx3)
    print(regx3)
    
    print("===================================================")  
    print("Obtener el Regex de: no-reply@dropbox.com")

    archivo = open("message_id_dropbox.txt", "r")
    mssg_id=[]
    for linea in archivo:
        mssg_id.append(linea)
    archivo.close()
    regx4=extract(mssg_id)
    regx4=regx4.rstrip(regx4[-1])
    regx4=regx4.rstrip(regx4[-1])
    expr_regular.append(regx4)
    print(regx4)

    
    print("===================================================")  
    print("Obtener el Regex de: notifications@instructure.com")

    archivo = open("message_id_instructure.txt", "r")
    mssg_id=[]
    for linea in archivo:
        mssg_id.append(linea)
    archivo.close()
    regx5=extract(mssg_id)
    regx5=regx5.rstrip(regx5[-1])
    regx5=regx5.rstrip(regx5[-1])
    expr_regular.append(regx5)
    print(regx5)

    print("===================================================")  


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

        if(opcion == "udiegoportales@difusion.udp.cl"):
            #--obtener las ids de los mensajes con remitente edufindme--
            typ, data = mail.search(None,'(FROM "udiegoportales@difusion.udp.cl")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            print("=========================================================")
            print("Se encontraron ",len(id_list), "mensajes de este emisor" )
            os.system("PAUSE")
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

                        #--Receiver--
                        message_receiver1=msg_data.get('Received')

                        #--UTC--
                        UTC=msg_data.get('Date')

                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')

                        # --Validando la el Message-ID--
                        id_re = re.compile(expr_regular[0]) #tipo de expresion regrular del id
                        if (id_re.search(message_id) == None):
                            print("<-@-@-WARNING-@-@-> ESTE CORREO PODRIA SER FALSO!!! <-@-@-WARNING-@-@->")
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)
                            print("=========================================================")


                        else:
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)
                            print("=========================================================") 

        elif(opcion == "edufindme@edufindme.com"):
            #--obtener las ids de los mensajes con remitente steam--
            typ, data = mail.search(None,'(FROM "edufindme@edufindme.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            print("=========================================================")
            print("Se encontraron ",len(id_list), "mensajes de este emisor" )
            os.system("PAUSE")
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

                        #--Receiver--
                        message_receiver1=msg_data.get('Received')

                        #--UTC--
                        UTC=msg_data.get('Date')

                        message_id=message_id.replace('<','')
                        message_id=message_id.replace('>','')
                        # --Validando la el Message-ID--
                        id_re = re.compile(expr_regular[1]) #tipo de expresion regrular del id
                        if (id_re.search(message_id) == None):
                            print("<-@-@-WARNING-@-@-> ESTE CORREO PODRIA SER FALSO!!! <-@-@-WARNING-@-@->")
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)
                            print("=========================================================")


                        else:
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)
                            print("=========================================================")


        elif(opcion == "no-reply@accounts.google.com"):
            #--obtener las ids de los mensajes con remitente twitch--
            typ, data = mail.search(None,'(FROM "no-reply@accounts.google.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            print("=========================================================")
            print("Se encontraron ",len(id_list), "mensajes de este emisor" )
            os.system("PAUSE")
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

                        #--Receiver--
                        message_receiver1=msg_data.get('Received')

                        #--UTC--
                        UTC=msg_data.get('Date')


                        # --Validando la el Message-ID--
                        id_re = re.compile(expr_regular[2]) #tipo de expresion regrular del id
                        if (id_re.search(message_id) == None):
                            print("<-@-@-WARNING-@-@-> ESTE CORREO PODRIA SER FALSO!!! <-@-@-WARNING-@-@->")
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)
                            print("=========================================================")


                        else:
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)
                            print("=========================================================")



        elif(opcion == "no-reply@dropbox.com"):
            #--obtener las ids de los mensajes con remitente twitch--
            typ, data = mail.search(None,'(FROM "no-reply@dropbox.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            print("=========================================================")
            print("Se encontraron ",len(id_list), "mensajes de este emisor" )
            os.system("PAUSE")
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

                        #--Receiver--
                        message_receiver1=msg_data.get('Received')

                        #--UTC--
                        UTC=msg_data.get('Date')

                        # --Validando la el Message-ID--
                        id_re = re.compile(expr_regular[3]) #tipo de expresion regrular del id
                        if (id_re.search(message_id) == None):
                            print("<-@-@-WARNING-@-@-> ESTE CORREO PODRIA SER FALSO!!! <-@-@-WARNING-@-@->")
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)                            
                            print("=========================================================")


                        else:
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)
                            print("=========================================================")



        elif(opcion == "notifications@instructure.com"):
            #--obtener las ids de los mensajes con remitente twitch--
            typ, data = mail.search(None,'(FROM "no-reply@accounts.google.com")')
            ids = data[0]
            id_list = ids.split()

            for i in range( len(id_list) ):
                id_list[i]= int(id_list[i])
            id_list.reverse() #para que la lista quede desde los mensajes resividos mas recientemente hasta el mas antiguos

            print("=========================================================")
            print("Se encontraron ",len(id_list), "mensajes de este emisor" )
            os.system("PAUSE")
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

                        #--Receiver--
                        message_receiver1=msg_data.get('Received')
                        part = respuesta[1].decode('utf-8')
                        msg = email.message_from_string(part)
                        print(msg)

                        #--UTC--
                        UTC=msg_data.get('Date')

                        # --Validando la el Message-ID--
                        id_re = re.compile(expr_regular[4]) #tipo de expresion regrular del id
                        if (id_re.search(message_id) == None):
                            print("<-@-@-WARNING-@-@-> ESTE CORREO PODRIA SER FALSO!!! <-@-@-WARNING-@-@->")
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)
                            print("=========================================================")


                        else:
                            print("Asunto: ", subject)
                            print("Enviado desde: ", from_)
                            print("Message-ID: ", message_id)
                            print("Received: ", message_receiver1)
                            print("UTC: ", UTC)
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
    print('-----------------------------------------')

    print('--Obtener datos de un email--')
    os.system("PAUSE")
    print('Es necesario hacer esta operacion? (si ya se cuenta con los .txt con los message_id No se debe hacer.')
    eleccion= input("(1)=seguir y obtener mssg_id o digite cualquier caracter: ")

    if(eleccion == '1'):
        obtener_ids( email_address, getpass.getpass())

    print('-----------------------------------------')

    print('Generacion de Regex (sin mails falsos)')
    os.system("PAUSE")
    regex()

    print('-----------------------------------------')
    
    print('Una ves generados los mails falsos por medio de los regex obtenidos se podra detectar estos correos falsos')
    os.system("PAUSE")
    #--datos de usuario para deteccion--
    email_address = input('Enter your email: ')
    print("Username: %s" % ( email_address ))
    detectar(email_address,getpass.getpass())

