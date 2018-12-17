# Introducción a Play Framework para las prácticas de MADS #

Vamos a ver cómo lanzar y desarrollar una aplicación Play Framework en
Java. Presentaremos las principales características de este framework
de desarrollo de aplicaciones web mediante ejemplos concretos de
código que vamos a utilizar en las prácticas de la asignatura.

## Aplicación `play-proyecto-inicial` ##

### Descarga de la aplicación ###

La aplicación `play-proyecto-inicial` se encuentra en GitHub:
<https://github.com/domingogallardo/play-proyecto-inicial>. Es un
esqueleto de aplicación Play con ejemplos básicos del funcionamiento
del framework.

Puedes descargarla usando el comando `git clone`:

```text
$  git clone https://github.com/domingogallardo/play-proyecto-inicial.git
```

Se creará el directorio `play-proyecto-inicial` en el que se habrá
descargado la aplicación Play.

### Uso de IntelliJ para trabajar con la aplicación Play ###

Aunque es posible trabajar con editores como _Visual Studio Code_,
vamos a explicar cómo desarrollar las aplicaciones Play usando el IDE
IntelliJ IDEA.

Las aplicaciones Play se pueden escribir en Java y en Scala. Nosotros
usaremos Java. Una parte importante de las librerías del framework
están escritas en Scala, por lo que debe estar instalado el plugin de
Scala en IntelliJ.

Se debe importar el proyecto usando la opción `sbt`, la herramienta de
build que usa Play. 

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/import-intellij-1.png" width="400px"/>

Sbt es una herramienta similar a Maven para Java, es la herramienta que
se usa para construir proyectos Scala. El fichero de configuración de
un proyecto sbt es el fichero `build.sbt` situado en el directorio
raíz.

Para compilar los proyectos también es necesario tener instalado
JDK. Nos aseguramos de que aparece en el panel de importación. Si no,
seleccionamos el directorio donde se encuentra la versión del JDK que
vamos a utilizar.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/import-intellij-2.png" width="400px"/>

Es conveniente activar la auto-importación del proyecto sbt. De esta
forma, si IntelliJ detecta algún cambio en la configuración sbt
realiza la importación de forma automática.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/sbt-enable-auto-import.png" width="300px"/>

Si se pincha en el icono de la esquina inferior izquierda de la
ventana de IntelliJ podremos activar o desactivar la visualización de
los nombres de los paneles en los bordes de la ventana. 

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/mostrar-nombre-paneles.png" width="80px"/>

Es recomendable dejarlos visibles.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/bordes-con-nombres-paneles.png" width="400px"/>

Utilizaremos el panel `Terminal` para trabajar con `sbt` y con
`git`. Es recomendable abrir dos tabs, uno para cada cosa. 

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/terminal.png" width="500px"/>


### Uso de Visual Studio Code para trabajar con la aplicación Play ###

Si no es posible utilizar un editor avanzado como IntelliJ es posible
usar en su lugar _Visual Studio Code_.

Abre la carpeta con el directorio del proyecto y abre un terminal con
la opción _Ver > Terminal integrado_. En ese terminal lanzaremos el
comando Docker para trabajar con `sbt`. Puedes abrir otro terminal
pulsando en el símbolo `+` para trabajar con Git.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/visual-studio-code.png" width="700px"/>

### Lanzar la aplicación Play ###

Podemos ejecutar la aplicación Play de tres formas. Utilizaremos las
tres a lo largo de las prácticas.

- Usando una máquina Docker.
- Usando el `sbt shell` que proporciona IntelliJ.
- Usando la configuración de ejecución de IntelliJ.

#### Máquina Docker ####

La máquina docker `domingogallardo/playframework` contiene todo el
software y librerías para ejecutar aplicaciones Play 2.5.18. La
ventaja de utilizar la máquina Docker es que Una vez
descargada la máquina ya no es necesario descargar librerías
adicionales. Está instalada en los laboratorios de la EPS.

Nos movemos al directorio de la aplicación Play y desde el terminal
lanzamos el comando `docker run` para ejecutar la máquina sobre el
directorio actual conectando el puerto 9000 en el mismo puerto de
nuestra máquina:

```text
$ cd play-proyecto-inicial
$ docker run --rm  -it -v "${PWD}:/code" -p 9000:9000 domingogallardo/playframework
[play-java] $ 
```

Aparecerá el prompt de sbt con el nombre del proyecto. Podremos lanzar
comandos de sbt como `run` o `test`. Haciendo `run` se ejecuta la
aplicación web. Por defecto el puerto al que hay que atacar es
el 9000. Accediendo a la URL <http://localhost:9000> pondremos en
marcha la aplicación. Haciendo `test` se lanzan los tests incluidos en
la aplicación.

Con `exit` se sale del prompt de sbt y automáticamente se para el
contenedor y se elimina el contenedor de Docker.

#### Shell sbt de IntelliJ ####

También es posible arrancar el shell de `sbt` en un panel propio que
proporciona IntelliJ.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/sbt-shell.png" width="400px"/>

Cuando lo ejecutamos por primera vez se descargan todas las librerías
necesarias. 

#### Configuración de ejecución de IntelliJ ####

También podemos crear una configuración de ejecución de IntelliJ con
la que podremos ejecutar y depurar los proyectos con la opción _Run >
Edit Configurations.._.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/run-debug-configuration.png" width="400px"/>

Una vez creada la configuración podremos seleccionarla y realizar una
ejecución o una depuración de la aplicación pulsando los botones
correspondientes en la parte superior de la ventana de IntelliJ.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/botones-run-debug.png" width="200px"/>


### Fichero routes ###

El `routes`, situado en el directorio `conf`, especifica el código a
ejecutar como respuesta a una petición HTTP.

**Fichero `conf/routes`**:

```text
# Routes
# This file defines all application routes (Higher priority routes first)
# ~~~~

# An example controller showing a sample home page
GET     /                           controllers.HomeController.index
# An example controller showing how to use dependency injection
GET     /count                      controllers.CountController.count
# An example controller showing how to write asynchronous code
GET     /message                    controllers.AsyncController.message

# Map static resources from the /public folder to the /assets URL path
GET     /assets/*file               controllers.Assets.versioned(path="/public", file: Asset)
```

Por ejemplo, cuando se recibe la petición `GET /` (cuando en
el navegador escribimos la URL `http::/localhost/`) se ejecutará el
método `index` de la clase `controllers.HomeController`. O cuando
desde el navegador accedamos a la URL `http://localhost/count` se
generará la petición `GET /count` y se ejecutará el método `count` de
la clase `controllers.CountController`.

### Controllers ###

El código a ejecutar cuando se realiza una petición HTTP se define en
métodos de clases que heredan de `Controller`. Se suelen colocar en el paquete
`controllers`. 

Por ejemplo, en la clase `controllers.HomeController` se define el
método `index`.

**Fichero `app/controllers/HomeController.java`**:

```java
public class HomeController extends Controller {

    /**
     * An action that renders an HTML page with a welcome message.
     * The configuration in the <code>routes</code> file means that
     * this method will be called when the application receives a
     * <code>GET</code> request with a path of <code>/</code>.
     */
    public Result index() {
        return ok(index.render("Your new application is ready."));
    }

}
```

Los métodos de las clases `Controller` deben devolver un objeto
`Result` que representa la respuesta HTTP a la petición. En el caso
anterior se devuelve un OK (código HTTP 200) junto con el código HTML
resultante de renderizar la vista `index`.

### Vistas ###

Las páginas HTML que se devuelven se construyen mediante
_vistas_. Las vistas se definen mediante plantillas Scala definidas
en el directorio `views`. En la llamada a renderizar la vista se
pueden pasar parámetros cuyos valores se utilizan en la propia vista.

Por ejemplo, la vista anterior `index` se define en el fichero
`index.scala.html` situado en el directorio `views`.

**Fichero `views/index.scala.html`**:

```text
@*
 * This template takes a single argument, a String containing a
 * message to display.
 *@
@(message: String)

@*
 * Call the `main` template with two arguments. The first
 * argument is a `String` with the title of the page, the second
 * argument is an `Html` object containing the body of the page.
 *@
@main("Welcome to Play") {

    @*
     * Get an `Html` object by calling the built-in Play welcome
     * template and passing a `String` message.
     *@
    @welcome(message, style = "java")

}
```

La vista recibe un parámetro `String`. En el cuerpo de la vista se
puede escribir código HTML, código Scala, y también llamar a otras
plantillas. Por ejemplo, en la vista anterior se llama a la plantilla
`main` que se define en el fichero `main.scala.html`, pasándole como
parámetro el código HTML generado por la plantilla `welcome`, definida
en el fichero `welcome.scala.html`.

**Fichero `views/main.scala.html`**:

```html
@*
 * This template is called from the `index` template. This template
 * handles the rendering of the page header and body tags. It takes
 * two arguments, a `String` for the title of the page and an `Html`
 * object to insert into the body of the page.
 *@
@(title: String)(content: Html)

<!DOCTYPE html>
<html lang="en">
    <head>
        @* Here's where we render the page title `String`. *@
        <title>@title</title>
        <link rel="stylesheet" media="screen" href="@routes.Assets.versioned("stylesheets/main.css")">
        <link rel="shortcut icon" type="image/png" href="@routes.Assets.versioned("images/favicon.png")">
        <script src="@routes.Assets.versioned("javascripts/hello.js")" type="text/javascript"></script>
    </head>
    <body>
        @* And here's where we render the `Html` object containing
         * the page content. *@
        @content
    </body>
</html>

```

**Fichero `views/welcome.scala.html`**:

