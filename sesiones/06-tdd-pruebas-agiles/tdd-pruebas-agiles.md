
## TDD y pruebas ágiles

<kbd><img src="diapositivas/tdd-pruebas-agiles.001.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.002.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.003.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.004.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.005.png" width="800px"></kbd>

- [JUnit.org](http://junit.org/junit4/)

<kbd><img src="diapositivas/tdd-pruebas-agiles.006.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.007.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.008.png" width="800px"></kbd>

- [Twitter](https://twitter.com/mfeathers) de Michael Feathers
- [Working Effectively with Legacy Code](https://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052)
- [Mockito](https://github.com/mockito/mockito)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock)
- [Sinon.JS](http://sinonjs.org)

<kbd><img src="diapositivas/tdd-pruebas-agiles.009.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.010.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.011.png" width="800px"></kbd>

La pirámide de la automatización de tests es una figura muy usada que
indica los porcentajes de la cantidad de tests que debe haber en un
proyecto. 

La base de la pirámide (el mayor porcentaje de tests) debe estar
formada por tests unitarios. Además de constituir el mayor número de
tests del proyecto, son ejecutados muchas más veces y su mantenimiento
es mayor, ya que en general son realizados y probados por los propios
desarrolladores en sus equipos.

Sobre ellos se construyen los tests de integración o tests a nivel de
API. Son menos que los tests unitarios, prueban funcionalidades de
mayor nivel y normalmente se ejecutan sólo en el servidor de
integración continua.

Sobre los tests de integración se construyen también tests automáticos
de los aspectos de interfaz de usuario. Son menos cantidad que los
tests de integración, pero también son automáticos.

Y, por último, se realizan una cantidad pequeña (en proporción a los
anteriores) de tests manuales no automatizados.

<kbd><img src="diapositivas/tdd-pruebas-agiles.012.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.013.png" width="800px"></kbd>

- [Test-Driven Development by Example](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530)
- [Growing Object-Oriented Software, Guided by Tests](http://www.growing-object-oriented-software.com)

<kbd><img src="diapositivas/tdd-pruebas-agiles.014.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.015.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.016.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.017.png" width="800px"></kbd>

- [The Three Rules of TDD](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd)

<kbd><img src="diapositivas/tdd-pruebas-agiles.018.png" width="800px"></kbd>

- [Classic TDD or "London School"?](http://codemanship.co.uk/parlezuml/blog/?postid=987)
- [Mocks Aren't Stubs](http://martinfowler.com/articles/mocksArentStubs.html)

<kbd><img src="diapositivas/tdd-pruebas-agiles.019.png" width="800px"></kbd>


<kbd><img src="diapositivas/tdd-pruebas-agiles.020.png" width="800px"></kbd>


- [Refactoring: Improving the Design of Existing Code](https://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672)

<kbd><img src="diapositivas/tdd-pruebas-agiles.021.png" width="800px"></kbd>


<kbd><img src="diapositivas/tdd-pruebas-agiles.022.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.023.png" width="800px"></kbd>

- En [este enlace](./kata-arabigos-a-romanos.md) se encuentra la transcripción de la kata.

<kbd><img src="diapositivas/tdd-pruebas-agiles.024.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.025.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.026.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.027.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.028.png" width="800px"></kbd>

<kbd><img src="diapositivas/tdd-pruebas-agiles.029.png" width="800px"></kbd>

- [Continuous integration at CartoDB](https://www.slideshare.net/juanignaciosl/continuous-integration-at-cartodb-march-16)

<kbd><img src="diapositivas/tdd-pruebas-agiles.030.png" width="800px"></kbd>

- James Shore - The Art of Agile Development [Capítulo Test-Driven
  Develpment](http://www.jamesshore.com/Agile-Book/test_driven_development.html)
- Polémica TDD is dead
  - [Artículo
    inicial](http://david.heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.html)
    de David Heinemeier Hansson, autor del framework [Ruby On Rails](http://rubyonrails.org)
  - [Nota sarcástica](https://www.facebook.com/notes/kent-beck/rip-tdd/750840194948847) de Kent Beck
  - [Is TDD dead?](https://martinfowler.com/articles/is-tdd-dead/)
    Hangouts sobre el tema entre David Heinemeir, Martin Fowler y Kent Beck
