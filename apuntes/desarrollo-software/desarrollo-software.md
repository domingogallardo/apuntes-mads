
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
poco más de 60 años. Todavía están vivos (y algunos siguen activos)
los programadores que trabajaron con los primeros computadores como
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


- Escritura: código escrito y leído
- Cultivo: crecimiento orgánico
- Cultivo por acreción (ostra): niveles que esconden detalles
- Construcción: planificación y objetivos

Otras metáforas:

- Sistema legal: relación entre componentes
- Película: proceso creativo de múltiples profesionales


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

