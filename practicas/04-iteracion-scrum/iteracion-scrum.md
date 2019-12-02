# Práctica 4: Sprint de Scrum 

## Objetivos y resumen de la práctica

En esta práctica seguiremos trabajando con los mismos equipos y
proyecto que en la práctica 3.

Durante las 4 semanas de la práctica el equipo realizará una iteración
para desarrollar un incremento de la aplicación
`TodoList`. Usaremos el mismo flujo de trabajo de la práctica 3 para
desarrollar sobre la rama `develop`:

- Una tarjeta en el tablero de Trello para cada historia de
  usuario. Cada historia de usuario continuará la numeración que
  comenzamos en la práctica 2. 
- La historia de usuario se puede descomponer en mas de un issue en
  GitHub o hacerla en un único issue si es corta. En cualquier caso,
  se deberán etiquetar los issues con la etiqueta asociada a la
  historia de usuario.
- Cada issue se resuelve en una rama y se integra en `develop` con un
  pull request.
- En el tablero en GitHub se representan el estado de los issues y
  pull requests
- El repositorio está conectado a Travis para hacer la integración
  continua. Se comprueban de forma automática los tests en las
  integraciones de los pull requests en `develop` y se sube una imagen
  docker a Docker Hub cuando se realiza la integración. 
- En Docker Hub se tienen numerados todos los builds exitosos de
  `develop`, y está etiquetada como `latest` la última versión de la
  imagen.

Al final de la práctica se lanzará una nueva versión (`1.4.0`), usando
el mismo flujo de trabajo que en la práctica anterior.

Además, aplicaremos algunos elementos de Scrum y prácticas de XP:

- Planificación del sprint
- Reuniones de _scrum diario_
- Revisión del sprint (se hará el último día de clases de la asignatura)
- Retrospectiva del sprint
- Al menos dos sesiones de _pair programming_ en las que deben
  participar todos los miembros del equipo. Se harán en clase los días
  4 y 11 de diciembre.


## Artefactos del sprint ##

El equipo utilizará un tablero Trello para documentar el backlog del
producto y el tablero de GitHub para el backlog del sprint.

### Tablero Trello ###

Cada equipo creará un tablero Trello compartido en el que se anotarán
en forma de tarjeta las historias de usuario candidatas para realizar en el
sprint. El tablero debe ser público y su enlace se incluirá en el
título del proyecto en GitHub, para que el profesor pueda consultarlo.

El tablero Trello contendrá el **backlog del producto** y servirá para
trabajar con estas historias de usuario en formato de tarjeta,
escribirlas rápidamente, estimarlas y ordenarlas.

Cada tarjeta Trello contendrá:

- Título de la historia de usuario
- Descripción en el formato visto en teoría: "Como ... quiero ... para
  ..."
- Estimación del tamaño de la historia (definido con una etiqueta)
- Responsable de la historia de usuario (otra etiqueta) : miembro del
  equipo que liderará el desarrollo de la historia. Puede que más de
  una persona intervenga en el desarrollo de la historia, pero una
  persona será la responsable.
- Enlace a una página Google Docs con los **detalles de la historia de
  usuario** realizada por el responsable de la historia de usuario:
    - Título de historia de usuario
    - Descripción y detalles
    - Borrador del aspecto de la interfaz de usuario resultante
      (dibujado a mano y fotografiado o con alguna herramienta de
      mockup, lo que os resulte más sencillo)
    - Condiciones de satisfacción (COS). Estas condiciones de
      satisfacción son esenciales a la hora de determinar el alcance
      de la historia.

Utilizaremos un tablero en formato Kanban, definiendo cinco columnas
que representarán las fases por las que pasará cada historia de
usuario: `Backlog`, `Listas`, `En marcha`, `En prueba` y `Terminadas`.

|Tipo de columna | Características de las historias                                                                 |
|----------------|--------------------------------------------------------------------------------------------------|
| **Backlog**    | Estimado el tamaño de la historia y pendiente de elaborar detalles.                              |
| **Listas**     | Se han elaborado todos los detalles de la historia (página Google Docs).                         |
| **En marcha**  | Se ha abierto el primer _issue_ en GitHub y el equipo ha comenzado a desarrollar la historia.    |
| **En prueba**  | La historia completa está integrada en `develop` y publicada en la última versión de Docker Hub. |
| **Terminadas** | Se han comprobado las condiciones de satisfacción en la imagen descargada de Docker Hub.         |

