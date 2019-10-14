
<!---

Práctica 3:
   - Publicación en DockerHub y Heroku

Más adelante (en la práctica 3) veremos cómo usar la configuración de
producción para ejecutar la práctica en un servicio de hosting.


Práctica 2:

   
https://github.com/domingogallardo/mads-todolist-inicial/commit/498442afc689e81cc02d5022cfa6a85722a56bc7

- Explicar cómo se añade Travis en la configuración de la organización
  / cuenta personal.

- Diferenciar entre travis.org y travis.com

- Incluir la configuración de base de datos MySQL y lanzar los tests
  con esta base de datos. ¿Cómo lanzar los tests con distintos fichero
  de configuración? ¿Cómo lanzar la aplicación usando un fichero de
  configuración distinto?

Fichero de configuración para trabajar con el perfil MySQL en ejecución:

`src/main/resources/application-mysql.properties`:
```
spring.datasource.url=jdbc:mysql://localhost:3316/mads
spring.datasource.username=root
spring.datasource.password=mads
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQL5Dialect
spring.jpa.hibernate.ddl-auto=update
spring.datasource.initialization-mode=never
```

Comando para lanzar el perfil en modo run:

```
 mvn spring-boot:run -Dspring-boot.run.profiles=mysql
```

Fichero de configuración para trabajar con el perfil MySQL en test:

`src/test/resources/application-mysql.properties`:
```
spring.datasource.url=jdbc:mysql://localhost:3316/mads
spring.datasource.username=root
spring.datasource.password=mads
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQL5Dialect
```

Y para lanzar los tests:

```
mvn -DargLine="-Dspring.profiles.active=mysql" test
```


Comando para lanzar la base de datos MySQL:

```
$ docker run -d -p 3316:3306 -e MYSQL_ROOT_PASSWORD=mads -e MYSQL_DATABASE=mads mysql:5
```

Comando para modificar los valores de las propiedades:

```
mvn spring-boot:run -Dspring-boot.run.arguments=--spring.datasource.username=pepe
```

Podmeos añadir propiedades más cortas e inicializar esas:

Fichero `application-prod.properties`:

```
# abreviaturas para sobreescribir en línea de comando
datasource=jdbc:mysql://localhost:3316/mads
dbuser=root
dbpasswd=mads
spring.datasource.url=${datasource}
spring.datasource.username=${dbuser}
spring.datasource.password=${dbpasswd}
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQL5InnoDBDialect
spring.jpa.hibernate.ddl-auto=validate
spring.datasource.initialization-mode=never
```

- Para lanzar mysql docker con usuario root sin password en el puerto 3306:

```
$ docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_DATABASE=mads mysql:5
```

- Travis deberá lanzar los tests unitarios usando MySQL


### Maven Wrapper ###


Maven Wrapper: https://www.baeldung.com/maven-wrapper

Para instalar Maven Wrapper:

```
mvn -N io.takari:maven:wrapper
```

Para ejecutar la aplicación con Maven Wrapper:

```
./mvnw spring-boot:run
```

## Para la práctica 3 ##

### Dockerizar la aplicación ###



https://spring.io/guides/gs/spring-boot-docker/

### Docker compose ###

https://medium.com/@chrischuck35/how-to-create-a-mysql-instance-with-docker-compose-1598f3cc1bee
https://docs.docker.com/compose/

-->


# Práctica 2: Integración con Travis y TDD

En esta práctica 2 de la asignatura realizaremos dos tareas principales:

- Configuraremos un sistema de integración continua conectando el
  repositorio de GitHub con Travis. En este sistema se lanzarán los
  tests automáticamente en cada _pull request_ sobre la base de datos
  MySQL.
- Añadiremos nuevas funcionalidades usando la práctica XP de TDD
  (_Test Driven Design_).

!!! Important
    Lee con cuidado todo el enunciado y dedica especial atención a los
    apartados con el título `Pasos a seguir en la práctica`. Ahí están
    especificadas las acciones que debes realizar en la práctica.

La duración de la práctica es de 2 semanas y la fecha límita de
entrega es el día 30 de octubre.

## Refactorización de la relación uno-a-muchos ##

Antes de comenzar la práctica hay que hacer una refactorización en la
relación una-a-muchos entre usuario y tareas: pasar la lista de tareas
de un usuario de `List` a `Set`. 

A diferencias del tipo `List`, el `Set` no permite elementos repetidos
y es más conveniente definir las relaciones JPA de esta forma.

### Pasos a seguir en la práctica ###

