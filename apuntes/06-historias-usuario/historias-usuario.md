# Historias de usuario #


#### Práctica: Stories ####

Los elementos que debemos usar para planificar el trabajo son pequeños
"trozos" de funcionalidad visible por el cliente. Beck denomina estos
pequeños trozos "historias". Después se utilizará el término "historias
de usuario" (_user stories_). Una vez que se escribe la historia, se
debe intentar estimar el esfuerzo necesario para implementarla, que se
anota en un esquina:

<img src="imagenes/story.png" width="250px"/>

Beck no define un formato para escribir las historias, aunque después
se haría popular el estilo "Como (rol), quiero (acción) para conseguir
(objetivo)":

<img src="imagenes/user-story-card.png" width="400px"/>

Cada equipo tiene un estilo de escribir las historias. No hay que ser
demasiado estricto con la idea de usar un formato concreto. A veces la
historia encaja bien en el formato estándar, pero otras no. Si tienes
que darle demasiadas vueltas a cómo formular tu historia con un
formato, no lo uses.

Lo importante es que la descripción de la historia sea corta y que en
ella se especifique alguna funcionalidad visible por el
cliente. También debe tener un título y una estimación del tiempo que
se va a usar para terminarla.

Es más adecuado hablar de “historias” que de “requisitos” (palabra
con connotaciones de “inmutabilidad” y “permanencia” que no son
compatibles con “abrazar el cambio”).

Una vez escritas las historias, las podremos colocar en la pared,
agrupar, seleccionar, hablar sobre ellas, moverlas, etc.

##### Conversation, Card, Confirmation #####

<img src="imagenes/tres-cs.png" width="400px"/>

Jon Jeffries amplía las características de las historias para
responder a las críticas relacionadas con la falta de
concreción, definiendo lo que se conoce como las tres Cs:

- Conversation
- Card
- Confirmation

Las historias son un texto corto escrito en una tarjeta que se
refiere a una conversación con los clientes sobre la funcionalidad
que se quiere incluir y que debe tener una lista larga de criterios de
aceptación en los que se especifican de forma más concreta sus
detalles. Estos criterios de aceptación estarán documentados aparte,
no en la misma tarjeta.

##### Lenguaje del dominio #####

Es muy importante usar en las tarjetas un lenguaje y un vocabulario
propio de los clientes y del negocio o dominio que estamos
programando. Es parte de nuestro trabajo conseguir que ese vocabulario
sea preciso y corregir las posibles ambigüedades que pudiera
contener. Cuando escribimos código y tests debemos usar el mismo
vocabulario que el usado por los clientes, de forma que sea posible
entender el programa en términos lo más cercanos posibles al modelo de
negocio.

Por ejemplo, para realizar la asignación de presencialidad a los
estudiantes de una universidad (debido a restricciones de ocupación en
las aulas por, por ejemplo, estar la universidad en una zona en la que
se sufre una pandemia), hay que distinguir entre "grupos", "turnos" y
"actividades". Una asignatura tiene varias actividades: por ejemplo,
teoría y práctica. Cada actividad se divide en grupos de estudiantes
que comparten aula y horario. Y cada grupo se divide en turnos:
presencial y on-line. Estos términos ("grupos", "turnos" y
"actividad") son precisos y es posible utilizarlos para definir reglas
y especificaciones. Pero lo habitual es que no haya sido sencillo
llegar a ellos y que sólo se hayan obtenido después de muchas
confusiones y malentendidos (por ejemplo, hablar de "grupos" cuando
queremos decir "actividad" o "turno").

Es muy importante hacer este esfuerzo de precisión con el lenguaje,
porque ayuda mucho a la hora de especificar las funcionalidades y
también de desarrollar y entender el código de la aplicación.

Existe toda una metodología de diseño que se basa en esta idea. Se
denomina [_Domain Driven
Design_](https://martinfowler.com/bliki/DomainDrivenDesign.html) y
hablaremos de ella más adelante.

##### INVEST #####

El acrónimo INVEST fue creado por [Bill
Wake](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)
para definir seis atributos que debe tener una buena historia de usuario:

- **I**ndependiente: las dependencias entre las historias crean
  problemas de priorización y estimación. 
- **N**egociable: las historias no son contratos, son recordatorios de conversaciones.
- **V**aliosa: las historias deben ser valiosas para los que pagan el software.
- **E**stimable: el tamaño de la historia debe poder ser estimado,
  aunque sea de forma gruesa.
- **S**mall: para poder estimarse correctamente es recomendable que
  la historia sea pequeña. Si la historia es demasiado grande (lo que
  se denomina una épica) hay que refinarla y dividirla en historias
  más pequeñas.
- **T**estable: las historias deben ser probadas y los tests deben poder ser
automatizados.

