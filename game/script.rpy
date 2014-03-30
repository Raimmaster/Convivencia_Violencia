# Fondos
image bg escenario1 = "escenario1.png"

# Personajes

define p = Character('Papá', color="#c8ffc8")

init:
    $ perName = ""

    $ per = DynamicCharacter("perName", color=(192, 64, 64, 255))

# The game starts here.
# - El juego comienza aquí.
label start:
    scene black
    with fade
    "Beep Beep…" 
    "¿Tienes un nombre?"

    menu:

        "Sí.":
            $ perName = renpy.input(_("¿Cual??")) or _("Volentto")

        "No.":    
            "¿Estás seguro que tu nombre no es Volentto?"
            "..."
            $ perName = "Volentto"

    scene bg escenario1
    with fade

    p "Hijo, ya es hora de ir a la escuela."
    per "Solo 5 minutos mas."
    p "No inventes, levantate y báñate. Te tenes que alistar para poder ir a la escuela."
    

    return