!!! Important "Importante"
    Aunque parezca evidente, lo resalto: hay que pasar las fases de
    forma ordenada. No podemos empezar a desarrollar una historia de
    usuario antes de haber terminado todos sus detalles en la página
    de Google Docs.

### Tablero GitHub ###

El tablero GitHub contendrá el **backlog del sprint** en el que se
visualizarán los _issues_ con los trabajos que está realizando el
equipo de desarrollo. 

En los issues podremos tener:

- Desarrollo de historias de usuario (en parte o completas)
- Bugs y refactorizaciones
- Desarrollos técnicos necesarios no relacionados con una historia de
  usuario en concreto

Usaremos las etiquetas para definir el tipo de issue:

- Código de historia de usuario
- Bug
- Refactor
- Mejora técnica

Los primeros tipos de issue serán obligatorios y los tres siguientes
serán opcionales, dependiendo de si el proyecto lo requiere.

En cuanto a las columnas, definiremos el tablero como un tablero
Kanban. Usaremos las mismas columnas que hasta ahora, con los
issues/_pull requests_ moviéndose por ellas según se vayan
desarrollando.

| Tipo de columna    | Características de los issues |
|--------------------|-------------------------------|
| **Sprint backlog** | Issues esperando a ser desarrollados. |
| **In progress**    | El issue tiene asignado un responsable y se ha abierto una rama para su desarrollo. |
| **In pull request**| El issue tiene un pull request abierto (se archivará la tarjeta del issue y se dejará sólo la tarjeta del pull request).|
| **Done**           | El pull request que se ha resuelto y el issue está integrado en `develop`.|


## Planificación del sprint

La planificación del sprint se realizará en la clase de prácticas del
27 de noviembre. Se seleccionarán las historias de usuario a realizar
en el sprint y se completarán sus descripciones.

### Selección del backlog ###

Al comienzo de la práctica el equipo seleccionará las historias de
usuario a realizar en la iteración, de forma que el tamaño total de
las historias seleccionadas sea de **18 puntos** (6 puntos por persona). 

Podrán escogerse cualquiera de las historias definidas en el taller de
_mapping_ de historias de usuario realizado en clase, o idear alguna
nueva. El resultado del taller de _mapping_ de historias de usuario
está recogido en el siguiente tablero:

- [https://trello.com/b/V4zRe1Hi/historias-de-usuario-todolist](https://trello.com/b/V4zRe1Hi/historias-de-usuario-todolist)

Todos los miembros deberán tomar el papel _product owner_ y aportar
ideas y sugerencias para definir las historias de usuario. 

Las historias seleccionadas se incluirán en la columna **Backlog** del
tablero Trello del equipo. Cada historia se analizará,
especificando claramente su descripción y su alcance. 

En la tarjeta de Trello se escribirá el título, el tamaño (etiqueta) y
unas notas rápidas con alguna aclaración. También se enlazará un
documento Google Docs en el que el responsable de la historia deberá
especificarla con más detalle.

### Responsables de historia de usuario ###

Una vez seleccionadas todas las historias los miembros del equipo
elegirán responsables para cada historia, se creará su página Google
Docs, y se detallará allí las condiciones de satisfacción y el
borrador de la interfaz de usuario.

Se creará el issue (o issues) correspondiente a la historia de usuario
y se añadirá el responsable al issue.

Todos los miembros del equipo deberán realizar un trabajo equitativo,
y se repartirán las historias de forma que queden también equilibrados
los tamaños totales de las historias asignadas a cada uno.

## Desarrollo del sprint

Se deberán realizar los siguientes eventos definidos por Scrum,
tomando nota y redactando un informe con la fecha de la reunión, su
duración y su desarrollo:

1. Scrum diario (al menos simular 2 reuniones: la segunda y tercera
   semana). En nuestro "tiempo simulado" en las prácticas, una semana
   es como un día de trabajo completo en una empresa.
2. 2 sesiones de _pair programming_ con turnos de 20 minutos (en cada
   sesión se deben hacer 4 turnos). Se podrán hacer estas sesiones en
   clase de prácticas.
3. Retrospectiva del sprint (en la semana final)

### Desarrollo de issues e historias ###

- Cada miembro del equipo selecciona el issue a desarrollar. Lo normal
  es que cada miembro desarrolle un único issue de forma concurrente,
  aunque podría darse el caso de ser más (por ejemplo, si algún issue
  no puede terminarse por estar bloqueado por otro).

- Se deben crear ramas para los issues y pull requests con revisión de
  código para integrar los pull requests en master. Es suficiente con
  que haya una única aprobación para integrar el pull request.

- Seguimos usando Travis para la integración continua.

- Como hemos hecho hasta ahora, cada issue debe contener **tests
  automáticos** que prueben los cambios.
  
- Una vez terminados todos los issues de una historia de usuario, el
  responsable de la historia moverá su tarjeta en el tablero Trello a
  `En prueba` y el miembro del equipo responsable del producto
  realizará las **pruebas manuales** especificadas en sus COS sobre la
  última imagen subida a Docker. Cuando se hayan superado todas las
  pruebas se pasará la historia a `Terminada`. Si se detectara algún
  fallo, se volverá la historia a `En marcha` y se abrirá un issue de
  tipo `bug` para resolver el problema.

### Publicación de nueva versión  ###

Al final del desarrollo se deberá lanzar una nueva release (1.4.0) en
la rama `master`, y subir a DockerHub la imagen resultante con la
etiqueta `1.4.0`.

### Documentación del desarrollo ###

- Documentar los _dailys_, para incluir un informe en el documento.
- Documentar las sesiones de _pair programming_.
- Documentar la evolución semanal de los tableros Trello y GitHub y
  calcular alguna métrica del desarrollo (pull requests por semana,
  velocidad de la semana, gráfica de burndown, etc.).

## Entrega y evaluación

La práctica tiene una duración de 4 semanas.

- Se realizará una **revisión del sprint** de 20 minutos en las
  **clases de teoría y práctica del 18 de diciembre**. La revisión
  constará de:
    - Presentación con diapositivas en la que se explicará la
      **metodología seguida** en el sprint y las **nuevas funcionalidades** introducidas.
    - Demostración de las nuevas funcionalidades utilizando la última
      imagen docker subida a Docker Hub.

- La fecha de entrega de la práctica será el **domingo 22 de
  diciembre**. En esa fecha se deberá tener disponible:
    - Entrega en Moodle la última versión del proyecto subida a
      GitHub. Deberá contener:
        - Directorio `doc` en el repositorio del proyecto en el que se
          incluirá un documento PDF o Markdown con la memoria de la
          práctica y un PDF con las diapositivas presentadas en la
          demo. En la memoria de la práctica se incluirá:
            - **Sprint Backlog**: historias de usuario escogidas para el
              sprint (copiar la descripción, las condiciones de
              satisfacción y el borrador de interfaz de usuario tal y
              como aparecen en la Wiki).
            - **Funcionalidades implementadas**: breve descripción para el
              usuario y breve descripción técnica.
            - **Informe sobre la metodología seguida**: ejemplos de
              evolución del tablero, alguna métrica del desarrollo
              realizado en el sprint, etc.
            - **Informes sobre las reuniones de Scrum**: planificación del
              sprint, scrum diario, revisión y sobre las sesiones de
              _pair programming_.
            - Resultado de la retrospectiva: qué ha ido bien en el
              sprint y qué se podría mejorar en el siguiente sprint.
    - Versión 1.4.0 de la máquina Docker en Docker Hub (es la máquina
      que voy a usar para revisar la ejecución de la práctica).
    - El repositorio GitHub deberá incluir el tablero con el backlog
      del sprint con los PR completados.
    - El tablero de Trello deberá incluir el backlog del producto con
      las historias de usuario que se debían implementar en el sprint
      y los enlaces a los documentos Google Docs con sus detalles.

La calificación de la práctica tiene un peso de un 15% en la nota
final de la asignatura.

Para la evaluación se tendrá en cuenta:

- Desarrollo continuo de los issues
- Corrección del código
- Correcto funcionamiento
- Informe de la práctica
- Si el trabajo de algún miembro del equipo es significativamente de
  menor calidad y/o cantidad que el del resto, se penalizará su
  calificación