- Realiza un commit en `master` (no hace falta que hagas un pull
  request) con los cambios que aparecen este [commit](https://github.com/domingogallardo/mads-todolist-inicial/commit/498442afc689e81cc02d5022cfa6a85722a56bc7).
- Lanza los tests para comprobar que todo funciona correctamente y
  sube el commit a GitHub.

## Configuración de la aplicación ##

Hasta ahora hemos trabajado con la aplicación en una configuración
local con nuestro ordenador de desarrollo trabajando sobre una base de
datos H2 en memoria. Pero el objetivo final es poner la aplicación en
producción, en un servidor en Internet y usando una base de datos
MySQL de producción. 

En esta práctica vamos a configurar un perfil de la aplicación para
poder lanzar los tests y ejecutar la aplicación usando una base de
datos MySQL. En la práctica 3 veremos cómo definir un perfil para
trabajar con una base de datos de producción.

!!! Note
    La **base de datos de producción** es la que mantiene los datos
    introducidos por los usuarios de la misma. Hay que prestar una
    atención especial a esta base de datos y definir políticas de
    respaldo y de control de cambios para evitar que se produzca
    cualquier pérdida de información. Veremos en la práctica 3 que una
    de las cuestiones que hay que asegurar es que la aplicación no
    puede modificar el esquema de datos de esta base de datos. Habrá
    que definir un flujo de trabajo para implementar en el esquema de
    datos de la base de datos un cambio en el modelo de datos de la
    aplicación.

Vamos a ver en este apartado cómo definir distintas configuraciones de
ejecución de la aplicación, utilizando los denominados
_perfiles_. Definiremos, además del perfil base, un perfil adicional
para lanzar la aplicación y los tests usando la base de datos MySQL.

La configuración de tests con base de datos MySQL la utilizaremos para
ejecutar los tests de integración en el proceso de integración
continua de Travis.

### Ficheros de configuración de la aplicación ###

Ya hemos comentado que la configuración de la aplicación se define en
el fichero `application.properties`. Ahí se definen distintas
propiedades de la ejecución de la aplicación que se pueden modificar
(puerto en el que se lanza la aplicación, base de datos con la que
conectarse, etc.). 

Tenemos dos ficheros `application.properties`: uno en el directorio
`src/main/resources` que define la configuración de ejecución y otro
en el directorio `src/test/resources` que define la configuración que
se carga cuando se lanzan los tests.

Spring Boot permite definir ficheros de configuración adicionales que
pueden sobreescribir las propiedades definidas en el fichero de
configuración por defecto. El nombre de estos ficheros de
configuración debe ser `application-xxx.profile` donde `xxx` define el
nombre del perfil. En nuestro caso definiremos los ficheros
`application-mysql.profile` (uno en el directorio `main` y otro en
`test`) para definir las configuraciones de ejecución y de test con
MySQL.


### Pasos a seguir en la práctica ###

- Instala [Docker
  Desktop](https://www.docker.com/products/docker-desktop). 
  
  Docker es un software de virtualización que utiliza el propio
  sistema operativo compartimentado y permite gestionar _contenedores_
  (similares a las máquinas virtuales) de forma mucho menos pesada y
  rápida que con sistemas de virtualización tradicionales como
  VirtualBox.
  
  Lo vamos a utilizar para **lanzar el servidor MySQL de base de
  datos** y también para la futura práctica 3.
  
  Si tienes Windows, Docker no es compatible con VirtualBox. Si
  quieres usar ambos programas puedes usar una versión limitada de
  Docker llamada [Docker
  Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)

- Crea un nuevo _issue_ llamado `Añadir perfiles y permitir trabajar
  con MySQL`. Crea una rama nueva y haz los siguientes cambios en ella.

- Copia el siguiente fichero en `src/main/resources/application-mysql.properties`:

```
spring.datasource.url=jdbc:mysql://localhost:3306/mads
spring.datasource.username=root
spring.datasource.password=
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQL5Dialect
spring.jpa.hibernate.ddl-auto=update
spring.datasource.initialization-mode=never
```

   En este fichero de configuración se define la URL de conexión a la
   base de datos MySQL, su usuario (`root`) y contraseña (vacía) y el
   dialecto que se va a utilizar para trabajar desde JPA con la base
   de datos (`org.hibernate.dialect.MySQL5Dialect`). Además se indica
   que no se debe cargar ningún fichero de datos inicial. El esquema
   de la base de datos se actualizará si hay cambios en las entidades
   de la aplicación, y los datos se mantendrán en la base de datos.
    
- Copia el siguiente fichero en `src/test/resources/application-mysql.properties`:
    
```
spring.datasource.url=jdbc:mysql://localhost:3306/mads
spring.datasource.username=root
spring.datasource.password=
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQL5Dialect
spring.jpa.hibernate.ddl-auto=create
```
     
   La diferencia más importante es el valor de
   `spring.jpa.hibernate.ddl-auto`, que es `create`. De esta forma la
   base de datos se inicializa antes de cargar los datos de los tests
   y de ejecutarlos.

- Añade la siguiente dependencia en el fichero `pom.xml` para que se
  descargue el driver `mysql-connector-java` y poder utilizar una base
  de datos MySQL en la aplicación:

**Fichero `pom.xml`**:

```diff
            <artifactId>h2</artifactId>
             <scope>runtime</scope>
         </dependency>
+         <dependency>
+             <groupId>mysql</groupId>
+             <artifactId>mysql-connector-java</artifactId>
+         </dependency>
         <dependency>
             <groupId>org.springframework.boot</groupId>
```


- Para lanzar la aplicación necesitarás un servidor MySQL en el puerto
  3306 con el usuario `root` sin contraseña. Es muy sencillo
  descargarlo y ejecutarlo si tienes instalado Docker. Ejecuta desde
  el terminal:

    ```
    $ docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_DATABASE=mads mysql:5
    ```

   Docker se descarga la imagen `mysql:5` y lanza el contenedor (una
   instancia en marcha de una imagen) conectado al puerto 3306 y sobre
   la base de datos `mads`. 
   
   Puedes ejecutar los siguientes comandos de docker:

    ```
    $ docker container ls -a (comprueba todos los contenedores en marcha)
    $ docker container stop <nombre o id de contenedor> (para un contenedor)
    $ docker container rm <nombre o id de contenedor> (elimina un contenedor)
    ```

- Arranca la aplicación con el siguiente comando:

```
$ mvn spring-boot:run -Dspring-boot.run.profiles=mysql
 ```

   Se cargarán las preferencias de `src/main/resource/application.profile` y
   `src/main/resource/application-mysql.profile`.

   Prueba a introducir datos en la aplicación y comprueba que se están
   guardando en la base de datos con `MySQL Workbench` o alguna
   aplicación similar.


<img src="images/mysql-workbench.png" width="600px"/>






La propiedad Java `config.file` permite definir un fichero de
configuración distinto del de por defecto. Se puede configurar en las
`javaOptions` de `sbt`:

```text
[mads-todolist-dgallardo] $ set javaOptions += "-Dconf.file=conf/<FICHERO-CONF>.conf"
```

Vamos a utilizar dos ficheros de configuración distintos:

- Fichero `conf/develop-mysql.conf`: para lanzar las pruebas de integración.
- Fichero `conf/production.conf`: para ejecutar la aplicación en producción.

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


Ambos ficheros incluyen el fichero `application.conf` en el que se
definen las siguientes propiedades relacionadas con la base de datos:

**Fichero `conf/application.conf**:

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
  # Definimos el nombre JNDI de la BD que va a usar la aplicación
  default.jndiName=DBTodoList

  # You can turn on SQL logging for any datasource
  # https://www.playframework.com/documentation/latest/Highlights25#Logging-SQL-statements
  # default.logSql=true
}
```


### Fichero de configuración de JPA ###

Vemos en los ficheros anteriores que la diferencia fundamental es el valor de la
propiedad `jpa.default`. En esta propiedad se define el nombre de la
unidad de persistencia que se va a usar en JPA. Las unidades de
persistencia están definidas en el fichero
`conf/META-INF/persistence.xml`.


**Fichero `conf/META-INF/persistence.xml**:

```xml
<!-- MySQL Persistence Unit - Develop: hbm2ddl.auto = UPDATE -->

<persistence-unit name="develop" transaction-type="RESOURCE_LOCAL">
   <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>
   <non-jta-data-source>DBTodoList</non-jta-data-source>
   <class>models.Usuario</class>
   <class>models.Tarea</class>
   <class>models.Equipo</class>
   <class>models.Admin</class>
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
   <class>models.Admin</class>
   <properties>
      <property name="hibernate.dialect" value="org.hibernate.dialect.MySQL5Dialect"/>
      <property name="hibernate.hbm2ddl.auto" value="validate"/>
   </properties>
</persistence-unit>
```

La diferencia fundamental entre ambas unidades de persistencia es el
valor de la propiedad `hibernate.hbm2ddl.auto`, que define cómo
gestiona JPA el mapeo entre las entidades Java y las tablas físicas de
la base de datos.

En la unidad de persistencia `develop` hemos usado el valor
`update`. Esto significa que JPA actualizará la base de datos,
modificando su esquema, para hacerlo corresponder con las entidades
definidas en la aplicación. Si en alguna entidad añadimos algún
atributo, el esquema de la base de datos se actualizará, añadiendo un
campo en la tabla correspondiente.

En la unidad de persistencia `production` hemos usado el valor
`validate`. En este caso JPA comprobará si el esquema de la base de
datos se corresponde con las entidades de la aplicación. Si no es así,
se lanzará una excepción y JPA dejará de funcionar.

El primer valor es muy útil para el realizar el desarrollo y los tests
de integración de la aplicación. Pero no se debe usar en producción
porque no queremos que la base de datos de producción (donde están
todos los datos introducidos por los usuarios finales) se modifique
tan fácilmente. Cualquier modificación de la base de datos de
producción debe realizarse mediante un proceso que garantice la
posibilidad de la vuelta atrás y la recuperación de posibles errores
que se puedan cometer.

### Variables de entorno ###

En ambos ficheros se usan variables de entorno para definir los
valores de la URL de la conexión a la base de datos y el usuario y
contraseña de esa conexión.

Los valores de esas variables se pueden definir de dos formas para
que sean visibles dentro de `sbt`:

- En el shell en el que se lanza el comando `sbt`
  
        $ export DB_URL="jdbc:mysql://localhost:3316/mads"
        $ export DB_USER_NAME=root
        $ export DB_USER_PASSWD=mads
        $ sbt '; set javaOptions += \"-Dconfig.file=conf/develop-mysql.conf\"; test'
    
    En la última línea vemos cómo es posible lanzar `sbt` junto con
    unos comandos que se lanzarán dentro del propio `sbt`.
    
- Desde dentro del propio `sbt` con `set javaOptions`:

        [mads-todolist-dgallardo] $ set javaOptions += "-Dconfig.file=conf/develop-mysql.conf"
        [mads-todolist-dgallardo] $ set javaOptions += "-DDB_URL=jdbc:mysql://localhost:3316/mads"
        [mads-todolist-dgallardo] $ set javaOptions += "-DDB_USER_NAME=root"
        [mads-todolist-dgallardo] $ set javaOptions += "-DDB_USER_PASSWD=mads"
        [mads-todolist-dgallardo] $ test


### Pasos a seguir en la práctica ###

- Ejecuta los tests de la práctica usando el fichero de
configuración `develop-mysql.conf` para que los realice usando la base
de datos MySQL (que deberás tener activa).

- Captura la pantalla en la que aparezca el resultado de los tests y el
nombre de la base de datos `MySQL`. Por ejemplo, si ejecutas `sbt`
desde IntelliJ, la pantalla resultante deberá ser como la siguiente:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/02-pruebas-tdd/imagenes/salida-test-mysql.png" width="500px"/>


## Construcción y publicación de la imagen docker ##

Para facilitar la ejecución de la aplicación en diferentes entornos,
vamos a generar y publicar una imagen docker de la misma.

### Alta en Docker Hub ###

Crea una cuenta en [docker hub](https://hub.docker.com). La utilizarás
para subir allí, utilizando tu _Docker ID_, la image docker de tu
práctica.


### Construcción de la imagen docker ###

Empezamos construyendo la imagen docker en local y comprobando que
funciona correctamente.


#### Comando `stage` de `sbt` ####

El comando `stage` de `sbt` genera un comando ejecutable con el que se puede
lanzar la aplicación sin usar `sbt`. Genera un script con el nombre de
la aplicación en el directorio `target/universal/stage/bin`. Genera
también un fichero `bat` para Windows.

```
[mads-todolist-dgallardo] $ stage
```

El script generado lanza la aplicación en modo producción. En este modo es
necesario definir la variable `play.crypto.key` con una cadena inicial.

```
$ target/universal/stage/bin/mads-todolist-dgallardo -Dplay.crypto.secret=abcdefghijk
```

Al lanzar el comando generado por `sbt stage` es posible definir el
fichero de configuración que va a usar la ejecución de la
aplicación. Esta va a ser la característica clave que nos va a
permitir usar distintas configuraciones.

```
$ target/universal/stage/bin/mads-todolist-dgallardo -Dconfig.file=conf/<FICHERO-CONF>.conf
```

#### Fichero Dockerfile ####

El fichero `Dockerfile` es el fichero en el que se definen las
instrucciones para construir la imagen. Docker lo ejecuta paso a
paso para ir creando una imagen de una máquina virtual con los
elementos necesarios para ejecutar nuestra aplicación.

Debemos colocar el fichero `Dockerfile` en la raíz del proyecto.

**Fichero `Dockerfile`**:

```dockerfile
FROM domingogallardo/playframework
WORKDIR /app
COPY . /app
RUN sbt clean stage

EXPOSE 9000
ENV CONFIG_FILE=conf/application.conf
ENV SECRET=abcdefghijk

CMD target/universal/stage/bin/mads-todolist-2017 -Dplay.crypto.secret=$SECRET -Dconfig.file=$CONFIG_FILE
```

Algunos puntos a destacar:

- La línea `FROM` indica la imagen docker base sobre la que se construye
la aplicación.
- La línea `WORKDIR` indica el directorio en el que se van a ejecutar
todos los comandos `COPY`, `RUN` o `CMD`. Si el directorio no existe en
la imagen, se crea. En este caso creamos el directorio `/app` en el
que se va a compilar la aplicación.
- El comando `COPY` copia el directorio actual (y sus subdirectorios) en
el directorio `/app` de la máquina Docker. De esta forma copiamos
el fuente de la aplicación Play.
- El comando `RUN` ejecuta lo que hay a continuación dentro de la
máquina virtual en el proceso de construcción de la imagen. En este
caso se lanza `sbt clean stage` para compilar el proyecto y generar el
ejecutable (que se guardará en el directorio
`target/universal/stage/bin/NOMBRE_PROYECTO`).
- Los siguientes comandos ya son para cuando se ejecuta el
contenedor. El comando `EXPOSE` define un puerto a mapear con la
máquina host. En este caso el puerto 9000, que es en el que se lanza
la aplicación. El comando `ENV` define valores por defecto de
variables de entorno. Estas variables pueden ser sobreescritas con el
parámetro `-e` en un `docker run`. En nuestro caso definimos el
fichero de configuración por defecto y la palabra `SECRET` por
defecto.
- Por último, `CMD` define el comando que se ejecuta en el contenedor
cuando se realiza un `docker run`. En nuestro caso llamamos a la
aplicación pasando como parámetro el fichero de configuración y la
palabra `SECRET`.

#### Comando `docker build` ####

Una vez creado el fichero `Dockerfile` ya podemos hacer un
`docker build` para construir la imagen con nuestra aplicación. Como nombre de la imagen usaremos
`<usuario-docker>/mads-todolist:1.1.0`. Docker identifica el número que
hay después de los dos puntos como el número de versión.

```
$ cd mads-todolist-guia
$ docker build -t <DOCKER-ID>/mads-todolist:1.1.0 .
```

#### Ejecución de la imagen docker ####

Una vez construida la imagen es posible usarla para ejecutar la
aplicación de muchas maneras. En todas ellas se lanzará la imagen
usando el comando `docker run`. 

Lo más sencillo es ejecutar la aplicación trabajando con la base de
datos en memoria:

```
$ docker run -it --rm -p 9000:9000 domingogallardo/mads-todolist:1.1.0
```

El flag `-it` permite visualizar en el terminal de forma interactiva
la salida estándar de la aplicación Play y terminarla haciendo un `CTRL-C`.

También podemos lanzar la aplicación para que trabaje con MySQL,
definiendo las variables de entorno necesarias.

```
$ docker run --link db-mysql --rm -it -p 9000:9000 \
-e DB_URL="jdbc:mysql://db-mysql:3306/mads" -e DB_USER_NAME="root" \
-e DB_USER_PASSWD="mads" -e CONFIG_FILE="conf/develop-mysql.conf" domingogallardo/mads-todolist:1.1.0
```

El comando se conecta con el contenedor `db-mysql` en el que hemos
lanzado la base de datos MySQL:

```
$ docker run -d -p 3316:3306 --name db-mysql -e MYSQL_ROOT_PASSWORD=mads -e MYSQL_DATABASE=mads mysql:5
```


Si en algún momento nos encontramos con un error podemos ver el log
del contenedor (si estamos depurando es convieniente lanzar la aplicación sin el flag
`--rm` para poder examinar el contenedor):

```
$ docker container ls -a
CONTAINER ID        IMAGE                                STATUS              PORTS                               NAMES
19986a063c03        domingogallardo/mads-todolist:1.1.0  Up 2 minutes        0.0.0.0:9000->9000/tcp              zen_payne
$ docker container logs 19986a063c03
[info] application - Creating Pool for datasource 'default'
[info] p.a.d.HikariCPConnectionPool - datasource [default] bound to JNDI as DBTodoList
[info] p.a.d.DefaultDBApi - Database [default] connected at jdbc:mysql://db-mysql:3306/mads
[info] application - ApplicationTimer demo: Starting application at 2018-10-06T11:57:24.119Z
[info] play.api.Play - Application started (Prod)
[info] p.c.s.NettyServer - Listening for HTTP on /0.0.0.0:9000
```

#### Lanzamiento de tests ####

Podemos también ejecutar los tests haciendo que el contenedor ejecute el comando
`bash` con `sbt test`:

```
$ docker run --rm domingogallardo/mads-todolist:1.1.0 /bin/bash -c "sbt test"
```

Para los tests de integración con la base de datos real MySQL:

```
$ docker run --link db-mysql --rm -e DB_URL="jdbc:mysql://db-mysql:3306/mads" \
     -e DB_USER_NAME="root" -e DB_USER_PASSWD="mads" domingogallardo/mads-todolist:1.1.0 \
     /bin/bash -c "sbt '; set javaOptions += \"-Dconfig.file=conf/develop-mysql.conf\"; test'"
```

#### Subida a docker hub ####

Una vez construida la imagen se puede subir a Docker Hub haciendo
`docker push` (después de autenticarse con `docker login`). Tardará
bastante la primera vez. En las siguientes compilaciones ya no tardará
tanto, porque sólo se subirá la parte que cambia de la máquina.

```
$ docker login
Username: <docker-id>
Password: <contraseña>
$ docker push domingogallardo/mads-todolist:1.1.0
```

Allí estará disponible para descargarla y ejecutarla desde cualquier servidor.

#### La etiqueta latest ####

Utilizando la etiqueta `latest` marcamos una imagen como la imagen por
defecto que se descarga si no se proporciona un número de versión.

```
$ docker image ls
REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
domingogallardo/mads-todolist   1.1.0               b80593e5f646        31 hours ago        734MB
$ docker tag b80593e5f646 domingogallardo/mads-todolist:latest
$ docker push domingogallardo/mads-todolist:latest
```

Una vez subida esta imagen es la que se descargará si se hace un `pull` del repositorio `domingogallardo/mads-todolist`

### Pasos a seguir en la práctica ###

- Crea un nuevo _issue_ llamado `Integración continua con Travis`,
  crea una nueva rama `integracion-continua` y súbela a GitHub.
- Realiza un commit con el fichero `Dockerfile` añadido.
- Construye la máquina docker con tu práctica, prueba que funciona
  bien la ejecución en memoria y el lanzamiento de los tests contra la
  base de datos MySQL (tests de integración) y súbela a Docker
  Hub, con la versión `1.1.0` y la versión `latest`.
- Comparte en el foro de la asignatura el nombre de tu máquina y el
  enlace a tu página de Docker Hub.


## Integración continua con Travis ##

[Travis-ci.com](https://travis-ci.com/) es un servicio que permite realizar
integración continua on-line, sin necesidad de configurar un servidor
propio de integración continua.

Es un servicio de pago, pero es gratuito para los repositorios
abiertos (_open source_) y para las cuentas educativas de GitHub. La
organización de GitHub `mads-ua-18` también está autorizada como
organización educativa, por lo que todos los repositorios creados
dentro de esa organización podrán trabajar con Travis.

Puedes consultar el funcionamiento de Travis leyendo su documentación,
comenzando por la página [Getting
started](https://docs.travis-ci.com/user/getting-started/).

En la práctica vamos a configurar Travis para que todos los _pull
requests_ deban pasar los tests de integración (conectándose a la base
de datos MySQL) y para que cuando se realice el _merge_ con `master`
se suba una nueva versión de la máquina docker con la aplicación a
Docker Hub.

### Conexión con GitHub ###

En GitHub está configurada la conexión con Travis para todos los
proyectos en la organización `mads-u-18`. 

En tu cuenta de Travis, una vez logeado, podrás sincronizar tu
repositorio y configurar la conexión. Verás una pantalla como la
siguiente:

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/02-pruebas-tdd/imagenes/conexion-travis.png" width="700px"/>


### Tests en los pull requests ###

Usando Travis es posible configurar el repositorio de GitHub para que todos los
_pull requests_ deban pasar los tests de integración en el servicio.

En la siguiente imagen vemos el aspecto en GitHub de un _pull request_
estando activa la integración con Travis. Una vez abierto el PR,
Travis comprueba si la integración de master con la rama pasa los
tests definidos en el fichero de configuración. Sólo si los tests
pasan es posible realizar el _merge_ del PR en master.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/02-pruebas-tdd/imagenes/pull-request-travis.png" width="600px"/>



### El fichero de configuración  ###

La configuración de Travis se realiza con el fichero `.travis.yml` en
la raíz del repositorio.

El fichero `.travis.yml` para mi repositorio solución de la práctica
es el siguiente:

**Fichero `.travis.yml`**

```text
sudo: required

language: bash

branches:
  only:
  - master

services:
- docker

before_script:
- docker build -t domingogallardo/mads-todolist:$TRAVIS_BUILD_NUMBER .

script:
- docker run -d --rm -p 3306:3306 --name db-mysql -e MYSQL_ROOT_PASSWORD=mads -e MYSQL_DATABASE=mads mysql:5
- docker run --link db-mysql --rm -e DB_URL="jdbc:mysql://db-mysql:3306/mads" -e DB_USER_NAME="root" -e DB_USER_PASSWD="mads" domingogallardo/mads-todolist:$TRAVIS_BUILD_NUMBER /bin/bash -c "sbt '; set javaOptions += \"-Dconfig.file=conf/develop-mysql.conf\"; test'"

after_success:
- if [ "$TRAVIS_EVENT_TYPE" != "pull_request" ]; then
  docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD";
  docker push domingogallardo/mads-todolist:$TRAVIS_BUILD_NUMBER;
  docker tag domingogallardo/mads-todolist:$TRAVIS_BUILD_NUMBER domingogallardo/mads-todolist:latest;
  docker push domingogallardo/mads-todolist:latest;
  fi
```

Puntos interesantes a destacar:

- Se puede espeficar la rama en la que se activa la integración
  continua en el apartado `branches`. En nuestro caso es la rama
  `master`. En cualquier commit o _pull request_ que se haga sobre esa
  rama se lanzará la integración continua.
- El apartado `services` define los servicios necesarios para que se
  ejecute el script de integración. En nuestro caso `docker`.
- En el apartado `before_script` se definen los comandos a realizar
  antes de ejecutar el _script_ con los tests. En nuestro caso
  construimos la imagen docker.
- En el apartado `script` se definen los comandos a realizar para
  lanzar los tests. En nuestro caso ponemos en marcha el servicio
  docker de MySQL y lanzamos la máquina docker de la aplicación para
  que ejecute los tests usando la conexión con ese servicio.
- Por último, el apartado `after_success` se ejecuta si los tests han
  pasado correctamente. En nuestro caso definimos la condición
  adicional de que la ejecución de Travis se haya lanzado no por un
  _pull request_ abierto sino porque se ha hecho un _merge_ del _pull
  request_ en master. En ese caso se sube a Docker Hub la última
  imagen creada, con el número de versión definido por el número de
  _build_ de Travis y también con la etiqueta `latest`.


### Builds en Travis ###

En Travis tenemos toda la información de los _builds_. Es posible
visualizarla una vez ha terminado el _build_ o mientras se está
ejecutando.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/02-pruebas-tdd/imagenes/builds-travis.png" width="600px"/>

!!! Note "Nota"

    Sólo es posible ejecutar un _build_ simultáneo en la organización
    `mads-ua-18`. Cuando hay otro _build_ ejecutándose los nuevos
    _builds_ que se lancen quedarán encolados por fecha de inicio.


### Versiones en Docker Hub ###

En Docker Hub tendremos el histórico de versiones generadas en la
integración continua. Y la última estará etiquetada con `latest`.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/02-pruebas-tdd/imagenes/docker-hub.png" width="500px"/>


### Pasos a seguir en la práctica ###

- Date de alta en [Travis-ci.com](https://travis-ci.com) y conéctalo al repositorio de la práctica.
- Adapta el fichero `.travis.yml` a tu práctica y añádelo con un
  commit a la rama `integracion-continua`.
- Sube el commit a GitHub y abre un _pull request_ con la rama.
- Comprueba que se pasan los tests en Travis y que se marca como
  correcto el _pull request_. Si hay algún fallo, realiza los cambios
  necesarios para corregirlos y vuelve a subir el commit.
- Mezcla el _pull request_ con `master`. Se volverán a lanzar los
  tests en Travis y se subirá la máquina docker resultante a Docker
  Hub.
- Crea en la wiki una página llamada `Integración continua` y
  documenta en ella lo que has hecho en esta parte de la
  práctica. Como mínimo:
  - Captura de pantalla de los tests de integración con `sbt`.
  - Enlace a Docker Hub.

## TDD ##

En la segunda parte de la práctica desarrollaremos, usando TDD (_Test
Driven Design_), una nueva _feature_ de la aplicación: la posibilidad
de definir definir equipos a los que puedan pertenecer los usuarios.

Descomponemos la _feature_ en las siguientes historias de usuario.

- 008 Listado de equipos
- 009 Gestionar pertenencia al equipo
- 010 Gestión de equipos

**008 Listado de equipos**: Como usuario podré consultar el listado de
los equipos existentes y los participantes en cada uno de ellos para
poder consultar la estructura de la empresa y los proyectos en marcha
y comprobar si estoy en los equipos correctos.

**009 Gestionar pertenencia al equipo**: Como usuario podré añadirme y
eliminarme de cualquier equipo para poder participar y dejar de
participar en ellos.

**010 Gestión de equipos**: Como administrador podré crear, cambiar el
nombre y eliminar los equipos para adaptarlos a los proyectos y
estructura de la empresa.

Vamos a hacer de forma guiada la primera historia y dejamos las
siguientes para que las hagas por tu cuenta.

### 008 Listado de equipos ###

La descripción de la historia de usuario es la siguiente:

```text
Listado de equipos

Como usuario podré consultar el listado de
los equipos existentes y los participantes en cada uno de ellos para
poder consultar la estructura de la empresa y los proyectos en marcha
y comprobar si estoy en los equipos correctos.

Detalles

    * En el menú aparcerá una opción `Equipos` que llevará a un
    listado con los nombres de todos los equipos existentes.
    * El listado de equipos estará ordenado por orden alfabético.
    * Pinchando en el nombre del equipo aparecerá un listado de todos
    los usuarios que lo componen.
    * Un usuario podrá pertenecer a más de un equipo.
```

Vamos a utilizar la técnica de TDD para construir la funcionalidad
**de abajo a arriba**. Comenzaremos con tests que construyan la capa
de modelo (clases de entidad y repository) y después pasaremos a tests
que construyan la capa de servicio.

Por último, una vez implementados los métodos de servicios necesarios,
deberás implementar (lo haremos sin tests) las vistas y
controllers. Las vistas y controllers los probaremos de forma manual,
sin tests automáticos.

!!! Important "Importante"

    Los controllers no deben implementar ningún código adicional, sólo
    llamar al método de servicio necesario. De esta forma nos
    aseguramos que todo el código importante para la funcionalidad está
    testeado y ha sido creado mediante TDD.

Recuerda que los pasos seguir la técnica de TDD:

- **Test**: Primero debes escribir el test.
- **Code**: Después debes escribir el código que hace pasar el test (**únicamente el código
necesario, no puedes escribir código de más**)
- **Refactor**: Y, si es necesario, realizar una refactorización del código (los
  tests deben seguir pasando después de la refactorización).

Deberás hacer **un commit por cada fase Test-Code**. Si haces
refactorización deberás hacerlo en otro commit adicional.


#### Pasos a seguir en la práctica ####

- Crea la historia de usuario en el tablero Trello.
- Crea los _issues_ correspondientes a esta historia:
    - Servicio y modelo listado de equipos.
    - Vista y controller listado de equipos.
- Crea una rama para desarrollar el primer _issue_ (llámala
  `servicio-equipos`, por ejemplo) y pásalo en el
  tablero a `In progress`.

Este primer _issue_ lo haremos de forma guiada usando TDD con los
tests que enumeraremos a continuación. El otro _issue_ lo deberás
implementar por ti mismo.


##### Primer test - Entidiad `Equipo` #####

El primer test es para crear la entidad `Equipo`. Por ahora sólo
creamos la clase Java, sin las anotaciones JPA. Un equipo

**Fichero `src/test/java/madstodolist/EquipoTest.java**:
```java
package madstodolist;

import madstodolist.model.Equipo;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import static org.assertj.core.api.Assertions.assertThat;

@RunWith(SpringRunner.class)
@SpringBootTest
public class EquipoTest {

    @Test
    public void crearEquipo() {
        Equipo equipo = new Equipo("Proyecto Cobalto");
        assertThat(equipo.getNombre()).isEqualTo("Proyecto Cobalto");
    }
}
```

Escribe el código necesario para que pase el test. **No debes escribir
código de más, sólo el código mínimo para que el test pase**. Haz un
_commit_ que contenga el test y el código y súbelo a la rama remota.

##### Segundo test - Entidad en base de datos #####

Con el segundo test queremos conseguir que funcione JPA con la entidad
`Equipo` y que podamos usar una tabla de equipos en la base de datos,
en la que podamos guardar entidades `equipo`.

Para comprobar que la entidad se ha guardado correctamente,
comprobaremos se ha actualizando su identificador. Lo hacemos
añadiendo el siguiente test:

```java

    @Autowired
    private EquipoRepository equipoRepository;

    @Test
    @Transactional
    public void grabarEquipo() {
        // GIVEN
        Equipo equipo = new Equipo("Proyecto Cobalto");

        // WHEN
        equipoRepository.save(equipo);

        // THEN
        assertThat(equipo.getId()).isNotNull();
    }
```

Escribe el código necesario para se pase el test y haz un commit.

##### Tercer test - Definición de igualdad entre equipos #####

Ahora que hemos introducido el `id` del equipo escribimos un test
para comprobar que dos equipos son iguales. Debes escribir el código
de los métodos `equals` y `hashCode` (necesario este último para que
funcione correctamente la comprobación de igualdades en las
colecciones).

```java
    @Test
    public void comprobarIgualdadEquipos() {
        // GIVEN
        // Creamos tres equipos sin id, sólo con el nombre
        Equipo equipo1 = new Equipo("Proyecto Cobalto");
        Equipo equipo2 = new Equipo("Proyecto Níquel");
        Equipo equipo3 = new Equipo("Proyecto Níquel");

        // THEN
        // Comprobamos igualdad basada en el atributo nombre
        assertThat(equipo1).isNotEqualTo(equipo2);
        assertThat(equipo2).isEqualTo(equipo3);

        // WHEN
        // Añadimos identificadores y comprobamos igualdad por identificadores
        equipo1.setId(1L);
        equipo2.setId(1L);
        equipo3.setId(2L);

        // THEN
        // Comprobamos igualdad basada en el atributo nombre
        assertThat(equipo1).isEqualTo(equipo2);
        assertThat(equipo2).isNotEqualTo(equipo3);
    }
```

Escribe el código necesario para se pase el test y haz un commit.

##### Cuarto test - Buscar equipo en base de datos #####

Escribimos ahora un test para recuperar equipos por su identificador
de la base de datos. Añadimos un equipo a la tabla en el fichero
`datos-test.sql` para poder comprobar que funciona correctamente.

Añadimos en el fichero **`src/test/java/resources/datos-test.sql`**:
```
INSERT INTO equipos (id, nombre) VALUES('1', 'Proyecto Cobalto');
```

Test:

```java
    @Test
    public void comprobarRecuperarEquipo() {
        // GIVEN
        // En el application.properties se cargan los datos de prueba del fichero datos-test.sql

        // WHEN

        Equipo equipo = equipoRepository.findById(1L).orElse(null);

        // THEN
        assertThat(equipo).isNotNull();
        assertThat(equipo.getId()).isEqualTo(1L);
        assertThat(equipo.getNombre()).isEqualTo("Proyecto Cobalto");
    }
```

Comprueba el test y si es necesario escribe el código estríctamente
necesario para que pase.

Haz un commit en la rama y súbelo a GitHub.

##### Quinto test - Relación en memoria muchos-a-muchos entre equipos y usuarios #####

Vamos ahora a diseñar un test que introduzca la relación entre equipos
y usuarios. Debe ser una relación muchos-a-muchos: un equipo contiene
muchos usuarios y un usuario puede pertenecer a 0, 1 o muchos equipos.

Empezamos por un test para crear la relación en memoria, con las
anotaciones mínimas para que JPA no se queje:

```java
    @Test
    public void relaciónMuchosAMuchosVacia() {
        // GIVEN

        Equipo equipo = new Equipo("Proyecto Cobalto");
        Usuario usuario = new Usuario("prueba@gmail.com");

        // WHEN
        // THEN

        assertThat(equipo.getUsuarios()).isEmpty();
        assertThat(usuario.getEquipos()).isEmpty();
    }
```

Para que este test funcione hay que crear la relación muchos-a-muchos
entre equipos y usuarios. Por sólo la definimos en memoria, sin
especificar cómo se mapea en la base de datos:

**Fichero `src/main/java/madstodolist/model/Equipo.java`**:
```diff
    private String nombre;
+    @ManyToMany
+    Set<Usuario> usuarios = new HashSet<>();

...

    public void setId(Long id) {
        this.id = id;
    }

+    public Set<Usuario> getUsuarios() {
+        return usuarios;
+    }
```


**Fichero `src/main/java/madstodolist/model/Usuario.java`**:
```diff
    @OneToMany(mappedBy = "usuario", fetch = FetchType.EAGER)
    Set<Tarea> tareas = new HashSet<>();

+    @ManyToMany
+    Set<Equipo> equipos = new HashSet<>();

...

+    public Set<Equipo> getEquipos() {
+        return equipos;
+    }
```


##### Sexto test - Relación entre usuarios y equipos en base de datos #####

```diff
INSERT INTO tareas (id, titulo, usuario_id) VALUES('2', 'Renovar DNI', '1');
+ INSERT INTO equipos (id, nombre) VALUES('1', 'Proyecto Cobalto');
+ INSERT INTO equipo_usuario (fk_equipo, fk_usuario) VALUES('1', '1');
```


```java
    @Autowired
    private UsuarioRepository usuarioRepository;
    
    @Test
    public void comprobarRelacionBaseDatos() {
        // GIVEN
        // En el application.properties se cargan los datos de prueba del fichero datos-test.sql

        // WHEN
        Equipo equipo = equipoRepository.findById(1L).orElse(null);
        Usuario usuario = usuarioRepository.findById(1L).orElse(null);
        
        // THEN
        
        assertThat(equipo.getUsuarios()).hasSize(1);
        assertThat(equipo.getUsuarios()).contains(usuario);
        assertThat(usuario.getEquipos()).hasSize(1);
        assertThat(usuario.getEquipos()).contains(equipo);
    }
```

Solución:

```diff
    @ManyToMany
+    @JoinTable(name = "equipo_usuario",
+            joinColumns = { @JoinColumn(name = "fk_equipo") },
+            inverseJoinColumns = {@JoinColumn(name = "fk_usuario")})
    Set<Usuario> usuarios = new HashSet<>();
```

```diff
-    @ManyToMany
+    @ManyToMany(mappedBy = "usuarios")
    Set<Equipo> equipos = new HashSet<>();
```


##### Séptimo test - listado de equipos #####

```diff
INSERT INTO equipo_usuario (fk_equipo, fk_usuario) VALUES('1', '1');
+ INSERT INTO equipos (id, nombre) VALUES('2', 'Proyecto Adamantium');
```


```java
    @Test
    @Transactional
    public void comprobarFindAll() {
        // GIVEN
        // En el application.properties se cargan los datos de prueba del fichero datos-test.sql

        // WHEN
        List<Equipo> equipos = equipoRepository.findAll();

        // THEN
        assertThat(equipos).hasSize(2);
    }
```

Solución:


**Fichero `EquipoRepository.java`**:

```diff
+ import java.util.List;

public interface EquipoRepository extends CrudRepository<Equipo, Long> {
+     public List<Equipo> findAll();
}

```

##### Octavo test - Método de servicio para el listado de equipos #####


**Fichero `src/test/java/madstodolist/EquipoServiceTest.java`**:

```java
package madstodolist;

 import madstodolist.model.Equipo;
 import madstodolist.service.EquipoService;
 import org.junit.Test;
 import org.junit.runner.RunWith;
 import org.springframework.beans.factory.annotation.Autowired;
 import org.springframework.boot.test.context.SpringBootTest;
 import org.springframework.test.context.junit4.SpringRunner;

 import java.util.List;

 import static org.assertj.core.api.Assertions.assertThat;

 @RunWith(SpringRunner.class)
 @SpringBootTest
 public class EquipoServiceTest {

     @Autowired
     EquipoService equipoService;

     @Test
     public void obtenerListadoEquipos() {
         // GIVEN
         // En el application.properties se cargan los datos de prueba del fichero datos-test.sql

         // WHEN
         List<Equipo> equipos = equipoService.findAllOrderedByName();

         // THEN
         assertThat(equipos).hasSize(2);
         assertThat(equipos.get(0).getNombre()).isEqualTo("Proyecto Adamantium");
         assertThat(equipos.get(1).getNombre()).isEqualTo("Proyecto Cobalto");
     }
 }
```

##### Noveno test - Método de servicio para recuperar un equipo #####


En el fichero `src/test/java/madstodolist/EquipoServiceTest.java`
añadimos el siguiente test.

El test sirve para crear el método de servicio que recupera un equipo
y para asegurarnos de que la relación entre equipos y usuarios es `LAZY`.

```java
    @Test
    public void obtenerEquipo() {
        // GIVEN
        // En el application.properties se cargan los datos de prueba del fichero datos-test.sql

        // WHEN
        Equipo equipo = equipoService.findById(1L);

        // THEN
        assertThat(equipo.getNombre()).isEqualTo("Proyecto Cobalto");
        // Comprobamos que la relación con Usuarios es lazy: al
        // intentar acceder a la colección de usuarios se debe lanzar una
        // excepción de tipo LazyInitializationException.
        assertThatThrownBy(() -> {
            equipo.getUsuarios().size();
        }).isInstanceOf(LazyInitializationException.class);
    }
```


##### Décimo test - Método de servicio para obtener los usuarios de un equipo #####

Un test algo complejo, que sirve para definir el método de servicio
`usuariosEquipo(Long idEquipo)` que devuelve la lista de usuarios de
un equipo.

Después de comprobar que la lista que se devuelve es correcta, se
comprueba que la relación entre usuarios y equipos es `EAGER`, esto
es, que desde un usuario se puede obtener la lista de equipos a los
que pertenece.

```java

    @Test
    public void obtenerUsuariosEquipo() {
        // GIVEN
        // En el application.properties se cargan los datos de prueba del fichero datos-test.sql

        // WHEN
        List<Usuario> usuarios = equipoService.usuariosEquipo(1L);

        // THEN
        assertThat(usuarios).hasSize(1);
        assertThat(usuarios.get(0).getEmail()).isEqualTo("ana.garcia@gmail.com");
        // Comprobamos que la relación entre usuarios y equipos es eager
        // Primero comprobamos que la colección de equipos tiene 1 elemento
        assertThat(usuarios.get(0).getEquipos()).hasSize(1);
        // Y después que el elemento es el equipo Proyecto Cobalto
        assertThat(usuarios.get(0).getEquipos().stream().findFirst().get().getNombre()).isEqualTo("Proyecto Cobalto");
    }
}
```




### Pasos a seguir en la práctica ###

- Crea una _feature_ nueva en la wiki, un nuevo _issue_ para
  resolverla (con el _milestone_ 1.2.0) y una nueva rama en la que
  desarrollarás el _issue_. 
- Completa el código para pasar los tests, uno a uno, **haciendo un
  commit después de cada fase test-code** y otro en la fase
  **refactor** (en el caso en que tengas que hacer refactorización).
- Continua usando TDD y haciendo commits **test-code** y **refactor**
  para terminar de implementar la _feature_, escribiendo los tests
  necesarios para terminar de implementar la capa de repositorio y la
  capa de servicio con los métodos necesarios para implementar la
  nueva funcionalidad. Los incrementos de código introducidos por los
  tests deben ser pequeños. Debe haber **entre 15 y 25 líneas de
  código** añadidas en las fases de codificación (sin contar el código
  de los tests). No tomes este número de forma demasiado estricta; si
  en algún ciclo hay que añadir 35 líneas no pasa nada. Tampoco si
  haces menos de 15. Pero estaría mal tener que añadir 70 líneas para
  resolver un test.
- Termina de implementar la historia de usuario modificando las vistas
  y los controllers necesarios.
- Crea un _pull request_ y mezcla en `master` la nueva
  funcionalidad. Se subirá a Docker Hub la nueva versión de la máquina docker.
- Realiza el nuevo _release_ con el número `1.2.0`, genera a mano la máquina
  docker con esa versión y súbela a Docker Hub.
  
## Entrega y evaluación ##

- La práctica tiene una duración de 3 semanas y debe estar terminada
  el martes 30 de octubre.
- La calificación de la práctica tiene un peso de un 8% en la nota
  final de la asignatura. 
- Para realizar la entrega se debe subir a Moodle un ZIP que contenga
  todo el proyecto, incluyendo el directorio `.git` que contiene la
  historia Git. Para ello comprime tu directorio local del proyecto
  **después de haber hecho un `clean` en `sbt`** para eliminar el
  directorio `target` que contiene los binarios compilados. Debes
  dejar también en Moodle la URL del repositorio en GitHub y la URL de
  la máquina en Docker Hub.

Para la evaluación se tendrá en cuenta:

- Desarrollo continuo (los _commits_ deben realizarse a lo largo de
  las 3 semanas y no dejar todo para la última semana).
- Correcto desarrollo de la metodología.
- Diseño e implementación del código y de los tests de las
  características desarrolladas.

