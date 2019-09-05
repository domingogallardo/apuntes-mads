
# Práctica 0 #

En esta práctica tendremos un primer contacto con Spring Boot. También
usaremos Git.

Los objetivos principales son:

- Empezar a conocer Spring Boot, ejecutando una sencilla aplicación _hola mundo_ en Spring Boot.
- Empezar a conocer el _framework_ de plantillas Thymeleaf, realizando
  pequeñas modificaciones en la aplicación que usen un formulario.
- Trabajar de forma regular, realizando pequeños commits que se deben
  subir al repositorio personal de la asignatura en GitHub.

## Instalación de software ##

Vamos a trabajar bastante con el terminal. En Linux o macOS podemos
usar el terminal que viene con el sistema. En Windows usaremos el
terminal Git Bash que se instala en la instalación de Git para
Windows.

Es posible desarrollar la práctica en cualquier sistema
operativo. Debemos instalar el siguiente software:

- Git
- Java JDK 8 o posterior
- Maven
- IntelliJ Ultimate

### Instalación básica ###

#### Linux ####

Para instalar el software en Linux.

- Instalar Git, Java y Maven:

```
$ sudo apt install git
$ sudo apt install default-jdk
$ sudo apt install maven
```

- Instalar [IntelliJ Ultimate](https://www.jetbrains.com/idea/download/)

#### macOS ####

- Git y Java vienen instalados con el sistema operativo. Recomendamos usar
[Homebrew](https://brew.sh) para instalar Maven:

```
$ brew install maven
```

- Instalar [IntelliJ Ultimate](https://www.jetbrains.com/idea/download/)

#### Windows ####

Es recomendable instalar [git for Windows](https://gitforwindows.org),
que además de Git instala Git BASH, un terminal Bash integrado en
Windows.

Además, hay que instalar Java, Maven e [IntelliJ Ultimate](https://www.jetbrains.com/idea/download/).


### Después de la instalación básica  ###

Es fácil probar que funciona el software instalado. Basta con ejecutar
desde el terminal:

```
$ git --version
$ mvn --version (imprime la versión de Maven y de Java)
```

Configurar el nombre de usuario y el correo electrónico en Git:

```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

Es también bastante útil configurar el prompt para que aparezca la
rama del repositorio Git en que nos encontramos. Para ello se debe
añadir en el fichero `$HOME/.bashrc` (linux y Git Bash Windows) o
`$HOME/.bash_profile` (macOS) :

```
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\[\e[37m\]\A \[\e[m\]\[\033[32m\]\W\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
```

Podemos encontrar más opciones de configuración del prompt en muchas
páginas en Internet. Por ejemplo
[aquí](https://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html).

## Repositorio GitHub ##

Para inicializar el repositorio de GitHub en el que vas a trabajar en
esta práctica debes seguir los siguientes pasos:

1. Inicializa tu nombre de usuario y tu correo en Git. El nombre de
   usuario será el nombre que aparecerá en los _commits_. Pon tu nombre
   y apellido.
   
        $ git config --global user.name "Pepe Perez"
        $ git config --global user.email pepe.perez@example.com<

2. Crea una cuenta en GitHub. Puedes usar el nombre de usuario que
   quieras (o usar el que ya tienes), pero **escribe correctamente tu
   nombre y apellidos en el perfil** usando la opción _Settings >
   Profile_ y actualizando el campo _Name_.
   
3. Una vez logeado en GitHub, copia el enlace con una invitación que
   compartiremos en el foro de Moodle. Con esa invitación se creará
   automáticamente el repositorio `practica0-<usuario>` en la
   organización [mads-ua](https://github.com/mads-ua). Es un
   repositorio privado al que tienes acceso tú y el
   profesor. Contiene el código inicial del proyecto demostración de
   Spring Boot (es una copia del repositorio
   [domingogallardo/spring-boot-demoapp](https://github.com/domingogallardo/spring-boot-demoapp)

    Es importante que tengas en cuenta que el repositorio recién
    creado no reside en tu cuenta, sino en la organización
    `mads-ua`. Puedes acceder a él desde el _dashboard_ de GitHub que
    aparece cuando te logeas:
   
    <img src="imagenes/dashboard-github.png" width="600px"/>

    También el profesor te invitará a formar parte de la organización
    y recibirás un mensaje de correo electrónico en el que deberás
    aceptar esta invitación. También se puede aceptar la invitación
    accediendo a <https://github.com/mads-ua>.
   

## Documentación a consultar ##

[Spring Boot](https://spring.io/projects/spring-boot) es un
_framework_ ligero que permite ejecutar aplicaciones [Spring](https://spring.io/projects/spring-framework) de forma
_standalone_, sin necesidad de un servidor de aplicaciones.

La documentación de referencia de estos frameworks se encuentra en las
páginas enlazadas, en la pestaña `Learn`. Podemos encontrar una
extensa cantidad de tutoriales y guías rápidas en la web de Spring, en
la url [https://spring.io/guides](https://spring.io/guides).

Para realizar la práctica leer la [Introducción a Spring Boot para las
prácticas de MADS](./intro-spring-boot.md) y las siguientes guías:

- [Building an Application with Spring Boot](https://spring.io/guides/gs/spring-boot/)
- [Serving Web Content with Spring MVC](https://spring.io/guides/gs/serving-web-content/)
- [Validating Form Input](https://spring.io/guides/gs/validating-form-input/)


## Enunciado de la práctica ##

Haremos una primera práctica sencilla en la que pondremos en
marcha una aplicación inicial en Spring Boot y añadiremos alguna
funcionalidad.

### Trabajamos con la aplicación Demo de Spring Boot ###

Debemos hacer lo siguiente:

- Descargar la [aplicación Demo]() de Spring Boot usando el comando git clone.
- Importarla en IntelliJ
- Probar que se pasan todos los tests usando Maven e IntelliJ
- Ejecutarla desde línea de comando y desde IntelliJ
- Hacer algún pequeño cambio
    
### Añadimos alguna funcionalidad sencilla a la aplicación ###
    
Debemos añadir alguna funcionalidad sencilla a la aplicación que
realice lo siguiente:

- Leer datos de un formulario usando Thymeleaf.
- Llamar a un método de servicio que procese los datos leídos.
- Mostrar el resultado devuelto por el servicio en una página Thymeleaf.
- Incluir al menos 2 tests:
    - 1 de la capa de servicio
    - 1 de la capa de presentación usando MockMvc y moqueando el servicio

Muy importante, debemos desarrollar la aplicación en **pequeños
commits**. Cada commit debe compilar correctamente y añadir una
pequeña funcionalidad. Debemos subir los commits al repositorio
personal de GitHub.

## Comandos Git ##

Comandos Git necesarios para realizar la práctica:

- git clone
- git status
- git add
- git commit
- git push
- git log

Puedes encontrar más información sobre estos comandos en documento
[comandos Git](./comandos-git.md) que resume los conceptos más
importantes de Git necesarios para estas primeras prácticas de la
asignatura.


## Entrega ##

- Realizar la aplicación en el directorio `practica1` del repositorio
  GitHub `practicas-mads-ESTUDIANTE`.
- Fecha límite de entrega: 17 de septiembre (1 semana)

