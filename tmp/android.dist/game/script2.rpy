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


label muerte:
    
    "Danos el dinero que nos debes"
    show countdown at Position(xalign=.1, yalign=.1)
    "Tienes 15 segundos para entregar el dinero o te mueres.."

    
    

    
    hide countdown
    with dissolve

    return
    
    