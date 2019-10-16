
## Conversión de números decimales a romanos usando TDD ##

Queremos diseñar una función que convierta números decimales a romanos:

- `1` -> `I`
- `2` -> `II`
- `3` -> `III`
- `4` -> `IV`
- ...
- `129` -> `CXXIX`

Cada ciclo de TDD consta de 3 pasos:

- Test sencillo con el que añadimos una nueva comprobación.
- Código que hace pasar el test.
- Refactorización si es necesaria.



### Ciclo 1 ###

Test:

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestDecimalARomano {
    @Test
    public void testConvierteUno() {
        assertEquals("I", Convertir.aRomano(1));
    }

}
```

Código que lo soluciona:

```java
public class Convertir {

    public static String aRomano(int num) {
        return "I";
    }
}
```

### Ciclo 2 ###

Test:

```java
    @Test
    public void testConvierteDos() {
        assertEquals("II", Convertir.aRomano(2));
    }
```

Código:

```diff
public class Convertir {

    public static String aRomano(int num) {
+       if (num == 2) return "II";
        return "I";
    }
}
```


### Ciclo 3 ###

Test:

```java
    @Test
    public void testConvierteTres() {
        assertEquals("III", Convertir.aRomano(3));
    }
```

Código:

```diff
public class Convertir {

    public static String aRomano(int num) {
+       if (num == 3) return "III";
        if (num == 2) return "II";
        return "I";
    }
}
```

**Refactorización**. Generalizamos, eliminando código repetido (tres
returns) y escribiendo una solución en la que el número romano es `I`
concatenado tantas veces como dice el `num`:

```java
public class Convertir {

    public static String aRomano(int num) {
        int n = 0;
        String romano = "";

        // Se concatena "I" num veces
        while (n < num) {
            romano += "I";
            n += 1;
        }
        return romano;
    }
}
```

### Ciclo 4 ###

Test:

- `4` -> `IV`

Código:

```diff
public class Convertir {

    public static String aRomano(int num) {
        int n = 0;
        String romano = "";

+       if (num == 4) return "IV";
        
        while (n < num) {
            romano += "I";
            n += 1;
        }
        return romano;
    }
}
```


### Ciclo 5 ###

Test

- `5` -> `V`

Código:

```diff
public class Convertir {

    public static String aRomano(int num) {
        int n = 0;
        String romano = "";

+       if (num == 5) return "V";
        if (num == 4) return "IV";
        
        while (n < num) {
            romano += "I";
            n += 1;
        }
        return romano;
    }
}
```

### Ciclo 6 ###

Test

- `6` -> `VI`

Código:

```diff
public class Convertir {

    public static String aRomano(int num) {
        int n = 0;
        String romano = "";

+       if (num == 6) return "VI";
        if (num == 5) return "V";
        if (num == 4) return "IV";
        
        while (n < num) {
            romano += "I";
            n += 1;
        }
        return romano;
    }
}
```


### Ciclo 7 ###

Test

- `7` -> `VII`

Código:

```diff
public class Convertir {

    public static String aRomano(int num) {
        int n = 0;
        String romano = "";

+       if (num == 7) return "VII";
        if (num == 6) return "VI";
        if (num == 5) return "V";
        if (num == 4) return "IV";
        
        while (n < num) {
            romano += "I";
            n += 1;
        }
        return romano;
    }
}
```

**Refactorización**. Generalizamos. Si el número es mayor de 5, escribimos
la `V` y añadimos tantos `I` como `num - 5`:

```java
public class Convertir {

    public static String aRomano(int num) {
        int n = 0;
        String romano = "";

        if (num > 5) {
            romano = "V";
            num = num - 5;
            // Añadimos num - 5 en romano
            while (n < num) {
                romano += "I";
                n += 1;
            }
            return romano;
        }

        if (num == 5) return "V";
        if (num == 4) return "IV";

        while (n < num) {
            romano += "I";
            n += 1;
        }
        return romano;
    }
}
```

**Refactorización**. Podemos simplificar aun más el código
anterior. Para obtener la cadena que añadimos a `V` podemos hacer una
llamada recursiva:

```diff
public class Convertir {

    public static String aRomano(int num) {
        int n = 0;
        String romano = "";
        
        if (num > 5)
-           romano = "V";
-           num = num - 5;
-           // Añadimos num - 5 en romano
-           while (n < num) {
-               romano += "I";
-               n += 1;
-           }
-           return romano;
+           return "V" + aRomano(num - 5);

        if (num == 5) return "V";
        if (num == 4) return "IV";

        while (n < num) {
            romano += "I";
            n += 1;
        }
        return romano;
    }
}
```

**Refactorización**. Podemos simplificar aun más usando la recursión
para evitar el último bucle:

```diff
public class Convertir {

