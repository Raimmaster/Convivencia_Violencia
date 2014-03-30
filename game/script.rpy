# Fondos
image bg escenario1 = "escenario1.png"
image bg cuarto_nino = "cuartonino.png"
image bg escuela = "escuela2dejunio.png"
image bg trucha = "pulperia_shalom.png"

# Imagenes - Personajes 
# Vol
image vol abusador = "nino_abusador.png"
image vol asustado = "nino_asustado.png"
image vol desorientado = "nino_desorientado.png"
image vol enojado = "nino_enojado.png"
image vol feliz = "nino_feliz.png"
image vol incredulo = "nino_incredulo.png"
image vol llorando = "nino_llorando.png"
image vol platicando = "nino_platicando.png"
image vol dormido = "nino_dormido.png"
# image vol flip = im.Flip("nino_dormido.png", horizontal=True)

# Papá
image papa abusador = "papa_abusador.png"
image papa asustado = "papa_asustado.png"
image papa baleado = "papa_baleado.png"
image papa decapitado = "papa_decapitado.png"
image papa feliz = "papa_feliz.png"
image papa incredulo = "papa_incredulo.png"
image papa llorando = "papa_llorando.png"
image papa platicando = "papa_platicando.png"
image papa enojado = "papa_enojado.png"

# Tor
image tor asustado = "tor_asustado.png"
image tor abusador = "tor_abusador.png"
image tor golpeado = "tor_golpeado.png"
image tor incredulo = "tor_incredulo.png"
image tor platicando = "tor_platicando.png"

# Audino
image aud normal = "Audino.png"
image aud alegre = "Audino alegre.png"
image aud confu = "Audino confundido.png"
image aud enoj = "Audino enojado.png"
image aud furi = "Audino furioso.png"
image aud mole = "Audino molesto.png"
image aud triste = "Audino triste.png"
image aud flip = im.Flip("Audino.png", horizontal=True)

# Morfeno
image mof aver = "monferno_avergonzado.png"
image mof tris = "monferno_triste.png"

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
    play music "coming-back-home.ogg"
    scene black
    with fade
    "Beep Beep…" 
    "¿Tienes un nombre?"

    menu:

        "Sí.":
            $ perName = renpy.input(_("¿Cual?")) or _("Volentto")

        "No.":    
            "¿Estás seguro que tu nombre no es Volentto?"
            "..."
            $ perName = "Volentto"

    scene bg cuarto_nino
    with fade

    show papa platicando at right
    with dissolve
    p "Hijo, ya es hora de ir a la escuela."
    show vol dormido at left
    with dissolve
    per "Solo 5 minutos mas."
    show papa abusador at right
    with dissolve
    p "Levantate y báñate. Te tienes que alistar para poder ir a la escuela."
    
    "15 minutos después."
    show vol feliz
    with dissolve
    show papa feliz
    with dissolve
    per "¡Ya estoy listo!"    
    p "Esta bien ya podemos irnos."
    show vol desorientado
    with dissolve
    per "¿Hoy tampoco abriras la pulpería?"
    show papa platicando
    with dissolve
    p "No puedo hacerlo en este momento, no preguntes porque, solo obedece."
    per "Ya tienes mucho tiempo sin abrirla, deberías hacerlo."
    show papa abusador
    with dissolve
    p "¡Calla, te dije que no preguntaras porque!"
    "Una sombra se percibe detrás de ellos."
    "***5 MINUTOS DESPUES****"
    jump escuela

label escuela:
    scene bg escuela 
    with fade
    show papa feliz at right
    with dissolve
    p "¡Cuidate hijo! Nos vemos en la casa."
    hide papa