```html
@(message: String, style: String = "java")

@defining(play.core.PlayVersion.current) { version =>

    <link rel="stylesheet" media="screen" href="/@@documentation/resources/style/main.css">

    <section id="top">
        <div class="wrapper">
            <h1><a href="https://playframework.com/documentation/@version/Home">@message</a></h1>
        </div>
    </section>

    <div id="content" class="wrapper doc">
        <article>

            <h1>Welcome to Play</h1>

            <p>
                Congratulations, you’ve just created a new Play application. This page will help you with the next few steps.
            </p>

            <blockquote>
                <p>
                    You’re using Play @version
                </p>
            </blockquote>

    ...
}
```

Para incorporar el valor del parámetro en la plantilla hay que
preceder el parámetro con `@`. En el ejemplo anterior se obtiene así
el mensaje, que se pinta en la parte superior de la página.


La página HTML resultante mostrada en el navegador es la siguiente:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/vista-main.png" width="500px"/>

La directiva `@defining` permite obtener un valor y
asignárselo a una variable que se utiliza en un bloque de código. En
el caso anterior se utiliza para obtener la versión de Play. Otro
ejemplo de su utilización es el que aparece en la documentación de
Play sobre plantillas:

```html
@defining(user.getFirstName() + " " + user.getLastName()) { fullName =>
  <div>Hello @fullName</div>
}
```


### Inyección de dependencias ###

Play usa el framework Java de Google [_Guice_]() para realizar inyección
de dependencias.

La anotación `@Inject` hace que Play inyecte en la variable anotada un
objeto nuevo del tipo indicado por la variable. Se puede definir la
anotación en la variable o en el constructor de la clase. 

Es posible definir _singletons_ con la anotación `@Singleton`.

En la aplicación ejemplo se define un servicio y un controller para
implementar un contador que se incrementa en cada petición a la acción
`count`. En el controller se inyecta el componente `counter`:

**Fichero `controllers/CountController.java`**:

```java
package controllers;

import javax.inject.*;
import play.mvc.*;

import services.Counter;

@Singleton
public class CountController extends Controller {

    private final Counter counter;

    @Inject
    public CountController(Counter counter) {
       this.counter = counter;
    }

    /**
     * An action that responds with the {@link Counter}'s current
     * count. The result is plain text. This action is mapped to
     * <code>GET</code> requests with a path of <code>/count</code>
     * requests by an entry in the <code>routes</code> config file.
     */
    public Result count() {
        return ok(Integer.toString(counter.nextCount()));
    }

}
```


El contador se define con una interfaz y una implementación
concreta. 

**Fichero `services/Counter.java`**:

```java
package services;

/**
 * This interface demonstrates how to create a component that is injected
 * into a controller. The interface represents a counter that returns a
 * incremented number each time it is called.
 *
 * The {@link Modules} class binds this interface to the
 * {@link AtomicCounter} implementation.
 */
public interface Counter {
    int nextCount();
}

```

**Fichero `services/AtomicCounter.java`**:

```java
package services;

import java.util.concurrent.atomic.AtomicInteger;
import javax.inject.*;

/**
 * This class is a concrete implementation of the {@link Counter} trait.
 * It is configured for Guice dependency injection in the {@link Module}
 * class.
 *
 * This class has a {@link Singleton} annotation because we need to make
 * sure we only use one counter per application. Without this
 * annotation we would get a new instance every time a {@link Counter} is
 * injected.
 */
@Singleton
public class AtomicCounter implements Counter {

    private final AtomicInteger atomicCounter = new AtomicInteger();

    @Override
    public int nextCount() {
       return atomicCounter.getAndIncrement();
    }

}
```

La definición de la clase concreta que se inyecta se realiza en el
método `configure()` de una clase llamada `Module` que debe extender
`AbstractModule` y estar situada en el paquete raíz.

**Fichero `Module.java`**:

```java
import com.google.inject.AbstractModule;

import services.AtomicCounter;
import services.Counter;

/**
 * This class is a Guice module that tells Guice how to bind several
 * different types. This Guice module is created when the Play
 * application starts.
 *
 * Play will automatically use any class called `Module` that is in
 * the root package. You can create modules in other locations by
 * adding `play.modules.enabled` settings to the `application.conf`
 * configuration file.
 */
public class Module extends AbstractModule {

    @Override
    public void configure() {
        // Set AtomicCounter as the implementation for Counter.
        bind(Counter.class).to(AtomicCounter.class);
    }

}
```


### Tests ###

Los tests se encuentran en el directorio `tests`. Se utiliza `JUnit`
como framework de testing.

Desde los tests se puede comprobar los distintos componentes de la
aplicación, incluyendo plantillas y peticiones a controllers.

#### Lanzamiento de los tests desde sbt ####

Para lanzar los tests desde la consola `sbt` se debe usar el comando
`test`. 

```text
[play-java] $ test
[info] Updating {file:/code/}root...
[info] Resolving jline#jline;2.14.3 ...
[info] Done updating.
[info] Test run started
[info] Test ApplicationTest.simpleCheck started
[info] Test ApplicationTest.renderTemplate started
[info] Test run finished: 0 failed, 0 ignored, 2 total, 1.337s
[info] Test run started
[info] Test IntegrationTest.test started
[info] application - Creating Pool for datasource 'default'
[info] application - ApplicationTimer demo: Starting application at 2018-08-21T07:41:46.226Z
[info] application - ApplicationTimer demo: Stopping application at 2018-08-21T07:41:52.807Z after 6s.
[info] application - Shutting down connection pool.
[info] Test run finished: 0 failed, 0 ignored, 1 total, 9.704s
[info] Passed: Total 3, Failed 0, Errors 0, Passed 3
[success] Total time: 37 s, completed Aug 21, 2018 7:41:53 AM
```

Podemos lanzar una parte de los tests con el comando `testOnly`
seguido del nombre completo de la clase (incluyendo el paquete en el
que esté incluida):

```text
[play-java] $ testOnly ApplicationTest
[info] Test run started
[info] Test ApplicationTest.simpleCheck started
[info] Test ApplicationTest.renderTemplate started
[info] Test run finished: 0 failed, 0 ignored, 2 total, 1.405s
[info] Passed: Total 2, Failed 0, Errors 0, Passed 2
[success] Total time: 12 s, completed Aug 21, 2018 9:58:57 AM
[play-java] $ 
```


#### Lanzamiento de los tests de IntelliJ ####

También es posible lanzar los tests desde el entorno IntelliJ pulsando
con el botón derecho la opción `Run` sobre la clase de test
seleccionada.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/tests-intellij.png" width="400px"/>


## Aplicación `mads-todolist-inicial` ##

La aplicación `mads-todolist-inicial` es una versión inicial de la
aplicación que se va a desarrollar durante todo el cuatrimestre en la
asignatura. 

Es una aplicación bastante más compleja que la vista
anteriormente. Entre otros, tiene los siguientes elementos:

- Distintos comandos HTTP en el fichero de rutas: GET, POST, DELETE.
- Recogida de datos en formularios HTML y validación de los datos.
- Base de datos gestionada con JPA (_Java Persisence API_), un ORM (_Object Relational
  Mapping_) implementado por la librería Hibernate. Se utiliza una
  capa de persistencia basada en clases _repository_.
- _Capa de servicio_ que proporciona la **lógica de negocio** a los
  controllers.
- Las _clases controller_ sólo se encargan de hacer de interfaz de la
  capa de servicio: 
    - Recoger datos de la petición HTTP,
    - tratar y validar estas entradas, 
    - llamar a la clase de servicio para que se realice la acción
      requerida, y
    - convertir la respuesta obtenida de la aplicación en una vista
      que se devuelve como respuesta de la petición.
- En las plantillas se incluye _Bootstrap_ y scripts JavaScript.
- Las clases de servicio y de _repository_ se obtienen por inyección
  de dependencias.
- Gran número de tests que prueban sobre todo la capa de servicios.
- Distintos ficheros de configuración para poder arrancar la
  aplicación en distintos entornos: desarrollo, integración y _stage_
  (similar a producción).

A continuación se muestran dos de sus pantallas.

<table>
<tr>
<td><img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/login.png" width="700px"/></td>
</tr>
<tr>
<td align="center"> Pantalla de login </td>
</table>


<table>
<tr>
<td><img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/tareas.png" width="700px"/></td>
</tr>
<tr>
<td align="center"> Pantalla con listado de tareas </td>
</table>


### Descarga de la aplicación `mads-todolist-inicial` ###

Se encuentra en GitHub:
<https://github.com/domingogallardo/mads-todolist-inicial>. 

Puedes descargarla con el comando `git clone`:

```text
$ git clone https://github.com/domingogallardo/mads-todolist-inicial.git
```

Se creará el directorio `mads-todolist-inicial` en el que se habrá
descargado la aplicación.

### Importación en IntellJ IDEA ###

Al importar la aplicación en IntelliJ IDEA aparece el aviso de que
se ha detectado el framework JPA y da la opción de configurarlo. La
configuración es sencilla, sólo hay que aceptar la localización del
fichero `persistence.xml` que nos muestra la ventana de diálogo.

Hablaremos más adelante de JPA.

### Ejecución de la aplicación usando la base de datos en memoria ###

Si ejecutamos la aplicación usando el comando `docker run` ya visto se
utilizará la base de datos H2 en memoria. Los datos almacenados en
ella sólo durarán mientras que está en marcha el contenedor.

```text
$ docker run --rm  -it -v "${PWD}:/code" -p 9000:9000 domingogallardo/playframework
```


### Base de datos MySQL con Docker ###

Si queremos que los datos introducidos persistan a distintas
activaciones de la aplicación web debemos usar una base de datos
externa. Esto es necesario cuando la aplicación esté en producción,
pero también puede ser útil para realizar pruebas manuales en
desarrollo.

Podemos utilizar Docker para poner en marcha un servidor MySQL con el
siguiente comando:

```text
$ docker run -d -p 3316:3306 --name db-mysql -e MYSQL_ROOT_PASSWORD=mads -e MYSQL_DATABASE=mads mysql:5
```

