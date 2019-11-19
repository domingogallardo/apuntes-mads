

## Historias de usuario


<img src="diapositivas/historias-usuario.001.png" width="800px">

<img src="diapositivas/historias-usuario.002.png" width="800px">

<img src="diapositivas/historias-usuario.003.png" width="800px">

## Objetivo de las historias de usuario ##

Las palabras escritas son ambiguas y se prestan a malentendidos cuando
se utilizan para expresar los requisitos de algo tan complejo como el
software. Tenemos que sustituir las palabras escritas por conversaciones
frecuentes entre desarrolladores, clientes y usuarios.

Las historias de usuario nos proporcionan una forma de tener escrito
sólo lo suficiente para que no olvidemos y para que podamos estimar y
planificar y al mismo tiempo promueven la conversación y la
comunicación directa.

Una historia de usuario describe una funcionalidad que será valiosa al
usuario final o al cliente que nos compra el software. 

## Definición de una historia ##

Una historia de usuario es una descripción rápida y sencilla de una
forma en la que un usuario utilizará el software. La mayoría de
historias de usuario se deben escribir entre una y cuatro
frases. Deben caber en una tarjeta de 3x5 pulgadas (_index card_).

<img src="diapositivas/historias-usuario.004.png" width="800px">

Un formato que se ha hecho popular a la hora de formular las historias
de usuario es:

- Título de la historia
- Descripción: Como un _&lt;tipo de usuario&gt;_, quiero _&lt;acción específica que estoy
  realizando&gt;_ para que _&lt;resultado que quiero que suceda&gt;_.

Ejemplo. Supongamos una web de venta de artículos usados (como Walapop):

- **Título**: Vistas de mi producto
- **Descripción**: como usuario que ha puesto un producto a la venta un
  producto quiero poder consultar quiénes lo han mirado para conocer
  cómo evoluciona el número de personas interesadas.

Muchas veces se puede omitir algún elemento si es obvio, o no está
elaborado. Por ejemplo, en una web para currículums (como InfoJobs):

- **Título**: Subir curriculum
- **Descripción**: Un usuario pude subir su currículum a la web de empleo.

Se cual sea el formato, es importante que la historia conteste a tres preguntas:

- Quién es el usuario que realiza la acción
- Qué quiere hacer el usuario
- Por qué lo quiere hacer

<img src="diapositivas/historias-usuario.005.png" width="800px">

Una historia de usuario está compuesta de tres aspectos:

- Una descripción escrita de la historia usada como un recordatorio
  para la planificación.
- Una conversación sobre la historia que sirve para desgranar los
  detalles de la misma.
- Prueba que contemplan y documentan los detalles y que pueden
  utilizarse para determinar cuando la historia está completa.

Las tarjetas "representan" requerimientos del cliente más que los
"documentan". Las tarjetas representan historias relacionadas con los
usuarios, no requisitos técnicos.

<img src="diapositivas/historias-usuario.006.png" width="800px">


Es importante conocer qué condiciones se deben cumplir para considerar
una historia terminada. Es lo que se denominan **condiciones de
satisfacción**, también denominadas **criterios de aceptación** o
**definición de Hecho** (_definition of Done_).

Se pueden escribir en la misma tarjeta, en su parte de detrás.

Estas condiciones son valiosas para el equipo de desarrollo, porque le
ayuda a evitar declarar la victoria demasiado pronto. Muchas veces el
equipo de desarrollo tiene la tendencia de implementar partes técnicas
de la funcionalidad, pero no proporcionar una historia de usuario
integrada por completo que se puede entregar.

Por ejemplo, para la historia de _Visitas de mi producto_, podríamos
definir las siguientes condiciones:

- Se debe poder conocer el número total de visitas que ha tenido mi
  producto. Y cuántas de ellas han sido en el último día.
- Se debe poder conocer la lista de todos los posibles compradores que
  han mirado el producto.
- Se debe poder conocer si un algún posible comprador ha visto el
  producto más de una vez.


<img src="diapositivas/historias-usuario.007.png" width="800px">

