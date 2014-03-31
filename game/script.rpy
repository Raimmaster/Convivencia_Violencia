# Fondos
image bg escenario1 = "escenario1.png"
image bg cuarto_nino = "cuartonino.png"
image bg escuela = "escuela2dejunio.png"
image bg trucha = "pulperia_shalom.png"
image bg trucha2 = "pulperia_shalom2.png"
image bg final = "escena_final.png"
image escena_hostigamiento = "escena_hostigamiento.png"

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

# Tía
image tia = "tia.png"

# Personajes

define p = Character('Papá', color="#c8ffc8")
define t = Character('Tor', color="#c8dfc9")
define m = Character('Monferno', color="#c7fdc9")
define a = Character('Alduino', color="#c5ddc9")
define tia = Character('Tía', color="#c8ffc8")

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
    per "Solo 5 minutos más."
    show papa abusador at right
    with dissolve
    p "Levantate y báñate. Te tienes que alistar para poder ir a la escuela."
    
    "15 minutos después."
    show vol feliz
    with dissolve
    show papa feliz
    with dissolve
    per "¡Ya estoy listo!"    
    p "Está bien ya podemos irnos."
    show vol desorientado
    with dissolve
    per "¿Hoy tampoco abriras la pulpería?"
    show papa platicando
    with dissolve
    p "No puedo hacerlo en este momento, no preguntes porque, solo obedece."
    per "Ya tienes mucho tiempo sin abrirla, deberías hacerlo."
    show papa enojado
    with dissolve
    p "¡Calla, te dije que no preguntaras porque!"
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
    per "Pues, la verdad no se. Hoy en la mañana me dijo que no le preguntara sobre eso." 
    per "Pero no entiendo porque, si el tiene toda la pulpería llena de muchos dulces y cosas. Aparte que le he visto mucho dinero."
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
    "Ambos niños van caminando por la calle, cuando Tor se desvía por un callejón y habla con un par de muchachos de apariencia de poco fiar."
    "[perName!t]  lo espera en el mismo lugar mientras Tor conversa. Tor regresa donde [perName!t]."
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
    play music "applying-law.ogg"
    scene bg trucha2
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
    "Antes de que uno de los mareros saque sus puñales contra Pancho..."
    show countdown at Position(xalign=.1, yalign=.1)
    menu:
        "Caminar...":
            "[perName!t] caminó hacia donde su padre..."
        "Gritar...":
            per "¡AAAAAAH!"
        "Quedarse inmóvil del miedo...":
            per "..."

    hide countdown
    show papa baleado 
    with dissolve
    "El marero le apuñala y dispara por todo el cuerpo, desfigurando su rostro en el proceso y degollándolo."
    show papa decapitado at right
    with dissolve
    "Los 2 mareros salen corriendo a esconderse. El niño atónito observa como el cuerpo del padre, ensangrentado y con muchos tiros, yace en el piso de su casa."
    "Los pandilleros se disponían a huir, cuando observaron a [perName!t] de pie desde la otra esquina. [perName!t] se dio cuenta que los pandilleros que habían matado a su padre lo habían visto escondido detrás del poste de energía eléctrica."
    with fade
    m "Hey, ese mico nos vio. Hay que darle jabón."
    scene bg trucha
    with fade
    show aud flip at right
    with dissolve
    show vol asustado at left
    with dissolve
    a "Vos no viste nada güirro. Si nos damos cuenta de que andas de sapo te vamos a matar."
    m "Let’s go man, go, go."
    hide aud
    with fade
    "Los pandilleros salen corriendo y se pierden a lo lejos."
    show papa decapitado at right
    with dissolve
    show vol llorando
    with dissolve
    "Horas después las personas salen de su casa a ver lo que había ocurrido, un vecino llamó a la policía y la ambulancia." 
    
    scene bg final
    with fade
    "[perName!t]  queda atónito por lo que ha ocurrido y no se mueve." 
    "Después de sufrir el shock de haber presenciado el asesinato de su padre, [perName!t] fue llevado a vivir con su tía a la colonia el Rocosal."   

# TOMA DE DECISION
    stop music fadeout 1.0
    play music "some-time-later.ogg"
    scene black 
    with fade

    "Aunque un año haya transcurrido, [perName!t] aun se encuentra afectado emocionalmente por la muerte de su padre, pero igual el mundo sigue girando y proponiendo situaciones en las que nuestro personaje ha de decidir su destino mediante su juicio."

    "Hoy es día de escuela, así que sale de casa mientras su tía le dice adiós."

    "[perName!t] tiene que ser cuidadoso, puesto que al igual que su papá, su tía no dispone de holgura económica y viven en un sector de alto riesgo."

    "Un día, mientras [perName!t] sale de la escuela..."
    scene escena_hostigamiento with fade
    "Frente al camino de regreso a casa, hay un chiki molestando a un niño."
    "No se distingue qué, pero parece que intenta obligarlo a hacer algo."
    "[perName!t] se detiene."
    scene black with fade
    menu:
        "Pasar por otro lado sin llamar la atención":
            "[perName!t] logra llegar a salvo a su casa y espera no encontrarse nunca más en el futuro con una cría de esas."
        "Pasar de largo sin voltear a ver a nadie, de todas formas el chiki tiene las manos llenas":
            "Al estar bastante cerca de la situación, el chiki lo llama y por nervios [perName!t] se tropieza con una piedra
y cae encima de los tipos."
            "El chiki lo toma personal y los agarra a ambos a patadas."
            "Al final de la paliza, deciden regresar a sus casas sin el dinero de la comida para mañana."
        "Tengo miedo, me esconderé.":
            "Detrás de la pared de una casa, [perName!t] se queda paralizado sin poder mover las piernas."
            "Mientras tanto, el otro niño es desbalijado."
            "Un rato después, [perName!t] decide volver a su casa. Será mejor que sea rápido, ya que se hizo pipí."
        "Fingir un estornudo bien fuerte y gritar varios nombres simulando llamar gente que lo acompañan":
            "El chiki se pone alerta cuando escucha ruido de multitud, no sin hacer una última amenaza al niño, decide abandonar
con prontidud la escena."
            "El niño hostigado, de lejos le hace un gesto discreto a [perName!t], mostrandole agradecimiento."
            "El día siguiente a la hora del recreo, el niño del día anterior le invita un pollo con tajadas que ambos comparten."
