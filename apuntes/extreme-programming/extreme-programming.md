# eXtreme Programming #

## Historia de XP ##

El origen de Extreme Programming (XP) se encuentra en la comunidad
Smalltalk, en particular en la colaboración entre Kent Beck y Ward
Cunningham a finales de los 80 en temas relacionados con el diseño y
programación orientada a objetos. Por ejemplo, en 1989, publicaron el
artículo [A laboratory for teaching object-oriented
thinking](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.129.4074)
en el que introducen las tarjetas CRC para definir las
responsabilidades de las clases en un diseño orientado a objetos.

En 1996 Kent Beck comenzó a trabajar en el Chrysler Comprehensive
Compensation System ([proyecto C3](https://www.martinfowler.com/bliki/C3.html), en el que conoció a
Ron Jeffries. Se trató de un proyecto de gestión Chrysler que se
hizo famoso no por terminarse con éxito (fue cancelado en 1999) sino
por considerarse el proyecto en el que nació XP.

El proyecto comenzó realmente en 1993, como un intento de reemplazar y
unificar numerosos sistemas de nóminas _legacy_ basados en
COBOL. Martin Fowler comenzó a participar en él como consultor en esta
época. En 1995 se tomó la decisión de reescribir todo el sistema en el
lenguaje de programación Smalltalk y Kent Beck tomó la dirección del
proyecto. Allí puso en acción todas las prácticas que después tomaron
el nombre de _Extreme Programming_ (aunque había utilizado enfoques
similares en proyectos previos). Beck contó también con la
colaboración de Ron Jeffries en el equipo. Ron fue también otro autor
del manifiesto ágil y de numerosas publicaciones relacionadas con XP y
metodologías ágiles.
  
El software se puso en producción en 1997, realizando la gestión de
nóminas de alrededor de diez mil personas. El proyecto continuó,
intentando cubrir al resto de empleados, pero terminó fracasando y se
detuvo el desarrollo en 1999 (volviéndose a poner en funcionamiento el
sistema _legacy_ en COBOL). Para esa fecha las prácticas XP ya se
habían popularizado y habían demostrado su éxito en otros proyectos (a
pesar de que, paradójicamente, su proyecto inicial terminara
fracasando).

<img src="imagenes/xp-books.png" width="200px" align="right"/>

En 1999 Kent Beck recopila todas sus ideas sobre XP en su primera
edición del "libro blanco" de Extreme Programming, en el que establece
el conjunto de valores, principios y prácticas iniciales de XP.

La metodología se vuelve muy popular a finales de los 90, siendo la
metodología ágil más popular al final de la década. De hecho, de las
17 personas que elaboran el manifiesto ágil en 2001, 6 provenían de la
filosofía de XP.

A mediados del 2000, en 2004, Kent Beck publica la segunda edición de
su libro. Esta nueva edición contenía una versión más estructurada y
madura de la metodología. En la primera edición se definían 12
prácticas principales que en la segunda se convierten en 13 y se suman
11 prácticas secundarias.

Las fechas de publicación de estos dos libros (finales de 1990s y
principios de 2000s) fueron el punto álgido del interés y la adopción
de XP. A partir aquí la metodología pierde popularidad y en la última
década y media ha sido sustituida por Scrum, una metodología más
general (menos orientada a desarrollo de software) que tiene roles y
ceremonias más establecidos y fáciles de replicar.

Sin embargo, paradójicamente, el interés por las prácticas XP no ha
dejado de crecer. Prácticas como el test driven development (TDD), la
refactorización, la integración continua o el pair programming son
cada vez más populares, aunque las encontramos en el marco de otras
corrientes como el [software
craftmanship](https://en.wikipedia.org/wiki/Software_craftsmanship).

<img src="imagenes/state-of-agile-practicas-desarrollo.png" width="300px" align="right"/>

De hecho, en el último informe sobre adopción de metodologías ágiles
[14th Annual State of Agile
Report](https://stateofagile.com/#ufh-i-615706098-14th-annual-state-of-agile-report/7027494)
en la lista de prácticas más populares (imagen derecha) aparecen
bastantes promovidas por XP: 

- Continuous integration (55%), 
- Refactoring (43%)
- Continuous delivery (41%)
- Pair programming (31%)
- Test Driven Development (30%)
- Collective Code Ownership (29%)


## Introducción rápida a XP ##


> XP involves as one team, in a sustainable process without imposed
> overtime, developers working in pairs who truly enjoy their work,
> and an informed and available customer to whom they regularly
> deliver releases. The system's design is clearly described for all
> by a forceful metaphor, driven by a comprehensive suite of developer
> and customer tests, and kept simple and understandable by constant
> refactoring and coding to uniform standards under the team's
> collective responsibility. This turns out to be a lot of fun and
> counter-intuitively effective.
>
> [Short definition of XP](https://web.archive.org/web/20160709051640/http://c2.com/cgi/wiki?ShortDefinitionOfXp)


## Valores ##

## Principios ##

<img src="imagenes/puente-principios-practicas.png" width="300px"/>

## Prácticas ##

<img src="imagenes/practicas-xp.png" width="600px"/>

### 1. Sit Together ###

<img src="imagenes/open-space-spotify.png" width="500px"/>

### 2. Whole Team ###

<img src="imagenes/cross-functional-team.png" width="500px"/>

### 3. Informative Workspace ###

<img src="imagenes/informative-workspace.png" width="500px"/>

### 4. Energized Work ###

<img src="imagenes/pomodoro-technique.png" width="200px"/>


### 5. Pair Programming ###

<img src="imagenes/pair-programming.png" width="300px"/>

<img src="imagenes/mob-programming.png" width="300px"/>

### 6. Stories ###

<img src="imagenes/story.png" width="250px"/>

<img src="imagenes/user-story-card.png" width="400px"/>

### 7. Weekly Cycle ###

### 8. Quarterly Cycle ###

### 9. Slack ###

### 10. Ten-Minute Build ###

### 11. Continuos Integration ###

<img src="imagenes/continous-delivery-pipeline.png" width="500px"/>

### 12. Test-First Programming ###

<img src="imagenes/tdd.png" width="400px"/>

### 13. Incremental Design ###

<img src="imagenes/evolutive-process.png" width="400px"/>

### Prácticas secundarias ###

Team

- Real Customer Involvement
- Team Continuity
- Shrinking Teams 

Programming

- Shared Code 
- Code and Test
- Single Code Base

Business

- Root-Cause Analysis 
- Negotiated Scope Contract
- Pay-Per-Use

Deliverying

- Incremental Deployment 
- Daily Deployment



## Referencias ##

- Ward Cunningham y otros, [Páginas de WikiWiki sobre Extreme Programming](http://wiki.c2.com/?ExtremeProgrammingRoadmap)
- Kent Beck (2004) [_Extreme Programming Explained: Embracing Change (Second
  Edition)_](https://learning.oreilly.com/library/view/extreme-programming-explained/0321278658/)