El comando pone en marcha un servidor MySQL escuchando en el puerto
3316 del host con el nombre docker `db-mysql`, con la contraseña de
root indicada y creando la base de datos `mads`.

El puerto del host 3316 se mapea con el puerto interno del
contenedor 3306. Ponemos el puerto 3316 para evitar posibles
conflictos con un posible servidor de MySQL que tengamos funcionando
en el host.

!!! Warning "Cuidado"

    En los laboratorios de la EPS está instalada la imagen
    5.7.18 de MySQL. Hay que definir explícitamente esa versión en el
    comando docker, escribiendo `mysql:5.7.18`.

Podemos comprobar que el contenedor está funcionando con el comando
`docker container ls`:

```text
$ docker container ls
CONTAINER ID  IMAGE  COMMAND                  CREATED         STATUS         PORTS                  NAMES
7c1bed0b5b7e  mysql  "docker-entrypoint..."   6 seconds ago   Up 4 seconds   0.0.0.0:3316->3306/tcp db-mysql
```

Para parar y volver a poner en marcha el contenedor mysql puedes usar
los comandos `docker stop <container-id>` y `docker start
<container-id>`. Los datos añadidos en la base de datos se mantendrán
mientras que el contenedor no se borre. El comando `docker container
ls` lista los contenedores en marcha, y con la opción `-a` también los
parados.
   
```text
$ docker container ls
CONTAINER ID        IMAGE                CREATED             STATUS              PORTS                               NAMES
bd057639b6ac        mysql:5              30 minutes ago      Up 22 minutes       33060/tcp, 0.0.0.0:3316->3306/tcp   db-mysql
$ docker container stop bd057639b6ac
$ docker container ls -a
CONTAINER ID        IMAGE                CREATED             STATUS                     PORTS               NAMES
bd057639b6ac        mysql:5              31 minutes ago      Exited (0) 7 seconds ago                       db-mysql
$ docker container start bd057639b6ac
$ docker container ls
CONTAINER ID        IMAGE                CREATED             STATUS              PORTS                               NAMES
bd057639b6ac        mysql:5              32 minutes ago      Up 5 seconds        33060/tcp, 0.0.0.0:3316->3306/tcp   db-mysql
```

Podemos usar el identificador o el nombre del contenedor para pararlo:

```text
$ docker container stop db-mysql
```

Para borrar un contenedor debe estar parado y debemos usar el comando

```text
docker container rm <container-id> o <container-name>
```


### Ejecución de la aplicación usando la base de datos MySQL ###

#### Desde Docker ####

Lanzamos la aplicación con Docker, definiendo en variables de entorno
la URL, el usuario y la contraseña con la que debe conectarse la
aplicación a la base de datos. Usamos la opción `link` de docker para
definir el nombre lógico del contenedor al que debe conectarse la
aplicación.

```text
$ docker run --link db-mysql --rm -it -p 9000:9000 -e \
DB_URL="jdbc:mysql://db-mysql:3306/mads" -e DB_USER_NAME="root" -e \
DB_USER_PASSWD="mads" -v "${PWD}:/code" domingogallardo/playframework
```

Y desde la consola sbt modificamos la preferencia `config.file` para
que la aplicación utilice la configuración definida en el fichero
`conf/develop-mysql.conf` (lo explicamos más adelante).

```text
[mads-todolist-2018] $ set javaOptions += "-Dconfig.file=conf/develop-mysql.conf"
[mads-todolist-2018] $ run
```

#### Desde el run/debug de IntelliJ ####

También es posible definir una configuración de run/debug en IntelliJ
en la que se inicialice la preferencia `config.file` y las variables
de entorno para conectarse con la base de datos, en el puerto del host
en el que está escuchando (3331, si hemos lanzado el servicio de base
de datos usando Docker como hemos visto anteriormente):

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/bdexterna-intellij.png" width="600px"/>

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/variables-entorno-intellij.png" width="300px"/>

!!! Warning "Cuidado"

    Si estás lanzando MySQL usando _Docker Toolbox_ debes
    modificar la `DB_URL` indicando el _host_ al que conectarse (no será
    _localhost_). La dirección IP será la que aparece en la consola de
    docker al arrancar. Por ejemplo `jdbd:mysql://192.168.99.100/mads`.


### Panel `Database` de IntelliJ ###

Desde el panel `Database` de IntelliJ (en la esquina superior derecha)
es posible crear una conexión a la base de datos que nos permitirá
verificar cómo se guardan los datos de la aplicación.

Hay que añadir una base de datos de tipo MySQL y configurarla con los
siguientes parámetros:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/conexionbd-intellij.png" width="500px"/>

!!! Warning "Cuidado"

    Igual que en el apartado anterior, si estás lanzando
    MySQL usando _Docker Toolbox_ debes indicar el _host_ al que
    conectarse (no será _localhost_) escribiendo la dirección IP que
    aparece en la consola de docker al arrancar. 

Es posible examinar el esquema de la base de datos:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/esquema-bd.png" width="300px"/>

Y examinar tablas en concreto:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/tablabd-intellij.png" width="300px"/>


### Configuración de la aplicación ###

Los distintos parámetros de la aplicación Play se configuran en
un fichero de propiedades. 

#### Configuración por defecto ####

El fichero de configuración que carga la
aplicación por defecto es `conf/application.conf`.

Por ejemplo, las propiedades relacionadas con la definición de la base
de datos que se definen en el fichero son las siguientes:

```text
# Default persistenceUnit for JPA
jpa.default = develop

db {
  # You can declare as many datasources as you want.
  # By convention, the default datasource is named `default`

  # https://www.playframework.com/documentation/latest/Developing-with-the-H2-Database
  # Memory H2 database
  default.driver = org.h2.Driver
  default.url = "jdbc:h2:mem:play;MODE=MYSQL"
  #default.username = sa
  #default.password = ""
  # Definiemos el nombre JNDI de la BD que va a usar la aplicación
  default.jndiName=DBTodoList

  # You can turn on SQL logging for any datasource
  # https://www.playframework.com/documentation/latest/Highlights25#Logging-SQL-statements
  # default.logSql=true
}
```

En el fichero por defecto se define una conexión con la base de datos
de memoria H2 en la fuente de datos llamada `default` (la fuente de
datos que usa por defecto la aplicación). Se definen las siguientes propiedades:

- `jpa.default`: Nombre de la unidad de persistencia JPA que se usará en la aplicación.
- `db.default.driver`: Driver de la base de datos.
- `db.default.url`: URL de conexión a la base de datos.
- `db.default.jndiName`: Nombre lógico JNDI que se asigna a la base de datos.
- `db.default.logSql`: Si se descomenta se mostrará en la consola el log de todas las
  operaciones sobre la base de datos.

#### Otras configuraciones ####

Como ya hemos visto, modificando la propiedad del sistema Java
`config.file` podemos definir un fichero de configuración distinto.

Se definen también los siguientes ficheros adicionales que se usarán
para lanzar la aplicación en distintas configuraciones:

- `develop-mysql.conf`: configuración de desarrollo con base de datos
  externa. La aplicación trabaja sobre una base de datos MySQL externa cuyo
  esquema se actualiza automáticamente al modificar y añadir nuevas
  entidades a la aplicación.
- `production.conf`: configuración de producción. La aplicación
  trabaja sobre una base de datos MySQL externa, cuyo esquema es
  validado para que se corresponda con las entidades de la aplicación.

**Fichero `conf/develop-mysql.conf`**:

```text
include "application.conf"

db.default.driver=com.mysql.jdbc.Driver
db.default.url=${?DB_URL}
db.default.username=${?DB_USER_NAME}
db.default.password=${?DB_USER_PASSWD}
```

**Fichero `conf/production.conf`**:

```text
include "application.conf"

play.crypto.secret="abcdefghijkl"

jpa.default = production

db.default.driver=com.mysql.jdbc.Driver
db.default.url=${?DB_URL}
db.default.username=${?DB_USER_NAME}
db.default.password=${?DB_USER_PASSWD}
```

Los dos ficheros de configuración incluyen el fichero
`application.conf` y después modifican las propiedades necesarias. Los
valores de los parámetros de configuración de la base de datos `url`,
`username` y `password` se obtienen de las variables de entorno.


### Gestión de persistencia con JPA ###

Para la gestión de la persistencia de los datos en una aplicación Play
usaremos JPA (_Java Persistence API_), en concreto la implementación
5.2.5 de Hibernate.

#### Definición del modelo de datos ####

El framework JPA permite definir el esquema de la base de datos usando
anotaciones en las clases denominadas de entidad. Para cada clase de
entidad se define una tabla en la base de datos, con columnas que se
mapean con sus atributos.

Por ejemplo, la clase `Usuario` define una tabla `Usuario` en la base
de datos. Los distintos atributos (`login`, `email`, ...) se
corresponden con las columnas de la tabla. 

El atributo `id` se corresponde con la clave primaria de la tabla. JPA
define varias estrategias para obtener esa clave primera, y se ha
escogido la estrategia `AUTO`. Cuando un usuario creado en memoria se haga
persistente en la base de datos, este atributo se actualizará con el
valor obtenido por Hibernate. La estrategia `AUTO` se basa en obtener
el valor de la clave primaria usando una tabla auxiliar
`hibernate_sequence` que guarda el siguiente valor a asignar a una
nueva clave primaria.

Además de los atributos, en la clase se define un constructor con los
atributos obligatorios para definir un usuario, unos _getters_ y
_setters_ y los métodos `equals` y `hashCode` para comparar usuarios.

**Fichero `models/Usuario.java`:**

