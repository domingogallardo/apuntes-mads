
# Desarrollo de software #

Puntos a tratar:

- Metáforas del desarrollo de software
- Capacidad de cambio del software
- Artículo de Fowler sobre el desarrollo como proceso no predecible
- Artículo No Silver Bullet

## Software ##

El software es un invento muy reciente de la humanidad. Fue a mitad
del siglo XX cuando se empezaron a utilizar los primeros computadores
electrónicos programables en organismos oficiales y grandes
empresas. Y los primeros lenguajes de programación de alto nivel
(FORTRAN y Lisp) se desarrollaron a finales de los años 50 (ver
detalles en
[https://github.com/domingogallardo/historia-computadores](https://github.com/domingogallardo/historia-computadores)). 

La programación, por tanto, es una profesión relativamente joven con
poco más de 60 años. Todavía están vivos (¡y activos!)
algunos programadores que trabajaron con los primeros computadores como
[Donald Knuth con el IBM
650](https://catonmat.net/donald-knuths-first-computer). Comparémoslo
con profesiones o disciplinas como medicina, física, derecho o
arquitectura, todas ellas con cientos de años de antigüedad.

Podemos decir que el software es el invento más importante y
complicado de la historia de la humanidad. El software ha conquistado
el mundo y está presente en todos los aspectos de la vida actual. El
entretenimiento, la medicina, la economía, etc. dependen cada vez más
de complejos sistemas de software desarrollados y mantenidos por
ingenieros/as como vosotros/as. Detrás de cualquier sistema de
software está un conjunto de personas que ha tenido que interactuar,
decidir, entender y modificar decenas de miles de líneas de código.

Hoy en día, gracias a servicios como GitHub, podemos echar un vistazo
al código de muchos de estos sistemas software y a su
evolución. Algunos ejemplos:

- [CartoDB](https://github.com/CartoDB/cartodb). Software español para representación visual de datos geográficos.
- [Guice](https://github.com/google/guice). Framework de inyección de dependencias en Java.
- [swift-nio](https://github.com/apple/swift-nio). Framework asíncrono de entrada-salida en Swift.
- [Spring Boot](https://github.com/spring-projects/spring-boot). Framework web en Java
- [Swift](https://github.com/apple/swift). Compilador y librería
  stándar de Swift. Escrito en C++ y Swift.


## Metáforas ##

Cuando queremos explicar algo complejo, muy a menudo usamos
metáforas. Las metáforas permiten relacionar conceptos desconocidos
con situaciones usuales ya vistas y nos permiten arrojar nueva luz
sobre estos conceptos desconocidos (¡esto ha sido una metáfora!).

En la metáfora anterior lo desconocido lo comparamos con una
habitación a oscuras que podemos explorar con la luz con una
linterna. La metáfora nos da una indicación de en qué consiste el
proceso de investigar algo. Mediante ella nos damos cuenta de la
importancia de la dirección en la que estamos apuntando la linterna y
de la necesidad moverla en varias direcciones. La metáfora nos lleva
entonces a pensar que para conocer algo desconocido hay que estudiarlo
desde distintos puntos de vista, siempre cambiando el detalle de lo
que estamos estudiando, hasta poder conocerlo en su totalidad (haber
iluminado toda la habitación).

La metáfora anterior puede o no ser correcta. Lo importante es que al
formularla hemos tenido una representación de algo desconocido (el
proceso de investigar) basada en algo conocido (explorar una
habitación oscura con una linterna). Y esa es muy importante, porque
nos representación nos lleva a tomar acciones y decisiones reales que
podrían haber sido distintas si hubiéramos usado otra metáfora
(explorar distintos aspectos del problema a resolver, en lugar de
centrarnos en un aspecto concreto y profundizar en él).

### Cultura de las organizaciones ###

Las metáforas son una parte importante de la cultura de una
organización. Una cultura proporciona un conjunto de reglas invisibles
que todos cumplimos de forma casi automática. Estas reglas
proporcionan un contexto común y favorecen que todos nos movamos en
una dirección similar.

Las metáforas, expresiones o giros del lenguaje proporcionan uno de
los elementos básicos de la cultura de la organización.

Por ejemplo, una organización centrada en la competición y con una
dinámica combativa con sus adversarios utilizará metáforas
relacionadas con la guerra o los deportes:

> "Hemos ganado este combate"  
> "Nos lo jugamos todo en esta campaña"  
> "Es una oportunidad de vida o muerte"  

Sin embargo, una organización orientada a la cooperación y al
planteamiento de situaciones de "win-win" en las negociaciones
utilizará otro tipo de metáforas:

> "Hemos coreografiado perfectamente la puesta en marcha del producto"  
> "Todos debemos participar en este viaje"  
> "Nuestro ecosistema premia la lealtad de nuestros clientes"  

Escoger las metáforas correctas es, por tanto, fundamental para
establecer una cultura, un estilo común de trabajo en el equipo o en
la empresa.

### Desarrollo de software ###

¿Por qué es interesante hablar de metáforas para referirnos al
software? Porque podemos utilizarlas para crear una cultura, una
visión, sobre nuestro trabajo, aplicable tanto a los compañeros del
equipo como a los managers y directivos con los que interactuamos.

El hablar sobre metáforas del desarrollo de software nos sirve también
para argumentar en contra de prejuicios o metáforas erróneas que se
pueden tener a priori. Metáforas que nosotros sabemos que no son
correctas, pero que están muy implantadas en la mentalidad de mucha
gente.

Veamos un listado de las metáforas que se han ido utilizando para el
desarrollo de software. Podemos encontrarlas en muchos sitios. En el
libro de Steve McConnell [_Code
Complete_](https://learning.oreilly.com/library/view/code-complete-second/0735619670/),
se dedica un capítulo completo a hablar de ellas.

> "A confusing abundance of metaphors has grown up around software
> development. David Gries says writing software is a science
> (1981). Donald Knuth says it's an art (1998). Watts Humphrey says
> it's a process (1989). P. J. Plauger and Kent Beck say it's like
> driving a car, although they draw nearly opposite conclusions
> (Plauger 1993, Beck 2000). Alistair Cockburn says it's a game
> (2002). Eric Raymond says it's like a bazaar (2000). Andy Hunt and
> Dave Thomas say it's like gardening. Paul Heckel says it's like
> filming Snow White and the Seven Dwarfs (1994). Fred Brooks says
> that it's like farming, hunting werewolves, or drowning with
> dinosaurs in a tar pit (1995). Which are the best metaphors?" 

Entre las metáforas más usadas se encuentran las siguientes.

#### Escritura ####

<img src="imagenes/literate-programming.jpg" width="150px" align="right"></img>

El software es algo que debe ser escrito y leído, de forma similar a
como escribimos una carta, un libro o un manual de instrucciones. 

Esta metáfora se lleva al extremo por los practicantes de [_literate
programming_](https://en.wikipedia.org/wiki/Literate_programming), un
paradigma de programación en el que el código queda embebido en una
explicación en lenguaje natural del problema que se está
resolviendo. Donald Knuth fue el fundador de este paradigma con su
libro _Literate programming_.

Elementos positivos de esta metáfora es que resalta el que el código
debe ser legible y entendible por los compañeros. El código se escribe
para las personas y no sólo para los computadores. Tan importante como
escribir el código es leerlo después. De hecho, para poder modificar
código debemos entenderlo, y para entenderlo debemos leerlo, hablar
sobre él, etc.

La metáfora no representa bien el carácter colectivo del desarrollo de
software. Habitualmente la escritura es un hecho individual, mientras
que el desarrollo es una labor de equipo. Tampoco comunica
correctamente el carácter evolutivo y cambiante del software. Cuando
un libro se termina de escribir muy raramente se modifica. Quizás sí
se hace en una siguiente edición de un manual de usuario o un libro
técnico, pero eso conlleva otra vez meses de esfuerzo. En el caso del
software es cambio es continuo y de un día para otro. Además el software se
escribe apoyándose en otro software que previamente se ha
desarrollado y depende de él. Estas dependencias tampoco se recogen en
la metáfora.
  
#### Jardinería ####

<img src="imagenes/jardineria.png" width="150px" align="right"></img>

En su libro [The Pragmatic
Programmer](https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977)
David Thomas y Andrew Hunt repasan la metáfora de la jardinería.

> "Software is more like gardening—it is more organic than concrete."

El crecimiento y cuidado de un jardín es algo orgánico. Se plantan
inicialmente todas las cosas de acuerdo a un plan. Algunas de las
plantas crecen bien pero otras no, y las destinamos a compost. Podemos
mover las plantas y recolocarlas, para aprovecharnos de las relaciones
entre ellas, de las luces y las sombras, del viento y la
lluvia. Tenemos que podar o separar las plantas que crecen
demasiado. Y podemos recolocarlas también por motivos estéticos, para
combinar mejor los colores. Recogemos las semillas y fertilizamos las
zonas que necesitan ayuda extra. Continuamente monitorizamos la salud
del jardín, y hacemos ajustes (a la tierra, las plantas, la
disposición) conforme se necesita.

La metáfora recoge bien los aspectos evolutivos del software, pero no
la escala temporal. El desarrollo de software es mucho más dinámico y
rápido que el crecimiento del jardín. 

A priori podría ser difícil encontrar una correspondencia entre la
parte parte del crecimiento orgánico del jardín (semillas y plantas
que crecen por si mismas, en configuraciones poco predecibles) y el
desarrollo de software. El software no crece si se deja solo. ¿Y qué
es el viento, la lluvia o las problemas de la naturaleza? En el
desarrollo de software tenemos todo controlado (hacemos tests) y no
dependemos elementos externos. 

¿De verdad es así? ¿Está todo controlado? Si pensamos de esta forma
nos estamos olvidando del elemento fundamental del desarrollo de
software: los usuarios finales. Cuando dejamos el software
desarrollado en sus manos lo van a utilizar como ellos mejor sepan. Lo
van a intentar introducir en sus procesos de trabajo ya
consolidados. Y el software les va a proporcionar valor o no
dependiendo de lo bien que se adapte a esos procesos.

Los usuarios finales son el viento, la lluvia, las fuerzas de la
naturaleza del jardín. La única forma de saber si el software va a
proporcionarles valor es dejarlo crecer entre ellos.

La metáfora del jardín no es tan descabellada como parecía al
principio. 

#### Crecimiento por acreción ####


#### Construcción ####

- Cultivo por acreción (ostra): niveles que esconden detalles
- Construcción: planificación y objetivos

Otras metáforas:

- Película: proceso creativo de múltiples profesionales

Cada metáfora resalta unas características del desarrollo de software
y ninguna recoge completamente todas ellas. Por eso, dependiendo de
qué metáfora se use en nuestra empresa o equipo de desarrollo, se
estará enfatizando un aspecto y disminuyendo otros.



## Movimiento open-source ##

La aparición del movimiento de código abierto [a mediado de los años
90](https://en.wikipedia.org/wiki/History_of_free_and_open-source_software)
supuso un punto de inflexión en el desarrollo de los sistemas
software. Hasta entonces los sistemas de software eran sistemas
cerrados, gestionados por equipos de desarrollo altamente
jerarquizados, con procesos rígidos y un alto porcentaje de fallos. 

El movimiento de código abierto demostró que era posible crear de
forma distribuida y auto-organizada complejos sistemas de software con
decenas de miles de líneas de código como sistemas operativos ([Linux](https://en.wikipedia.org/wiki/Linux)),
editores de texto extensibles con un lenguaje de programación incluido
([Emacs](https://en.wikipedia.org/wiki/Emacs)) o bases de datos ([MySQL](https://en.wikipedia.org/wiki/MySQL)).



## Referencias ##