    public static String aRomano(int num) {

        if (num > 5)
            return "V" + aRomano(num - 5);

        if (num == 5) return "V";
        if (num == 4) return "IV";
        
-       while (n < num) {
-           romano += "I";
-           n += 1;
-       }
-       return romano;

+       if (num > 1) 
+           return "I" + aRomano(num - 1);
+       // num == 1
+       return "I";

    }
}
```

### Ciclo 8 ###

Test:

- `8` -> `VIII`

No necesita modificarse el código; pasa el test.


### Ciclo 9 ###

Test:

- `9` -> `IX`

Código:

```diff
public class Convertir {

    public static String aRomano(int num) {

+       if (num == 9) return "IX";
        
        if (num > 5)
            return "V" + aRomano(num - 5);

        if (num == 5) return "V";
        if (num == 4) return "IV";
        
        if (num > 1) 
            return "I" + aRomano(num - 1);

        // num == 1
        return "I";
    }
}
```

### Ciclo 10 ###

Test:

- `10` -> `X`

Código:

```diff
public class Convertir {

    public static String aRomano(int num) {
    
+       if (num == 10) return "X";
        if (num == 9) return "IX";

        if (num > 5)
            return "V" + aRomano(num - 5);

        if (num == 5) return "V";
        if (num == 4) return "IV";
        
        if (num > 1) 
            return "I" + aRomano(num - 1);

        // num == 1
        return "I";
    }
}
```

### Ciclo 11 ###

Test:

- `11` -> `XI`

Código:

```diff
public class Convertir {

    public static String aRomano(int num) {

+       if (num > 10)
+           return "X" + aRomano(num - 10);

        if (num == 10) return "X";
        if (num == 9) return "IX";

        if (num > 5)
            return "V" + aRomano(num - 5);

        if (num == 5) return "V";
        if (num == 4) return "IV";

        if (num > 1)
            return "I" + aRomano(num - 1);

        return "I";

    }
}
```

**Rafactorización**. Generalizamos, eliminando código repetido. Usamos
un par de arrays en los que guardamos los números y las letras romanas
asociadas. Y usamos una variable `pos` con la que vamos recorriendo el
array:

```java
public class Convertir {

    static String[] letras = {"X", "IX", "V", "IV", "I"};
    static int[] nums = {10, 9, 5, 4, 1};

    public static String aRomano(int num) {
        int pos = 0;

        if (num > nums[pos])
            return letras[pos] + aRomano(num - nums[pos]);
        if (num == nums[pos]) return letras[pos];

        pos = pos + 1;

        if (num == nums[pos]) return letras[pos];

        pos = pos + 1;

        if (num > nums[pos])
            return letras[pos] + aRomano(num - nums[pos]);
        if (num == nums[pos]) return letras[pos];

        pos = pos + 1;

        if (num == nums[pos]) return letras[pos];

        pos = pos + 1;

        if (num > nums[pos])
            return letras[pos] + aRomano(num - nums[pos]);
        return letras[pos];

    }
}
```

**Refactorización**. En la que eliminamos el código repetido usando un
bucle que va moviendo `pos`. Lo que hace este bucle es buscar la letra
romana estrictamente menor o igual que el número que queremos
convertir:

```java
public class Convertir {

    static String[] letras = {"X", "IX", "V", "IV", "I"};
    static int[] nums = {10, 9, 5, 4, 1};

    public static String aRomano(int num) {
        int pos = 0;
        String romano = "";

        while (pos <= 4) {
            // Buscamos la letra romana que es estrictamente
            // menor que el número que queremos convertir

            if (num > nums[pos]) {
                romano = letras[pos] + aRomano(num - nums[pos]);
                break;
            }
            if (num == nums[pos]) {
                romano = letras[pos];
                break;
            }
            pos = pos + 1;
        }

        return romano;
    }
}
```

**Otra refactorización**, para quitar el caso especial del `==`. Lo
solucionamos haciendo que cuando el número coincida con la letra
también se llame a la recursión, y haciendo que la llamada devuelva
una cadena vacía. Basta con poner el caso base de que si el número es
`0` se devuelva la cadena vacía.

También se quita el código repetido del número `4` que hace del límite
del bucle. Realmente es algo repetido, porque se está refiriendo a la
longitud del array de letras.

```java
public class Convertir {

    static String[] letras = {"X", "IX", "V", "IV", "I"};
    static int[] nums = {10, 9, 5, 4, 1};

    public static String aRomano(int num) {
        int pos = 0;
        String romano = "";

        if (num == 0) 
            return "";
        else {
            while (pos <= nums.length) {
                // Buscamos la letra romana que es estrictamente
                // menor que el número que queremos convertir
                
                if (num >= nums[pos]) {
                    // En el caso de que num == nums[pos], se llamará
                    // a aRomano(0), que devolverá la cadena vacía
                    romano = letras[pos] + aRomano(num - nums[pos]);
                    break;
                }
                pos = pos + 1;
            }
            return romano;
        }
    }
}
```

### Ciclo 12 ###

El código anterior funciona para todos los números romanos hasta el
39. Lo comprobamos con un test, que compruebe varios números. Por
ejemplo el 18, el 34 y el 39:


Test:

```java
    @Test
    public void testConvierte18_34_39() {
        assertEquals("XVIII", Convertir.aRomano(18));
        assertEquals("XXXIV", Convertir.aRomano(34));
        assertEquals("XXXIX", Convertir.aRomano(39));
    }
