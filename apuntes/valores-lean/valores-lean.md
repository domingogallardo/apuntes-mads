# Valores _lean_ #


## Taylorismo ##

<img src="imagenes/henry-ford.png" width="200px"/>

<img src="imagenes/cadena-montaje.png" width="400px"/>

- Cadena de producción

- Henry Ford

Ejemplo típico de un proceso de fabricación: fabricación de automóviles

- En las fábricas de Henry Ford se desarrolla en EEUU en 1910 el
proceso de fabricación en cadena que permite acometer una producción
en gran escala:

    - Descomponer la fabricación en pequeños pasos especializados
    - El producto que se va construyendo se va moviendo de un proceso a otro (cadena que fluye)
    - Trabajadores fáciles de formar y de reemplazar: se especializan en hacer poco y hacerlo bien

- Problemas:
    - Falta de motivación de los trabajadores
    - Sistema muy útil para la fabricación en escala pero muy rígido:
      se tarda mucho en responder a los cambios que piden los
      consumidores
      
## El desarrollo de software como un proceso de fabricación ##

<img src="imagenes/proceso-fabricacion.png" width="500px"/>

- Fabricación de un producto
    - Entradas: materias primas y componentes
    - Salida: producto terminado (automóvil, teléfono móvil,
      televisor, etc.)
    - Proceso: diferentes máquinas y pasos en la cadena de montaje
- Si vemos el desarrollo software como un proceso iterativo podemos
  definir un proceso de desarrollo general: 
    - Entradas: software funcionando e ideas de nuevas características
      (features) en forma de casos de uso, historias de usuario, etc. 
    - Salida: software funcionando al que se le ha añadido las nuevas
	características. 
    - Proceso: cada característica debe ser analizada, desarrollada,
      probada, añadida y entregada. 
    - 2 ejes de calidad: elegir qué característica (right product) y
    desarrollar correctamente la característica (product right). 

- Cuando miramos el proceso de desarrollo de nuevas características
  como un proceso de fabricación, podemos aplicar al desarrollo de
  software muchas ideas aprendidas en los procesos de
  fabricación. Sobre todo las técnicas de fabricación lean. 


- El software es un **producto** muy distinto a los productos
  tradicionales: una aplicación no es una bicicleta, ni un televisor,
  ni un edificio. Tanto su desarrollo como su funcionamiento es
  singular.

- El proceso de desarrollo de software es un **proceso creativo** que
  tiene más elementos de **diseño** que de fabricación.
    - Los procesos de fabricación tradicionales son rígidos. En
      general los planos y características del objeto a producir están
      claramente determinados a priori y hay pocas decisiones que
      tomar.
    - En un proceso de diseño hay muchos **grados de libertad**, se
      deben escoger entre muchas posibles soluciones. El proceso
      intenta obtener la mejor opción, cumpliendo un conjunto de
      **restricciones** necesarias. Por ejemplo: el diseño de nuevo
      móvil, de un automóvil o de un mueble.

- Veremos que la filosofía _lean_ acerca ambos planteamientos: permite
  introducir **flexibilidad** en los procesos de fabricación tradicionales
  y un cierto **orden y método** en un proceso de diseño.