```java
@Entity
public class Usuario {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String login;
    private String email;
    private String password;
    private String nombre;
    private String apellidos;
    @Temporal(TemporalType.DATE)
    private Date fechaNacimiento;
    // Relación uno-a-muchos entre usuario y tarea
    @OneToMany(mappedBy = "usuario", fetch = FetchType.EAGER)
    private Set<Tarea> tareas = new HashSet<>();
    @ManyToMany(mappedBy = "usuarios", fetch = FetchType.EAGER)
    private Set<Equipo> equipos = new HashSet<>();

    // Un constructor vacío necesario para JPA
    public Usuario() {
    }

    // El constructor principal con los campos obligatorios
    public Usuario(String login, String email) {
        this.login = login;
        this.email = email;
    }

    // Getters y setters necesarios para JPA
    ...
 
    // Función para imprimr los datos de un usuario
    public String toString() {
        String fechaStr = null;
        if (fechaNacimiento != null) {
            SimpleDateFormat formateador = new SimpleDateFormat("dd-MM-yyyy");
            fechaStr = formateador.format(fechaNacimiento);
        }
        return String.format("Usuario id: %s login: %s password: %s nombre: %s " +
                        "apellidos: %s e-mail: %s fechaNacimiento: %s",
                id, login, password, nombre, apellidos, email, fechaNacimiento);
    }


    // Funciones hashCode y equals para poder comparar usuarios y
    // necesarias para poder crear un Set de usuarios
    @Override
    public int hashCode() {
        // Devolvemos el hash de los campos obligatorios
        return Objects.hash(login, email);
    }

    // Si el usuario tiene un ID (se ha obtenido de la BD)
    // la comparación se basa en ese ID. Si el ID no existe (el usuario
    // se ha creado en memoria y todavía no se ha sincronizado con la BD)
    // la comparación se basa en los atributos obligatorios.
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (getClass() != obj.getClass()) return false;
        Usuario other = (Usuario) obj;
        if (id != null && other.id != null) {
            // Si tenemos los ID, comparamos por ID
            return (id == other.id);
        }
            // sino comparamos por campos obligatorios
        else {
            if (login == null) {
                if (other.login != null) return false;
            } else if (!login.equals(other.login)) return false;
            if (email == null) {
                if (other.email != null) return false;
            } else if (!email.equals(other.email)) return false;
        }
        return true;
    }
}
```

En la definición de la entidad también se incluyen relaciones con
otras entidades. En este caso un `Usuario` tiene muchas `Tarea`s (una
relación una-a-muchos) y puede participar en `Equipo`s (relación
muchos-a-muchos). 

La relación uno-a-muchos se representa en la base de datos con una
clave ajena. El atributo `mappedBy` indica que la clave ajena se va a
guardar en la columna correspondiente con el atributo `usuario` de la
entidad `Tarea`.

La relación muchos-a-muchos se representa en la base de datos con una
tabla auxiliar con dos claves ajenas. El atributo `mappedBy` indica
que la definición de esa tabla se encuentra en el atributo `usuario`
de la entidad `Equipo`.

Las definiciones de `Tarea` y `Equipo` son las siguientes:

**Fichero `models/Tarea.java`**:

```java
@Entity
public class Tarea {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String titulo;
    // Relación muchos-a-uno entre tareas y usuario
    @ManyToOne
    // Nombre de la columna en la BD que guarda físicamente
    // el ID del usuario con el que está asociado una tarea
    @JoinColumn(name = "usuarioId")
    public Usuario usuario;

    public Tarea() {
    }

    // Constructor, getters y setters, equals y hashCode

}
```

**Fichero `models/Equipo.java`**:

```java
@Entity
public class Equipo {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String nombre;
    @ManyToMany
    @JoinTable(name = "Equipo_Usuario",
        joinColumns = { @JoinColumn(name = "fk_equipo") },
        inverseJoinColumns = {@JoinColumn(name = "fk_usuario")})
    private Set<Usuario> usuarios = new HashSet<>();

    // Un constructor vacío necesario para JPA
    public Equipo() {
    }

    // Constructor, getters y setters, equals y hashCode
    
    // Métodos de actualización de la relación muchos-a-muchos con usuario

    public void addUsuario(Usuario usuario) {
        usuarios.add(usuario);
        usuario.getEquipos().add(this);
    }

    public void removeUsuario(Usuario usuario) {
        usuarios.remove(usuario);
        usuario.getEquipos().remove(this);
    }

}
```

#### Fichero de configuración de JPA ####

El fichero `conf/META-INF/persistence.xml` es necesario para que JPA
funcione correctamente. Es el fichero de configuración en el que se
definen distintos elementos necesarios para la configuración de JPA.

- Nombre JNDI de la fuente de datos con la que se conectará la
  aplicación: `DBTodoList`, definida en el fichero de configuración de
  la aplicación Play (`/conf/application.conf`).
- Clases entidad que se definen en la aplicación.
- Propiedad `hibernate.hbm2ddl.auto` que indica cómo JPA va a
  gestionar las tablas en la base de datos.
    - Si el valor es `update`, al arrancar la aplicación las tablas de
      la base de datos se actualizan (o se crean, si la base de datos
      está vacía) para que se correspondan con las entidades. Se suele
      utilizar este valor cuando estamos desarrollando la aplicación.
    - Si el valor es `validate`, al arrancar la aplicación se
      comprueba si la base de datos contiene tablas que se
      corresponden con las definiciones de las entidades. Si no es
      así, JPA lanza una excepción y deja de funcionar. Se suele
      utilizar este valor en el funcionamiento de la aplicación en
      producción.
      
Definimos dos configuraciones, una denominada `develop` y otra
denominada `production`. La única diferencia entre ellas es el valor
de la propiedad `hibernate.hbm2ddl.auto`.

**Fichero `conf/META-INF/persistence.xml`**:

```xml
<persistence xmlns="http://xmlns.jcp.org/xml/ns/persistence"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/persistence http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd"
   version="2.1">

    <!-- MySQL Persistence Unit - Develop: hbm2ddl.auto = UPDATE -->

<persistence-unit name="develop" transaction-type="RESOURCE_LOCAL">
   <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>
   <non-jta-data-source>DBTodoList</non-jta-data-source>
   <class>models.Usuario</class>
   <class>models.Tarea</class>
   <class>models.Equipo</class>
   <properties>
        <property name="hibernate.dialect" value="org.hibernate.dialect.MySQL5Dialect"/>
        <property name="hibernate.hbm2ddl.auto" value="update"/>
   </properties>
</persistence-unit>

<!-- MySQL Persistence Unit - Production: hbm2ddl.auto = VALIDATE -->

<persistence-unit name="production" transaction-type="RESOURCE_LOCAL">
   <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>
   <non-jta-data-source>DBTodoList</non-jta-data-source>
   <class>models.Usuario</class>
   <class>models.Tarea</class>
   <class>models.Equipo</class>
   <properties>
      <property name="hibernate.dialect" value="org.hibernate.dialect.MySQL5Dialect"/>
      <property name="hibernate.hbm2ddl.auto" value="validate"/>
   </properties>
</persistence-unit>
</persistence>
```

#### Actualización de los datos ####

Se definen clases _repository_ que definen métodos para actualizar las
entidades y realizar _queries_ sobre ellas. Para dejar abierta la
posibilidad de cambiar la implementación, se definen con interfaces.

**Fichero `models/UsuarioRepository.java`**:

```java
public interface UsuarioRepository {
    Usuario add(Usuario usuario);
    
    // Queries
    Usuario findById(Long id);
    Usuario findByLogin(String login);
}
```

**Fichero `models/TareaRepository.java`**:

```java
public interface TareaRepository {
    Tarea add(Tarea tarea);
    Tarea update(Tarea tarea);
    void delete(Tarea tarea);
    
    // Queries
    Tarea findById(Long idTarea);
}
```

**Fichero `models/EquipoRepository.java`**:

```java
public interface EquipoRepository {
    Equipo add(Equipo equipo);
    Equipo update(Equipo equipo);
    void delete(Equipo equipo);
    void addUsuarioEquipo(Usuario usuario, Equipo equipo);
    void deleteUsuarioEquipo(Usuario usuario, Equipo equipo);

    // Queries
    Equipo findById(Long idEquipo);
    Equipo findByNombre(String nombre);
    List<Equipo> findAll();
    List<Usuario> findUsuariosEquipo(String nombreEquipo);
}
```

La implementación utiliza JPA para realizar las actualizaciones y
consultas sobre las entidades. Cada método abre y cierra una
transacción en la que se propaga el cambio a la base de datos. 

Para trabajar con JPA en Play se debe usar un objeto `JPAApi` que se
obtiene por inyección de dependencias. Play guarda en la variable
`jpaApi` una instancia con la que podemos, entre otras cosas, abrir y
cerrar transacciones.

Por ejemplo, la implementación de la parte de la interfaz
`EquipoRepository` que trata de la actualización de la entidad en la
base de datos es la siguiente:


**Fichero `models/JPAEquipoRepository.java`**:

```java

public class JPAEquipoRepository implements EquipoRepository {
    JPAApi jpaApi;

    @Inject
    public JPAEquipoRepository(JPAApi api) {
        this.jpaApi = api;
    }

    @Override
    public Equipo add(Equipo equipo) {
        return jpaApi.withTransaction(entityManager -> {
            entityManager.persist(equipo);
            entityManager.flush();
            entityManager.refresh(equipo);
            return equipo;
        });
    }

    @Override
    public Equipo update(Equipo equipo) {
        return jpaApi.withTransaction(entityManager -> {
            return entityManager.merge(equipo);
        });
    }

    @Override
    public void delete(Equipo equipo) {
        jpaApi.withTransaction( () -> {
            EntityManager entityManager = jpaApi.em();
            Equipo equipoBD = entityManager.getReference(Equipo.class, equipo.getId());
            entityManager.remove(equipoBD);
        });
    }

    @Override
    public void addUsuarioEquipo(Usuario usuario, Equipo equipo) {
        jpaApi.withTransaction( () -> {
            EntityManager entityManager = jpaApi.em();
            Equipo equipoBD = entityManager.merge(equipo);
            Usuario usuarioBD = entityManager.merge(usuario);
            equipoBD.addUsuario(usuarioBD);
        });
    }

    @Override
    public void deleteUsuarioEquipo(Usuario usuario, Equipo equipo) {
        jpaApi.withTransaction( () -> {
            EntityManager entityManager = jpaApi.em();
            Equipo equipoBD = entityManager.merge(equipo);
            Usuario usuarioBD = entityManager.merge(usuario);
            equipoBD.removeUsuario(usuarioBD);
        });
    }
```