```

El código existente pasa este test.

Escribimos un nuevo test para añadir una nueva letra y número a los arrays:

Nuevo test:

- `40` -> `XL` 

Código:

```diff
public class Convertir {

-   static String[] letras = {"X", "IX", "V", "IV", "I"};
-   static int[] nums = {10, 9, 5, 4, 1};
+   static String[] letras = {"XL", "X", "IX", "V", "IV", "I"};
+   static int[] nums = {40, 10, 9, 5, 4, 1};

    public static String aRomano(int num) {
        int pos = 0;
        String romano = "";

        if (num == 0)
            return "";
        else {
            while (pos <= nums.length) {
                // Buscamos la letra romana que es estrictamente
                // menor que el número que queremos convertir

                if (num >= nums[pos]) {
                    romano = letras[pos] + aRomano(num - nums[pos]);
                    break;
                }
                pos = pos + 1;
            }
            return romano;
        }
    }
}
```


### Ciclo 13 ###

Escribimos un nuevo test para introducir la letra `L` correspondiente
al número `50`. Puede ser cualquier número entre el 50 y el 90:

Test:

- `59` -> `LIX`

Código:

```diff
public class Convertir {

-   static String[] letras = {"XL", "X", "IX", "V", "IV", "I"};
-   static int[] nums = {40, 10, 9, 5, 4, 1};
+   static String[] letras = {"L", "XL", "X", "IX", "V", "IV", "I"};
+   static int[] nums = {50, 40, 10, 9, 5, 4, 1};

    public static String aRomano(int num) {
        int pos = 0;
        String romano = "";

        if (num == 0)
            return "";
        else {
            while (pos <= nums.length) {
                // Buscamos la letra romana que es estrictamente
                // menor que el número que queremos convertir

                if (num >= nums[pos]) {
                    romano = letras[pos] + aRomano(num - nums[pos]);
                    break;
                }
                pos = pos + 1;
            }
            return romano;
        }
    }
}
```

**Refactorización**. Vamos a aplicar el principio de la
responsabilidad única. El bucle está haciendo dos cosas: buscar la
letra estrictamente menor y concatenar el número romano. Lo separamos:


```java
public class Convertir {

    static int[] nums = {50, 40, 10, 9, 5, 4, 1};
    static String[] letras = {"L", "XL", "X", "IX", "V", "IV", "I"};

    public static String aRomano(int num) {
        int pos = 0;

        if (num == 0)
            return "";
        else {
            // Buscamos la letra romana que es estrictamente
            // menor que el número que queremos convertir
            while (pos <= nums.length) {
                if (num >= nums[pos]) {
                    break;
                }
                pos = pos + 1;
            }
            // Construimos el número romano
            return letras[pos] + aRomano(num - nums[pos]);
        }
    }
}
```

**Refactorización final**. Para que todo el código tenga un nivel de
abstracción uniforme y reducir el tamaño del método extraemos el
bucle, substituyéndolo por una llamada a una función privada. Ponemos
como nombre de la función un nombre con el mismo sentido que el
comentario:


```java
public class Convertir {

    static int[] nums = {50, 40, 10, 9, 5, 4, 1};
    static String[] letras = {"L", "XL", "X", "IX", "V", "IV", "I"};

    public static String aRomano(int num) {

        if (num == 0)
            return "";
        else {
            int pos = buscaLetraEstrictamenteMenorOIgual(num);
            return letras[pos] + aRomano(num - nums[pos]);
        }
    }

    private static int buscaLetraEstrictamenteMenorOIgual(int num) {
        int pos = 0;

        while (pos <= nums.length) {
            if (num >= nums[pos]) {
                break;
            }
            pos = pos + 1;
        }
        return pos;
    }
}
```


Y este es casi el código final resultante. Nos faltan añadir las
letras `XC` (`90`), `C` (`100`), `CD` (`400`), `D` (`500`), `CM`
(`900`) y `M` (`1000`). 

Añadimos tests para cada caso y vamos modificando el código hasta
llegar al algoritmo final:


```java
public class Convertir {

    static String[] letras = {"M", "CM", "D", "CD", "C", 
              "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    static int[] nums = {1000, 900, 500, 400, 100, 
              90, 50, 40, 10, 9, 5, 4, 1};

    public static String aRomano(int num) {

        if (num == 0)
            return "";
        else {
            int pos = buscaLetraEstrictamenteMenorOIgual(num);
            return letras[pos] + aRomano(num - nums[pos]);
        }
    }

    private static int buscaLetraEstrictamenteMenorOIgual(int num) {
        int pos = 0;

        while (pos <= nums.length) {
            if (num >= nums[pos]) {
                break;
            }
            pos = pos + 1;
        }
        return pos;
    }
}
```
    
