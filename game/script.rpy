# Fondos
image bg escenario1 = "escenario1.png"

# Personajes

define p = Character('Papá', color="#c8ffc8")
define t = Character('Tor', color="#c8ffc9")
define m = Character('Monferno', color="#c7ffc9")
define a = Character('Alduino', color="#c5ffc9")

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
    p "Levantate y báñate. Te tienes que alistar para poder ir a la escuela."

    "15 minutos después."
    per "¡Ya estoy listo!"    
    p "Esta bien ya podemos irnos."
    per "¿Hoy tampoco abriras la pulpería?"
    p "No puedo hacerlo en este momento, no preguntes porque, solo obedece."
    per "Ya tienes mucho tiempo sin abrirla, deberías hacerlo."
    p "¡Calla, te dije que no preguntaras porque!"
    "Una sombra se percibe detrás de ellos."
    "***5 MINUTOS DESPUES****"
    jump escuela
#   jump muerte
    return

label escuela:
    p "¡Cuidate hijo! Nos vemos en la casa."
# Junior entra a la escuela y se encuentra con un niño llamado Tor.
    t "¡Hey Junior! ¿Que onda?"
    per "¡Pues nada, Vengo llegando de mi casa!"
    t "¡Ah que bueno! ¿Por qué tu papa no ha abierto la pulpería? He querido comprar varios dulces y no puedo."
    per "Pues, la verdad no se. Hoy en la mañana me dijo que no le preguntara sobre eso. Pero no entiendo porque, si el tiene toda la pulpería llena de muchos dulces y cosas. Aparte que le he visto mucho dinero."
    t "Mmm…¡Que raro! Quisiera ver que tantas cosas tiene tu padre, tal vez podemos comer un par de dulces, asi no se desperdician. "
    per "¡Buena idea, vamos!"
    jump camino_casa

label camino_casa:
    "Ambos niños van caminando por la calle, cuando Tor se desvía por un callejón y habla con un par de muchachos de apariencia rara."
    "Junior  lo espera en el mismo lugar mientras Tor conversa. Tor regresa donde Junior."
    t "¡Disculpame! Estaba hablando con un par de amigos."
    per "¡Ah no te preocupes! Vamos a la casa. Apresurémonos antes de  que mi padre llegue."
    jump llegar_casa

label llegar_casa:
    "Llegan a la esquina de la calle y observan al padre conversar con los mismos hombres de apariencia rara que vio a Tor conversar en el callejon."
    "Rápidamente se esconden detrás de un poste de alumbrado público."
    p "Ya les dije que quite la  pulperia. No tengo más ingresos, es más ando buscando trabajo por lo mismo." 
    m "Sabemos que tenes cash escondido, dont lie to me man, no pagaste el último mes, no busques fayas man."
    p "No se de que hablan, saben que ese mes no les pague porque ya nadie me compraba."
    a "Tenés 1 minuto, para sacar la guita, si no quieres plomo dentro de vos."
    p "Ya estoy harto de esto!!! ¿Acaso quieren que deje de darle de comer a mi hijo?" 
    p "Ya no soporto esta injusticia, por escoria como ustedes es que no progresa este país!!!"
    m "Dame el cash man y nadie sale herido."
    p "¡Dejame en paz!"
    a "Apurate."