Todos los métodos trabajan con un `EntityManager`, que es la clase de
JPA que gestiona las actualizaciones y _queries_ sobre la base de
datos.

Y las _queries_ se implementan de la siguiente manera:

**Fichero `models/JPAEquipoRepository.java`**:

```java
    @Override
    public Equipo findById(Long idEquipo) {
        return jpaApi.withTransaction(entityManager -> {
            return entityManager.find(Equipo.class, idEquipo);
        });
    }

    @Override
    public Equipo findByNombre(String nombre) {
        return jpaApi.withTransaction(entityManager -> {
            TypedQuery<Equipo> query = entityManager.createQuery(
                    "select e from Equipo e where e.nombre = :nombre", Equipo.class);
            try {
                Equipo equipo = query.setParameter("nombre", nombre).getSingleResult();
                return equipo;
            } catch (NoResultException ex) {
                return null;
            }
        });
    }

    @Override
    public List<Equipo> findAll() {
        return jpaApi.withTransaction(entityManager -> {
            TypedQuery<Equipo> query = entityManager.createQuery(
                    "select e from Equipo e", Equipo.class);
            return query.getResultList();
        });
    }

    public List<Usuario> findUsuariosEquipo(String nombreEquipo) {
        return jpaApi.withTransaction(entityManager -> {
            TypedQuery<Usuario> query = entityManager.createQuery(
                    "select u from Usuario u join u.equipos e where e.nombre = :nombreEquipo", Usuario.class);
            try {
                return query.setParameter("nombreEquipo", nombreEquipo).getResultList();
            } catch (NoResultException ex) {
                return null;
            }
        });
    }
}
```

#### Recuperación _eager_ y _lazy_ de las colecciones ####

En la aplicación se definen relaciones _a-muchos_ entre las
entidades:

- Relación _uno-a-muchos_ entre usuarios y tareas: un usuario tiene muchas tareas
- Relación _muchos-a-muchos_ entre usuarios y equipos: un equipo tiene
  muchos usuarios y un usuario participa en varios equipos.
  
En las entidades estas relaciones se definen de la siguiente forma:

```java
@Entity
public class Usuario {
    ...
    // Relación uno-a-muchos entre usuario y tarea
    @OneToMany(mappedBy = "usuario", fetch = FetchType.EAGER)
    private Set<Tarea> tareas = new HashSet<>();
    @ManyToMany(mappedBy = "usuarios", fetch = FetchType.EAGER)
    private Set<Equipo> equipos = new HashSet<>();
    ...
}

@Entity
public class Tarea {
    ...
    // Relación muchos-a-uno entre tareas y usuario
    @ManyToOne
    // Nombre de la columna en la BD que guarda físicamente
    // el ID del usuario con el que está asociado una tarea
    @JoinColumn(name = "usuarioId")
    public Usuario usuario;
    ...
}

public class Equipo {
    ...
    @ManyToMany
    @JoinTable(name = "Equipo_Usuario",
        joinColumns = { @JoinColumn(name = "fk_equipo") },
        inverseJoinColumns = {@JoinColumn(name = "fk_usuario")})
    private Set<Usuario> usuarios = new HashSet<>();
    ...
}
```

**Relaciones _lazy_**

Por defecto, todas las relaciones _a-muchos_ en JPA se definen de
tipo `LAZY`. 

La característica de los atributos marcados como _lazy_ en JPA es que
no se traen a memoria cuando se recupera la entidad, sino cuando se
consultan. Por ejemplo, en el caso de equipos y usuarios, la lista de
usuarios de un equipo es un atributo _lazy_. Veamos el método
`findById` de un equipo que devuelve una entidad `Equipo` a partir de
su identificador:


```java
public Equipo findById(Long idEquipo) {
    return jpaApi.withTransaction(entityManager -> {
        return entityManager.find(Equipo.class, idEquipo);
    });
}
```

El método `jpaApi.withTransaction` abre y cierra una conexión con la base de
datos que es gestionada por el _entity manager_. La conexión está
abierta mientras se ejecuta el código dentro del `withTransaction` (la
llamada a `find` que recupera el equipo). Pero cuando se hace el
`return` esa conexión se cierra y se devuelve un equipo cuya lista de
usuarios no se ha cargado a memoria. 

Si intentamos acceder a una colección _lazy_ sin estar en el ámbito
del _entity manager_ se producirá un error porque no se puede
inicializar esa colección. Por ejemplo, el siguiente test produce un
error cuando se llama al método `size()` y se intenta contar los
elementos de la conexión _lazy_:

```java
@Test
public void errorLazy() {
    EquipoRepository equipoRepository = injector.instanceOf(EquipoRepository.class);
    Equipo equipo = equipoRepository.findById(1005L);
    assertEquals(1, equipo.getUsuarios().size());
}

// Se produce el siguiente error:
// Test models.EquipoTest.errorLazy failed:
// org.hibernate.LazyInitializationException: failed to lazily initialize a collection 
// of role: models.Equipo.usuarios, could not initialize proxy - no Session
```

¿Cómo podemos solucionar esto? La clave es que sólo podremos recuperar
una colección _lazy_ **estando en un _entity manager_
abierto**. 

Por ejemplo, podemos hacer un método específico que devuelve la
colección de usuarios de un equipo:

```java
// Versión en la que se obtienen los usuarios accediendo a la colección lazy
public List<Usuario> findUsuariosEquipo(Long idEquipo) {
    return jpaApi.withTransaction(entityManager -> {
        Equipo equipo = entityManager.find(Equipo.class, idEquipo);
        equipo.getUsuarios().size();
        List<Usuario> usuarios = new ArrayList(equipo.getUsuarios());
        return usuarios;
    });
}
```

La llamada a `size()` en la línea 5 accede a la colección estando el
_entity manager_ abierto y trae a memoria sus elementos de la base de
datos. Por ello la colección de usuarios que se devuelve ya contiene
todos los usuarios del equipo.

Otra forma de recuperar colecciones _lazy_ es haciendo directamente
una query:

```java
// Versión en la que obtienen los usuarios mediante una query
public List<Usuario> findUsuariosEquipo(Long idEquipo) {
    return jpaApi.withTransaction(entityManager -> {
        TypedQuery<Usuario> query = entityManager.createQuery(
                "select u from Usuario u join u.equipos e where e.id = :idEquipo", Usuario.class);
        try {
            return query.setParameter("idEquipo", idEquipo).getResultList();
        } catch (NoResultException ex) {
            return null;
        }
    });
}
```

**Relaciones _eager_**

Frente a la recuperación _lazy_ de colecciones, también existe la
posibilidad de definir una colección como de tipo _EAGER_. En este
caso JPA se traerá siempre a memoria todos los elementos. Es el caso
de la relación entre un usuario y sus tareas.

En general, no es conveniente definir una relación como _eager_ porque
puede provocar problemas de rendimiento en el caso en que haya muchos
elementos relacionados. 

Pero si no hay muchos datos en la relación y los vamos a usar con
frecuencia, sí que es aconsejable usar el tipo _EAGER_ para facilitar
el manejo de la entidad.

### Servicios ###

La capa de servicios es la capa intermedia entre la capa de
_controllers_ y la de _repository_. Es la capa que implementa toda la
lógica de negocio de la aplicación.

La responsabilidad principal de la capa de servicios es obtener o
crear los objetos entidad necesarios para cada funcionalidad a partir
de los datos que manda la capa _controller_, trabajar con ellos en
memoria y hacer persistentes los cambios utilizando la capa
_repository_.

La capa de servicios también gestionará errores y lanzará excepciones
cuando no se pueda realizar alguna funcionalidad.

Los servicios obtienen instancias de _Repository_ usando inyección de
dependencias.

**Ventajas de utilizar una capa de servicios**

Al utilizar clases de servicios podemos aislar la lógica de negocio de
la aplicación usando métodos y objetos Java, sin preocuparnos de cómo
obtener los datos de la interfaz de usuario ni de cómo mostrar los
resultados. De esto ya se ocuparán las clases _controller_. De esta
forma, si se necesita modificar la interfaz de usuario de la
aplicación, o convertirla en un servicio REST que devuelva JSON en
lugar de HTML sólo tendremos que tocar las clases _controller_, no las
de servicio.

Además, al no tener ninguna dependencia con la interfaz de usuario,
estas clases de servicios también podrán ser fácilmente testeadas. La
mayoría de los tests automáticos los haremos sobre ellas.

**Fichero `services/UsuarioService.java`**:

```java
public class UsuarioService {
    UsuarioRepository repository;

    // Play proporcionará automáticamente el UsuarioRepository necesario
    // usando inyección de dependencias
    @Inject
    public UsuarioService(UsuarioRepository repository) {
        this.repository = repository;
    }

    public Usuario creaUsuario(String login, String email, String password) {
        if (repository.findByLogin(login) != null) {
            throw new UsuarioServiceException("Login ya existente");
        }
        Usuario usuario = new Usuario(login, email);
        usuario.setPassword(password);
        return repository.add(usuario);
    }

    public Usuario findUsuarioPorLogin(String login) {
        return repository.findByLogin(login);
    }

    public Usuario findUsuarioPorId(Long id) {
        return repository.findById(id);
    }

    public Usuario login(String login, String password) {
        Usuario usuario = repository.findByLogin(login);
        if (usuario != null && usuario.getPassword().equals(password)) {
            return usuario;
        } else {
            return null;
        }
    }
}
```

**Fichero `services/UsuarioServiceException.java`**:

