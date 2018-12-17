# Práctica 4: Sprint de Scrum 

## Objetivos y resumen de la práctica

En esta práctica seguiremos trabajando con los mismos equipos y
proyecto que en la práctica 3.

Durante las 4 semanas de la práctica el equipo realizará una iteración
para desarrollar un incremento de la aplicación
`todolist`. Usaremos el mismo flujo de trabajo de la práctica 3 para
desarrollar sobre la rama `develop`:

- Una página en la Wiki de GitHub para cada historia de usuario. La
  historia de usuario se puede descomponer en mas de un issue, o
  seguir como hasta ahora haciendo un issue por historia de usuario.
- Cada issue se resuelve en una rama y se integra en `develop` con un
  pull request.
- En el tablero en GitHub se representan el estado de los issues y
  pull requests
- El repositorio está conectado a Travis que comprueba de forma
  automática los tests en las integraciones de los pull requests en
  `develop` y sube una imagen docker a Docker Hub cuando se realiza la
  integración.
- En Docker Hub se tienen numerados todos los builds exitosos de
  `develop`, y está etiquetada como `latest` la última versión de la
  imagen.

Al final de la práctica se lanzará una nueva versión (`1.4.0`), usando
el mismo flujo de trabajo que la práctica anterior.

Además, aplicaremos algunos elementos de Scrum y prácticas de XP:

- Planificación del sprint
- Reuniones de _scrum diario_
- Revisión del sprint (se hará el último día de clases de la asignatura)
- Retrospectiva del sprint
- Al menos dos sesiones de _pair programming_ en las que participen
  todos los miembros del equipo.

## Planificación del sprint

En la reunión de planificación del sprint se seleccionarán las
historias de usuario a realizar en el sprint y se completarán sus
condiciones de satisfacción.

### Artefactos del sprint ###

El equipo utilizará un tablero Trello, la wiki y el tablero de GitHub
para documentar el backlog del producto y el backlog del sprint.

#### Tablero Trello ####

Cada equipo creará un tablero Trello compartido en el que se anotarán
en forma de tarjeta las historias de usuario candidatas para realizar en el
sprint.

El tablero Trello servirá para trabajar con estas historias de usuario
en formato de tarjeta, escribirlas rápidamente, estimarlas y ordenarlas.

#### Wiki ####

La wiki del proyecto deberá contener los detalles de las historias de
usuario escogidas para realizar en el sprint.

Como hasta ahora, se definirá una página de la wiki para cada historia
de usuario. En la página se escribirá el título de la historia, su
descripción y sus condiciones de satisfacción.

