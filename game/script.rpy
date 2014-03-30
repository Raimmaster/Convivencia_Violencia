# Fondos
image bg escenario1 = "escenario1.png"

# Personajes

define e = Character('Tu', color="#c8ffc8")
init:
    $ perName = ""

    $ per = DynamicCharacter("perName", color=(192, 64, 64, 255))

# The game starts here.
# - El juego comienza aquí.
label start:
    scene black
    with fade
    "¿Tienes un nombre?"

    menu:

        "Sí.":
            scene bg escenario1 
            $ perName = renpy.input(_("¿Cual??")) or _("Volentto")

        "No.":    
            "¿Estás seguro que tu nombre no es Volentto?"
            "..."

    scene bg escenario1
    with fade
    "Es una noche oscura"
    $ perName = "Volentto"
    per "Tengo frío."

label nombre:

    return