# Junior entra a la escuela y se encuentra con un niño llamado Tor.
    show vol desorientado at left
    with dissolve
    show tor platicando at right
    with dissolve
    t "¡Hey, [perName!t]! ¿Que onda?"
    show vol platicando
    with dissolve
    per "¡Pues nada, Vengo llegando de mi casa!"
    show tor abusador at right
    with dissolve
    t "¡Ah que bueno! ¿Por qué tu papa no ha abierto la pulpería? He querido comprar varios dulces y no puedo."
    per "Pues, la verdad no se. Hoy en la mañana me dijo que no le preguntara sobre eso. Pero no entiendo porque, si el tiene toda la pulpería llena de muchos dulces y cosas. Aparte que le he visto mucho dinero."
    show tor incredulo 
    with dissolve
    t "Mmm…¡Que raro! Quisiera ver que tantas cosas tiene tu padre, tal vez podemos comer un par de dulces, asi no se desperdician. "
    show vol feliz
    with dissolve
    per "¡Buena idea, vamos!"
    jump camino_casa

label camino_casa:
    scene bg escenario1
    with fade
    "Ambos niños van caminando por la calle, cuando Tor se desvía por un callejón y habla con un par de muchachos de apariencia rara."
    "Junior  lo espera en el mismo lugar mientras Tor conversa. Tor regresa donde Junior."
    show vol incredulo at left
    with dissolve
    show tor platicando at right
    with dissolve
    t "¡Disculpame! Estaba hablando con un par de amigos."
    show vol platicando 
    with dissolve
    per "¡Ah no te preocupes! Vamos a la casa. Apresurémonos antes de  que mi padre llegue."
    jump llegar_casa

label llegar_casa:
    stop music fadeout 1.0
    scene bg trucha
    with fade
    "Llegan a la esquina de la calle y observan al padre conversar con los mismos hombres de apariencia rara que vio a Tor conversar en el callejon."
    "Rápidamente se esconden detrás de un poste de alumbrado público."
    show aud normal at left 
    with dissolve
    show mof aver at center behind aud
    with dissolve
    show papa asustado at right
    with dissolve
    p "Ya les dije que quite la  pulperia. No tengo más ingresos, es más ando buscando trabajo por lo mismo." 
    show aud enoj
    with dissolve
    m "Sabemos que tenes cash escondido, dont lie to me man, no pagaste el último mes, no busques fayas man."
    show papa incredulo 
    with dissolve
    p "No se de que hablan, saben que ese mes no les pague porque ya nadie me compraba."
    show aud furi
    with dissolve
    a "Tenés 1 minuto, para sacar la guita, si no quieres plomo dentro de vos."
    show papa enojado
    with dissolve
    p "Ya estoy harto de esto!!! ¿Acaso quieren que deje de darle de comer a mi hijo?" 
    p "Ya no soporto esta injusticia, por escoria como ustedes es que no progresa este país!!!"
    m "Dame el cash man y nadie sale herido."
    p "¡Dejame en paz!"
    a "Apurate."
    show aud normal
    with dissolve
    "Uno de los mareros sacan sus puñales contra Pancho..."
    show papa baleado 
    with dissolve
    "...apuñalándolo 50 veces por todo el cuerpo, desfigurando su rostro en el proceso y degollándolo."
    
    "Los 2 mareros salen corriendo a esconderse. El niño atónito observa como el cuerpo del padre, ensangrentado y con muchos tiros, yace en el piso de su casa."
    "Los pandilleros se disponían a huir, cuando observaron a Junior de pie desde la otra esquina. Junior se dio cuenta que los pandilleros que habían matado a su padre lo habían visto escondido detrás del poste de energía eléctrica."
    m "Hey, ese mico nos vio. Hay que darle jabón."
    a "Vos no viste nada güirro. Si nos damos cuenta de que andas de sapo de vamos a matar."
    m "Let’s go man, go, go."
    "Los pandilleros salen corriendo y se pierden a lo lejos."
    show papa decapitado 
    with dissolve
    "Horas después las personas salen de su casa a ver lo que había ocurrido, un vecino llamó a la policía y la ambulancia. Junior  queda atónito por lo que ha ocurrido y no se mueve." 

# TOMA DE DECISION
    play music "some-time-later.ogg"
    scene black 
    with fade
    "Los años pasaron y [perName!t] seguía con trauma después de la muerte de su padre, al haberla presenciado y sobre todo, haber sido amenazado por los mismo pandilleros que habían matado a su padre."

    "¿Qué harás ahora?"

    menu:
        "Mejorar a la sociedad.":
            jump path_bueno

        "Vengarme de los que asesinaron a mi padre.":
            jump path_batman
