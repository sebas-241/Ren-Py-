label start:
    $ player_name = renpy.input("Ingresa tu nombre: ")      #Introducir datos
    $ player_name = player_name.strip()         # Para evitar espacios

    if not player_name:
        $ player_name = "Minami"

    play music BGM_escena_inicial fadein 1.5 
    sara "Holaaa [player_name], como estas? Espero que andes super bien"
    player "Holaaa como estas [sara]"

    scene background1

    "Comienza otro dia mas..."
    "Es increible que siga vivo despues de todo esto."

    player "Wow, la noche esta muy linda, cierto [sara]?"
    show yuuStandar at top with dissolve
    sara "Estas en lo cierto [player_name] jeje"
    hide yuuStandar with dissolve

    "Otro dia comun y corriente, estoy con [sara] en el centro"
    "Todo es tan tranquilo que simplemente parece un sueño"
    stop music fadeout 1.5

    $ respuesta = None
menu: 
    "ENSERIO QUIERES PREOCUPARLA?"

    "Si":
        $ respuesta = True

    "No":
        $ respuesta = False

if respuesta:
        "Un sueño...."
        "El cerebro es increible, puedes soñar cosas que nunca has vivido de antemano o simplemente ni lo haras"
        "Llega a dar miedo..."
        "AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA"
        "AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA"
        "AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA AYUDA" 
        show yuuStandar at yuuFree with dissolve
        play music BGM_escena_inicial fadein 1.5 
        sara "[player_name] estas bien?"   
else:
        #Menu de decisiones jump es para saltar al label correspondiente - menu
    menu:
        player "Que deberia responderle a [sara]?"

        "A, tranquila no me sucede nada Jsjsjsjs":
            jump respuesta_positiva
            
        "Dios, que fastidiosa eres. Tirate a un pozo":
            jump respuesta_negativa

    label respuesta_positiva:
        show yuuStandar at top with dissolve
        sara "A bueno, me alegra que estes bien"
        sara "Vamos a algun lado?"
        player "Sip, vamos al centro comercial"
        sara "Siiii"
        return

    label respuesta_negativa:
        stop music fadeout 1.5
        player_name "A... no soy capaz de decirle eso..."
        "Vuelvo a mi rutina"
        "En que estaba pensando?"
        "No recuerdo, bueno si mi cerebro no lo recuerda es porque no era importante."
        player_name "No tranquila estoy bien. A donde iremos hoy?"
        return

    # Para que el juego finalice correctamente y retorne al menú principal, debes colocar return al final del label donde estás indentado.


    