- Joel Spolsky (creador de _Stack Overflow_) explica en el artículo
  [Software
  Inventory](https://www.joelonsoftware.com/2012/07/09/software-inventory/)
  de su famoso blog [Joel on Software](https://www.joelonsoftware.com)
  la relación entre el desarrollo de software y un proceso de
  fabricación:
  
  Piensa en las **ideas** a añadir al producto como el **material
  bruto**. Dependiendo del proceso, estas ideas pueden pasar por
  distintos puntos de ensamblaje antes de ser entregadas como
  **_features_ terminadas** al cliente:
  
  - Proceso de toma de decisión (¿deberíamos implementar esta
    _feature_?)
  - Proceso de diseño (especificaciones, pizarras, mockups, etc.)
  - Proceso de implementación (escribir código)
  - Proceso de prueba (encontrar bugs)
  - Proceso de depuración (arreglar bugs)
  - Proceso de despliegue (enviar el código a los clientes, ponerlo en
    el servidor web, etc.)

<img src="imagenes/tablero-kanban-basico.png" width="400px"/>


## 1950: Sistema de producción de Toyota ##

<img src="imagenes/taiichi-ohno.png" width="300px"/>

<img src="imagenes/toyota-way.png" width="300px"/>

- Después de la Segunda Guerra Mundial, en el marco de un Japón
  empobrecido y sin apenas recursos, en la fabrica de automóviles
  Toyota Taiichi Ohno empezó a  desarrollar una filosofía de gestión y
  producción que a la postre terminaría aupando a Toyota (y al resto
  de fabricantes japoneses) a dominar la producción de automóviles,
  superando a los gigantes americanos Ford y General Motors.
  
- TPS [Toyota Production
  System](en.wikipedia.org/wiki/Toyota_Production_System), también
  denominado “producción just-in-time”

    - Eliminar los desperdicios (waste). 
    - Flujo de producción just-in-time, evitando gastos de
	inventario. Ciclos de producción cortos. 
    - Cultura de “parar la cadena” en el momento en que se detecta el mínimo error.
    - Cultura de mejora continua en todos los niveles: desde los trabajadores de la cadena hasta los directivos.
    - Pensar en el conjunto. Equipos multi-funcionales.
    - Herramientas para visualizar el proceso.
	- La esencia de TPS es una mentalidad (mindset) o cultura de
      empresa basada en la mejora continua y el desarrollo de las
      capacidades de los empleados y los colaboradores.
      
Comentarios:

- El objetivo de Ohno no era conseguir producción en masa. Su ideal
  era fabricar y entregar un producto inmediatamente después de que el
  cliente hubiera realizado un pedido. Pensaba que era mejor esperar
  un pedido que construir un inventario en anticipación del pedido.
    
- Uno de los elementos fundamentales del TPS (Toyota Production
  System) era identificar y eliminar "desperdicio" (waste) en todo el
  proceso de producción de un vehículo. El concepto de "desperdicio"
  (waste) es un concepto muy general: es todo aquello que no crea
  valor al cliente: piezas que no se usan, elementos innecesarios,
  transporte, movimiento, espera, procesamiento extra, defectos. 

- En 1945, bajo la dirección de Ohno, Toyota optimizó el ratio de
  producción de cada sistema, reconsiderando la posición de todas las
  máquinas de forma que la salida de una máquina alimentaba la
  siguiente. Se redujo la velocidad de las máquinas para que todas
  tuvieran la misma cadencia, y sólo se produjo material cuando era
  necesario. Después de optimizar las fábricas de Toyota, Ohno entrenó
  a los proveedores para que la producción completa de un vehículo
  fuera just-in-time, transformando la producción en masa en
  producción lean. El sistema pull resultante resultó ser fácil de
  reconfigurar, minimizó el inventario y permitió tiempos cortos de
  producción. 

- Toyota también usó el concepto de desperdicio no sólo para
  fabricación, sino también en el desarrollo del producto. Cuando se
  comienza un proceso de desarrollo, el objetivo es completarlo tan
  rápidamente como sea posible, porque todo el trabajo que va en
  desarrollo no está añadiendo valor hasta que el coche sale de la
  línea de producción. En cierto sentido, los proyectos de desarrollo
  en marcha son idénticos al inventario. Los diseños y los prototipos
  no son útiles a los clientes, reciben valor sólo cuando se entrega
  el nuevo producto. 

- Hay estudios que estiman que la aplicación de sistemas similares al
  TPS en empresas automovilísticas de Japón tiene como resultado una
  reducción a la mitad del esfuerzo de ingeniería y reduce en 1/3 el
  tiempo de desarrollo comparado con los enfoques tradicionales. 

- Una de las características es el desarrollo rápido y concurrente y
  la habilidad de realizar cambios tarde en el ciclo de desarrollo. No
  hay que hacer decisiones irreversibles en primer lugar, hay que
  retrasar las decisiones tanto como sea posible, manteniendo abiertas
  distintas opciones, y cuando se realicen, hacerlas con la mejor
  información posible.
  
## Sistemas de fabricación lean ##

<img src="lean-books.png" width="300px" align="right"/>

- Estas ideas dan origen a los denominados sistemas de fabricación
  lean (lean = austero, flaco) 
    - El proceso siempre puede ser mejorado y los trabajadores son los
      que mejor pueden proponer estas mejores.
    - Método científico: los trabajadores aprenden a crear hipótesis,
      probarlas, analizar los resultados y, si los datos confirman la
      hipótesis, hacer el cambio permanente. 

    - Identificar los distintos pasos del proceso de producción (el
      value stream) cadena de valor del proceso. 

    - Una idea central es la continua búsqueda y eliminación de los
      desperdicios (waste) generados por el proceso. Simplificar. 

    - Cuando se eliminan los desperdicios la calidad mejora, y el
      tiempo de producción y los costes se reducen y la producción se
      vuelve fluida (flow). 

    - Consecuencias: alta disciplina y alta respuesta al cambio. 

    - Es una mentalidad (mindset), no un conjunto prescrito de
      reglas. 

- El término lean se ha popularizado: lean startups, lean thinking 

## Value Stream Map ##

<img src="imagenes/value-stream.png" width="700px"/>

- Avanzamos un ejemplo de aplicación de una de estas técnicas al
  desarrollo de software. El **value stream map** (**mapa de flujo de
  valor**) consiste en analizar todas las fases por las que pasa una
  funcionalidad, característica, historia de usuario, tarea,
  etc. desde que se decide desarrollar hasta que se sube a
  producción. Dibujar una caja por cada uno de los pasos y estudiar el
  tiempo de trabajo y tiempo de espera en cada una de las fases. Es
  recomendable hacerlo con características reales, una vez terminadas.

- En el ejemplo anterior las fases serían: (1) crear el documento de requerimiento, (2)
  dividir en tareas y estimar, (3) documento de planificación, (4)
  revisión del plan y obtener visto bueno, (5) desarrollar software,
  (6) pruebas del software, (7) validación del alcance, (8) despliegue.

- Cada empresa, dependiendo de la metodología de desarrollo que use,
  tiene un mapa de flujo de valor distinto. Es una herramienta
  importante para diseñar los tableros kanban.
  
- El enfoque _lean_ consiste en identificar y eliminar _waste_ en el
  _value stream_. Debemos identificar tres tipos de actividades:
  actividades que claramente crean valor; actividades que no crean
  valor para el cliente pero que son necesarias en la actualidad para
  fabricar el producto; y actividades que no crean valor para el
  cliente, son innecesarias y, por lo tanto, deberían ser eliminadas
  inmediatamente (_waste_).

- Un problema importante en el caso del software es la identificación
  de las tareas que van a pasar por el _value stream_. ¿Qué unidades
  son las que hay que analizar? ¿Historias de usuario? ¿Tareas
  técnicas más pequeñas en las que se descomponen las historias de
  usuario?. La recomendación es que sean elementos que no tengan mucha
  variabilidad de tamaño. Un concepto que se suele usar es el de
  **minimal marketable feature** (MMF): el "trozo" más pequeño de
  funcionalidad del producto que los clientes (o el _product owner_)
  puede priorizar. Suelen tomar forma de una historia de usuario, un
  requerimiento o una petición de funcionalidad. En el caso de Scrum,
  son los ítems del backlog.


## Buscar y eliminar desperdicios ##

- Todo aquellos elementos que no añaden valor al producto. Si
  minimizamos los desperdicios maximizaremos la cantidad de trabajo
  útil, que realmente da valor. 

- Ejemplos de desperdicios en procesos de fabricación y servicios: 
    - Espera: personas o hitos del proceso esperando que termine otro
      proceso o que llegue cierta información 
    - Movimiento: movimiento físico o mental que no añade valor
    - Inventario: almacenar servicios y componentes extra que el
      cliente no ha pedido 
    - Defectos: errores que hay que corregir 
    - Sobre-procesamiento: excesiva documentación, informes excesivos,
      partes no necesarias
      
      
En el artículo anteriormente mencionado de Joel Spolsky se mencionan
tres tipos de inventario que se pueden encontrar en el desarrollo de
software que deben minimizarse:

- **Backlog de _features_**: el 90% de las _features_ en el backlog no
  llega a implementarse. **Solución**: limitar el backlog a 1 o 2
  meses. Una vez que esté lleno no se introducirán nuevos ítems si no
  se quita alguno.
- **Base de datos de bugs**: algunas empresas mantienen bases de datos
  con cientos de bugs que nunca llegan a corregirse. **Solución**:
  implementar un sistema de triaje que indique si un bug debe
  corregirse o marcarse como cerrado. No hay que preocuparse en
  equivocarse, los bugs importantes reaparecerán.
- **_Features_ no desplegadas**: _features_ implementadas pero puestas
  en producción por ser el proceso de despliegue muy
  lento. **Solución**: mejorar el proceso de despliegue con
  integración continua.

## Sistemas de fabricación Pull ##

<imt src="imagenes/sistema-pull.png" width="400px"/>

- Uno de los pilares de la fabricación lean.
- El proceso de fabricación se divide en un conjunto de  pasos
  (celdas) que necesitan recursos y consumen los  resultados de
  procesos anteriores (upstream).
- Sistema push: se planifica a priori la cantidad de trabajo  a
  comenzar. Cuando un proceso upstream produce un  componente se
  empuja (push) a la siguiente celda para  que continue
  procesándolo. Muchas veces se provoca  sobrecarga en las celdas.
- Sistema pull: el origen del flujo de trabajo está al final de la
  cadena, al entregar el producto final a los clientes. Cada celda
  tiene un número máximo de productos (WIP), cuando se consume uno se
  envía una señal (pull signal) a la celda anterior de que se necesita
  recibir un nuevo componente.
- El flujo de trabajo se regula tirando (pull) de los materiales a
  transformar con una cadencia constante.
- Un sistema pull regula el flujo de los recursos mediante un proceso
  de fabricación reemplazando solo lo que ha sido consumido y lo que
  es inmediatamente entregable.
  
- WIP: **Work In Process**, es un término lean que indica el número de
  ítems que están siendo procesados en una determinada celda o fase
  del proceso. En Kanban veremos que para cada una de las fases del
  proceso se define un límite en el WIP, que obliga a no aceptar más
  ítems una vez que se ha llegado al WIP. Cuando algún ítem termine el
  proceso y pase a la fase siguiente, se vuelve a coger un ítem
  nuevo. Pero nunca estaremos procesando más ítems que los definidos
  por el WIP.

- El flujo de trabajo pull, junto con el WIP, garantiza que no se
  produce sobre inventario y permite **detectar** fácilmente **cuellos
  de botella** en el proceso, procesos que consumen demasiado tiempo y
  que obligan a esperas e impiden una cadencia fluida (flujo,
  **flow**). Una fase que tarda demasiado en procesar los ítems hace
  que las fases previas se queden paradas, esperando, porque no pueden
  sobrepasar su WIP. En un sistema push esas fases seguirían
  procesando ítems, que se acumularían.

- El flujo pull y el mapa de flujo de valor permiten **analizar y
  reflexionar** sobre el proceso de producción.

- Una visualización en
  [YouTube](https://www.youtube.com/watch?v=ZIv2e61SH1A) de los
  sitemas pull.

## Kanban ##

<img src="imagenes/informacion-visual.png" width="400px"/>

- Una de las herramientas más  importantes para organizar el
  proceso de producción son las kanban (del  japonés, kan=visual y ban
  = tablero o tarjeta), señales visuales que  implementan el sistema
  pull.

- Enfoque visual para el control de  la producción, usando
  herramientas  sencillas como contenedores retornables,  tarjetas o
  incluso espacios vacíos para “tirar” de los productos desde  los
  centros de producción hacia los centros de consumo o transformación.

- Una kanban es una señal o ayuda visual que indica que un centro de
  trabajo ha finalizado un proceso, necesita trabajo o necesita más
  materiales.

- Los tableros kanban permiten que los centros de trabajo hagan un
  seguimiento de las necesidades de los clientes o de los proveedores
  y que respondan rápida y adecuadamente.

- Ejemplos de tableros Kanban en el desarrollo de software:

<img src="imagenes/tableros-kanban.png" width="700px"/>