```java
public class UsuarioServiceException extends RuntimeException {

    public UsuarioServiceException() {
    }

    public UsuarioServiceException(String message) {
        super(message);
    }
}
```

### Controllers ###

Las clases _controllers_ son las que gestionan la interfaz de usuario
de la aplicación. Se encargan de recibir los datos de las peticiones
HTTP, llamar a la clase de servicio necesaria para procesar la lógica
de negocio y mostrar la vista con la información resultante
proporcionada por la clase de servicio.

En la aplicación se definen tres clases controller:

- `UsuarioController`: con métodos para registrar y logear usuarios.
- `TareasController`: con métodos para crear, borrar y modificar
  tareas de un usuario.
- `EquipoController`: con métodos para crear, añadir usuarios y listar equipos.

Por ejemplo, la clase `EquipoController` define las acciones
relacionadas con crear equipos de usuarios.

En este controlador se obtienen los datos del formulario de la
petición HTTP usando un `DynamicForm` que contiene todos los valores
(Strings) asociados a los datos del formulario. 

También es posible realizar un _mapping_ automático entre los datos de
un formulario y un objeto Java usando un objeto `Form`. En el
`UsuarioController` se puede ver un ejemplo que usa las clases `Login`
y `Registro`. En este caso es posible definir restricciones en los
atributos y realizar una validación en el servidor.

**Fichero `controllers/EquipoController.java`**:

```java
package controllers;

public class EquipoController extends Controller {
    @Inject
    FormFactory formFactory;
    @Inject
    EquipoService equipoService;

    @Security.Authenticated(ActionAuthenticator.class)
    public Result formularioNuevoEquipo() {
        return ok(formNuevoEquipo.render(""));
    }

    @Security.Authenticated(ActionAuthenticator.class)
    public Result creaNuevoEquipo() {
        DynamicForm requestData = formFactory.form().bindFromRequest();
        String nombre = requestData.get("nombre");
        if (nombre == null || nombre.equals("")) {
            return badRequest(formNuevoEquipo.render("Debes rellenar el nombre"));
        }
        equipoService.addEquipo(nombre);
        return ok("Equipo " + nombre + " añadido correctamente");
    }

    public Result listaEquipos() {
        List<Equipo> equipos = equipoService.allEquipos();
        return ok(listaEquipos.render(equipos));
    }

    @Security.Authenticated(ActionAuthenticator.class)
    public Result formularioAddUsuarioEquipo() {
        return ok(formEquipoUsuario.render());
    }

    @Security.Authenticated(ActionAuthenticator.class)
    public Result addUsuarioEquipo() {
        DynamicForm requestData = formFactory.form().bindFromRequest();
        String equipo = requestData.get("equipo");
        String usuario = requestData.get("usuario");
        try {
            equipoService.addUsuarioEquipo(usuario, equipo);
            return ok("Usuario " + usuario + " añadido al equipo " + equipo);
        } catch (EquipoServiceException exception) {
            return notFound("No existe usuario / equipo");
        }
    }
}
```


La clase `UsuarioController` se encarga de las acciones de registro y login.

**Fichero `controllers/UsuarioController.java`**:

```java
package controllers;

public class UsuarioController extends Controller {

    @Inject
    FormFactory formFactory;
    // Play injecta un usuarioService junto con todas las dependencias necesarias:
    // UsuarioRepository y JPAApi
    @Inject
    UsuarioService usuarioService;

    public Result saludo(String mensaje) {
        return ok(saludo.render("El mensaje que he recibido es: " + mensaje));
    }

    public Result formularioRegistro() {
        return ok(formRegistro.render(formFactory.form(Registro.class), ""));
    }

    public Result registroUsuario() {
        Form<Registro> form = formFactory.form(Registro.class).bindFromRequest();
        if (form.hasErrors()) {
            return badRequest(formRegistro.render(form, "Hay errores en el formulario"));
        }
        Registro datosRegistro = form.get();

        if (usuarioService.findUsuarioPorLogin(datosRegistro.login) != null) {
            return badRequest(formRegistro.render(form, "Login ya existente: escoge otro"));
        }

        if (!datosRegistro.password.equals(datosRegistro.confirmacion)) {
            return badRequest(formRegistro.render(form, "No coinciden la contraseña y la confirmación"));
        }
        Usuario usuario = usuarioService.creaUsuario(datosRegistro.login, datosRegistro.email, datosRegistro.password);
        return redirect(controllers.routes.UsuarioController.formularioLogin());
    }

    public Result formularioLogin() {
        return ok(formLogin.render(formFactory.form(Login.class), ""));
    }

    public Result loginUsuario() {
        Form<Login> form = formFactory.form(Login.class).bindFromRequest();
        if (form.hasErrors()) {
            return badRequest(formLogin.render(form, "Hay errores en el formulario"));
        }
        Login login = form.get();
        Usuario usuario = usuarioService.login(login.username, login.password);
        if (usuario == null) {
            return notFound(formLogin.render(form, "Login y contraseña no existentes"));
        } else {
            // Añadimos el id del usuario a la clave `connected` de
            // la sesión de Play
            // https://www.playframework.com/documentation/2.5.x/JavaSessionFlash
            // Esa clave es la usada en la autenticación
            session("connected", usuario.getId().toString());
            return redirect(controllers.routes.TareasController.listaTareas(usuario.getId()));
        }
    }

    // Comprobamos si hay alguien logeado con @Security.Authenticated(ActionAuthenticator.class)
    // https://alexgaribay.com/2014/06/15/authentication-in-play-framework-using-java/
    @Security.Authenticated(ActionAuthenticator.class)
    public Result logout() {
        session().remove("connected");
        return redirect(controllers.routes.UsuarioController.loginUsuario());
    }

    @Security.Authenticated(ActionAuthenticator.class)
    public Result detalleUsuario(Long id) {
        String connectedUserStr = session("connected");
        Long connectedUser = Long.valueOf(connectedUserStr);
        if (connectedUser != id) {
            return unauthorized("Lo siento, no estás autorizado");
        } else {
            Usuario usuario = usuarioService.findUsuarioPorId(id);
            if (usuario == null) {
                return notFound("Usuario no encontrado");
            } else {
                Logger.debug("Encontrado usuario " + usuario.getId() + ": " + usuario.getLogin());
                return ok(detalleUsuario.render(usuario));
            }
        }
    }
}
```

Para mapear los datos de los formularios se usan las clases `Login` y
`Registro`.

**Fichero `controllers/Login.java`**:

```java
package controllers;

import play.data.validation.Constraints;

public class Login {
    @Constraints.Required
    public String username;
    @Constraints.Required
    public String password;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
```

**Fichero `controllers/Registro.java`**:

```java
package controllers;

import play.data.validation.Constraints;

public class Registro {
    @Constraints.Required
    public String login;
    @Constraints.Required
    @Constraints.Email
    public String email;
    @Constraints.Required
    public String password;
    @Constraints.Required
    public String confirmacion;

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getConfirmacion() {
        return confirmacion;
    }

    public void setConfirmacion(String confirmacion) {
        this.confirmacion = confirmacion;
    }
}
```


### Vistas ###

Todas las vistas de la aplicación usan como plantilla base la vista
`main.scala.html`, en la que se carga el framework CSS _Bootstrap_ y
la librería JavaScript _JQuery_. Ambos se encuentran en el directorio
`public`, el directorio por defecto en el que se guardan los recursos
estáticos de una aplicación Play.

Es importante hacer notar que se obtiene la ruta absoluta a los
ficheros estáticos llamando a `routes.Assets.versioned` con su ruta
relativa. De esta forma se modificar el directorio por defecto en el
que se guardan los recursos estáticos sin afectar a la aplicación.

A la plantilla `main` se le pasa el título de la página, scripts
JavaScript (por defecto vacío) y un contenido HTML que se inserta en
el cuerpo principal.

**Fichero `views/main.scala.html`**:

```html
@*
 * This template is called from the `index` template. This template
 * handles the rendering of the page header and body tags. It takes
 * two arguments, a `String` for the title of the page and an `Html`
 * object to insert into the body of the page.
 *@
@(title: String, scripts: Html = Html(""))(content: Html)
<!DOCTYPE html>
<html lang="en">
    <head>
        @* Here's where we render the page title `String`. *@
        <title>@title</title>
        <link href="@routes.Assets.versioned("bootstrap/css/bootstrap.min.css")" rel="stylesheet" media="screen">
        <link rel="stylesheet" media="screen" href="@routes.Assets.versioned("stylesheets/main.css")">
        <link rel="shortcut icon" type="image/png" href="@routes.Assets.versioned("images/favicon.png")">
        <script src="@routes.Assets.versioned("javascripts/hello.js")" type="text/javascript"></script>
    </head>
    <body>
        <div class="container">
            @content
        </div>
        <script src="@routes.Assets.versioned("javascripts/jquery.min.js")" type="text/javascript"></script>
        <script src="@routes.Assets.versioned("bootstrap/js/bootstrap.min.js")" type="text/javascript"></script>
        @scripts
    </body>
</html>
```

Un ejemplo del uso de esta plantilla es la plantilla principal del
listado de tareas. Se trata de una plantilla compleja, con bastantes
ejemplos de cómo usar los distintos elementos de Play:

- La plantilla recibe una lista de tareas, un usuario y un mensaje
(consultar en el controller `TareasController` cómo se obtienen esos
datos). 
- Define un script JavaScript en el que se realiza una petición
  `DELETE` a la URL que se le pasa como parámetro (se utilizará para
  lanzar la acción de borrar una tarea).
- Utiliza una instrucción `for` para construir los elementos de la
  tabla de tareas.
- En las acciones de añadir y editar tareas se usan enlaces a las URLs
  definidas por rutas inversas.

**Fichero `views/listaTareas.scala.html`**:

```html
@(tareas: List[Tarea], usuario: Usuario, mensaje: String)
@scripts = {
    <script type="text/javascript">
        function del(urlBorrar) {
            $.ajax({
                url: urlBorrar,
                type: 'DELETE',
                success: function(results) {
                    //refresh the page
                    location.reload();
                }
            });
        }
    </script>
}
@main("Tareas del usuario @usuario.getLogin()", scripts) {

    <h2> Listado de tareas de @usuario.getLogin()</h2>

    <table class="table table-striped">
        <tr>
            <th>Tareas</th>
            <th>Acción</th>
        </tr>
    @for(tarea <- tareas) {
        <tr>
            <td>@tarea.getTitulo()</td>
            <td><a href="@routes.TareasController.formularioEditaTarea(tarea.getId())">
                <span class="glyphicon glyphicon-pencil"></span>&nbsp;</a>
                <a onmouseover="" style="cursor: pointer;"
                onclick="del('@routes.TareasController.borraTarea(tarea.getId())')">
                <span class="glyphicon glyphicon-trash" aria-hidden="true"></span></a></td>
        </tr>
      }

      <tr>
          <td><a href="@routes.TareasController.formularioNuevaTarea(usuario.getId())">
              <span class="glyphicon glyphicon-plus"/></a></td>
          <td><a href="@routes.UsuarioController.logout()">Salir</a></td>
      </tr>

  </table>

  @if(mensaje != null) {
      <div class="alert alert-success" role="alert">
          <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          @mensaje
      </div>
  }
}
```


### Tests ###

La mayoría de los tests que contiene la aplicación son tests de
integración, en los que no se usan _mocks_, sino que se comprueba el
funcionamiento de la capa de servicio y la de repositorio.

Como framework de testing se usa _JUnit_. Los datos de prueba en las
tablas de la base de datos se definen y se cargan usando _DBUnit_.

Por ejemplo, la clase `models.EquipoTest` contiene tests para el
modelo `Equipo` y el `EquipoRepository`.

Los tests se realizarán utilizando la base de datos definida en el
fichero de configuración. En el fichero de configuración por defecto
(`conf/application.conf`) se define la base de datos de memoria
`H2`. 

#### Tests con la base de datos de memoria `H2` ####

Ejemplo de ejecución de los tests sobre la base de datos de memoria:

```text
$  docker run --rm  -it -v "${PWD}:/code" -p 9000:9000 domingogallardo/playframework
[mads-todolist-inicial] $ test
..
[info] Test run finished: 0 failed, 0 ignored, 5 total, 1.753s
[info] Passed: Total 36, Failed 0, Errors 0, Passed 36
[success] Total time: 51 s, completed Aug 21, 2018 10:56:42 AM
```

Podemos lanzar una clase de test en concreto:

```text
[mads-todolist-inicial] $ testOnly models.EquipoTest
...
[info] Test run finished: 0 failed, 0 ignored, 6 total, 11.377s
[info] Passed: Total 6, Failed 0, Errors 0, Passed 6
[success] Total time: 38 s, completed Aug 22, 2018 7:41:09 AM
```

#### Tests con la base de datos MySQL ####

La otra configuración que vamos a usar en los tests es
`conf/develop-mysql.conf`, en la que se utiliza una base de datos
MySQL. Como ya vimos anteriormente, para utilizar esta configuración
hay que lanzar el servicio de MySQL usando docker y definir en la
ejecución del contenedor de Play las variables de entorno `DB_URL`,
`DB_USER_NAME` y `DB_USER_PASSWD` con los datos correctos para acceder
a la base de datos MySQL.

```text
$ docker run -d --rm -p 3306:3306 --name db-mysql -e MYSQL_ROOT_PASSWORD=mads -e MYSQL_DATABASE=mads mysql
$ docker run --link db-mysql --rm -it -p 9000:9000 -e \
DB_URL="jdbc:mysql://db-mysql:3306/mads" -e DB_USER_NAME="root" -e \
DB_USER_PASSWD="mads" -v "${PWD}:/code" domingogallardo/playframework
[mads-todolist-inicial] $ set javaOptions += "-Dconfig.file=conf/develop-mysql.conf"
[mads-todolist-inicial] $ test
...
[success] Total time: 44 s, completed Aug 22, 2018 7:48:32 AM
[mads-todolist-inicial] $ 
```

#### Ejemplos de tests de la aplicación ####

En la aplicación se definen tests sobre los modelos (clases entidad y
clases repositorio) y sobre los servicios. Como hemos mencionado antes
se tratan de unos tests de integración que se prueban directamente
sobre la base de datos activa en el fichero de configuración. Aunque
Play proporciona facilidades para el uso de _mocks_ no los hemos
utilizado por simplificar la realización de los tests.

Se utiliza DBUnit para rellenar las tablas con los datos de
pruebas. El método `initData()` limpia las tablas e inicializa estos
datos con los existentes en `test/resources/test_dataset.xml` comienzo
de la ejecución de cada test.

DBUnit rellena las tablas físicas de la base de datos, no usa JPA. Hay
que utilizar los nombres de las tablas y de las columnas de la propia
base de datos, no los de las entidades JPA. Hay que incluir en el
fichero de dataset todas las tablas de la aplicación, incluyendo las
tablas auxiliares de las relaciones muchos-a-muchos, para que se
inicialicen los de datos de prueba (por ejemplo, la tabla
`Equipo_Usuario`).

Por último, se debe tener cuidado con las claves ajenas. No es posible
borrar una tabla si hay claves ajenas que referencian a algunos de sus
elementos. Para esto hay que considerar que DBUnit inserta los datos
de arriba a abajo y los borra de abajo a arriba.

**Fichero `test/resources/test_dataset.xml`**:

```xml
<?xml version="1.0" encoding="UTF-8"?>
 <dataset>
    <Usuario id="1000" login="juangutierrez" nombre="Juan" apellidos="Gutierrez"
         password="123456789" eMail="juan.gutierrez@gmail.com" fechaNacimiento="1993-12-10"/>
    <Usuario id="1005" login="anagarcia" nombre="Ana" apellidos="Garcia"
             password="123456789" eMail="ana.garcia@gmail.com" fechaNacimiento="1993-02-08"/>
    <Tarea id="1001" titulo="Renovar DNI" usuarioId="1000"/>
    <Tarea id="1002" titulo="Práctica 1 MADS" usuarioId="1000"/>
    <Equipo id="1003" nombre="Equipo A"/>
    <Equipo id="1004" nombre="Equipo B"/>
    <Equipo id="1005" nombre="Equipo C"/>
    <Equipo_Usuario fk_equipo="1003" fk_usuario="1000"/>
    <Equipo_Usuario fk_equipo="1003" fk_usuario="1005"/>
    <Equipo_Usuario fk_equipo="1004" fk_usuario="1000"/> 
  </dataset>
```

En cuanto a los tests propiamente dichos hay que resaltar algunos
puntos.

- Los objetos definidos con inyección de dependencias (la anotación
  `@Inject`) se instancian mediante el `Injector` de la aplicación
  Play. La aplicación se construye leyendo el fichero de
  configuración por defecto (se puede modificar con la variable
  `config.file` de las opciones Java al lanzar el test). De esta forma
  los objetos instanciados utilizarán la fuente de datos definida en
  la configuración de la aplicación (H2 o MySQL).
- Los tests sobre los modelos contienen pruebas sobre las entidades
  (por ejemplo, se comprueba el método `equal` con entidades con y sin
  identificador) y sobre el repositorio del modelo, en los que se
  comprueba que las operaciones sobre la base de datos funcionan correctamente.
- Los tests sobre los servicios contienen pruebas sobre los métodos de
  negocio de la clase servicio, incluyendo comprobaciones de que se
  lanzan excepciones si hay algún error.

**Fichero `test/Models/EquipoTest.java`**:

