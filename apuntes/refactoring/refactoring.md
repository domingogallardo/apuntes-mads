# Refactoring #

Una refactorización (_refactoring_ en inglés) de un programa consiste
en la realización de una transformación de su código fuente sin
cambiar su funcionamiento.

Por ejemplo, cuando cambiamos el nombre de un método y cambiamos el
nombre de todas las invocaciones a ese método estamos haciendo un
ejemplo concreto de la refactorización _Change Function
Declaration_. 

Por ejemplo, el método de la siguiente clase `Movie` es muy poco
descriptivo.


```java
public class Movie {
    public double compute(int number) {
        ...
    }
}

    ...
    int daysRented = 4;
    double price = movie.compute(daysRented);
    ...
```

Si cambiamos el nombre del método y su invocación, queda el siguiente
código:

```java
public class Movie {
    public double getCharge(int numberOfDays) {
        ...
    }
}

    ...
    int daysRented = 4;
    double price = movie.getCharge(daysRented);
    ...
```

El comportamiento del programa no ha cambiado en absoluto. Pero hemos
modificado su diseño y lo hemos hecho más comprensible. Hemos cambiado
el nombre genérico de _calcular(int number)_ por el nombre mucho más concreto e
informativo de _obtenerCargo(int diasDeAlquiler)_. Ahora está mucho
más claro qué hace ese método.

En esta sesión vamos a ver brevemente la historia de las técnicas de
refactoring, una pequeña lista de técnicas concretas, los denominados
_code smells_ que nos indican cuándo es posible que necesitemos
aplicar alguna refactorización y terminaremos con un ejemplo completo
de refactorización de código aplicando distintas técnicas completas.

<img src="imagenes/refactoring.png" width="600px"/>

Este tema está basado en la primera y segunda edición del libro
_Refactoring_ de  Martin Fowler (ver el apartado de Referencias).

## Introducción ##

El objetivo de las técnicas de refactorización es mejorar el diseño
del código, haciéndolo más sencillo, comprensible y modificable. Pero
(y esto es fundamental) sin modificar en absoluto el comportamiento
del programa.

En palabras de Martin Fowler:

> "Refactoring es el proceso de cambiar un sistema de software de
> una forma que no se altera el comportamiento externo del código,
> pero sí que se mejor su estructura interna. Es una forma
> disciplinada de limpiar el código que minimiza las posibilidades de
> introducir nuevos bugs. En esencia, cuando realizas una
> refactorización, mejoras el diseño del código después de haberlo
> escrito.

La idea de mejorar el diseño mediante la realización de
refactorizaciones es una idea muy importante. Ya la vimos en
TDD. Tradicionalmente, en las metodologías clásicas de cascada o otras
basadas en enfoques predictivos, el diseño se hace siempre al
principio, antes de empezar a desarrollar el código.

En metodologías como XP, TDD o _software craftmanship_ el diseño del
software es algo que estamos mejorando continuamente. No se sobre
diseña, sino que diseñamos sólo para lo que necesita el programa
actual. Conforme vamos escribiendo más código, añadiendo nuevas
funcionalidades, vamos también realizando rediseño mediante
refactorizaciones del código.

Hemos comentado que la refactorización no debe modificar el
comportamiento del código. ¿Cómo podemos garantizar que el
funcionamiento del programa sigue siendo el mismo después de la
refactorización? La forma más habitual es mediante una batería de
tests que prueba el código que se refactoriza. Basta con comprobar,
una vez hecha la refactorización, que los tests siguen pasando.

Es conveniente que la refactorización se realice mediante pasos
pequeños. Una refactorización grande se puede subdividir en
refactorizaciones más elementales. El hecho de hacer pasos pequeños
hace más difícil introducir bugs.


### Orígenes de las técnicas de refactorización ###

Es difícil encontrar el origen de la palabra o el concepto de
_refactoring_. La idea de modificar el código fuente para mejorar su
diseño ha estado presente desde el principio de la historia de la
programación.

Pero sí que podemos trazar el origen de la idea de usar la
refactorización como un elemento fundamental del proceso de diseño de
software. 


El libro de Martin Fowler contiene una colección de patrones de
refactorización.

Como ya sabes, la refactorización es una parte fundamental de la
técnica de TDD.

### Refactorización en los IDEs ###

Aunque veremos que no es complicado realizar las refactorizaciones
manualmente, es posible usar las acciones de refactorización de los
IDEs que, en ocasiones, pueden ser de ayuda.

Casi todos los IDEs tienen la refactorización más básica, que es la de
renombrar un método, variable o función. Para realizar de forma
correcta la refactorización el IDE tiene que usar el análisis
sintáctico del código fuente para identificar quién usa esa variable,
método o función y no limitarse a hacer una mera substitución y
reemplazo de un texto por otro.

