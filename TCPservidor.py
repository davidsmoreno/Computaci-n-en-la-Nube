
def saldo():
    file=open("saldo.txt")
    x=file.read()
    x=int(x)
    file.close()
    return x
   



def debitar(y):
    file=open("saldo.txt")
    x=file.read()
    x=int(x)
    file.close()
    m=x-y
  
    if m >=0:
        m=str(m)
        file1=open("saldo.txt","w")
        file1.write(m)
        file1.close()
        print("OK")
        return("OK")
    else:
        print("Saldo insuficiente")
        return ("Saldo insuficiente")
        
        file1.close()
    
    
def acreditar(y):
    file=open("saldo.txt")
    x=file.read()
    x=int(x)
    file.close()
    m=x+y
    m=str(m)
    file1=open("saldo.txt","w")
    file1.write(m)
    print ("Nuevo saldo: "+ m)
    return ("Nuevo saldo: "+ m)
    file1.close()



from socket import *

servidorPuerto = 1000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)

print("El servidor está listo para recibir mensajes")
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    print("Mensaje recibido de ", clienteDireccion)
    mensaje = mensaje.upper()
    if mensaje == "SALDO":
        mensajeRespuesta= saldo()
        print(mensajeRespuesta)
    
    elif "ACREDITAR" in mensaje:
        mensaje=mensaje.split()
        x=int(mensaje[1])
        mensajeRespuesta = acreditar(x)
        print(mensajeRespuesta)
        
    elif "DEBITAR" in mensaje:
        mensaje=mensaje.split()
        x = int (mensaje[1])
        mensajeRespuesta = debitar(x)
        print(mensajeRespuesta)
    #print(mensaje)
    #mensajeRespuesta = mensaje.upper()
    
    conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
    conexionSocket.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
