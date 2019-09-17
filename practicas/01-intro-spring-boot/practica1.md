# Enunciado práctica 1

## 1. Objetivos

En la primera práctica de la asignatura vamos a tomar contacto con el
_framework_ de desarrollo de aplicaciones web en Java _Spring Boot_,
trabajando sobre la aplicación inicial
[domingogallardo/mads-todolist-inicial](https://github.com/domingogallardo/mads-todolist-inicial).

La práctica tendrá una duración de cuatro semanas. Deberás realizarla de
forma individual, siguiendo las indicaciones que encontrarás en este
documento. Tendrás que desarrollar código y trabajar en GitHub
desarrollando _issues_, _pull requests_, _releases_ y actualizando la
wiki del proyecto.

Igual que en la práctica 0, debes leer la [introducción a Spring Boot
para las prácticas de MADS](./intro-spring-boot.md) para entender los
conceptos fundamentales del framework.

### 1.1. Aplicación inicial

La aplicación inicial es una aplicación para gestionar listas de
tareas pendientes de los usuarios de la aplicación. Se pueden registrar
y logear usuarios y los usuarios registrados pueden añadir, modificar
y borrar tareas pendientes de hacer.

A continuación puedes ver dos de las pantallas de la aplicación.

<table>
<tr>
<td><img src="./imagenes/login.png" width="700px"/></td>
</tr>
<tr>
<td align="center"> Pantalla de login </td>
</table>


<table>
<tr>
<td><img src="./imagenes/tareas.png" width="700px"/></td>
</tr>
<tr>
<td align="center"> Pantalla con listado de tareas </td>
</table>

Iremos desarrollando características adicionales de la aplicación a lo
largo de las prácticas. El nombre de la aplicación es **ToDo List**.


### 1.2. Metodología de desarrollo

En cuanto a la metodología de desarrollo, en esta primera práctica
repasaremos e introduciremos el uso de:

- [Git](https://git-scm.com) como sistema de control de versiones que nos permitirá
  registrar paso a paso los cambios realizados en el desarrollo,
  realizando e integrando ramas de _features_ en las que
  desarrollaremos pequeños incrementos que añadirán poco a poco las
  funcionalidades necesarias en la aplicación.
- [GitHub](https://github.com) como servicio en el que publicaremos los cambios e
  integraremos las ramas usando _pull requests_ (PRs). Utilizaremos un
  gran número de características de GitHub para realizar el
  seguimiento del desarrollo del proyecto: _issues_, _labels_,
  _milestones_, etc.
- JUnit y las [características de testing de Spring
  Boot](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-testing.html)
  para realizar continuamente pruebas unitarias que
  validen el desarrollo.

El objetivo es desarrollar software de una forma similar a cómo se
hace en cientos de proyectos punteros de desarrollo _open
source_. 

Existen muchos proyectos que tienen un desarrollo abierto,
transparente, en GitHub. Podemos aprender de sus metodologías
estudiándolos. A continuación listamos ejemplos de repositorios en
GitHub interesantes, en los que podemos estudiar los procesos de _pull
requests_, _issues_, tableros, etc. y las dinámicas de comunicación
que utilizan.

- [CartoDB](https://github.com/CartoDB/cartodb). Software español para
  representación visual de datos geográficos.
- [Vapor](https://github.com/vapor/vapor). Framework web en Swift.
- [Guice](https://github.com/google/guice). Framework de inyección de
  dependencias en Java.
- [swift-nio](https://github.com/apple/swift-nio). Framework asíncrono
  de entrada-salida en Swift. 
- [Spring
  Boot](https://github.com/spring-projects/spring-boot). Framework web
  en Java.

#### Git

Git es el sistema de control de versiones más utilizado en la
actualidad. Es muy flexible, distribuido, adaptable a múltiples flujos
de trabajo e ideal para una metodología de desarrollo en
equipo. Suponemos que ya tienes cierta experiencia con su uso. Puedes
usar los siguientes enlaces para repasar su funcionamiento.

- [Resumen de comandos de Git](comandos-git.md): Resumen de comandos
  principales para empezar a trabajar con Git.
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials/):
  Tutoriales muy orientados al uso de Git con gran cantidad de
  ejemplos. Es recomendable repasar los tutoriales básicos [Getting
  Started](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
  y los tutoriales
  [Syncing](https://www.atlassian.com/git/tutorials/syncing) y [Using
  Branches](https://www.atlassian.com/git/tutorials/using-branches) en
  el apartado _Collaborating_.
- [Libro de Scott Chacon](https://git-scm.com/book/en/v2): Completo
  manual con todos los detalles de todos los comandos de Git.

Cuando utilicemos git es muy importante realizar unos mensajes de
_commit_ claros. Un mensaje de _commit_ es la forma de comunicar a los
compañeros del equipo qué cambios se han introducido en la aplicación
y ponerlos en contexto (explicar por qué se han hecho, dar algún
detalle de implementación, etc.). El post
[How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit/)
explica muy bien esto.


#### Flujo de trabajo

Desarrollaremos la aplicación de forma iterativa, utilizando
inicialmente un flujo de trabajo Git denominado _feature branch_
(consultar la
[guía de GitHub](https://guides.github.com/introduction/flow/)) en el
que cada característica nueva se implementa en una rama separada que
después se mezcla con la rama principal de desarrollo. Más adelante
veremos otros flujos de trabajo. Puedes ver una introducción a
distintos flujos de trabajo básicos con Git en este
[documento de Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows).

Para implementar este flujo de trabajo utilizaremos los siguientes
instrumentos de GitHub que facilitan la comunicación entre los
miembros del equipo:

- **Issues** (_incidencias_): GitHub permite abrir _issues_
  (incidencias o tareas), asignarlos a personas, realizar comentarios,
  asignar etiquetas y cerrarlos cuando la implementación ha
  terminado. Consultar
  [Mastering Issues](https://guides.github.com/features/issues/).

    <img src="./imagenes/github-issues.png" width="500px"/>

    Definiremos distintos tipos de _issues_ en función de su
    propósito: _bug_, _technical_, _enhancement_. Los _issues_ que
    implementan una historia de usuario los etiquetaremos con el
    código de la historia de usuario.
  
    <img src="./imagenes/labels-issues.png" width="400px"/>
  
    Cada _issue_ se desarrollará en una rama de Git y se integrará en la
    rama _master_ haciendo un _pull request_.


- **Pull Requests**: Un _pull request_ permite avisar al equipo de que
  se va a integrar en la rama principal una rama con un desarrollo
  nuevo. Cuando creamos un PR, GitHub crea una página en la que se
  pueden realizar comentarios, revisiones de código o definir
  políticas de aceptación del PR. Consultar
  [About pull requests](https://help.github.com/articles/about-pull-requests/).
  
    Implementaremos cada _issue_ en una rama separada de git y la
    integraremos en la rama `master` haciendo un _pull
    request_. Cuando se mezcle el PR en `master` el _issue_ se
    cerrará.
  
    <img src="./imagenes/github-pr.png" width="700px"/>

    Más adelante añadiremos otra rama de largo recorrido `releases` para
    incluir en ella las _releases_ del proyecto.

- **Milestones** y **Releases**: Etiquetaremos cada _issue_ con el
  _milestone_ en el que queremos que se lance. Para identificar el
  _milestone_ usaremos el [versionado semántico](https://semver.org):
  MAJOR.MINOR.PATCH. 
  
    <img src="./imagenes/github-milestones.png" width="600px"/>
  
    Usaremos la funcionalidad de GitHub _Releases_ para etiquetar los
    commits en los que queramos marcar una versión nueva del
    proyecto. Podemos añadir información sobre las novedades de la
    versión (normalmente serán enlaces a los _issues_ y _pull
    requests_ de ese _milestone_).
  
    <img src="./imagenes/github-releases.png" width="600px"/>

- **Tablero de proyecto**: Un tablero de proyecto nos ayudará a hacer
  un seguimiento de en qué estado se encuentra cada _issue_ o PR:
  cuáles han sido implementados, cuáles faltan por asignar,
  implementar, probar, etc. Vamos a utilizar la funcionalidad propia
  de GitHub llamada _Projects_. Consultar
  [project boards](https://help.github.com/articles/tracking-the-progress-of-your-work-with-project-boards/).

    <img src="./imagenes/github-tablero.png" width="700px"/>
  

También utilizaremos un panel de [Trello](https://trello.com/) para representar las
historias de usuario que se van implementando en el proyecto. 

<img src="./imagenes/historias-usuario-trello.png" width="600px"/>

Cada historia de usuario tendrá un código numérico y podrá
implementarse con uno o más issues. En GitHub crearemos una etiqueta
por cada historia de usuario y se la asignaremos a los issues que se
usen para implementarla.

!!! Important
    Puede parecer redundante el uso de dos tableros, uno para las
    historias de usuario y otro para los _issues_ y _PR_. La
    justificación es que los objetivos de ambos tableros son distintos
    (y los contenidos también). El tablero de GitHub será un tablero
    técnico gestionado por el equipo de desarrollo, mientras que el
    tablero Trello es un tablero de funcionalidades de usuario, que
    es gestionado por el _product owner_, usado por el equipo de
    desarrollo y puede ser compartido también con clientes y gerencia.


La documentación en Trello y en GitHub (en los _issues_, en los PRs y
en el propio `README.md` del proyecto) hay que escribirla en
**Markdown**, un lenguaje de marcado muy popular y sencillo de
dominar. Si no has trabajado todavía con él puedes leer estas [guías
de GitHub](https://help.github.com/categories/writing-on-github/).

!!! Note
    Existen herramientas y servicios más avanzados para gestionar
    todos estos elementos del desarrollo. Por ejemplo
    [Jira](https://www.atlassian.com/software/jira),
    [YouTrack](https://www.jetbrains.com/youtrack/),
    [Confluence](https://www.atlassian.com/software/confluence) o
    incluso [Trello](https://www.atlassian.com/software/trello). Pero
    lo que nos ofrece GitHub es suficiente para lo que vamos a
    realizar en la asignatura y tiene la ventaja de estar integrado en
    una misma plataforma.


<!--

## 2. Entorno para realizar la práctica

Software necesario:

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/community-edition), para ejecutar la
   imagen (similar a una máquina virtual) que contiene Java y Play
   Framework. En esta primera práctica se utiliza para compilar y
   ejecutar los proyectos Play y para lanzar el servicio de base de
   datos MySQL.
- Como entorno de desarrollo proporcionamos dos opciones:
   - [Visual Studio Code](https://code.visualstudio.com): IDE para
     trabajar en el desarrollo del proyecto si no es posible usar
     IntelliJ. No tiene las funcionalidades de IntelliJ de
     autocompletar código, depuración, etc.
   - [IntelliJ IDEA](https://www.jetbrains.com/idea/): IDE recomendado
     para trabajar en el desarrollo del proyecto. Debes descargar la
     versión **Ultimate**. Es de pago, pero puedes conseguir una
     licencia educativa en
     [https://www.jetbrains.com/student/](https://www.jetbrains.com/student/). Es
     necesario disponer del **JDK Java 8**.  En la instalación se debe
     instalar el **plugin de Scala**.

### Docker ###

[Docker](https://docs.docker.com) es una tecnología que ha tenido una
gran expansión en los últimos años. Permite construir máquinas
virtuales ligeras que utilizan el mismo sistema operativo de la
máquina host. Estas máquinas virtuales se denominan _contenedores_ y,
al compartir el propio sistema operativo en el que se están
ejecutando, su gestión (construcción, arranque, parada, etc.) es
muchísimo más rápida que las máquinas virtuales tradicionales.

Utilizaremos la imagen Docker
[domingogallardo/playframework](https://hub.docker.com/r/domingogallardo/playframework/),
que **lanza el comando `sbt` sobre el directorio actual** necesario
para compilar y ejecutar aplicaciones Play.

Cada máquina docker se define con un fichero `Dockerfile`. Puedes
mirar el fichero `Dockerfile` de la imagen de la asignatura en [este
enlace](https://github.com/domingogallardo/playframework/blob/master/Dockerfile). Más
adelante en la asignatura estudiaremos más sobre Docker.

Tal y como hemos explicado en la [introducción a Play Framework para
las prácticas de MADS](./intro-play-teoria.md) para lanzar esta imagen
tenemos que ejecutar el siguiente comando, estando en el directorio de
la aplicación Play:

```text
$ cd /path/to/my/play/project
$ docker run --rm  -it -v "${PWD}:/code" -p 9000:9000 domingogallardo/playframework
```

El comando `docker run` buscará la imagen
`domingogallardo/playframework` en local y la descargará si no la
encuentra. Después la ejecutará montando el directorio actual en el
directorio `/code` y mapeando el puerto 80 de la máquina host en el
puerto 9000 del contenedor. La imagen está configurada para lanzar el
comando `sbt` sobre el directorio `code`.

Como en este directorio está montado el directorio de la máquina
_host_ en donde tienes el proyecto, podrás editar y modificar los
ficheros en la propia máquina _host_ y compilarlos y ejecutarlos desde
el comando `sbt` en el contenedor.

En la configuración por defecto (fichero `conf/application.conf`) la
aplicación trabaja con la base de datos en memoria. Existe otra
configuración (`conf/develop-mysql.conf`) para que la aplicación
trabaje con una base de datos MySQL. La utilizaremos también en la práctica.

### Entorno de trabajo  ###

Es importante que el entorno de trabajo permita realizar con facilidad
tanto el desarrollo de la aplicación como las pruebas.

#### Pruebas manuales y automáticas ####

Durante el desarrollo de la práctica será necesario realizar **pruebas
manuales** de la aplicación, introducir datos en sus pantallas y
comprobar que los cambios que hemos añadido funcionan correctamente.

Para estas pruebas manuales recomendamos utilizar la configuración de
ejecución trabajando sobre la **base de datos real MySQL**. De esta forma
podemos introducir datos y reutilizarlos en posteriores pruebas
manuales.

Para poner en marcha la base de datos MySQL recomendamos usar
Docker. El siguiente comando lanza un contenedor llamado `play-mysql`
con una base de datos MySQL trabajando en el puerto interno `3306` y en
el puerto del host `3316` con el usuario `root` con la contraseña `mads`:

```
$ docker run -d -p 3316:3306 --name play-mysql -e MYSQL_ROOT_PASSWORD=mads -e MYSQL_DATABASE=mads mysql:5
```

!!! Warning "Importante"

    En los laboratorios de la EPS está instalada la
    imagen Docker 5.7.18 de MySQL. Hay que definir explícitamente esa versión
    en el comando docker, escribiendo `mysql:5.7.18`.

También durante el desarrollo hay que implementar y lanzar **tests
automáticos**. Recomendamos en este caso usar la **base de datos de
memoria**, en lugar de la base de datos MySQL, para que la ejecución de
los tests tenga más velocidad y para que no se borren los datos
introducidos en las pruebas manuales.

Debemos configurar el entorno de trabajo para que sea posible realizar
los dos tipos de pruebas, manuales y automáticas,
simultáneamente. 

Dependiendo de si utilizamos o no IntelliJ lo haremos
de forma distinta.

#### Configuración de trabajo usando Visual Studio Code ####

Si tu ordenador no tiene prestaciones suficientes para trabajar con
IntelliJ IDEA puedes usar un editor como Visual Studio Code.

Recomendamos trabajar con tres pestañas de terminal abiertas en el editor:

- **Terminal 1**: ejecución de la aplicación para hacer **pruebas
  manuales** sobre base de datos MySQL. Lanzamos en el shell el
  comando docker para lanzar la aplicación usando la base de datos
  MySQL.

        $ docker run --link db-mysql --rm -it -p 9000:9000 -e \
        DB_URL="jdbc:mysql://db-mysql:3306/mads" -e DB_USER_NAME="root" -e \
        DB_USER_PASSWD="mads" -v "${PWD}:/code" domingogallardo/playframework

Y desde la consola sbt modificamos la preferencia `config.file` para
que la aplicación utilice la configuración definida en el fichero
`conf/develop-mysql.conf`

        [mads-todolist-dgallardo] $ set javaOptions += "-Dconfig.file=conf/develop-mysql.conf"
        [mads-todolist-dgallardo] $ run
  
- **Terminal 2**: **pruebas automáticas** sobre la base de datos de
  memoria. Lanzamos en el shell el comando docker para lanzar sbt.
  No hace falta exportar el puerto 9000 porque sólo se va
  a usar el contenedor para lanzar los tests:


        $ docker run --rm  -it -v "${PWD}:/code" domingogallardo/playframework
        [mads-todolist-dgallardo] $ test

- **Terminal 3**: shell en el que usaremos git:

        $ git status
        On branch master
        Your branch is up to date with 'origin/master'.

        nothing to commit, working tree clean


#### Configuración de trabajo usando IntelliJ ####

Si tenemos un ordenador con suficiente capacidad es recomendable usar
IntelliJ IDEA como entorno de desarrollo.

Recomendamos la siguiente configuración:

- **Pruebas manuales**: para lanzar la aplicación y poder realizar
  pruebas manuales usando la base de datos MySQL debemos crear una
  [configuración de run/debug que trabaje sobre
  MySQL](./intro-play-teoria.md#desde-el-rundebug-de-intellij) y
  lanzar la ejecución.

- **Pruebas automáticas**: se lanza `sbt` desde la propia pestaña de
  IntelliJ o desde un terminal con el comando `docker run`. Como hemos
  comentado anteriormente, no es necesario mapear el puerto 9000
  porque el contenedor sólo se va a usar para lanzar los tests:
  
        $ docker run --rm  -it -v "${PWD}:/code" domingogallardo/playframework
        [mads-todolist-dgallardo] $ 

    Y se lanza el comando `test`.

- **Shell de git**: es recomendable tener abierta una ventana de
  terminal adicional para trabajar con git.

!!! Warning "Cuidado en las máquinas de la EPS"

    En las máquinas virtuales Ubuntu de la EPS, la aplicación
    Docker se ejecuta con el usuario `root`. Si se lanza una ejecución de
    la máquina de docker con el directorio del proyecto antes de haberlo
    compilado con IntelliJ, se crearán directorios de trabajo `logs` y
    `target` con propiedad de `root`. Esto provocará un error de permisos cuando vayamos a compilar desde
    IntelliJ y hará imposible la compilación desde el IDE. 

    Para que funcione correctamente la compilación desde IntelliJ
    debemos eliminar esos directorios y hacer que sea IntelliJ quien
    los cree. Por ejemplo, podemos borrarlos a mano con `$ sudo rm
    -rf logs` y `$ sudo rm -rf target`.

    O podemos volver a descargar el proyecto de GitHub y compilarlo
    por primera vez con IntelliJ.


## 3. Antes de empezar la práctica

1. Descarga e instala el software indicado en el apartado anterior.

2. Inicializa tu nombre de usuario y tu correo en Git. El nombre de
   usuario será el nombre que aparecerá en los _commits_. Pon tu nombre
   y apellido.
   
        $ git config --global user.name "Pepe Perez"
        $ git config --global user.email pepe.perez@example.com<

3. Descarga la imagen de Docker para poder compilar y ejecutar los
   proyectos Play:

        $ docker pull domingogallardo/playframework
        $ docker image ls
        REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
        domingogallardo/playframework   latest              95c1eb17ecb4        5 weeks ago         530MB

4. Crea una cuenta en GitHub. Puedes usar el nombre de usuario que
   quieras (o usar el que ya tienes), pero **escribe correctamente tu
   nombre y apellidos en el perfil** usando la opción _Settings >
   Profile_ y actualizando el campo _Name_.
   
5. Una vez logeado en GitHub, copia el enlace con una invitación que
   compartiremos en el foro de Moodle. Con esa invitación se creará
   automáticamente el repositorio `todolist-2018-<usuario>` en la
   organización [mads-ua-18](https://github.com/mads-ua-18). Es un
   repositorio privado al que tienes acceso tú y el
   profesor. Contiene el código inicial de un proyecto base Play (es
   una copia del repositorio
   [domingogallardo/mads-todolist-inicial](https://github.com/domingogallardo/mads-todolist-inicial))
   en la que se han comprimido todos los commits en uno.

    Es importante que tengas en cuenta que el repositorio recién
    creado no reside en tu cuenta, sino en la organización
    `mads-ua`. Puedes acceder a él desde el _dashboard_ de GitHub que
    aparece cuando te logeas:
   
    <img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/dashboard-github.png" width="600px"/>

    También el profesor te invitará a formar parte de la organización
    y recibirás un mensaje de correo electrónico en el que deberás
    aceptar esta invitación. También se puede aceptar la invitación
    accediendo a <https://github.com/mads-ua-18>.
   
6. Descarga el proyecto y comprueba que se compila y ejecuta
   correctamente con la imagen de Docker y usando la base de datos de
   memoria (muy útil para pruebas y lanzar los tests).
   
        $ git clone https://github.com/mads-ua/todolist-2018-usuario.git
        $ cd todolist-2018-usuario
        $ docker run --rm  -it -v "${PWD}:/code" -p 9000:9000 domingogallardo/playframework
        [info] Loading project definition from /code/project
        [info] Updating {file:/code/project/}code-build...
        [info] Resolving org.fusesource.jansi#jansi;1.4 ...
        [info] Done updating.
        [info] Set current project to play-java (in build file:/code/)
        [mads-todolist-inicial] $ test
        ...
        [info] Passed: Total 35, Failed 0, Errors 0, Passed 35
        [success] Total time: 35 s, completed Sep 4, 2018 9:34:04 AM
        [mads-todolist-inicial] $ run
   
    Comprueba que la aplicación está funcionando en
    <http://localhost:9000> en la máquina host.
   
    <img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/login.png" width="600px"/>
 
    Para salir del comando `run` de `sbt` debemos hacer
    `CTRL+d`. Podemos lanzar cualquier otro comando de sbt (consultar
    [Using the SBT console](https://playframework.com/documentation/2.5.x/PlayConsole).  
   
    Para salir del contenedor podemos escribir el comando `exit` o hacer `CTRL+c`.

7. Prueba que la aplicación funciona correctamente trabajando con la
   base de datos MySQL (el funcionamiento real de la aplicación y para
   hacer pruebas de integración).

    Lanza MySQL con Docker:
   
        $ docker run -d -p 3316:3306 --name db-mysql -e MYSQL_ROOT_PASSWORD=mads -e MYSQL_DATABASE=mads mysql:5

    !!! Warning "Importante"

        En los laboratorios de la EPS está instalada la
        imagen Docker 5.7.18 de MySQL. Hay que definir explícitamente esa versión
        en el comando docker, escribiendo `mysql:5.7.18`.

    Para parar y volver a poner en marcha el contenedor mysql puedes
    usar los comandos `docker stop` y `docker start`. Los datos
    añadidos en la base de datos se mantendrán mientras que el
    contenedor no se borre. El comando `docker container ls -a` lista
    todos los contenedores existentes (parados y en marcha):
   
        $ docker container ls
        CONTAINER ID        IMAGE               CREATED             STATUS              PORTS                               NAMES
        bd057639b6ac        mysql:5             30 minutes ago      Up 22 minutes       33060/tcp, 0.0.0.0:3316->3306/tcp   db-mysql
        $ docker container stop bd057639b6ac
        CONTAINER ID        IMAGE               CREATED             STATUS                     PORTS               NAMES
        bd057639b6ac        mysql:5             31 minutes ago      Exited (0) 7 seconds ago                       db-mysql
        $ docker container start bd057639b6ac
        CONTAINER ID        IMAGE               CREATED             STATUS              PORTS                               NAMES
        bd057639b6ac        mysql:5             32 minutes ago      Up 5 seconds        33060/tcp, 0.0.0.0:3316->3306/tcp   db-mysql

    Ahora ya podemos lanzar la aplicación con docker para que trabaje
    con la base de datos del contenedor, definiendo ahora en variables
    de entorno la URL, el usuario y la contraseña con la que debe
    conectarse la aplicación a la base de datos. Usamos la opción
    `link` de docker para definir el nombre lógico del contenedor al
    que debe conectarse la aplicación.

        $ docker run --link db-mysql --rm -it -p 9000:9000 -e \
        DB_URL="jdbc:mysql://db-mysql:3306/mads" -e DB_USER_NAME="root" -e \
        DB_USER_PASSWD="mads" -v "${PWD}:/code" domingogallardo/playframework

    Y desde la consola sbt modificamos la preferencia `config.file`
    para que la aplicación utilice la configuración definida en el
    fichero `conf/develop-mysql.conf`.

        [mads-todolist-inicial] $ set javaOptions += "-Dconfig.file=conf/develop-mysql.conf"
        [mads-todolist-inicial] $ run

    Prueba que la aplicación funciona correctamente. Puedes comprobar
    las tablas y los datos almacenados en la base de datos
    conectándote a la base de datos en el puerto 3316 desde cualquier
    cliente MySQL:
   
    - En los laboratorios de la EPS, usando _MySQL Workbench_. 
    - En IntelliJ IDEA puedes usar la consola MySQL:
   
    <img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/conexionbd-intellij.png" width="500px"/>

    Es posible examinar el esquema de la base de datos:

    <img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/esquema-bd.png" width="300px"/>

    Y examinar tablas en concreto:

    <img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/tablabd-intellij.png" width="300px"/>

8. Con todo lo hecho hasta ahora ya hemos comprobado que la aplicación
   se compila correctamente y se ejecuta sin problema en las dos
   configuraciones más importantes con las que trabajaremos: base de
   datos en memoria y base de datos MySQL.

Para el desarrollo de la práctica que viene a continuación es
fundamental que entiendas el funcionamiento de Play Framework. Lo
explicaremos rápidamente en la clase de teoría usando el documento
[introducción a Play Framework para las prácticas de
MADS](./intro-play-teoria.md). Pero es imprescindible que hagas tú un
esfuerzo descargando, probando y modificando las dos aplicaciones:
`domingogallardo/play-proyecto-inicial` y
`domingogallardo/mads-todolist-inicial` (es la aplicación que se ha
copiado en tu repositorio).
   
Puedes trabajar en estos proyectos sin miedo de estropearlos. Es más,
cuanto más los estropees mejor, porque es la forma de aprender. No
deberás entregar nada de estos proyectos.

## 4. Desarrollo de la práctica

En esta primera práctica vamos a desarrollar las siguientes dos
historias de usuario o _features_:

1. Página _Acerca de_
2. Barra de menú
3. Página listado de equipos
4. Página descripción de equipo

La práctica va a consistir en la realización en tu proyecto de todos
los elementos necesarios para implementar estas _features_ : wiki,
_issues_, _pull requests_ (con sus _commits_ en los que se desarrolla paso a paso
cada _issue_) y tablero del proyecto. 

Haremos paso a paso la primera característica, creando la primera
versión 1.0.0 de la aplicación. Las siguientes características las
deberás desarrollar tu mismo y entregar la versión 1.1.0.

### 4.1. Versión 1.0.0 ###

La versión 1.0.0 será la versión inicial de la
aplicación. Desarrollaremos en esta versión la primera característica:
**Página _Acerca de_**.

#### 4.1.1. Wiki ####

Utilizaremos la Wiki del proyecto GitHub para documentar las
características a desarrollar en la aplicación. Deberá haber una
página para cada característica. La página principal de la Wiki será
el _backlog_ del proyecto y deberá tener los enlaces a todas las
características desarrolladas y pendientes de desarrollar.

Añade la página principal, en la que organizarás el listado de
_features_ desarrolladas en proyecto. Un posible ejemplo de
organización es el siguiente:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/wiki-practica.png" width="700px"/>

Añade una página con la descripción de la característica **Página
_Acerca de_**:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/wiki-practica-acerca-de.png" width="700px"/>


#### 4.1.2. Tablero del proyecto ####

Configura el tablero del proyecto, poniendo como nombre `ToDoList` y
seleccionando como plantilla `Automated kanban`. Elimina las tarjetas
en la columna `To do` y añade la columna `In pull request` entre `In
progress` y `Done`.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/project-practica.png" width="900px">

En las columnas deberán aparecer los _issues_ y _pull requests_ del
proyecto. GitHub permite automatizar el movimiento de las tarjetas de
una columna a otra. A continuación mostramos la configuración que
usaremos:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/projecto-practica-automation.png" width="900px"/>

Deberemos mover manualmente las tarjetas en algún caso, porque GitHub
no podrá detectar las condiciones. En resumen, las condiciones de las
fichas que habrá en cada columna son las siguientes:

- Columna `To do`: Nuevos _issues_ añadidos al proyecto. Cuando
  añadimos el proyecto al _issue_ (en la página del _issue_) GitHub
  lo coloca automáticamente en esta columna.
- Columna `In progress`: _Issues_ que se han comenzado a implementar
  (se ha creado una rama su desarrollo). Manual.
- Columna `In pull request`: _Pull request_ creados. Cuando añadimos
  el proyecto al _pull request_ (en la página del _pull request_)
  GitHub lo coloca automáticamente en esta columna. Archivaremos el
  _issue_ implementado por el _pull request_ manualmente.
- Columna `Done`: _Pull requests_ cerrados. GitHub lo detecta automáticamente.

#### 4.1.3. Issues ####

Añade el primer _issue_, correspondiente a la _feature_ a desarrollar
**Página _Acerca de_**. Añade las etiquetas que inicialmente vamos a
usar (ver la imagen) y el _milestone_ 1.0.0.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/labels-issues.png" width="500px"/>

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/issue-acerca-de-listado.png" width="500px"/>

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/issue-acerca-de-detalle.png" width="500px"/>

Añade el _issue_ al tablero (desde la página del _issue_) y
automáticamente se añadirá en la columna `To do`.


#### 4.1.4. Desarrollo ####

Para desarrollar el _issue_ abriremos una rama en Git, realizaremos
commits sobre ella hasta estar terminado y después crearemos un _pull
request_ en GitHub para realizar la integración con la rama `master`.

Mueve en el tablero la tarjeta con el _issue_ a la columna `In
progress`.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/in-progress-issue-1.png" width="300px" />

Empezamos el desarrollo importando el proyecto en IntelliJ y creando
dos pestañas en el panel `Terminal`: una para lanzar el proyecto con
Docker y trabajar con Sbt y la otra para trabajar con Git.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/intellij-practica.png" width="700px"/>

Creamos la rama en la que desarrollaremos la _feature_ y la subimos a
GitHub (en el panel `Git`):

```text
$ git checkout -b acerca-de
Switched to a new branch 'acerca-de'
$ git push -u origin acerca-de
Username for 'https://github.com': domingogallardo2
Password for 'https://domingogallardo2@github.com': 
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/mads-ua-18/todolist-2018-domingogallardo2.git
 * [new branch]      acerca-de -> acerca-de
Branch 'acerca-de' set up to track remote branch 'acerca-de' from 'origin'.
```

##### Primer commit #####

Hacemos un primer commit.

Cambia en `build.sbt` el nombre del proyecto a `mads-todolist-<tu-nombre>` y
la versión a `1.0.0-SNAPSHOT`. El sufijo `SNAPSHOT` indica _en
desarrollo_. Cuando hagamos el _release_ de la versión 1.0.0
eliminaremos el sufijo.

Realiza el commit y súbelo a GitHub:
   
```text
$ git add build.sbt
$ git status
On branch acerca-de
Your branch is up to date with 'origin/acerca-de'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   build.sbt

$ git commit -m "Cambiado el nombre del proyecto y empezamos versión 1.0.0"
[acerca-de f6180cc] Cambiado el nombre del proyecto y empezamos versión 1.0.0
 1 file changed, 2 insertions(+), 2 deletions(-)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 367 bytes | 367.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/mads-ua-18/todolist-2018-domingogallardo2.git
   6767016..a332017  acerca-de -> acerca-de
```

Consulta en GitHub que el _commit_ se ha subido en GitHub:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/commit-practica-github.png" width="400px"/>
   
De esta forma habrás comprobado que tienes permiso de escritura en
el repositorio y que ya puedes comenzar a realizar la práctica.
   
Si ahora vuelves a lanzar la máquina Docker en el proyecto, verás
que ha cambiado el nombre del proyecto (en el panel `Sbt`):
   
```text
$ docker run --rm  -it -v "${PWD}:/code" -p 9000:9000 domingogallardo/playframework
[info] Loading project definition from /code/project
[info] Set current project to mads-todolist-dgallardo (in build file:/code/)
[mads-todolist-dgallardo] $ 
```

##### Segundo commit #####

En el segundo commit incluiremos el desarrollo de los elementos
necesarios para la página _acerca de_:

- Ruta
- Acción en controller
- Vista

Realiza los siguientes cambios.

**Fichero `conf/routes`**:

```diff
GET     /equipos/addUsuario         controllers.EquipoController.formularioAddUsuarioEquipo()
POST    /equipos/addUsuario         controllers.EquipoController.addUsuarioEquipo()

+ GET     /about                      controllers.HomeController.about()

# Map static resources from the /public folder to the /assets URL path
GET     /assets/*file               controllers.Assets.versioned(path="/public", file: Asset)
```

**Fichero `app/controllers/HomeController.java`**:


```diff
    public Result index() {
        return ok(index.render("Your new application is ready."));
    }

+   public Result about() {
+       return ok(about.render());
+   }
}
```


**Fichero `app/views/about.scala.html`**:

```diff
+@main("Acerca de") {
+   <div class="container-fluid">
+        <h1>ToDo List</h1>
+        <ul>
+            <li>Desarrollada por Domingo Gallardo</li>
+            <li>Versión 1.0.0 (en desarrollo)</li>
+            <li>Fecha de release: pendiente de release</li>
+        </ul>
+    </div>
+}
```

Prueba la página accediendo a la url <http://localhost:9000/about>.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/pagina-acerca-de.png" width="400px"/>

Por último, confirma el commit en la rama y súbelo a GitHub. En el
panel `Git`:

```text
$ git add .
$ git status

On branch acerca-de
Your branch is up to date with 'origin/acerca-de'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   app/controllers/HomeController.java
        new file:   app/views/about.scala.html
        modified:   conf/routes
$ git commit -m "Añadida ruta, vista y controller 'about'"
[acerca-de 2831312] Añadida ruta, vista y controller 'about'
 3 files changed, 14 insertions(+)
 create mode 100644 app/views/about.scala.html
$ git push
```


##### Tercer commit #####

En el tercer commit pondremos un enlace a la página _acerca de_ en la página de
login de la aplicación.

Realiza el siguiente cambio:

**Fichero `app/views/formLogin.scala.html`**:

```diff
            <a class="btn btn-link" href="@routes.UsuarioController.registroUsuario()">Ir a registro</a>
        </p>
+       <p><a class="btn btn-link" href="@routes.HomeController.about()">Acerca de</a></p>
     }
```

Prueba que funciona correctamente, haz el commit y súbelo a GitHub:

```text
$ git commit -am "Añadido enlace a página 'about' en página 'login'"
[acerca-de 672c28f] Añadido enlace a página 'about' en página 'login'
1 file changed, 1 insertion(+)
$ git push
```


#### 4.1.5. Pull request ####

Una vez terminada la implementación de la _feature_ en la rama,
creamos un _pull request_ en GitHub para indicar que estamos listos
para mezclar la rama con la _feature_ con la rama principal de
desarrollo (_master_).

Más adelante añadiremos al _pull request_ una comprobación automática
de las pruebas y una revisión de código por parte de compañeros del
equipo. Por ahora haremos nosotros ambas tareas.

Vamos a verlo paso a paso.

Empezamos por mezclar la rama de forma local con `master`, antes de
hacer el _pull request_ en GitHub, para probar que no se ha roto nada
(todos los tests deben seguir pasando) y que los tests que hemos
añadido también funcionan correctamente (en este caso no hemos añadido
ninguno).

En el panel `Git`:

```text
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
$ git merge acerca-de 
Updating 6767016..672c28f
Fast-forward
 app/controllers/HomeController.java | 4 ++++
 app/views/about.scala.html          | 8 ++++++++
 app/views/formLogin.scala.html      | 1 +
 build.sbt                           | 4 ++--
 conf/routes                         | 2 ++
 5 files changed, 17 insertions(+), 2 deletions(-)
 create mode 100644 app/views/about.scala.html
```

En el panel `Sbt`:

```text
[mads-todolist-dgallardo] $ test
...
[info] Passed: Total 35, Failed 0, Errors 0, Passed 35
[success] Total time: 71 s, completed Sep 6, 2018 10:04:55 AM
[mads-todolist-dgallardo] $ 
```

Una vez que hemos comprobado que todo funciona bien, deshacemos el
merge que acabamos de realizar en la rama `master`, ya que
actualizaremos después la rama con el resultado del _pull request_ en
GitHub:

```text
$ git reset --hard origin/master
HEAD is now at 6767016 Commit inicial
$ git checkout acerca-de 
Switched to branch 'acerca-de'
Your branch is up to date with 'origin/acerca-de'.
```

Ya podemos crear el _pull request_ en GitHub. 

Accede a la rama y comprueba que están todos los cambios pulsando
`Compare`. Pulsa después el botón `New pull request` para crear el
_pull request_.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/rama-acerca-de.png" width="700px"/>

Introduce el nombre del _pull request_, el comentario, el _milestone_
y la etiqueta. Copia los datos del _issue_, y en el comentario escribe

```text
Closes #1
```

De esta forma, cuando se cierre el _pull request_ se cerrará
automáticamente el _issue_. El número `#1` lo convierte GitHub en un
enlace al _issue_ correspondiente. De esta forma podemos examinar el
_issue_ resuelto por el PR.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/pull-request-practica.png" width="700px"/>

Añade también el PR al tablero del proyecto. Se colocará
automáticamente la columna `In pull request`. Entra en el proyecto y
archiva la tarjeta con el _issue_, ya que la actividad de desarrollar
la _feature_ queda representada por el _pull request_.

En este momento se debería hacer una revisión del código del pull
request y comprobar de forma automática que la integración con
_master_ no introduce errores en los tests. Lo haremos en siguientes
prácticas.

GitHub informa de que no hay conflictos con la rama `master` y que es
posible hacer el merge. Pulsa el botón de `Merge` y confírmalo. Borra
la rama en GitHub, pulsando el botón correspondiente.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/merge-pull-request-1.png" width="500px"/>

Por último, este _merge_ lo has hecho en GitHub, debes integrarlo en tu
repositorio local. En la pestaña de Git:

```text
$ git checkout master
$ git fetch
remote: Counting objects: 1, done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (1/1), done.
From https://github.com/mads-ua-18/todolist-2018-domingogallardo2
   6767016..9527ae2  master     -> origin/master
$ git pull
Updating 6767016..9527ae2
Fast-forward
 app/controllers/HomeController.java | 4 ++++
 app/views/about.scala.html          | 8 ++++++++
 app/views/formLogin.scala.html      | 1 +
 build.sbt                           | 4 ++--
 conf/routes                         | 2 ++
 5 files changed, 17 insertions(+), 2 deletions(-)
 create mode 100644 app/views/about.scala.html
$ git branch -d acerca-de 
Deleted branch acerca-de (was 672c28f).
$ git remote prune origin
Pruning origin
URL: https://github.com/mads-ua-18/todolist-2018-domingogallardo2.git
 * [pruned] origin/acerca-de
$ git log --oneline --graph --all
*   9527ae2 (HEAD -> master, origin/master, origin/HEAD) Merge pull request #2 from mads-ua-18/acerca-de
|\  
| * 672c28f Añadido enlace a página 'about' en página 'login'
| * 3fdfb83 Añadida ruta, vista y controller 'about'
| * a332017 Cambiado el nombre del proyecto y empezamos versión 1.0.0
|/  
* 6767016 Commit inicial
```

Comprobamos también la historia de _commits_ en GitHub. Aparecerá el
_commit_ de _merge_ introducido por el _pull request_.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/historia-commits-practica1.png" width="800px"/>

De esta forma hemos cerrado el PR e integrado su código en la rama
principal de desarrollo. En el tablero de proyecto debe haber cambiado
la tarjeta con el PR a la columna `Done`.


#### 4.1.6. Versión 1.0.0 ####

Por último creamos el _release_ 1.0.0. Haremos un commit directamente
sobre la rama `master` (más adelante explicaremos una forma más
elaborada de hacer un _release_, cuando expliquemos el flujo de
trabajo de GitFlow).


Crea un commit con la confirmación del número de versión y fecha en
los ficheros `build.sbt` y `about.scala.html`

**Fichero `build.sbt`**:

```diff
 name := """mads-todolist-dgallardo"""
 
-version := "1.0.0-SNAPSHOT"
+version := "1.0.0"
 
 lazy val root = (project in file(".")).enablePlugins(PlayJava)
 
```

**Fichero `app/views/about.scala.html`**:

```diff
    <h1>ToDo List</h1>
        <ul>
            <li>Desarrollada por Domingo Gallardo</li>
-           <li>Versión 1.0.0 (en desarrollo)</li>
-           <li>Fecha de release: pendiente de release</li>
+           <li>Versión 1.0.0</li>
+           <li>Fecha de release: 6/9/2018</li>
        </ul>
}
```

Añadimos el commit y lo subimos a GitHub

```text
$ git add .
$ git commit -m "Cambio de versión a 1.0.0"
[master 61d4ac8] Cambio de versión a 1.0.0
 2 files changed, 3 insertions(+), 3 deletions(-)
$ git push
```

Y, por último, creamos la versión 1.0.0 en GitHub pulsando en el
enlace `release` en la página principal (pestaña `Code`).

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/release-practica1.png" width="700px"/>

Un _release_ en GitHub se guarda como una una etiqueta Git, junto con
información asociada. Se suelen indicar las nuevas _features_ añadidas
en el _release_ mediante enlaces a los _pull requests_
añadidos. También añadiremos enlaces a la página de la Wiki en la que
se describe la característica.


<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/primer-release-practica1.png" width="700px"/>

El resultado será:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/release-practica1-terminado.png" width="400px"/>


### 4.2. Versión 1.1.0 ###

El resto de la práctica consistirá en desarrollar la versión 1.1.0,
usando la misma metodología vista anteriormente.

Deberás desarrollar tres características nuevas obligatorias y 2 opcionales:

- Barra de menú, obligatoria.
- Página de equipos de un usuario, obligatoria.
- Página de descripción de un equipo con el listado de usuarios que
  participan en él, obligatoria.
- (Opcional) Usuario administrador que gestiona los equipos

Deberás implementar cada característica siguiendo la metodología que
hemos usado anteriormente. En la implementación, deberás añadir el
código necesario en cada una de las capas de la aplicación:

- Capa de presentación (vista)
- Nuevo método en la capa de controller
- Métodos necesarios en la capa de servicio y de repository
  
En cada característica deberás también incluir **tests** que prueben los
nuevos métodos añadidos en la capa de servicio.


#### Barra de menú ####

La aplicación deberá tener una barra de menú común a todas sus
páginas, menos en las páginas de login y registro.

- La barra de menú estará situada en la parte superior de la página y
será un [Navbar](https://getbootstrap.com/docs/4.0/components/navbar/).
de Bootstrap.
- La barra de menú tendrá como mínimo los siguientes elementos (de
izquierda a derecha):
   - `ToDoList`: enlace a la página _acerca de_.
   - `Tareas`: enlace a la página de tareas, con la lista de tareas
  pendientes del usuario.
   - `Equipos`: enlace a la página de equipos, con el listado de equipos al
  que pertenece el usuario.
   - _Nombre usuario_: A la derecha de la página. Desplegable con las opciones:
      - `Cuenta`: Futura página para gestionar la cuenta
      - `Cerrar sesión <nombre usuario>`: cierra la sesión y lleva a la
     página de login.

#### Equipos de un usuario ####

Cuando el usuario pinche en la opción `Equipos` del menú irá a una
página con un listado del equipo a los que pertenece.

- El listado de equipos será una tabla similar al listado de tareas,
pero sin acciones.
- La ruta para obtener el listado de los equipos de un usuario será
`/usuarios/:id/equipos`. Al igual que el listado de tareas, la ruta
estará protegida para que sólo pueda acceder un usuario logeado y
siendo el usuario logeado el mismo que el `id`.

#### Descripción de equipo ####

En la lista de equipos de un usuario los equipos tendrán un enlace para
acceder a su descripción.

- En la descripción de un equipo aparecerá: su nombre y el listado de
  personas del equipo.
- La ruta para obtener la descripción de un equipo será
`/equipos/:id`. La ruta estará protegida para que sólo pueda acceder
un usuario logeado.

#### Usuario administrador (opcional) ####

Al realizar el registro será posible darse de alta como usuario
administrador.

- Para darse de alta como administrador se deberá activar un _check
  box_ en la página de registro.
- Sólo puede haber un administrador. Si ya existe un administrador, no
  debe aparecer el _check box_ en la página de registro.
- El usuario administrador tendrá una barra de menú en la que se
  añadirá la opción vacía `Administración` (que iremos cambiando
  conforme añadamos funcionalidades a realizar por el administrador).

#### Gestión equipos por usuario administrador (opcional) ####

El usuario administrador podrá gestionar los equipos: añadir y editar
equipos (la opción de borrar la dejamos para más adelante).

- El administrador tendrá una opción adicional del menú llamada
  `Administración` de la que se desplegarán la opción `Equipos`.
- En la administración de equipos se entrará en una página donde se
  mostrará un listado de todos los equipos existentes (como el listado
  de tareas) y se dará la opción de añadir y editar.
- En la página de edición de un equipo se podrá modificar su nombre y
  aparecerá una tabla con todos los usuarios. Se podrá eliminar
  usuarios del equipo o añadir nuevos usuarios al mismo. 
- Los usuarios a añadir se escogerán de un desplegable en el que se
  mostrarán todos los usuarios no pertenecientes al equipo que se está
  modificando.


## 5. Entrega y evaluación ##

- La práctica tiene una duración de 4 semanas y debe estar terminada
  el martes 9 de octubre.
- La parte obligatoria puntúa sobre 7 y la opcional sobre 3 puntos.
- La calificación de la práctica tiene un peso de un 12% en la nota
  final de la asignatura.
- Para realizar la entrega se debe subir a Moodle un ZIP que contenga
  todo el proyecto, incluyendo el directorio `.git` que contiene la
  historia Git. Para ello comprime tu directorio local del proyecto
  **después de haber hecho un `clean` en `sbt`** para eliminar el
  directorio `target` que contiene los binarios compilados. Debes
  dejar también en Moodle la URL del repositorio en GitHub.

Para la evaluación se tendrá en cuenta:

- Desarrollo continuo (los _commits_ deben realizarse a lo largo de
  las 4 semanas y no dejar todo para la última semana).
- Correcto desarrollo de la metodología.
- Diseño e implementación del código y de los tests de las
  características desarrolladas.

-->
