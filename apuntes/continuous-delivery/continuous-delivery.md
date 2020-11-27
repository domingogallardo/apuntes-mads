# Continuouos Delivery #

- Comparación con entrega basada en versiones
- Integración continua vs. entrega continua
- Entornos
- Tubería de despliegue

Desde hace bastante tiempo se viene hablando de _Integración
continua_ como una técnica basada en tests automáticos que se lanzan
continuamente, cada vez que se añade nuevo código al proyecto. En los
últimos años se ha dado un paso más allá y se ha comenzado a hablar de
_Entrega continua_ (_Continous Delivery_ en inglés) con la idea de
promover software que esté listo en cualquier momento para salir a
producción. Además, se han popularizado herramientas como _Docker_ o
_Kubernetes_ que facilitan el despliegue del software y su
automatización y cada vez se demandan más profesionales (denominados
_DevOps_) con capacidad de gestionar estos despliegues automatizados.

En este tema veremos todos estos conceptos, con la idea de tomar un
primer contacto con todos ellos. Necesitaríamos un curso (o más)
para verlos en profundidad. Intentaremos al menos conocer los
conceptos básicos por si queremos seguir profundizando en alguno de
ellos en el futuro.

## El problema de la puesta en producción ##

En las empresas tradicionales no ágiles el proceso de subir a
producción una nueva versión es un proceso muy complicado y
estresante. Se hace pocas veces, cuatro o cinco veces al año, durante
el fin de semana cuando todos los servicios están parados.

El proceso de genera muchos trastornos y dolores de cabeza. El equipo
de operaciones tiene que estar pendiente del móvil para detectar
posibles problemas y caídas del sistema. Una vez puesto el software en
producción el equipo de desarrollo se dedicará continuamente a
corregir bugs y solucionar problemas detectados por los usuarios.

Esto no es ágil. Esto no permite conseguir lo que hemos comentado
muchas veces de un ciclo corto de retroalimentación para que el
cliente pueda probar rápidamente las nuevas características y se pueda
comprobar su valor. Recordemos que en entornos inciertos y no
predecibles es fundamental poder validar con el cliente las nuevas
funcionalidades introducidas, para adaptarse y corregir posibles
errores.

La realización de entregas frecuentes también permite minimizar el
riesgo. Todo el tiempo que estamos desarrollando algo sin ponerlo en
producción es un riesgo acumulado. Hasta que no está en producción y
ha sido aceptado por el cliente no sabemos si lo que estamos
desarrollando va a ser validado o no. Cuanto menos tardemos en
validarlo, menor será el riesgo.

La siguiente figura está sacada de la charla de Eduardo Ferro
([@eferro](https://twitter.com/eferro)) [Continuous Delivery:
Germinando una cultura ágil
moderna](https://youtu.be/hbggtXmQcf8?t=444). 

<img src="imagenes/small-increments.png" width="500px"/>

El proceso de puesta en producción del software depende mucho del tipo
de software. En un extremo, por ejemplo, una página web se puede
cambiar modificando directamente el fichero HTML en la propia máquina
en la que se está ejecutando el servidor web. No hace falta ni
recompilar, ni reiniciar el servidor. En el otro extremo, un software
de control de una placa de un satelite espacial puede estar embebido
en el propio firmware de la placa y para realizar un cambio puede ser
necesario hasta volver a grabar y producir la placa.

En general, la mayoría de sistemas software se encuentran entre ambos
extremos. Es importante analizar con detalle cuál es el proceso de
despliegue de nuestro software, cuánto tarda en subir a producción un
cambio de una línea de código y cuáles son los cuellos de botella en
el proceso.

<img src="imagenes/ultima-milla.png" width="500px"/>

La denominada _ultima milla_ consiste en los pasos necesarios para la
puesta en producción de nuestro sistema. De nada nos sirve tener un
equipo ágil que hace iteraciones y reuniones con el cliente si después
tenemos un equipo de QA (_Quality Assurance_) con un 90% de pruebas
manuales y otro de operaciones que tiene que configurar manualmente
cualquier nuevo despliegue a producción y al que le cuesta dos días
revertir un despliegue fallido.

Debemos analizar cuál es nuestro proceso de release y hacer lo posible
por mejorarlo. Encontrar los cuellos de botella, reducir los tiempos,
automatizar todo lo que podamos. De forma que pasemos de un release
por trimestre a un release mensual. Y después a un release cada dos
semanas. Y después a un release semanal. Y después a un posible
release con cada posible cada cambio. Al final, como dice Eduardo
Ferro en la charla mencionada anteriormente, el tiempo de subir un
commit a producción debe ser de menos de 15 minutos y debemos de poder
automatizar el proceso de puesta en producción hasta el extremo que lo
podamos hacer a discreción, cuando queramos, únicamente pulsando un
botón.


## Integración continua ##

- Una práctica de XP
- Todos los desarrolladores deben de hacer commits en la línea de
  desarrollo principal al menos una vez al día. Cada commit es
  verificado y construido.
- Esta práctica obliga a incrementos pequeños, a que todo el equipo
  está obligado a conocer los cambios.
  
Testing automático.

## Despliegue continuo ##
### Despliegue ###

- Automatizados
- Sin pérdida de servicio, en horario de trabajo


#### Facilidad de despliegue ####

- Todo esto depende. No es lo mismo hacer software que se despliega en
  un sitio web que hacer el software de control de un chip de un
  satélite espacial que hay que grabarlo en hardware y que si falla se
  carga el satélite.


### Entornos ###

Entorno de desarrollo, de integración, de staging, 

### Producción ###

- Feedback (logs, métricas, dashboard)

- Posibilidad de recuperarse ante los fallos
## Cómo se hace Continuous delivery ##
### Posibilidad de deshacer ###
### Features toggles ###
### Canary releases ###