Entre los IDEs más avanzados en capacidades de refactorización se
encuentra IntelliJ. Podemos ver una introducción a sus capacidades de
refactorización en el tutorial [Introduction to
refactoring﻿](https://www.jetbrains.com/help/idea/tutorial-introduction-to-refactoring.html). Y
también en bastantes vídeos del canal de IntellJ, como por ejemplo
[Extract Refactorings in
Action](https://www.youtube.com/watch?v=UYrhNG9bRng&t=6s). El manual
completo con todas las opciones de refactorización de IntellJ se
encuentra en [este enlace](https://www.jetbrains.com/help/idea/refactoring-source-code.html).

## Ejemplos de refactorizaciones ##

En la primera edición del libro de Martin Fowler se presentan 72
refactorizaciones. En la segunda quedan reducidas a 61. Es una lista
amplia que recoge la mayoría de patrones más usados.

<img src="imagenes/list-refactorings.png" width="600px"/>

Obviamente, son demasiados para verlos en una clase. Veremos sólo
cuatro, con el objeto de tener una idea de cómo se plantean. La lista
completa también la puedes consultar en la web de Fowler
[refactoring.com](https://refactoring.com/catalog/). 

La segunda edición del libro está escrito en el lenguaje
JavaScript. Utilizaremos los ejemplos de la primera edición, escritos
en Java.

### Extract Method ###

En la refactorización _Extraer método_ se encapsula un conjunto de
código en una función y se reemplaza ese código por una llamada a la
nueva función.

**Código inicial**

```java
void printOwing(double amount) {
    printBanner();

    //print details
    System.out.println ("name:" + _name);
    System.out.println ("amount" + amount);
}
```

**Código refactorizado**

```java
void printOwing(double amount) {
    printBanner();
    printDetails(amount);
}

void printDetails (double amount) {
    System.out.println ("name:" + _name);
    System.out.println ("amount" + amount);
}
```

Un ejemplo algo más complicado:

**Código inicial**

```java
void printOwing(double previousAmount) {

    Enumeration e = _orders.elements();
    double outstanding = previousAmount * 1.2;

    printBanner();

    // calculate outstanding
    while (e.hasMoreElements()) {
        Order each = (Order) e.nextElement();
        outstanding += each.getAmount();
    }

    printDetails(outstanding);
}
```

**Código refactorizado**

```java
void printOwing(double previousAmount) {
    printBanner();
    double outstanding = getOutstanding(previousAmount * 1.2);
    printDetails(outstanding);
}

double getOutstanding(double initialValue) {
    double result = initialValue;
    Enumeration e = orders.elements();
    while (e.hasMoreElements()) {
        Order each = (Order) e.nextElement();
        result += each.getAmount();
   }
    return result;
}
```

### Move Method ###

La refactorización _Mover método_ consiste en crear un nuevo método
con un cuerpo similar en la clase que lo usa más. El método antiguo
podemos transformarlo en una delegación, manteniendo sin cambios el
código llamador, o eliminarlo y sustituir el código llamador por una
llamada al nuevo método.

**Código inicial**

```java
public class Account {
    private AccountType type;
    private int daysOverdrawn;
    ...
    double overdraftCharge() {
        if (type.isPremium()) {
             double result = 10;
             if (daysOverdrawn > 7) result += (_daysOverdrawn - 7) * 0.85;
             return result;
        }
        else return daysOverdrawn * 1.75;
    }

    double bankCharge() {
        double result = 4.5;
        if (daysOverdrawn > 0) result += overdraftCharge();
        return result;
    }
}
```

**Código refactorizado**

```java
public class Account {
    ...
    double overdraftCharge() {
        return type.overdraftCharge(daysOverdrawn);
    }
    
    double bankCharge() {
        double result = 4.5;
        if (daysOverdrawn > 0) result += overdraftCharge();
        return result;
    }
}

public class AccountType {
    ...
    double overdraftCharge(int daysOverdrawn) {
        if (isPremium()) {
            double result = 10;
            if (daysOverdrawn > 7) result += (daysOverdrawn - 7) * 0.85;
            return result;
        }
        else return daysOverdrawn * 1.75;
    }
}
```


### Replace Temp with Query ###

En la refactorización _Reemplazar variable temporal por invocación_ se
sustituye el uso de una variable por una llamada a un método.

**Código inicial**

```java
    double basePrice = _quantity * _itemPrice;
    if (basePrice > 1000)
        return basePrice * 0.95;
    else
        return basePrice * 0.98;
```

**Código refactorizado**

```java
    if (basePrice() > 1000)
        return basePrice() * 0.95;
    else
        return basePrice() * 0.98;
...
  double basePrice() {
      return _quantity * _itemPrice;
  }
```

Otro ejemplo

**Código inicial**

```java
double getPrice() {
    int basePrice = quantity * itemPrice;
    double discountFactor;
    if (basePrice > 1000) discountFactor = 0.95;
    else discountFactor = 0.98;
    return basePrice * discountFactor;
}
```

**Paso 1**

```java
double getPrice() {
    double discountFactor;
    if (basePrice() > 1000) discountFactor = 0.95;
    else discountFactor = 0.98;
    return basePrice() * discountFactor;
}

private int basePrice() {
    return quantity * itemPrice;
}
```

**Paso 2**

```java
double getPrice() {
    double discountFactor = discountFactor()
    return basePrice() * discountFactor;
}

private int basePrice() {
    return quantity * itemPrice;
}

private double discountFactor() {
    if (basePrice() > 1000) return 0.95;
    else return 0.98;
}
```



**Código refactorizado (Paso 3)**

```java
double getPrice() {
    return basePrice() * discountFactor();
}

private int basePrice() {
    return quantity * itemPrice;
}

private double discountFactor() {
    if (basePrice() > 1000) return 0.95;
    else return 0.98;
}
```


### Parameterize Function ###

La refactorización _Parametrizar función_ permite unificar varias
funciones o métodos que tienen una lógica similar en una única función
o método añadiendo algún parámetro adicional.

Un ejemplo muy sencillo:

**Código inicial**

```java
public class Employee {
    void tenPercentRise() {
        salary *= 1.1;
    }
    
    void fivePercentRise() {
        salary *= 1.05;
    }
}

    ...
    employee.tenPercentRise();
    otherEmployee.fivePercentRise();
    ...
```


**Código refactorizado**

```java
public class Employee {
    void raisePercentage(double percentage) {
        salary *= (1 + (percentage / 100));
    }
}

    ...
    employee.raisePercentage(10);
    otherEmployee.raisePercentage(5);
    ...
```


Otro ejemplo:

**Código inicial**

```java
public class Book {
    ...
    public void addReservation(Customer customer) {
        this.reservations.push(customer);
    }
    
    public void addReservationWithPriority(Customer customer) {
        this.priorityReservations.push(customer);
    }
}

    ...
    book.addReservation(aCustomer);
    ...
    // cliente prioritario
    book.addReservationWithPriority(prioritaryCustomer);
    ...
```

**Código refactorizado**

```java
public class Book {
    ...
    public void addReservation(Customer customer, boolean priority) {
        if (priority) {
            this.priorityRservations.push(customer);
        } else {
            this.reservations.push(customer);
        }
    }
}

    ...
    book.addReservation(aCustomer, false);
    ...
    // cliente prioritario
    book.addReservation(prioritaryCustomer, true);
    ...
```



## Code smells ##

Indicadores de que el diseño no es correcto y habría que refactorizar.

DRY

## Ejemplo completo ##

Veamos un ejemplo completo  que usa alguna de las refactorizaciones
presentadas anteriormente.

Está sacado del libro de Martin Fowler _Refactoring_.


### Versión inicial ###

DESCRIPCIÓN DEL NEGOCIO DE ALQUILER DE PELÍCULAS

**Clase Movie**

```java
public class Movie {

    public static final int CHILDRENS = 2;
    public static final int REGULAR = 0;
    public static final int NEW_RELEASE = 1;

    private String title;
    private int priceCode;

    public Movie(String title, int priceCode) {
        this.title = title;
        this.priceCode = priceCode;
    }

    public int getPriceCode() {
        return priceCode;
    }

    public void setPriceCode(int arg) {
        priceCode = arg;
    }

    public String getTitle (){
        return title;
    };
}
```


**Clase Rental**

```java
class Rental {
    private Movie movie;
    private int daysRented;

    public Rental(Movie movie, int daysRented) {
        this.movie = movie;
        this.daysRented = daysRented;
    }
    public int getDaysRented() {
        return daysRented;
    }
    public Movie getMovie() {
        return movie;
    }
}
```

**Clase Customer**

```java
import java.util.Enumeration;
import java.util.Vector;

class Customer {
    private String name;
    private Vector rentals = new Vector();

    public Customer(String name) {
        this.name = name;
    }

    public void addRental(Rental arg) {
        rentals.addElement(arg);
    }

    public String getName() {
        return name;
    }

    public String statement() {
        double totalAmount = 0;
        int frequentRenterPoints = 0;
        Enumeration allRentals = rentals.elements();
        String result = "Rental Record for " + getName() + "\n";
        while (allRentals.hasMoreElements()) {
            double thisAmount = 0;
            Rental each = (Rental) allRentals.nextElement();

            //determine amounts for each line
            switch (each.getMovie().getPriceCode()) {
                case Movie.REGULAR:
                    thisAmount += 2;
                    if (each.getDaysRented() > 2)
                        thisAmount += (each.getDaysRented() - 2) * 1.5;
                    break;
                case Movie.NEW_RELEASE:
                    thisAmount += each.getDaysRented() * 3;
                    break;
                case Movie.CHILDRENS:
                    thisAmount += 1.5;
                    if (each.getDaysRented() > 3)
                        thisAmount += (each.getDaysRented() - 3) * 1.5;
                    break;
            }

            // add frequent renter points
            frequentRenterPoints++;
            // add bonus for a two day new release rental
            if ((each.getMovie().getPriceCode() == Movie.NEW_RELEASE) &&
                    each.getDaysRented() > 1) frequentRenterPoints++;
            //show figures for this rental
            result += "\t" + each.getMovie().getTitle() + "\t" +
                    String.valueOf(thisAmount) + "\n";
            totalAmount += thisAmount;

        }
        //add footer lines
        result += "Amount owed is " + String.valueOf(totalAmount) + "\n";
        result += "You earned " + String.valueOf(frequentRenterPoints) +
                " frequent renter points";
        return result;
    }
}
```


**Clase Main**

```java
public class Main {
    public static void main(String[] args) {
        Movie tenet = new Movie("Tenet", Movie.NEW_RELEASE);
        Movie busan = new Movie("Train to Busan", Movie.REGULAR);
        Movie padre = new Movie("Padre no hay más que uno", Movie.CHILDRENS);

        Rental rental1 = new Rental(tenet, 2);
        Rental rental2 = new Rental(busan, 2);
        Rental rental3 = new Rental(padre, 1);

        Customer customer = new Customer("domingogallardo");

        customer.addRental(rental1);
        customer.addRental(rental2);
        customer.addRental(rental3);

        System.out.println(customer.statement());
    }
}
```


Salida de la ejecución:

```
Rental Record for domingogallardo
	Tenet	6.0
	Train to Busan	2.0
	Padre no hay más que uno	1.5
Amount owed is 9.5
You earned 4 frequent renter points
```


### Refactorización para imprimir la cuenta en HTML ###

Supongamos que el cliente para el que hemos hecho el programa nos pide
que el resultado de la cuenta no sea en texto plano sino que sea en
HTML.

Podríamos copiar y pegar el código del método `statement()`, en un
nuevo método `htmlStatement()` en el que mantuviéramos los cálculos y
cambiáramos las sentencias de texto. El problema de esto es que
tendríamos duplicado el código con los cálculos y en el momento que
haya que cambiar algo este código habrá que hacerlo en dos sitios, con
los problemas que eso puede conllevar.

Vamos entonces a realizar una refactorización que que simplifique el
código del método `statement()` para que sólo se encargue de imprimir
y cumpla el principio de responsabilidad única.

#### Paso 1: Extract Method ####

Extraemos del método `Customer.statement()` el código que calcula el
precio de un alquiler y lo colocamos en el método `amountFor(Rental)`
de la propia clase.

La clase `Customer` queda así (mostramos sólo las líneas cambiadas y
el contexto en el que están definidas):

```java
class Customer {
    ...
    
    public String statement() {
        ...
        while (allRentals.hasMoreElements()) {
            double thisAmount = 0;
            Rental each = (Rental) allRentals.nextElement();
            thisAmount = amountFor(each);
            ...
            totalAmount += thisAmount;

        }
        ...
    }

    private double amountFor(Rental each) {
        double thisAmount = 0;
        //determine amounts for each line
        switch (each.getMovie().getPriceCode()) {
            case Movie.REGULAR:
                thisAmount += 2;
                if (each.getDaysRented() > 2)
                    thisAmount += (each.getDaysRented() - 2) * 1.5;
                break;
            case Movie.NEW_RELEASE:
                thisAmount += each.getDaysRented() * 3;
                break;
            case Movie.CHILDRENS:
                thisAmount += 1.5;
                if (each.getDaysRented() > 3)
                    thisAmount += (each.getDaysRented() - 3) * 1.5;
                break;
        }
        return thisAmount;
    }
}
```


#### Paso 2: Rename Variable ####

Renombramos las variables `each` y `thisAmount` del método recién
introducido `amountFor(Rental)` por los nombres más apropiados
`aRental` y `result`. El método queda así:

```java
class Customer {
    ...
    
    private double amountFor(Rental aRental) {
        double result = 0;
        //determine amounts for each line
        switch (aRental.getMovie().getPriceCode()) {
            case Movie.REGULAR:
                result += 2;
                if (aRental.getDaysRented() > 2)
                    result += (aRental.getDaysRented() - 2) * 1.5;
                break;
            case Movie.NEW_RELEASE:
                result += aRental.getDaysRented() * 3;
                break;
            case Movie.CHILDRENS:
                result += 1.5;
                if (aRental.getDaysRented() > 3)
                    result += (aRental.getDaysRented() - 3) * 1.5;
                break;
        }
        return result;
    }
}

```



#### Paso 3: Move Method ####

El método `amountFor(Rental)` es más apropiado que esté en la clase
`Rental`. Movemos el código de ese método a esa clase, creando un
nuevo método denominado `getCharge()`. Sustituimos el código original
por una llamada al método:


```java
class Customer {
    ...
    private double amountFor(Rental rental) {
        return rental.getCharge();
    }
}

class Rental {
    ...
    double getCharge() {
        double result = 0;
        //determine amounts for each line
        switch (getMovie().getPriceCode()) {
            case Movie.REGULAR:
                result += 2;
                if (getDaysRented() > 2)
                    result += (getDaysRented() - 2) * 1.5;
                break;
            case Movie.NEW_RELEASE:
                result += getDaysRented() * 3;
                break;
            case Movie.CHILDRENS:
                result += 1.5;
                if (getDaysRented() > 3)
                    result += (getDaysRented() - 3) * 1.5;
                break;
        }
        return result;
    }
}
```





#### Paso 4: Inline Method ####

Sustituimos la llamada a `amountFor()` en el método
`Customer.statement()` por el propio código del método y eliminamos
`amountFor()`:


```java

class Customer {
    ...
    public String statement() {
        ...
        while (allRentals.hasMoreElements()) {
            ...
            thisAmount = each.getCharge();
            ...
        }
        ...
    }
    
    // Eliminimamos el método amountFor()
}

```

#### Paso 5: Replace Temp with Query ####

Para hacer más entendible el código, sustituimos el uso de la variable temporal
`thisAmount` por una llamada a `each.getCharge()`. De esta forma
eliminamos una indirección, eliminamos la posibilidad de efectos
laterales y tenemos claro qué valor es el que estamos imprimiendo y
sumando al total.

```diff
class Customer {
    ...
    public String statement() {
        ...
        while (allRentals.hasMoreElements()) {
            ...
-           thisAmount = each.getCharge();
            ...
            result += "\t" + each.getMovie().getTitle() + "\t" +
+                    String.valueOf(each.getCharge()) + "\n";
+            totalAmount += each.getCharge();
        }
        ...
    }
}
```

Se podría argumentar que este código es menos eficiente que el
anterior. Pero en la realidad el cambio de eficiencia es mínimo. El
método `getCharge()` tiene una complejidad temporal de `O(1)` y no
afecta para nada a la eficiencia del programa llamarlo dos veces en
lugar de una (aunque estemos dentro de un bucle).

<table><tr><td>

**¿Código optimizado o código comprensible?**

Muchas veces nos vemos tentados a hacer el código menos entendible en
aras de una supuesta optimización. Existen programadores a los que les
gusta hacer continuamente estas optimizaciones y conseguir arañar
milisegundos de eficiencia. El problema es que el código resultante
muchas veces es menos comprensible y modificable que el original. Si
en algún momento hay que modificar ese código optimizado, tendremos
primero que perder el tiempo para entender qué era lo que hacía y
después tendremos casi seguramente que deshacer la optimización para
introducir la modificación.

Muchas supuestas optimizaciones que se realizan en el código resultan
no siendo tales, porque se hace un trabajo redundante al que realiza
el compilador o incluso se dificulta su funcionamiento. Los
compiladores modernos son muy avanzados y el código que generan es un
código altamente optimizado. No hagamos un trabajo que ya está
haciendo el compilador.

Mi consejo es que, en general, nunca debemos hacer el programa menos
comprensible por el hecho de intentar hacerlo más eficiente. Sólo
cuando hagamos un análisis de rendimiento y detectemos los verdaderos
cuellos de botella del programa es cuando tendremos que centrarnos en
optimizar su rendimiento. Pero sólo de aquel código responsable del
cuello de botella.

</table></tr></td>


#### Paso 6: Extract + Move Method ####

Repetimos la extracción de otra parte del código y lo movemos también
a la clase `Rental`. Esta vez el código que calcula los puntos de
promoción que gana el cliente por los alquileres.

```java
class Customer {
    ...
    public String statement() {
        ...
        while (allRentals.hasMoreElements()) {
            ...
            frequentRenterPoints += each.getFrequentRenterPoints();
            ...
        }
        ...
    }
}

class Rental {
    ...
    int getFrequentRenterPoints() {
        if ((getMovie().getPriceCode() == Movie.NEW_RELEASE) &&
                getDaysRented() > 1)
            return 2;
        else return 1;
    }
}
```



#### Paso 7: Replace Temp with Query ####

El último paso para dejar en el método `statement` sólo lo relacionado
con la impresión es sacar del bucle los cálculos del total de la
cuenta y del total de puntos de promoción.

Crearemos dos métodos que calculan esos totales y que podrán ser
usados tanto desde el actual método que imprime la cuenta como desde
el futuro método que lo hace en HTML.

Es un ejemplo de la refactorización _Replace Temp with Query_ pero
algo más complicado porque para realizar el cálculo hay que copiar
todo el bucle dentro del método al que se llama.

El código queda así:

```java
class Customer {
    ...
    public String statement() {
        Enumeration allRentals = rentals.elements();
        String result = "Rental Record for " + getName() + "\n";
        while (allRentals.hasMoreElements()) {
            Rental each = (Rental) allRentals.nextElement();

            //show figures for this rental
            result += "\t" + each.getMovie().getTitle() + "\t" +
                    String.valueOf(each.getCharge()) + "\n";
        }
        //add footer lines
        result += "Amount owed is " + String.valueOf(getTotalCharge()) + "\n";
        result += "You earned " + String.valueOf(getTotalFrequentRenterPoints()) +
                " frequent renter points";
        return result;
    }

    private double getTotalCharge() {
        double result = 0;
        Enumeration elements = rentals.elements();
        while (elements.hasMoreElements()) {
            Rental each = (Rental) elements.nextElement();
            result += each.getCharge();
        }
        return result;
    }

    private double getTotalFrequentRenterPoints() {
        double result = 0;
        Enumeration elements = rentals.elements();
        while (elements.hasMoreElements()) {
            Rental each = (Rental) elements.nextElement();
            result += each.getFrequentRenterPoints();
        }
        return result;
    }

}
```

#### Paso 8: Añadir método que genera el HTML ####

Y ahora ya estamos en situación de hacer fácil la adición del código
que genera el HTML:

```java
    ...
    public String htmlStatement() {
        Enumeration allRentals = rentals.elements();
        String result = "<h1>Rental Record for <em>" + getName() + "</em></h1>\n";
        result += "<ul>\n";
        while (allRentals.hasMoreElements()) {
            Rental each = (Rental) allRentals.nextElement();

            //show figures for this rental
            result += "<li>" + each.getMovie().getTitle() + ":" +
                    String.valueOf(each.getCharge()) + "</li>\n";
        }
        result += "</ul>\n";
        //add footer lines
        result += "<p>Amount owed is <em>" + String.valueOf(getTotalCharge()) + "</em></p>\n";
        result += "<p>You earned <em>" + String.valueOf(getTotalFrequentRenterPoints()) +
                "</em> frequent renter points</p>\n";
        return result;
    }
```

Al extraer todos los cálculos hemos podido crear el método
`htmlStatement` y reutilizar todo el código de cálculo que estaba en
el método original. No hemos copiado y pegado, de forma que si las
reglas de cálculo cambian solo tenemos que ir a modificarlas a un
único sitio.

### Refactorización para introducir herencia y polimorfismo ###

Supongamos que ahora nuestro cliente está planeando de hacer cambios
en la clasificación de las películas. Todavía no está claro que
cambios van a ser, pero parece que se van a introducir nuevas
categorías y se tendrán que decidir el cargo y los puntos de promoción
de estas nuevas categorías.

Vamos ahora a mejorar el diseño para evitar tener que entrar en los
códigos condicionales cada vez que vayamos a hacer alguna de estas
modificaciones. 

Haremos una refactorización en la que reemplazaremos la lógica
condicional por polimorfismo.

#### Paso 1: Move Method ####

Movemos el código del método `Rental.getCharge()` a la clase `Movie`,
que es donde debería estar. Un indicador de ello es que estamos
haciendo un `switch` basándonos en un atributo de otro objeto. Si
tenemos que hacer un `switch` debemos hacerlo basándonos en nuestros
propios datos, no en los datos de otro.

Quedaría así:

```java
class Rental {
    ...
    double getCharge() {
        return movie.getCharge(daysRented);
    }
    ...
}

public class Movie {
    ...
    double getCharge(int daysRented) {
        double result = 0;
        //determine amounts for each line
        switch (getPriceCode()) {
            case Movie.REGULAR:
                result += 2;
                if (daysRented > 2)
                    result += (daysRented - 2) * 1.5;
                break;
            case Movie.NEW_RELEASE:
                result += daysRented * 3;
                break;
            case Movie.CHILDRENS:
                result += 1.5;
                if (daysRented > 3)
                    result += (daysRented - 3) * 1.5;
                break;
        }
        return result;
    }
    ...
```



#### Paso 2: Move Method ####

Hacemos lo mismo con el cálculo de los puntos de promoción por
alquiler frecuente.

```java
class Rental {
    ...
    int getFrequentRenterPoints() {
        return movie.getFrequentRenterPoints(daysRented);
    }
}

public class Movie {
    ...
    int getFrequentRenterPoints(int daysRented) {
        if ((getPriceCode() == Movie.NEW_RELEASE) &&
                daysRented > 1)
            return 2;
        else return 1;
    }
    ...
```

#### Paso 3: Encapsulate Variable ####

Vamos a comenzar ahora el proceso de introducir la herencia y el
polimorfismo. 

Nuestra primera idea sería hacer una subclase de `Movie` por cada tipo
de película. Una clase `RegularMovie` otra `NewReleaseMovie`,
etc. 

<img src="imagenes/herencia-movies.png" width="400px"/>

Pero esto es problemático y no funciona, porque una película puede
cambiar su clase durante su vida. Podría ser que inicialmente una
película fuera `NewReleseMovie` y después pasara a ser
`RegularMovie`. Sin embargo un objeto no puede cambiar de clase en su
ciclo de vida.

Podemos modelar esto usando el patrón _State_, en el que definimos un
atributo `price` que es que define el tipo de película. Lo muestra la
siguiente figura:

<img src="imagenes/herencia-state.png" width="600px"/>

De esta forma para que una película cambiara de clase sólo tendríamos
que asociarle un nuevo objeto de tipo `Price`.

Para hacer esto, lo primero que debemos hacer es encapsular el
atributo `price` de `Movie` de forma que todos los accesos a él sean a
través de un método `getter` o `setter`.

Sólo hay que cambiar el acceso en el constructor de `Movie`:

```diff
    public Movie(String title, int priceCode) {
         this.title = title;
-        this.priceCode = priceCode;
+        setPriceCode(priceCode);
     }

```

#### Paso 4: Replace Type Code with State ####

En este paso introducimos la clase `Price` y reemplazamos la
instancia de tipo `int` en la que codificábamos el tipo de película
por un objeto de este tipo. El código `int` para el tipo de película
lo seguimos manteniendo, pero encapsulado en el objeto de tipo `Price`.

```java
public class Movie {
    ...
    private Price price;
    ...
    public int getPriceCode() {
        return price.getPriceCode();
    }

    public void setPriceCode(int arg) {
        switch (arg) {
            case REGULAR:
                price = new RegularPrice();
                break;
            case CHILDRENS:
                price = new ChildrensPrice();
                break;
            case NEW_RELEASE:
                price = new NewReleasePrice();
                break;
            default:
                throw new IllegalArgumentException("Incorrect Price Code");
        }
    }
    ...
}

abstract public class Price {
    abstract int getPriceCode();
}

class ChildrensPrice extends Price {
    int getPriceCode() {
        return Movie.CHILDRENS;
    }
}

class NewReleasePrice extends Price {
    int getPriceCode() {
        return Movie.NEW_RELEASE;
    }
}

class RegularPrice extends Price {
    int getPriceCode() {
        return Movie.REGULAR;
    }
}
```

#### Paso 5: Move Method ####

Ahora movemos el código del método `getCharge` de la clase `Movie` a
la clase `Price`:

```java
public class Movie {
    ...
    double getCharge(int daysRented) {
        return price.getCharge(daysRented);
    }
    ...
}

abstract public class Price {
    ...
    double getCharge(int daysRented) {
        double result = 0;
        switch (getPriceCode()) {
            case Movie.REGULAR:
                result += 2;
                if (daysRented > 2)
                    result += (daysRented - 2) * 1.5;
                break;
            case Movie.NEW_RELEASE:
                result += daysRented * 3;
                break;
            case Movie.CHILDRENS:
                result += 1.5;
                if (daysRented > 3)
                    result += (daysRented - 3) * 1.5;
                break;
        }
        return result;
    }
}
```



#### Paso 6: Replace Conditional with Polymorphism ####

Ahora ya podemos aplicar la refactorización de reemplazar el
condicional con el polimorfismo, para el método `getCharge`.

```java
abstract public class Price {
    abstract int getPriceCode();
    abstract double getCharge(int daysRented);
}

class ChildrensPrice extends Price {
    int getPriceCode() {
        return Movie.CHILDRENS;
    }

    double getCharge(int daysRented) {
        double result = 1.5;
        if (daysRented > 3)
            result += (daysRented - 3) * 1.5;
        return result;
    }
}

class NewReleasePrice extends Price {
    int getPriceCode() {
        return Movie.NEW_RELEASE;
    }

    double getCharge(int daysRented) {
        return daysRented * 3;
    }
}

class RegularPrice extends Price {
    int getPriceCode() {
        return Movie.REGULAR;
    }

    double getCharge(int daysRented) {
        double result = 2;
        if (daysRented > 2)
            result += (daysRented - 2) * 1.5;
        return result;
    }
}
```

Al haber definido el comportamiento de `getCharge` en cada subclase es
mucho más sencillo modificar cada uno de ellos de forma
independiente. También podemos incluir nuevas clases de forma más
sencilla que antes.




#### Paso 7: Replace Conditional with Polymorphism ####

Por último, podemos aplicar también el polimorfismo para obtener los
puntos de promoción por alquileres frecuentes. 

La lógica condicional está también basada en el tipo de precio. Para
los nuevos lanzamientos se devuelven 1 o 2 puntos dependiendo de los
días alquilados. En el resto de tipos se devuelve siempre 1.

Queda de la siguiente forma, después de la refactorización:

```java
public class Movie {
    ...
    int getFrequentRenterPoints(int daysRented) {
        return price.getFrequentRenterPoints(daysRented);
    }
}

abstract public class Price {
    ...
    int getFrequentRenterPoints(int daysRented) {
        return 1;
    }
}

class NewReleasePrice extends Price {
    ...
    int getFrequentRenterPoints(int daysRented) {
        return (daysRented > 1) ? 2 : 1;
    }
}
```

### Versión final ###

Mostramos a continuación la versión final del programa.

```java
public class Main {
    public static void main(String[] args) {
        Movie tenet = new Movie("Tenet", Movie.NEW_RELEASE);
        Movie busan = new Movie("Train to Busan", Movie.REGULAR);
        Movie padre = new Movie("Padre no hay más que uno", Movie.CHILDRENS);

        Rental rental1 = new Rental(tenet, 2);
        Rental rental2 = new Rental(busan, 2);
        Rental rental3 = new Rental(padre, 1);

        Customer customer = new Customer("domingogallardo");

        customer.addRental(rental1);
        customer.addRental(rental2);
        customer.addRental(rental3);

        System.out.println(customer.statement());
        System.out.println("*************************");
        System.out.println(customer.htmlStatement());
    }
}


import java.util.Enumeration;
import java.util.Vector;

class Customer {
    private String name;
    private Vector rentals = new Vector();

    public Customer(String name) {
        this.name = name;
    }

    public void addRental(Rental arg) {
        rentals.addElement(arg);
    }

    public String getName() {
        return name;
    }

    public String statement() {
        Enumeration allRentals = rentals.elements();
        String result = "Rental Record for " + getName() + "\n";
        while (allRentals.hasMoreElements()) {
            Rental each = (Rental) allRentals.nextElement();

            //show figures for this rental
            result += "\t" + each.getMovie().getTitle() + "\t" +
                    String.valueOf(each.getCharge()) + "\n";
        }
        //add footer lines
        result += "Amount owed is " + String.valueOf(getTotalCharge()) + "\n";
        result += "You earned " + String.valueOf(getTotalFrequentRenterPoints()) +
                " frequent renter points";
        return result;
    }

    public String htmlStatement() {
        Enumeration allRentals = rentals.elements();
        String result = "<h1>Rental Record for <em>" + getName() + "</em></h1>\n";
        result += "<ul>\n";
        while (allRentals.hasMoreElements()) {
            Rental each = (Rental) allRentals.nextElement();

            //show figures for this rental
            result += "<li>" + each.getMovie().getTitle() + ":" +
                    String.valueOf(each.getCharge()) + "</li>\n";
        }
        result += "</ul>\n";
        //add footer lines
        result += "<p>Amount owed is <em>" + String.valueOf(getTotalCharge()) + "</em></p>\n";
        result += "<p>You earned <em>" + String.valueOf(getTotalFrequentRenterPoints()) +
                "</em> frequent renter points</p>\n";
        return result;
    }

    private double getTotalCharge() {
        double result = 0;
        Enumeration elements = rentals.elements();
        while (elements.hasMoreElements()) {
            Rental each = (Rental) elements.nextElement();
            result += each.getCharge();
        }
        return result;
    }

    private double getTotalFrequentRenterPoints() {
        double result = 0;
        Enumeration elements = rentals.elements();
        while (elements.hasMoreElements()) {
            Rental each = (Rental) elements.nextElement();
            result += each.getFrequentRenterPoints();
        }
        return result;
    }

}


class Rental {
    private Movie movie;
    private int daysRented;

    public Rental(Movie movie, int daysRented) {
        this.movie = movie;
        this.daysRented = daysRented;
    }
    public int getDaysRented() {
        return daysRented;
    }
    public Movie getMovie() {
        return movie;
    }

    double getCharge() {
        return movie.getCharge(daysRented);
    }

    int getFrequentRenterPoints() {
        return movie.getFrequentRenterPoints(daysRented);
    }
}

public class Movie {

    public static final int CHILDRENS = 2;
    public static final int REGULAR = 0;
    public static final int NEW_RELEASE = 1;

    private String title;
    private Price price;

    public Movie(String title, int priceCode) {
        this.title = title;
        setPriceCode(priceCode);
    }

    double getCharge(int daysRented) {
        return price.getCharge(daysRented);
    }

    int getFrequentRenterPoints(int daysRented) {
        return price.getFrequentRenterPoints(daysRented);
    }

    public int getPriceCode() {
        return price.getPriceCode();
    }

    public void setPriceCode(int arg) {
        switch (arg) {
            case REGULAR:
                price = new RegularPrice();
                break;
            case CHILDRENS:
                price = new ChildrensPrice();
                break;
            case NEW_RELEASE:
                price = new NewReleasePrice();
                break;
            default:
                throw new IllegalArgumentException("Incorrect Price Code");
        }
    }

    public String getTitle (){
        return title;
    };
}


abstract public class Price {
    abstract int getPriceCode();
    abstract double getCharge(int daysRented);

    int getFrequentRenterPoints(int daysRented) {
        return 1;
    }
}

class ChildrensPrice extends Price {
    int getPriceCode() {
        return Movie.CHILDRENS;
    }

    double getCharge(int daysRented) {
        double result = 1.5;
        if (daysRented > 3)
            result += (daysRented - 3) * 1.5;
        return result;
    }
}

class NewReleasePrice extends Price {
    int getPriceCode() {
        return Movie.NEW_RELEASE;
    }

    double getCharge(int daysRented) {
        return daysRented * 3;
    }

    int getFrequentRenterPoints(int daysRented) {
        return (daysRented > 1) ? 2 : 1;
    }
}

class RegularPrice extends Price {
    int getPriceCode() {
        return Movie.REGULAR;
    }

    double getCharge(int daysRented) {
        double result = 2;
        if (daysRented > 2)
            result += (daysRented - 2) * 1.5;
        return result;
    }
}
```

## Referencias ##

Toda la sesión está basada en las dos ediciones de los libros
_Refactoring_ de Martin Fowler. Hay que hacer notar el cambio del
lenguaje de programación entre las dos ediciones. En la primera
edición era Java y en la segunda JavaScript.

- Martin Fowler (1999) [_Refactoring (primera edición)_](https://learning.oreilly.com/library/view/refactoring-improving-the/0201485672/)
- Martin Fowler (2019) [_Refactoring (segunda edición)_](https://learning.oreilly.com/library/view/refactoring-improving-the/9780134757681/)
