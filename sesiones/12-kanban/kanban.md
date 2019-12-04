
## Kanban

<kbd><img src="diapositivas/kanban.001.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.002.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.003.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.004.png" width="800px"></kbd>

- Kanban es un método para **mejorar los procesos** usados por los
  equipos ágiles. Los equipos que usan Kanban empiezan analizando y
  comprendiendo la forma que utilizan para construir el software, y lo
  utilizan para mejorar este proceso.
  
- Kanban nos ayuda a ir cambiando el prisma de ¿Qué hacen las
  personas? a **¿Cómo va el trabajo?**. En la línea de los valores
  ágiles, Kanban refuerza los valores de **Colaboración** y **Respeto**.

- El objetivo de Kanban es conseguir pequeñas mejoras en el proceso de
  desarrollo, empezando por el sistema que actualmente usa el equipo y
  persiguiendo **cambios evolutivos** obtenidos colaborativamente a
  través de experimentos.

- Kanban utiliza elementos de la **metodología _lean_**, como el _lead
  time_ (tiempo de terminación) o el flujo para medir el
  funcionamiento del equipo. 

<kbd><img src="diapositivas/kanban.005.png" width="800px"></kbd>

- El equipo de la izquierda está estresado; no tienen claras las
  prioridades. Nadie está seguro de en qué están trabajando los
  compañeros y las tareas se acumulan.

- El equipo de la derecha ha mejorado significativamente el tiempo de
  puesta en producción de las nuevas características y existe un
  funcionamiento común entre marketing, negocio y operaciones.

<kbd><img src="diapositivas/kanban.006.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.007.png" width="800px"></kbd>

- El tablero Kanban sirve para representar las distintas **fases del
  proceso** por las que deben de pasar los **ítems de trabajo**. Puede
  haber filas opcionales para distintos tipos de trabajos. Las
  tarjetas del tablero representan los ítems de trabajo.

- Un **ítem de trabajo** representa una parte del trabajo que debe
  terminarse. En la aplicación de Kanban a equipos de desarrollo puede
  representar:
    - Una funcionalidad (historia de usuario) a desarrollar.
    - Un conjunto de líneas de código a incorporar en el proyecto
      mediante un _pull request_.
    - Un diseño gráfico a realizar.

- El tablero Kanban indica en qué lugar del proceso está cada ítem de
  trabajo en el contexto de las demás. Permite al equipo identificar
  colas, **cuellos de botella** e incluso falta de carga de trabajo,
  promoviendo la colaboración. Busca hacer visible lo invisible.

    - Cuando algo se hace visible es más fácil identificar un problema
      y conseguir una solución. Esto se acentúa en equipos con
      distintas especialidades, donde cada uno tiene una idea distinta
      de las dependencias y los riesgos.

    - Los ítems de trabajo **se mueven** por las columnas del tablero
      Kanban indicando el cambio de su estado.

- El tablero **se actualiza en tiempo real** por los miembros del
  equipo. Los cuellos de botella se identifican en reuniones diarias.

- Al limitar el trabajo en proceso (WIP, _Work In Progress_) la gente
se centra en **terminar cosas**, en lugar de empezar muchas cosas o
comprometerse a demasiado trabajo a la vez.

- Se siguen **reglas explícitas** para mover una tarjeta. Esto obliga a
  discutir y acordar las **políticas del proceso**.

<kbd><img src="diapositivas/kanban.008.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.009.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.010.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.011.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.012.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.013.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.014.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.015.png" width="800px"></kbd>

