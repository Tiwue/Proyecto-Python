#iniciar
intentos=2

def jugar(intentos):

    respuesta = input("\n¿Dime de que  color es la fruta en que estoy pensando?: \n")
    if str(respuesta) != "naranja" :
        if intentos>0:
            intentos = intentos-1
            print("\n Fallaste te quedan "+ str(intentos+1)+" intentos.\n Intentalo de nuevo:")
            jugar(intentos)
        else:
            print("\n Perdiste el juego se acabaron los intentos :(\n")
    elif str(respuesta) =="naranja" :
        
        print("|  Ganaste era naranja | :) ")     
       
jugar(intentos)           