- Bill Wake: [INVEST in Good Stories](http://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)
- Bill Wake: [Small – Scalable – Stories in the INVEST Model](http://xp123.com/articles/small-scalable-stories-in-the-invest-model/)

<img src="diapositivas/historias-usuario.008.png" width="800px">

Si la historia es demasiado grande no puede ser estimada. Se llama
"épica" a una historia grande que debe subdividirse en historias más
pequeñas. Por ejemplo, en una web de una agencia de viajes "Un usuario
puede planear unas vacaciones" es una épica.

Una historia puede ser difícil de estimar porque:

- Historia compuesta
- Historia compleja

Ejemplo de historia compuesta: Web de empleo (estilo InfoJobs). Historia grande: "Un usuario
podrá subir su curriculum" se puede descomponer cuando se vaya a
desarrollar en:

- El curriculum puede incluir: formación, trabajos previos, historial
  de salario, publicaciones, presentaciones  y
  un objetivo.
- Los usuarios pueden tener múltiples curriculums.
- Los usuarios pueden marcar un curriculum como inactivo.
- Los usuarios pueden editar curriculums.
- Los usuarios pueden borrar curriculums.

Incluso se puede descomponer la primera historia en:

- Un usuario puede añadir y editar la información sobre formación previa.
- Un usuario puede añadir y editar la información sobre trabajos previos.
- Un usuario puede añadir y editar la información sobre el historial de salarios.
- Un usuario puede añadir y editar publicaciones.
- Un usuario puede añadir y editar presentaciones.
- Un usuario puede añadir y editar un objetivo.


Ejemplo de historia compleja: "Una empresa puede pagar con tarjeta de
crédito por una solicitud de empleo", suponiendo que nunca se ha
procesado ningún pago por tarjeta de crédito. Se puede dividir en:

- Investigar procesamiento de pagos con tarjeta de crédito.
- Un usuario puede pagar con una tarjeta de crédito.

El objetivo de la primera historia es desarrollar un _spike_, una
pequeña aplicación prototipo que sirva para probar la complejidad de
la historia. Se debe acotar su duración a como máximo una iteración. Y
colocar la historia de usuario de desarrollo en otra.

<img src="diapositivas/historias-usuario.009.png" width="800px">

<img src="diapositivas/historias-usuario.010.png" width="800px">

Es aconsejable utilizar **puntos** en lugar de horas para remarcar que
el tamaño es una forma de comparar la dificultad **relativa** de las
historias entre sí, independientemente de aspectos como la experiencia
del equipo de desarrollo.

- Opción 1: Tamaño: S, M, L, XL (puntos asociados: 1, 3, 5, 10)
- Opción 2: Escala Fibonacci: 1, 2, 3, 5, 8

Ejemplo: 

- Historia A: 10 puntos
    - Equipo 1 termina historia A en 2 días. Velocidad: 5 puntos/día.
    - Equipo 2 termina historia A en 1 día. Velocidad: 10 puntos/día.

- Historia B: 20 puntos
    - Equipo 1 (velocidad 5 puntos/día) la terminaría en 4 días
    - Equipo 2 (velocidad 10 puntos/día) la terminaría en 2 días

La velocidad del equipo puede cambiar conforme avanza el proyecto. El
tamaño de las historias, sin embargo, permanece constante.

<img src="diapositivas/historias-usuario.011.png" width="800px">

<img src="diapositivas/historias-usuario.012.png" width="800px">

[Web con productos de Atlassian](https://www.atlassian.com)

<img src="diapositivas/historias-usuario.013.png" width="800px">

<img src="diapositivas/historias-usuario.014.png" width="800px">

<img src="diapositivas/historias-usuario.015.png" width="800px">

<img src="diapositivas/historias-usuario.016.png" width="800px">

<img src="diapositivas/historias-usuario.017.png" width="800px">

<img src="diapositivas/historias-usuario.018.png" width="800px">

<img src="diapositivas/historias-usuario.019.png" width="800px">

<img src="diapositivas/historias-usuario.020.png" width="800px">

<img src="diapositivas/historias-usuario.021.png" width="800px">

- [The Purpose Of Storyboarding](https://www.youtube.com/watch?v=BSOJiSUI0z8)

<img src="diapositivas/historias-usuario.022.png" width="800px">

<img src="diapositivas/historias-usuario.023.png" width="800px">

- [Balsamic](https://balsamiq.com)

<img src="diapositivas/historias-usuario.024.png" width="800px">

<img src="diapositivas/historias-usuario.025.png" width="800px">

- Jeff Patton - [It's all in how you slice it](http://jpattonassociates.com/wp-content/uploads/2015/01/how_you_slice_it.pdf)

<img src="diapositivas/historias-usuario.026.png" width="800px">
