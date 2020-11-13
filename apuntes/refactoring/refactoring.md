# Refactoring #

Una refactorización (_refactoring_ en inglés) de un programa consiste
en la realización de una transformación de su código fuente sin
cambiar su funcionamiento.

El objetivo de las refactorizaciones es el de mejorar el diseño del
código, haciéndolo más sencillo, comprensible y modificable.

¿Cómo podemos garantizar que el funcionamiento del programa sigue
siendo el mismo después de la refactorización? La forma más habitual
es mediante una batería de tests que prueba el código que se
refactoriza. Basta con comprobar, una vez hecha la refactorización,
que los tests siguen pasando.

Además, es conveniente que las refactorización se realice mediante
pasos pequeños. Una refactorización grande se puede subdividir en
refactorizaciones más elementales. El libro de Martin Fowler contiene
una colección de patrones de refactorización.

Como ya sabes, la refactorización es una parte fundamental de la
técnica de TDD. Una vez que se ha hecho 


## Refactorización en los IDEs ##


## Code smells ##

Indicadores de que el diseño no es correcto y habría que refactorizar.



## Ejemplo completo ##


### Versión inicial ###


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

El objetivo de toda esta primera refactorización va a ser simplificar
el código del método `statement()` para que sólo se encargue de
imprimir. Ahora tiene mezcladas la impresión de la cuenta con el
cálculo de sus elementos. No cumple el principio de responsabilidad
única.

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
                    String.valueOf(each.getCharge()) + "\n";
            totalAmount += each.getCharge();
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

<table><tr></td>

**¿Código optimizado o código comprensible?**

Muchas veces nos vemos tentados a hacer el código menos entendible en
aras de una supuesta optimización. Existen programadores a los que les
gusta hacer continuamente estas optimizaciones y conseguir arañar
milisegundos de eficiencia. El problema es que el código resultante
muchas veces es menos comprensible y modificable que el original. Si
en algún momento hay que modificarlo, tendremos primero que perder el
tiempo para entender qué hacía el código y después tendremos casi
seguramente que deshacer la optimización para introducir la
modificación.

Además muchas supuestas optimizaciones que se realizan en el código
resultan no siendo tales, porque se hace un trabajo redundante al que
realiza el compilador o incluso se dificulta su funcionamiento. Los
compiladores modernos son muy avanzados y el código que generan es un
código altamente optimizado. No hagamos un trabajo que ya está
haciendo el compilador.

Mi consejo es que, en general, nunca debemos hacer el programa menos
comprensible o modular por el hecho de intentar hacerlo más
eficiente. Sólo cuando hagamos un análisis de rendimiento y detectemos
los verdaderos cuellos de botella del programa es cuando tendremos que
centrarnos en optimizar el rendimiento del código. Pero sólo de aquel
código responsable del cuello de botella.

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


### Refactorización para introducir herencia y polimorfismo ###

