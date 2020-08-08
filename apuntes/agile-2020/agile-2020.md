
# El estado de Agile en 2020 #

En este apartado haremos un breve repaso al informe sobre el estado de
Agile en 2020 realizado por la consultora digital.ai, comentaremos
algunos problemas en la puesta en práctica de metodologías ágiles y
terminaremos con una crítica a la visión reduccionista de que Agile es
igual a Scrum.

## State of Agile Report ##

<img src="imagenes/state-of-agile-report.png" width="150" align="right"></img>

El informe [_State of Agile_](https://stateofagile.com/) se realiza
anualmente desde hace 14 años por la consultora
[digital.ai](https://digital.ai). En los informes se recogen los
resultados de encuestas contestadas por profesionales de empresas
tecnológicas sobre la aplicación de metodologías ágiles en su
funcionamiento.

Hay que tomar el informe con cierta precaución, porque no se hace un
muestreo general a todas las empresas tecnológicas, sino que se recoge
la información entregada de forma voluntaria por profesionales que
están interesados en compartir su información. Por eso el informe
estará lógicamente sesgado hacia empresas que tienen una disposición
favorable a la aplicación de estas metodologías. Aún así, el informe
es muy interesante porque nos proporciona muchos detalles sobre cómo
se ponen en práctica estas metodologías en las empresas.

El último informe, el número 14 correspondiente a 2020, recoge la
información de una encuesta realizada a más de 40.000 personas de
empresas de todo el mundo y de todos los tamaños. 

#### Tamaño de las empresas ####

Empresas con equipos de software que van desde menos de 100 personas
(un 33%) hasta más de 5.000 personas (un 15%).

<img src="imagenes/demografia-state-of-agile.png" width="500px"></img>

Para que os hagáis una idea de lo que representan estas cifras del
tamaño de los departamentos de software, podríamos compararlas con la
Universidad de Alicante. La universidad tiene alrededor de 25.000
estudiantes y más de 3.500 trabajadores, entre profesores y personal
de administración. El tamaño del Servicio de Informática de la
universidad es de unas 100 personas. O sea, que cuando en el informe
se dice que un 36% de las empresas encuestadas tienen equipos de
desarrollo de entre 100 y 1.000 personas estamos hablando de equipos
del tamaño del de la UA, o 10 veces mayores. La UA estaría en el
primer rango del 33%.

#### Puesto de trabajo ####

<img src="imagenes/state-agile-role.png" width="400px"></img>

En cuanto al puesto de los que han respondido la encuesta, la gran
mayoría (casi el 40%) son _Scrum Masters_ o _Agile Coach_. Sólo un 7%
de los que han respondido la encuesta son miembros de los equipos de
desarrollo. Esto también puede representar un sesgo importante, que
también puede explicar la gran relevancia de Scrum en gráficos
posteriores.

#### Objetivos por los que se adoptan las metodologías ágiles ####

A los encuestados se les preguntaba por los objetivos que se pretenden
al adoptar metodologías ágiles. Podían responder más de una opción. 

<img src="imagenes/reasons-state-of-agile.png" width="400px"></img>

El objetivo principal de más del 70% de los que respondieron es
"Acelerar la entrega de software". Le sigue "Mejorar la posibilidad de
gestionar prioridades cambiantes" (63%) y "Mejorar la productividad"
(51%). Son objetivos muy relacionados con ser más eficientes en el
desarrollo de software y tener más capacidad de cambiar
prioridades. De forma indirecta esto nos indica un descontento con la
velocidad actual y la rigidez de desarrollo. Los encuestados perciben
que se tarda demasiado en que el software llegue a manos de los
usuarios finales y que es muy difícil de introducir cambios en los proyectos.

Es curioso que el último punto, al que menos importancia se le da, sea
el de "Mejorar la mantenibilidad del software" (18%). Quizás es debido
a que el concepto de "mantenibilidad" del software tiene connotaciones
demasiado tradicionales entre los encuestados, que lo asocian a
corregir bugs en software de poca calidad. Sin embargo, sí que se da
bastante importancia a mejorar la calidad del software (42%). 

Parece claro que el objetivo de los encuestados es conseguir que se
desarrolle software de calidad, que se entregue rápido y que sea fácil
de modificar y transformarse según las necesidades del negocio. Es un
objetivo bastante cercano a lo que pretenden las metodologías ágiles.

#### Indicadores para medir el grado de éxito  ####

<img src="imagenes/medicion-exito-state-of-agile.png" width="500px"></img>

En cuanto a la forma de medir el éxito en la aplicación de las
metodologías ágiles en proyectos, la encuesta muestra que se definen
muchas métricas distintas, desde el valor de negocio entregado (46%)
hasta número de horas individuales por iteración y por semana (8%),
pasando por conceptos de Kanban como WIP (_Work in Progress_) (20%) o
relacionados con el cumplimiento de la planificación como el número de
historias por iteración real vs. previstas (31%) o las fechas de
release previstas vs. reales (28%). También se incluyen medidas
relacionadas con la calidad del software como el número de defectos en
producción (26%), defectos a lo largo del tiempo (20%) o resolución de
defectos (15%). Las medidas más usadas son las relacionadas con el
valor entregado al cliente (46%) y su satisfacción (45%), así como la
velocidad del desarrollo (37%).

Es interesante comprobar que el abanico de indicadores es muy amplio y
que no hay un consenso claro en los que se usan. Hay indicadores más
alineados con las ideas ágiles, como son los relacionados con la
satisfacción del cliente y el valor entregado y otros más relacionados
con métodos clásicos de planificación de proyectos no tan ágiles, como
los que hacen énfasis en la precisión de la planificación. Uno de los
objetivos principales de las metodologías ágiles es entregar valor
al cliente en forma de software que funciona. Podemos hacer una
planificación perfecta del número de historias entregadas y de las
fechas de entrega, pero resultar que el software entregado no consigue
satisfacer los objetivos del cliente. No estaremos siendo ágiles en
ese caso.

<table markdown="1">
<tr><td style="background-color: #e0e0e0">

**La importancia de medir**

Hay una frase popular que se atribuye al científico Lord Kelvin y dice
que:

> "Lo que no se puede medir no se puede mejorar."

Esta claro que es importante poder medir algo para poder observar cómo
evoluciona. Si queremos evaluar la consecución de unos objetivos
deberemos cuantificarlos, por lo que lo primero que deberemos definir
es un conjunto de indicadores medibles (métricas) relacionados con
esos objetivos. El problema aparece cuando lo que se quiere medir es
algo difuso, poco definido, que está relacionado con múltiples
variables fuertemente interrelacionadas. La búsqueda de indicadores
adecuados se convierte entonces en un problema a investigar.

En el mundo de los negocios está muy generalizado el uso de
indicadores o métricas que permiten decidir si se está realizando un
buen desempeño o no. Un ejemplo son los denominados [KPIs](https://en.wikipedia.org/wiki/Performance_indicator) (_Key
Performance Indicator_), indicadores relacionados con las distintas
áreas de desempeño de una empresa (fabricación, marketing y ventas,
servicios, etc.).

Las empresas de tecnología han desarrollado versiones propias de esta
idea. Por ejemplo, empresas como Google, Intel o Twitter utilzan los
populares [OKRs](https://en.wikipedia.org/wiki/OKR) (_Objectives and
Key Results_). Un OKR contiene un objetivo claramente definido y un
conjunto de 3-5 resultados clave medibles que nos permiten hacer un
seguimiento del alcance de ese objetivo.

Como hemos comentado anteriormente es fundamental definir los
indicadores adecuados a lo que queremos medir. Por ejemplo, seguro que
conoces métricas usadas habitualmente para medir la calidad del
código. Por ejemplo el número de tests, el cubrimiento del código, el
número de _code smells_ o los bugs/duplicaciones/vulnerabilidades en
el tiempo. Si quisiéramos medir cómo evoluciona la deuda técnica en el
software que estamos desarrollando podrían ser buenos
indicadores. Pero si lo que quisiéramos es comprobar si estamos
entregando valor al cliente, no son los indicadores más
apropiados. Podemos estar construyendo correctamente un producto
incorrecto y no darnos cuenta.

Siempre que midamos la evolución del rendimiento usando indicadores
hay que tener cuidado con lo que en _Machine Learning_ se denomina el
problema del _overfitting_ o sobreajuste. En el caso de las redes
neuronales aparece este problema cuando las redes optimizan demasiado
el aprendizaje del conjunto inicial de muestras y no son capaces de
generalizar y clasificar correctamente nuevas muestras no vistas
previamente. 

En la medición del rendimiento del equipo podría darse el caso de que
los indicadores que el equipo maximiza funcionaran como incentivos que
estuvieran erosionando algún otro aspecto del equipo que terminara
haciendo que el equipo dejara de funcionar bien. Por ejemplo, si se
valorara el número de líneas escritas por el equipo, podría darse el
caso de que alguna persona que está haciendo un papel muy bueno
analizando la utilidad de nuevas funcionalidades y aportando ideas
valiosas al producto dejara de hacerlo para producir más código (que
podría aportar menos valor).

Hay que pensar que el equipo está formado por personas y que, como
dice el manifiesto ágil, las personas y la comunicación están por
encima de los procesos.

</td></tr></table>


### Agile es más que Scrum  ###

- Sacar alguna idea de la charla sobre la palabra "Agile" de Kevlin
  Henney Agile not = Speed (https://youtu.be/kmFcNyZrUNM)
- Revisar el artículo de Martín Pérez sobre equipos de alto
  rendimiento: https://dev.to/mpermar/measuring-high-performance-engineering-teams-from-a-value-perspective-46mo


## Referencias ##

- [“The State of Agile 2020”](https://explore.digital.ai/state-of-agile/14th-annual-state-of-agile-report) 
- Charla de Martin Fowler: _The State of Agile Software in 2018_
  [transcripción](https://martinfowler.com/articles/agile-aus-2018.html)
      y [vídeo](https://www.infoq.com/presentations/agile-2018).
- Andrea Janes, Giancarlo Succi: [_The dark side of agile software development_](https://www.researchgate.net/publication/266652972_The_dark_side_of_agile_software_development)
