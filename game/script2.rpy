init:
    python:
        
    
        def countdown(st, at, length=0.0):

            remaining = length - st

            if remaining > 5.0:
                return Text("%.1f" % remaining, color="#fff", size=72), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=72), .1
            else:
                return anim.Blink(Text("0.0", color="#fff", size=72)), None

    
    image countdown = DynamicDisplayable(countdown, length=15.0)


label path_bueno:
    
    "Danos el dinero que nos debes"
#   show countdown at Position(xalign=.1, yalign=.1)
    "Tienes 15 segundos para entregar el dinero o te mueres.."
 
#    hide countdown
#    with dissolve

    return

label path_batman:
    "Al darse cuenta que Tor, un supuesto amigo, era el que había ayudado en la muerte de su Padre..."
    "Junior creo un plan para vengarse de todos los pandilleros causantes de la muerte de su padre."
    per "¡Que gusto volverte a ver! Hace mucho tiempo que no hablábamos."
    t "Asi es, he estado muy ocupado estos dias. ¿Pero para que me citaste?"
    per "He notado que últimamente te has estado vistiendo muy bien y que siempre andas ropa de marca."
    t "Sí, es que estoy trabajando y me va rebien."
    per "¡Me alegro! ¿Dónde estas trabajando?"
    t "Pues…. No te puedo decir. Pero te puedo llevar al lugar en donde estoy trabajando, tal vez te llama la atención."
    "Junior accedió a ir con  Tor al lugar en donde estaba trabajando."