```java
package models;


public class EquipoTest {
    static Database db;
    static private Injector injector;

    // Se ejecuta sólo una vez, al principio de todos los tests
    @BeforeClass
    static public void initApplication() {
        // Creamos la aplicación a partir del fichero de configuración.
        // El fichero de configuración se puede cambiar en el comando
        // para lanzar sbt y los tests:
        // sbt '; set javaOptions += "-Dconfig.file=conf/develop-mysql.conf"; testOnly models.EquipoTest*'
        GuiceApplicationBuilder guiceApplicationBuilder =
                new GuiceApplicationBuilder().in(Environment.simple());
        injector = guiceApplicationBuilder.injector();
        // Obtenemos la base de datos utilizada por la aplicación
        db = injector.instanceOf(Database.class);
        // Necesario para inicializar JPA
        injector.instanceOf(JPAApi.class);
    }

    @Before
    public void initData() throws Exception {
        // Creamos la base de datos de test y le asignamos el nombre JNDI DBTodoList
        JndiDatabaseTester databaseTester = new JndiDatabaseTester("DBTodoList");
        IDataSet initialDataSet = new FlatXmlDataSetBuilder().build(new FileInputStream("test/resources/test_dataset.xml"));
        databaseTester.setDataSet(initialDataSet);
        databaseTester.setSetUpOperation(DatabaseOperation.CLEAN_INSERT);
        databaseTester.onSetup();
    }

    @Test
    public void testEqualsEquiposConId() {
        Equipo equipo1 = new Equipo("Equipo A");
        Equipo equipo2 = new Equipo("Equipo B");
        Equipo equipo3 = new Equipo("Equipo C");
        equipo1.setId(1L);
        equipo2.setId(1L);
        equipo3.setId(2L);
        assertEquals(equipo1, equipo2);
        assertNotEquals(equipo1, equipo3);
    }

    @Test
    public void testEqualsEquiposSinId() {
        Equipo equipo1 = new Equipo("Equipo A");
        Equipo equipo2 = new Equipo("Equipo A");
        Equipo equipo3 = new Equipo("Equipo B");
        assertEquals(equipo1, equipo2);
        assertNotEquals(equipo1, equipo3);
    }

    @Test
    public void testAddEquipoJPARepositoryInsertsEquipoDatabase() {
        EquipoRepository equipoRepository = injector.instanceOf(EquipoRepository.class);
        Equipo equipo = new Equipo("Equipo A");
        equipo = equipoRepository.add(equipo);
        Logger.info("Número de tarea: " + Long.toString(equipo.getId()));
        assertNotNull(equipo.getId());
        assertEquals("Equipo A", getNombreFromEquipoDB(equipo.getId()));
    }

    private String getNombreFromEquipoDB(Long equipoId) {
        String titulo = db.withConnection(connection -> {
            String selectStatement = "SELECT NOMBRE FROM Equipo WHERE ID = ? ";
            PreparedStatement prepStmt = connection.prepareStatement(selectStatement);
            prepStmt.setLong(1, equipoId);
            ResultSet rs = prepStmt.executeQuery();
            rs.next();
            return rs.getString("NOMBRE");
        });
        return titulo;
    }

    @Test
    public void testFindEquipoPorId() {
        EquipoRepository repository = injector.instanceOf(EquipoRepository.class);
        Equipo equipo = repository.findById(1003L);
        assertEquals("Equipo A", equipo.getNombre());
    }

    @Test
    public void testUpdateEquipo() {
        EquipoRepository repository = injector.instanceOf(EquipoRepository.class);
        Equipo equipo = new Equipo("Equipo B");
        equipo.setId(1003L);
        repository.update(equipo);
        Equipo equipoActualizado = repository.findById(1003L);
        assertEquals("Equipo B", equipo.getNombre());
    }

    @Test
    public void testDeleteEquipo() {
        EquipoRepository repository = injector.instanceOf(EquipoRepository.class);
        Equipo equipo = repository.findById(1003L);
        repository.delete(equipo);
        equipo = repository.findById(1003L);
        assertNull(equipo);
    }

    @Test
    public void testAddUsuarioEquipo() {
        EquipoRepository equipoRepository = injector.instanceOf(EquipoRepository.class);
        UsuarioRepository usuarioRepository = injector.instanceOf(UsuarioRepository.class);
        Equipo equipo = equipoRepository.findById(1005L);
        Usuario usuario = usuarioRepository.findById(1005L);
        equipoRepository.addUsuarioEquipo(usuario, equipo);

        // Recuperamos las entidades de la base de datos y comprobamos
        // que los datos se han actualizado
        List<Usuario> usuarios = equipoRepository.findUsuariosEquipo(equipo.getId());
        assertEquals(1, usuarios.size());
        Usuario usuarioBD = usuarioRepository.findById(1005L);
        assertEquals(2, usuarioBD.getEquipos().size());
    }
}
```


**Fichero `test/services/EquipoService.java`**:

```java
package services;

public class EquipoServiceTest {
    static private Injector injector;

    @BeforeClass
    static public void initApplication() {
        GuiceApplicationBuilder guiceApplicationBuilder =
                new GuiceApplicationBuilder().in(Environment.simple());
        injector = guiceApplicationBuilder.injector();
        injector.instanceOf(JPAApi.class);
    }

    @Before
    public void initData() throws Exception {
        JndiDatabaseTester databaseTester = new JndiDatabaseTester("DBTodoList");
        IDataSet initialDataSet = new FlatXmlDataSetBuilder().build(new FileInputStream("test/resources/test_dataset.xml"));
        databaseTester.setDataSet(initialDataSet);
        databaseTester.setSetUpOperation(DatabaseOperation.CLEAN_INSERT);
        databaseTester.onSetup();
    }

    @Test
    public void listaEquipos() {
        EquipoService equipoService = injector.instanceOf(EquipoService.class);
        List<Equipo> equipos = equipoService.allEquipos();
        assertEquals(3, equipos.size());
    }

    @Test
    public void addUsuarioEquipo() {
        EquipoService equipoService = injector.instanceOf(EquipoService.class);
        UsuarioService usuarioService = injector.instanceOf(UsuarioService.class);
        equipoService.addUsuarioEquipo(1000L, 1005L);
        Usuario usuario = usuarioService.findUsuarioPorLogin("juangutierrez");
        List<Equipo> equipos = new ArrayList(usuario.getEquipos());
        assertEquals(3, equipos.size());
    }

    @Test
    public void getUsuariosEquipo() {
        EquipoService equipoService = injector.instanceOf(EquipoService.class);
        UsuarioService usuarioService = injector.instanceOf(UsuarioService.class);
        List<Usuario> usuarios = equipoService.findUsuariosEquipo(1003L);
        assertEquals(2, usuarios.size());
        Usuario usuario = usuarioService.findUsuarioPorLogin("anagarcia");
        assertEquals(1, usuario.getEquipos().size());
    }

    @Test
    public void deleteUsuarioEquipo() {
        EquipoService equipoService = injector.instanceOf(EquipoService.class);
        UsuarioService usuarioService = injector.instanceOf(UsuarioService.class);
        equipoService.deleteUsuarioEquipo(1000L, 1003L);
        List<Usuario> usuarios = equipoService.findUsuariosEquipo(1003L);
        assertEquals(1, usuarios.size());
        Usuario usuario = usuarioService.findUsuarioPorLogin("juangutierrez");
        assertEquals(1, usuario.getEquipos().size());
    }
}
```


## Tecnologías usadas ##

### Play Framework ###

[Play Framework](https://playframework.com) es un framework de
desarrollo rápido de aplicaciones web disponible en los lenguajes Java
y Scala. Vamos a utilizar la versión Java. El framework proporciona un
soporte de ejecución que tiene como base el servidor
[Netty](http://netty.io). Con este soporte es posible diseñar y poner
en marcha distintos tipos de aplicaciones: servicios HTTP, servicios
HTTP asíncronos basados en websockets, aplicaciones asíncronas basadas
en eventos, etc. Nosotros vamos a implementar una aplicación
tradicional que implementa un servicio HTTP. Vamos a utilizar la
[versión 2.5 en Java](https://www.playframework.com/documentation/2.5.x/JavaHome).

Para entender el funcionamiento de esta primera práctica es necesario
consultar la siguiente documentación del framework:

Sobre el funcionamiento de Play:

- [Using the Play console](https://playframework.com/documentation/2.5.x/PlayConsole)
- [Anatomy of a Play application](https://playframework.com/documentation/2.5.x/Anatomy)

Sobre peticiones y respuestas HTTP:

- [Actions, Controllers and Results](https://www.playframework.com/documentation/2.5.x/JavaActions)
- [HTTP routing](https://www.playframework.com/documentation/2.5.x/JavaRouting)
- [Session and Flash scope](https://www.playframework.com/documentation/2.5.x/JavaSessionFlash)

Sobre plantillas:

- [The template engine](https://www.playframework.com/documentation/2.5.x/JavaTemplates)
- [Common template use cases](https://www.playframework.com/documentation/2.5.x/JavaTemplateUseCases)

Sobre envío de datos de formularios:

- [Handling form submission](https://www.playframework.com/documentation/2.5.x/JavaForms)
- [Rendering an <input> element](https://www.playframework.com/documentation/2.5.x/JavaFormHelpers#Rendering-an-%3Cinput%3E-element)

Sobre el acceso a base de datos y JPA

- [Acceso a base de datos SQL](https://www.playframework.com/documentation/2.5.x/JavaDatabase)
- [Integrating with JPA](https://www.playframework.com/documentation/2.5.x/JavaJPA)

Sobre la inyección de dependencias

- [Dependency Injection](https://playframework.com/documentation/2.5.x/JavaDependencyInjection)

Sobre los tests en Play:

- [Testing your application](https://playframework.com/documentation/2.5.x/JavaTest)

Sobre la configuración de la aplicación Play:

- [Configuración](https://www.playframework.com/documentation/2.5.x/ConfigFile)

### Java Persistence API (JPA) ###

JPA es el API que utilizaremos para acceder a bases de datos y
gestionar entidades persistentes usando un modelo ORM (_Object
Relational Mapping_). Está integrado en Play, no es necesario instalar
ninguna librería adicional.

JPA también es conocido por el nombre de una de sus implementaciones
más populares, Hibernate. Es una tecnología muy usada y madura en el
mundo Java. Permite gestionar la persistencia directamente con el
modelo de objetos de la aplicación (se denominan _entidades_),
independizándola del modelo relacional basado en tablas y registros.

La implementación de JPA ObjectDB tiene unos tutoriales muy completos
y accesibles:

- [JPA Quick tour](http://www.objectdb.com/java/jpa/getting/started)
- [Entity classes](http://www.objectdb.com/java/jpa/entity)
- [Using JPA](http://www.objectdb.com/java/jpa/persistence)
- [JPA Queries](http://www.objectdb.com/java/jpa/query)

No es necesario estudiar todos los tutoriales. El objetivo de las
prácticas no es aprender JPA, sino desarrollar de forma ágil una
aplicación. Vamos a utilizar lo más básico de JPA y en la mayoría de
las ocasiones se va a proporcionar el código necesario. Además, en
caso de duda, siempre podrás realizar preguntas sobre cómo implementar
una determinada funcionalidad en el foro de Moodle.

La implementación de JPA que se utiliza en PlayFramework 2.5 es
Hibernate 5.1.0.Final.

Puedes encontrar toda la información sobre esta implementación en la
guía de usuario:

- [Hibernate ORM 5.1 User Guide](http://docs.jboss.org/hibernate/orm/5.1/userguide/html_single/Hibernate_User_Guide.html#associations-many-to-one)


### Bootstrap ###

Para hacer más atractivo el diseño de las páginas HTML vamos a usuar
el framework CSS
[Bootstrap](https://getbootstrap.com/docs/3.3/getting-started/). Es conveniente
tener a mano su documentación, en concreto la lista de componentes:

- [Bootstrap components](https://getbootstrap.com/docs/3.3/components/)


