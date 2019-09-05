## Resumen de comandos Git

Comandos principales para trabajar con Git de forma individual. Los
comandos relacionados con el trabajo en equipo los veremos en la
práctica 2.

Al final del documento se incluyen enlaces a apartados del libro
[**Pro Git**](https://git-scm.com/book/en/v2). Es un libro totalmente
recomendable, deberías bajártelo y guardarlo como material de
aprendizaje y de referencia. Está disponible de forma gratuita en
múltiples versiones (PDF, eBook, HTML y mobi).

### Comandos básicos

- Configurar el usuario y dirección de correo en git:

    ```
    $ git config --global user.name "John Doe"
    $ git config --global user.email johndoe@example.com
    ```

- Inicializar git en un directorio:

        $ cd /ruta/a/mi/directorio
        $ git config --global user.name <nombre-usuario>
        $ git config --global user.email <email>
        $ git init
        $ git add .
        $ git commit -m "Versión inicial"

- Publicar por primera vez el repositorio local en el remoto (en GitHub):

        $ git remote add origin https://github.com/<usuario>/<nombre-repo>.git
        $ git push -u origin master

    El nombre del repositorio remoto será `origin` (nombre estándar
    del repositorio remoto en el caso en el que sólo haya
    uno). Subimos al repositorio la rama `master` (la rama por defecto
    que se crea al inicializar el repositorio local).

- Comprobar el estado del repositorio local: 

        $ git status

- Comprobar las diferencias entre los ficheros modificados en el
  directorio de trabajo y el último commit:

        $ git diff

- Añadir un fichero al
  [_stage_](http://programmers.stackexchange.com/questions/119782/what-does-stage-mean-in-git)
  (añadirlo para el próximo commit):

        $ git add <fichero o directorio>

    El área de _stage_ también se llama el _index_. Es muy importante
    entender su funcionamiento para trabajar con Git. El siguiente
    dibujo muestra su funcionamiento:

    <img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/staging-area.png" width="400px"/>


- Hacer un commit de los ficheros en el _stage_:

        $ git commit -m "Mensaje"

- Eliminar un fichero del _stage_ (si lo hemos añadido, pero al final
  decidimos no añadirlo en el siguiente commit):

        $ git reset HEAD <fichero>

- Se puede combinar en un único comando el `add` y el `commit` en
  ficheros ya añadidos al control de versiones:

        $ git commit -a -m "Mensaje"


    Se puede abreviar como 

        $ git commit -am "Mensaje"`

- Eliminar todos los cambios realizados en el directorio, volviendo al
  último commit:
  
        $ git reset --hard HEAD
        $ git clean -fd (si se ha añadido algún fichero)

- Publicar los cambios en el repositorio remoto:

        $ git push


- Consultar los mensajes de los commits (toda la historia de la rama
  actual). La opción `--oneline` muestra sólo la primera línea del
  mensaje, la opción `--graph` muestra el grafo de dependencias y la
  opción `--all`muestra el grafo completo, no sólo aquel en el que
  estamos (`HEAD`).

        $ git log [--oneline] [--graph] [--all]

- Comprobar las diferencias entre dos commits:

        $ git diff <hash-previo> <hash-nuevo>

    Devuelve las cambios que se han introducido desde el commit
    identificado por <hash-previo> y hasta el <hash-nuevo>.
    

### Ramas

Es muy importante entender que las ramas en Git son como etiquetas
móviles. La rama en la que estamos se actualiza de posición cada vez
que hacemos un nuevo commit. Git mantiene en la referencia `HEAD` la
rama actual.

<img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/ramas.png" width="500px"/>

- Crear una rama nueva:

        $ git checkout -b nueva-rama
        M   hola.txt (si hay cambios en el espacio de trabajo se llevan a la nueva rama)
        Switched to a new branch 'nueva-rama'

- Listar las ramas de un repositorio:

        $ git branch
        master
        * nueva-rama
        $ git commit -a -m "Confirmamos los cambios en la nueva rama"

- Moverse a otra rama:

        $ git checkout master
        Switched to branch 'master'

- Mostrar un fichero de una rama (o commit) dado:

        $ git show <commit o rama>:<nombre-fichero>

- Comparar dos ramas:

        $ git diff master nueva-rama

    El comando `git diff master nueva-rama` devuelve las diferencias
    entre las ramas `master` y `nueva-rama`: las modificaciones que
    resultarían de mezclar la rama `nueva-rama` en la rama `master`.

- **_Merge_ de ramas**: Mezclar la rama `nueva-rama` en la rama `master` (añade a la `master` los commits adicionales de la rama `nueva-rama`):

        $ git checkout master
        $ git merge [--no-ff] nueva-rama -m "Mensaje de commit"

    La opción `--no-ff` no hace un fast forward y mantiene separados
    los commits de la rama en el log de commits. Es útil para revisar
    la historia del repositorio.

- Si en la rama que se mezcla y en la actual hay cambios que afectan a
  las mismas líneas de un fichero, git detecta un conflicto y combina
  esas líneas conservando las dos versiones y añadiendo la información
  de la procedencia. Debemos resolver el conflicto: editarlos a mano y
  volver a hacer add y commit.

        $ git merge nueva-rama
        CONFLICT (content): Merge conflict in hola.txt  
        Automatic merge failed; fix conflicts and then commit the result.  
        # editar a mano el fichero con conflictos
        $ git commit -a -m "Arreglado el conflicto en el merge"
        $ git merge nueva-rama

    El comando `git status` después de un merge nos indica qué
    ficheros no se han mezclado y hay que editar manualmente.

- **_Rebase_ de una rama**. Si la rama master ha avanzado después de
  separar una rama alternativa y queremos incorporar esos cambios en
  la rama alternativa podemos hacer un `git rebase`:

        $ git checkout -b experiment
        # hacemos cambios
        $ git commit -m "Cambios en experiment"
        $ git checkout master  
        # hacemos cambios  
        $ git commit -a -m "Cambios en master"  
        $ git checkout experiment
        $ git rebase master  
        First, rewinding head to replay your work on top of it...  
        Applying: Corregido bug1  
        Applying: Corregido bug2

    <img src="https://raw.githubusercontent.com/domingogallardo/apuntes-mads/master/practicas/01-introduccion-play/imagenes/rebase.png" width="600px">

    El comando cambia la historia de la rama: primero la mueve al
    final de la rama master (_rewind head_) y a partir de ahí aplica
    los cambios propios de la rama.

    **IMPORTANTE**: No se debe hacer un _rebase_ de commits que
    existan en otros repositorios locales de compañeros. Al volver a
    aplicar los commits sobre los commits rebobinados, se cambia su
    número de hash (identificador) y se convierten en commits
    distintos.

    Una vez que hemos hecho el _rebase_ ya podemos añadir mover la
    rama `master` y tener una historia lineal:

        $ git checkout master
        $ git merge nueva-rama
        # Borramos la rama una vez mezclada
        $ git branch -d nueva-rama

- Igual que en el _merge_, al hacer un rebase pueden aparecer
  conflictos al hacer el _rebase_, basta con modificar los ficheros
  con conflictos, añadirlos y continuar el _rebase_:

        $ git rebase master
        CONFLICT (content): Merge conflict in <some-file>
        # hacemos git status para comprobar donde están los conflictos
        $ git status
        # Unmerged paths:
        # (use "git reset HEAD <some-file>..." to unstage)
        # (use "git add/rm <some-file>..." as appropriate to mark resolution)
        #
        # Editamos los ficheros para corregir los conflictos
        $ git add <some-file>
        $ git rebase --continue

    **IMPORTANTE**: Es posible integrar los cambios de una rama
    haciendo un _merge_ o haciendo un _rebase_. Ambas estrategias son
    correctas y cada una tiene sus pros y contras. Nosotros vamos a
    usar ambas para aprender su funcionamiento.

- Log en forma de grafo:

        $ git log --graph --oneline 

- Borrar una rama:

        $ git branch -d nueva-rama  
        Deleted branch nueva-rama (was c241d7b)

    Sólo podemos borrar de la forma anterior ramas en las que no
    estamos y que se han mezclado con alguna otra. El comando anterior
    no permite borrar ramas activas que tienen commits sin mezclar con
    otras.

- Borrar una rama descartando sus commits:

        $ git branch -D rama

- Subir una rama al repositorio remoto:

        $ git push -u origin <rama>

    **Para no tener que escribir la contraseña del repositorio remoto cada
    vez** puedes utilizar el siguiente comando que la guarda en una caché:

        $ git config --global credential.helper cache.

- Descargar una rama del repositorio remoto (origin, por ejemplo, el
  repositorio remoto por defecto)

        $ git fetch 
        $ git checkout -b <rama> origin/<rama>

- Consultar ramas locales y conexiones repositorio remoto (origin, por ejemplo)

        $ git remote show origin

- Subir todas las ramas y etiquetas:

        $ git push -u -all origin

    Al poner la opción -u hacemos tracking del repositorio remoto y
    las referencias quedan almacenadas en el fichero de configuración
    .git/config. A partir de ahora sólo es necesario hacer `git push`
    para subir los cambios en cualquiera de las ramas presentes.

- Borrar una rama en repositorio remoto:

        $ git push origin --delete <branchName>


### Modificar la historia

- Modificar el mensaje del último commit. Se abrirá un editor en el
  que modificar el mensaje. También se puede escribir el mensaje a
  mano:

        $ git commit --amend [--m "Nuevo mensaje"]

- Deshacer el último commit (sólo la acción del commit, dejando los cambios en el _stage_):

        $ git reset --soft HEAD^

- Descartar el último merge y volver a la situación anterior al hacer el merge:

        $ git reset --merge ORIG_HEAD

- Movernos atrás a un commit pasado, mirar los ficheros, crear una
  nueva rama allí (o no) y volver al commit actual:

        $ git checkout <hash> (o tag, por ejemplo v2.0)
        You are in 'detached HEAD' state.
        # Ahora estás en un detached HEAD
        $ git branch
        * (HEAD detached at 594b606)
        master
        $ git checkout -b v2.0.1
        Switched to a new branch 'v2.0.1'
        $ git branch
        master
        * v2.0.1
        $ git checkout master

- Movernos atrás a un commit pasado, descartando todos los commits
  realizados después (**peligroso**)

        $ git reset --hard <hash>

### Más información

Puedes encontrar más información en los siguientes documentos:

- _Pro Git_ - [Recording Changes to the Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- _Pro Git_ - [Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- _Pro Git_ - [Git Branching - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
- Tutorial de Atlassian - [Merging vs. Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
- _Pro Git_ - [Reset Demystified](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)