- [One day in Kanban land](http://blog.crisp.se/2009/06/26/henrikkniberg/1246053060000)

<kbd><img src="diapositivas/kanban.016.png" width="800px"></kbd>

- Veamos un ejemplo de cómo cambian de estado los ítems de trabajo
  respetando el límite de WIP de cada columna. Cuando una columna ha
  llegado a su límite de WIP **no es posible mover a ella ningún ítem
  más**.
  
  - Si hay ítems terminados en la columna anterior a otra que tiene
    cubierto su WIP esos ítems se quedan en espera en la columna
    anterior. Es habitual indicarlo creando una subcolumna que hará de
    _buffer_ en el que se acumularán los ítems en espera. **El número
    de ítems en el buffer también cuenta para el límite de WIP**.


<kbd><img src="diapositivas/kanban.017.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.018.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.019.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.020.png" width="800px"></kbd>

- Después de un tiempo con los ítems `B` y `C` en _Develop_ no se
  puede pasar el ítem `D` a esa columna porque se sobrepasaría su
  límite de WIP.

<kbd><img src="diapositivas/kanban.021.png" width="800px"></kbd>

- En la columna _Deploy_ se ha encontrado un problema en el ítem
  `A`. Mientras, en la columna _Develop_ se ha terminado el ítem
  `B`. No se puede pasar a _Deploy_ porque se rebasaría su límite de
  WIP de 1. Se deja en la columna _Develop_, pero en la subcolumna
  _Done_ que hace de _buffer_ para los ítems terminados que no pueden
  pasar a la siguiente columna.

<kbd><img src="diapositivas/kanban.022.png" width="800px"></kbd>

- El equipo de desarrollo no puede coger el ítem `D` porque
  sobrepasaría el límite de WIP de la columna. El problema del
  despliegue de `A` está creando un cuello de botella que obliga a que
  todos sean conscientes del problema.

<kbd><img src="diapositivas/kanban.023.png" width="800px"></kbd>

- Los desarrolladores que estaban con `B` echan una mano a los que
  están desplegando `A`. El problema de `A` se ha hecho visible y en
  el futuro los desarrolladores tendrán más cuidado en pasar a
  _Deploy_ ítems mal terminados.

- El _Product Owner_ ha seleccionado el ítem `K` y se ha alcanzado el
  límite de WIP de la columna _Selected_.

<kbd><img src="diapositivas/kanban.024.png" width="800px"></kbd>

- Se termina el desarrollo de `C`, pero se sigue sin poder comenzar
  ningún otro ítem porque el problema de `A` sigue sin resolverse.

<kbd><img src="diapositivas/kanban.025.png" width="800px"></kbd>

- El bloqueo producido por el ítem `A` llega a todo el equipo. Se
  generan conversaciones sobre el problema y que sirven para
  incorporar nuevas políticas.

<kbd><img src="diapositivas/kanban.026.png" width="800px"></kbd>

- ¡Hasta el PO quiere ayudar a desplegar!

<kbd><img src="diapositivas/kanban.027.png" width="800px"></kbd>

- La nueva política ayudan a que todo vaya más fluido.
- Se ha aumentado el límite de WIP de desarrollo a 3.

<kbd><img src="diapositivas/kanban.028.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.029.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.030.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.031.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.032.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.033.png" width="800px"></kbd>

- Es muy importante definir correctamente el **alcance** del tablero y
  la **granularidad** y el **estado** de los ítems de trabajo.
    - Si el alcance del tablero es demasiado grande, los ítems de
      trabajo son demasiado pequeños o sus estados son demasiado
      cortos en tiempo tendremos un tablero tan ocupado y que tiene
      que actualizarse tan frecuentemente que no será práctico.
    - Por el contrario, si el tablero tiene un alcance muy estrecho y
      sólo trata con ítems grandes cuyo estado cambia muy lentamente,
      tampoco será útil por no mostrar los elementos necesarios.


<kbd><img src="diapositivas/kanban.034.png" width="800px"></kbd>

- [Kanban – the next step in the agile evolution?](https://ketiljensen.wordpress.com/2009/10/31/kanban-the-next-step-in-the-agile-evolution/)

<kbd><img src="diapositivas/kanban.035.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.036.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.037.png" width="800px"></kbd>

- [10 kanban boards and their context](http://blog.crisp.se/2011/12/05/mattiasskarin/10-kanban-boards-and-their-context-version-1-2?xt-version-1-2)

<kbd><img src="diapositivas/kanban.038.png" width="800px"></kbd>

- Es posible trabajar con varios tableros orientados a distintas
  audiencias: un tablero para el desarrollo y otro para el Product
  Owner y la empresa. El primero podría tendría como ítems de trabajo las
  tareas en desarrollo del equipo. El segundo funcionalidades o
  historias de usuario.

<kbd><img src="diapositivas/kanban.039.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.040.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.041.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.042.png" width="800px"></kbd>

- [Lean from the trenches](https://www.crisp.se/file-uploads/Lean-from-the-trenches.pdf)

<kbd><img src="diapositivas/kanban.043.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.044.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.045.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.046.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.047.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.048.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.049.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.050.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.051.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.052.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.053.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.054.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.055.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.056.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.057.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.058.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.059.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.060.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.061.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.062.png" width="800px"></kbd>

<kbd><img src="diapositivas/kanban.063.png" width="800px"></kbd>

- Marcus Hammarberg, Joakim Sunden - Kanban in Action ([eBook Biblioteca UA](http://proquest.safaribooksonline.com/9781617291050?tocview=true))
- Henrik Kniberg - [Kanban and Scrum](https://www.infoq.com/minibooks/kanban-scrum-minibook)
- Mike Burrows - [Kanban from the inside](https://www.amazon.com/Kanban-Inside-Understand-connect-introduce/dp/0985305193)
- David J. Anderson - Kanban ([Catálogo UA](http://gaudi.ua.es/uhtbin/cgisirsi/x/0/0/5/?searchdata1=(OCoLC)865158880))