También se deberá incluir en cada historia de usuario un borrador del
aspecto de la interfaz de usuario resultante ([cómo añadir imágenes a
la wiki en
GitHub](https://help.github.com/articles/adding-images-to-wikis/)). Debe
ser un borrador hecho a mano y fotografiado o escaneado. 

También se actualizará la página _home_ y el índice lateral para
incluir las nuevas historias de usuario.

#### Tablero ####

La primera columna del tablero será el backlog del sprint en el que se
añadirán los issues correspondientes a historias de usuario y bugs.

Podría darse el caso en el que una historia de usuario se divida en
más de un issue. En ese caso indicaremos en el título del issue y
en su descripción a qué historia de usuario se corresponde.

El resto de columnas las utilizaremos como un tablero Kanban. Como
hasta ahora, los issues/_pull requests_ se irán moviendo por ellas
según se vayan desarrollando.

Tendremos las siguientes columnas:

- **Sprint backlog**: Issues que implementan las historias de usuario
  (o subtareas de las mismas) y los bugs a terminar en el sprint.
  
- **In progress**: Historias de usuario y bugs que se están
  desarrollando.

    Para pasar un issue que corresponde a una historia de
    usuario a esta columna, debe estar terminada su página en la wiki
    y debe tener un responsable.

- **In pull request**: issues que tienen un pull request abierto (se
  archivará la tarjeta del issue y se dejará sólo la tarjeta del
  pull request).

- **QA**: Historias de usuario a las que se les está realizando
  pruebas funcionales y de rendimiento. 
  
    Cuando todos los pull requests (correspondientes a issues y
    bugs) de una historia de usuario se han integrado, se anota en la
    página de la wiki el enlace al build en DockerHub y se prueba la
    imagen en un entorno de stage, realizándose pruebas funcionales y
    de rendimiento relacionadas con esa historia de usuario. Si se
    detectan nuevos bugs, se abren nuevos issues en GitHub para
    resolverlos, y la historia queda detenida en QA.
  
- **Done**: pull requests que se han probado satisfactoriamente.

### Selección del backlog ###

Al comienzo de la práctica el equipo seleccionará las posibles
historias de usuario a realizar en la iteración y estimará su
tamaño. Las anotarán en un tablero Trello compartido con el equipo y
con el profesor. El profesor validará la selección y la estimación de
tamaños.

Podrán escogerse cualquiera de las historias definidas en el taller de
_mapping_ de historias de usuario realizado en clase, o idear alguna
nueva.

El resultado del taller de _mapping_ de historias de usuario está
recogido en los siguientes tableros:

- [https://trello.com/b/KbUefDdN/mapa-1-todolist](https://trello.com/b/KbUefDdN/mapa-1-todolist)
- [https://trello.com/b/OyMQTu3W/mapa-2-todolist](https://trello.com/b/OyMQTu3W/mapa-2-todolist)
- [https://trello.com/b/MdxWoXPZ/mapa-3-todolist](https://trello.com/b/MdxWoXPZ/mapa-3-todolist)
- [https://trello.com/b/ZnK1Kq5R/mapa-4-todolist](https://trello.com/b/ZnK1Kq5R/mapa-4-todolist)
- [https://trello.com/b/kHml8CjF/mapa-5-todolist](https://trello.com/b/kHml8CjF/mapa-5-todolist)

Todos los miembros deberán tomar el papel _product owner_ y aportar
ideas y sugerencias para definir las historias de usuario. 

En el tablero Trello se definirá una única columna **Backlog** en la
que se incluirán las historias. Cada historia se analizará,
especificando claramente su descripción y su alcance. Para la
descripción se recomienda usar el formato que vimos en clase:

- Como _ROL_ quiero _ACCIÓN_ para _RESULTADO_ u _OBJETIVO_.

También se enumerarán brevemente una serie de condiciones de
satisfacción (COS) que deben cumplirse para dar la historia como
terminada. Estas condiciones de satisfacción son esenciales a la hora
de determinar el alcance de la historia.

Al incluir la historia se realizará un _planning pocker_ para volver a
consensuar su tamaño (considerad el tamaño previo de la historia como
una indicación, pero podéis modificarlo). El tamaño será un número del
1 al 4.

Se deben incluir en el sprint historias por un tamaño total 4 puntos x
número de personas del equipo:

- Equipo de 3 personas: 12 puntos
- Equipo de 4 personas: 16 puntos

El profesor no participará en el _planning pocker_, pero podrá pedir
aclaraciones sobre el tamaño de las historias.

En la tarjeta de Trello se escribirá el título, el tamaño (etiqueta) y
la descripción de la historia. 


### Responsables de historia de usuario ###

Una vez seleccionadas todas las historias los miembros del equipo
elegirán responsables para cada historia, se creará el issue (o
issues) correspondiente a la historia de usuario y se añadirá el
responsable al issue.

El responsable de la historia creará su página en la wiki de GitHub,
detallará allí las condiciones de satisfacción y añadirá el borrador
de la interfaz de usuario.

Todos los miembros del equipo deberán realizar un trabajo equitativo,
y se repartirán las historias de forma que queden también equilibrados
los tamaños totales de las historias asignadas a cada uno.

## Desarrollo del sprint

Se deberán realizar los siguientes eventos definidos por Scrum y XP,
tomando nota y redactando un informe con la fecha de la reunión, su
duración y su desarrollo:

1. Scrum diario (al menos simular 2 reuniones: la segunda y tercera
   semana). En nuestro "tiempo simulado" en las prácticas, una semana
   es como un día de trabajo completo en una empresa.
2. Retrospectiva del sprint.
3. 2 sesiones de pair programming con turnos de 20 minutos (en cada
   sesión se deben hacer 4 turnos). Se podrán hacer estas sesiones en
   clase de prácticas.

### Tablero Kanban ###

Debemos modificar el tablero del proyecto para acercarlo a un
tablero Kanban real.

- Límite de _Work In Progress_ (WIP): Estimar un número de límite de
  WIP para las columnas `In progress`, `In pull request` y `QA`. No se
  podrá incluir en esas columnas más tarjetas que las definidas en el
  número límite de WIP (las tarjetas en las columna `In progress -
  Done` se suman a las que hay en la columna `In progress`, y lo mismo
  con las columnas `In pull request - Done` y `In pull request`).
  
    Estimar el límite WIP para conseguir un flujo de trabajo
    correcto. Si se define un límite WIP demasiado bajo habrá personas
    ociosas, mientras que si se define un límite WIP demasiado alto
    habrá acumulación de tareas sin terminar.

- Añadimos las columnas de _buffer_ en el tablero de issues GitHub
  para adaptarlo mejor a Kanban:
    - **In progress - Done** - Se ha terminado el desarrollo y los
      tests unitarios y no se puede crear el PR porque la columna de `In pull
      request` ha alcanzado su límite WIP.
    - **In pull request - Done** - Se ha aprobado el pull request, se ha
      realizado la integración `master` y Travis da el OK. No se puede
      pasar a `QA` porque la columna ha alcanzado su límite WIP.

### Desarrollo de los issues ###

- Cada miembro del equipo selecciona el issue a desarrollar. Lo normal
  es que cada miembro desarrolle un único issue de forma concurrente,
  aunque podría darse el caso de ser más (por ejemplo, si algún issue
  no puede terminarse por estar bloqueado por otro).

- Se deben crear ramas para los issues y pull requests con revisión de
  código para integrar los pull requests en master. Es suficiente con
  que haya una única aprobación para integrar el pull request.

- Cada issue debe contener **tests automáticos** que prueben los
  cambios. También se debe especificar en la wiki de la historia de
  usuario del issue **los tests manuales que habría que hacer**
  (asociados a las condiciones de satisfacción).

- Seguimos usando Travis para la integración continua.

### Publicación de nueva versión  ###

Al final del desarrollo se deberá lanzar una nueva release (1.4.0) en
la rama `master`, y subir a DockerHub la imagen resultante con la
etiqueta `1.4.0`.

### Documentación del desarrollo ###

- Documentar los dailys, para incluir un informe en el documento.
- Documentar las sesiones de pair programming.
- Documentar la evolución del tablero GitHub y alguna métrica del
  desarrollo (pull requests por semana, velocidad de la semana,
  gráfica de burndown, etc.).

## Entrega y evaluación

La práctica tiene una duración de 4 semanas.

- Se realizará una **revisión del sprint** de 20 minutos en las
  **clases de teoría y práctica del 19 de diciembre**. La revisión
  constará de:
    - Presentación con diapositivas en la que se explicará la
      **metodología seguida** en el sprint y las **nuevas funcionalidades** introducidas.
    - Demostración de las nuevas funcionalidades utilizando la última
      imagen docker subida a Docker Hub.

- La fecha de entrega de la práctica será el **domingo 23 de
  diciembre**. En esa fecha se deberá tener disponible:
    - Entrega en Moodle la última versión del proyecto subida a
      GitHub (comprimida, sin el directorio `target` con los binarios
      y ejecutables). Deberá contener:
        - Directorio `doc` en el repositorio del proyecto en el que se
          incluirá un documento PDF o Markdown con la memoria de la
          práctica y un PDF con las diapositivas presentadas en la
          demo. En la memoria de la práctica se incluirá:
            - Sprint Backlog: historias de usuario escogidas para el
              sprint (copiar la descripción, las condiciones de
              satisfacción y el borrador de interfaz de usuario tal y
              como aparecen en la Wiki).
            - Funcionalidades implementadas (breve descripción para el
              usuario y breve descripción técnica).
            - Informe sobre la metodología seguida (ejemplos de
              evolución del tablero, alguna métrica del desarrollo
              realizado en el sprint, etc.)
            - Informes sobre las reuniones de Scrum (planificación del
              sprint, scrum diario, revisión) y sobre las sesiones de
              pair programming.
            - Resultado de la retrospectiva: qué ha ido bien y qué se
              podría mejorar.
    - Versión 1.4.0 de la máquina Docker en Docker Hub (es la máquina
      que voy a usar para revisar la ejecución de la práctica).
    - El repositorio GitHub deberá incluir el tablero de issues/PR
      completados y la Wiki con las historias de usuario que se debían
      implementar en el sprint..

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
