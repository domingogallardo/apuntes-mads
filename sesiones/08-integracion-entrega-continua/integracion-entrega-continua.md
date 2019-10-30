
## Integración y entrega continua

<kbd><img src="diapositivas/integracion-entrega-continua.001.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.002.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.003.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.004.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.005.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.006.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.007.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.008.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.009.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.010.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.011.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.012.png" width="800px"></kbd>

- [Martin Fowler - Continuous Integration](http://www.martinfowler.com/articles/continuousIntegration.html)

<kbd><img src="diapositivas/integracion-entrega-continua.013.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.014.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.015.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.016.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.017.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.018.png" width="800px"></kbd>

- [Todd Papaioannou - Slideshare](https://www.slideshare.net/drluckyspin/continuous-integration)

<kbd><img src="diapositivas/integracion-entrega-continua.019.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.020.png" width="800px"></kbd>

- [Gradle](https://gradle.org)
- [Sbt](http://www.scala-sbt.org/release/docs/index.html)

<kbd><img src="diapositivas/integracion-entrega-continua.021.png" width="800px"></kbd>

- [Artifactory](https://www.jfrog.com/open-source/#os-arti)
- [Nexus](http://www.sonatype.org/nexus/)

<kbd><img src="diapositivas/integracion-entrega-continua.022.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.023.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.024.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.025.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.026.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.027.png" width="800px"></kbd>


- Travis: [Using Docker in builds](https://docs.travis-ci.com/user/docker/)


### Demostración de Docker ###

Comprobamos la instalación de docker:


```
$ docker version
$ docker ps
```

Comprobamos las imágenes que hay descargadas en nuestra máquina:

```
$ docker image ls
```

Ejecutamos una imagen:

```
$ docker run docker/whalesay cowsay Hello world
```

Para generar el mensaje se producen los siguientes pasos:

1. El cliente Docker contacta el demonio Docker que se está ejecutando
   en la máquina host.
2. El demonio comprueba si tenemos la imagen `hello-world` y si no se
   la descarga del _Docker Hub_.
3. El demonio crea un nuevo contenedor a partir de la imagen que
   arranca el ejecutable que produce la salida de texto.
4. El demonio pasa las salida de texto al cliente Docker, el cual la
   envía a la terminal.

Para ver los contenedores en ejecución:

```
$ docker ps
```

Y todos los contenedores (incluyendo los parados):

```
$ docker ps -a
```

Podemos ejecutar un contenedor basado en una imagen Linux Alpine
(Alpine es una distribución Linux muy ligera):

```
$ docker run alpine /bin/echo 'Hello world'
```

Una vez lanzado el comando `/bin/echo` el contenedor se queda parado:

```
$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                     PORTS                               NAMES
ecf8be2a3ead        alpine              "/bin/echo 'Hello wo…"   8 seconds ago       Exited (0) 7 seconds ago                                       agitated_bhaskara
```

Se puede borrar:

```
$ docker container rm ecf8be2a3ead
```

También se puede lanzar un contenedor de forma interactiva, con el
flag `-it`. El flag `--rm` borra el contenedor cuando se para.

```
$ docker run --rm -it alpine /bin/sh
```

También como un demonio, que está en ejecución hasta que lo paramos:

```
$ docker run --rm -d alpine /bin/sh -c "while true; do echo hello world; sleep 1; done"

1e5535038e285177d5214659a068137486f96ee5c2e85a4ac52dc83f2ebe4147

$ docker ps
CONTAINER ID  IMAGE         COMMAND               CREATED        STATUS       PORTS    NAMES
1e5535038e28  alpine        /bin/sh -c 'while tr  2 minutes ago  Up 1 minute           insane_babbage

$ docker logs insane_babbage

hello world
hello world
hello world
...

$ docker stop insane_babbage
$ docker container ls -a

CONTAINER ID  IMAGE         COMMAND               CREATED        STATUS       PORTS NAMES
```


<kbd><img src="diapositivas/integracion-entrega-continua.027.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.028.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.029.png" width="800px"></kbd>


### Construir una imagen propia ###

Creamos un directorio:

```
$ mkdir midocker
$ cd midocker
```

Editamos el fichero **Dockerfile**

```
FROM docker/whalesay:latest
RUN apt-get -y update && apt-get install -y fortunes
CMD /usr/games/fortune -a | cowsay
```

Llamamos a `docker build` para construir la nueva imagen y le damos el nombre `docker-whale`:

```
$ docker build -t docker-whale .
```

Comprobamos que se ha añadido al repositorio local de imágenes:

```
$ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
docker-whale        latest              244786599109        13 seconds ago      275 MB
ubuntu              latest              42118e3df429        3 months ago        124.8 MB
python              2.7                 b5c7fb15c9cb        3 months ago        691.6 MB
hello-world         latest              c54a2cc56cbb        4 months ago        1.848 kB
docker/whalesay     latest              6b362a9f73eb        17 months ago       247 MB
```

Y ya podemos ejecutar el contenedor:

```
$ docker run docker-whale
 ________________________________________ 
/ The farther you go, the less you know. \
|                                        |
\ -- Lao Tsu, "Tao Te Ching"             /
 ---------------------------------------- 
    \
     \
      \     
                    ##        .            
              ## ## ##       ==            
           ## ## ## ##      ===            
       /""""""""""""""""___/ ===        
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   
       \______ o          __/            
        \    \        __/             
          \____\______/   
```


### Servidor web ###

Es posible también montar en el contenedor un directorio del host. 

Vamos, por ejemplo, a poner en marcha un servidor web y usar un
directorio del host como directorio del sitio web.


Creamos un directorio `webserver` y creamos dentro un fichero `default`:

```
server {
    root /var/www;
    index index.html index.htm;

    # Make site accessible from http://localhost/
    server_name localhost;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to index.html
        try_files $uri $uri/ /index.html;
    }
}
```

Creamos también el siguiente fichero `Dockerfile`:

```
FROM ubuntu:14.04

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/ssl
ADD default /etc/nginx/sites-available/default

EXPOSE 80

CMD ["nginx"]
```

El fichero anterior usa los siguientes comandos para construir la imagen:

- `FROM` le dice a Docker cuál es la imagen base
- `RUN` ejecutará el comando a continuación 
- `ADD` copiará un fichero de la máquina host en la imagen. Es muy útil para ficheros de configuración o scripts que queramos ejecutar.
- `EXPOSE` expondrá un port a la máquina host. Es posible exponer más de un puerto como: `EXPOSE 80 443 8888`
- `CMD` ejecutará un comando cuando se ponga en marcha el contenedor

Una vez definido el fichero `Dockerfile`, podemos construir la imagen:

```
$ docker build -t nginx-example .
```

Podemos comprobar que se ha construido listando las imágenes:

```
$ docker image ls
```

Por último, lanzamos el servidor web:

```
$ docker run -p 80:80 -d nginx-example
```

El parámetro `p 80:80` liga el puerto 80 del contenedor con el puerto 80 del host.

Hacemos `docker ps` para asegurarnos que el contenedor está
funcionando:

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                NAMES
a377dd528a85        nginx-example       "nginx"             22 seconds ago      Up 21 seconds       0.0.0.0:80->80/tcp   reverent_franklin
```

Si abrimos el navegador en `localhost` veremos que
responde, pero obtenemos un error 500 porque falta el fichero
`index.html`.

Para arreglarlo, creamos el fichero `index.html` en el directorio actual:

**`index.html`**:

```
<h1>Hola desde el contenedor</h1>
```

Y lanzamos el contenedor montando el directorio actual en el
directorio `/var/www` del contenedor (el servidor Nginx usa el
directorio `/var/www` como sitio por defecto donde poner los ficheros
HTML):

```
$ docker stop reverent_franklin
$ docker run -v $(PWD):/var/www:rw -p 80:80 -d nginx-example
```

Si comprobamos ahora el navegador, veremos que muestra el HTML que
hemos guardado. Podemos probar a cambiar el HTML y veremos cómo se
actualiza también en el contenedor.

### Borrar contenedores e imágenes ###

- Para borrar un contenedor

    ```
    $ docker container rm <ID o nombre contenedor>
    ```

- Para borrar todos los contenedores parados:

    ```
    $ docker container prune 
    ```

- Para borrar una imagen:

    ```
    $ docker image rm <nombre imagen>
    ```

- Para borrar todas las imágenes no usadas:

    ```
    $ docker image prune
    ```

- Para borrar todo lo no usado (contenedores e imágenes):

    ```
    $ docker system prune -a
    ```
    
### Más información sobre Docker ###

- [Docker Overview](https://docs.docker.com/engine/understanding-docker/)
- [Get Started with Docker](https://docs.docker.com/engine/getstarted/)


<kbd><img src="diapositivas/integracion-entrega-continua.028.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.029.png" width="800px"></kbd>

- [Charla Jezz Humble - Adopting Continuous Delivery](https://vimeo.com/68320415)

<kbd><img src="diapositivas/integracion-entrega-continua.030.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.031.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.032.png" width="800px"></kbd>

- [Charla John Allspaw](http://www.slideshare.net/jallspaw/ops-metametrics-the-currency-you-pay-for-change)


<kbd><img src="diapositivas/integracion-entrega-continua.033.png" width="800px"></kbd>


<kbd><img src="diapositivas/integracion-entrega-continua.034.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.035.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.036.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.037.png" width="800px"></kbd>


<kbd><img src="diapositivas/integracion-entrega-continua.038.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.039.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.040.png" width="800px"></kbd>

- [Etsy’s Product Development with Continuous Experimentation](https://www.infoq.com/presentations/Etsy-Deployment/)

<kbd><img src="diapositivas/integracion-entrega-continua.041.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.042.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.043.png" width="800px"></kbd>

- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)

<kbd><img src="diapositivas/integracion-entrega-continua.044.png" width="800px"></kbd>

La idea del [_canary
release_](https://martinfowler.com/bliki/CanaryRelease.html) consiste
en configurar un sistema de despliegue que permita mantener
simultáneamente en producción dos versiones de la aplicación. En el caso
de una aplicación web, podríamos configurar un proxy o router
intermedio que se encargue de encauzar las peticiones de los usuarios
a una versión de la aplicación o a otra.

Cuando se lanza una característica nueva se puede configurar el proxy
para que sólo sea probada por una pequeña cantidad de usuarios y
detectar posibles errores en este despliegue reducido. Cuando se haya
comprobado con este pequeño grupo que todo funciona correctamente se
modifica la configuración del proxy para que todos accedan a la nueva
versión.

La configuración del proxy puede llegar a ser bastante compleja,
haciendo el filtro de usuarios en función de parámetros que nos
interesen (localización, tipo de usuario, etc.).

Este sistema también puede utilizarse, junto con el de interruptores
de características, para realizar [pruebas
A/B](https://en.wikipedia.org/wiki/A/B_testing) de nuevas
características.

<kbd><img src="diapositivas/integracion-entrega-continua.049.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.050.png" width="800px"></kbd>

Explicación del libro de Jeff Humble:

> Cada cambio que se realiza sobre la configuración de la aplicación, su
> código fuente o sus datos, lanza la creación de una nueva instancia de
> la tubería. Uno de los primeros pasos en la tubería es crear los
> binarios y los instaladores. El resto de la tubería ejecuta una serie
> de tests sobre los binarios para probar que pueden ser lanzados. Cada
> test que pasa el candidato a release nos da más confianza de que
> funcionará correctamente esta combinación particular de código
> binario, información de configuración, entorno y datos. Si el
> candidato a release pasa todos los tests, puede ser lanzado.

<kbd><img src="diapositivas/integracion-entrega-continua.045.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.046.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.047.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.048.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.051.png" width="800px"></kbd>

- [Deploying the Netflix API](http://techblog.netflix.com/2013/08/deploying-netflix-api.html)

<kbd><img src="diapositivas/integracion-entrega-continua.052.png" width="800px"></kbd>


- Continuous Integration at CartoDB:
   - [Slideshare](https://www.slideshare.net/juanignaciosl/continuous-integration-at-cartodb-march-16)
   - [YouTube](https://www.youtube.com/watch?v=fRB_rlUtxys)
   - [Repositorio CartDB en GitHub](https://github.com/CartoDB/cartodb)

<kbd><img src="diapositivas/integracion-entrega-continua.053.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.054.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.055.png" width="800px"></kbd>

<kbd><img src="diapositivas/integracion-entrega-continua.056.png" width="800px"></kbd>

- [Martin Fowler - Continuous Integration](https://github.com/domingogallardo/apuntes-mads/raw/master/lecturas/martin-fowler_continuous-integration.pdf)
- [ThoughtWorks - Continuous Delivery](https://www.thoughtworks.com/continuous-delivery)
