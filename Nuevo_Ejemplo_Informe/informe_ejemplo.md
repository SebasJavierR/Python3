
<div style=" margin-top:3em; 
             margin-bottom:2.6em ">
    <div style="text-align:center;">
        <h1 style="border-bottom: 1px solid gold;">
            Informe de Ejemplo <br> 
            Juego Nim <br>
        </h1>
        <h3>
            75.40 Algoritmos y Programacion I<br>
            Cátedra Essaya<br>
        </h3>
    </div>
    <h4 style=" font-weight:300;
                margin-top:3em;">
        Alumno: Marty McFly<br> 
        Padrón: 101985 <br>
        Corrector: Emmett Brown
    </h4>
</div>

## Dificultades encontradas

* La manera de representar los datos del tablero, de manera lógica.
* La metodología para mostrar el tablero de la manera pedida por el enunciado.
* La _inteligencia artificial_ del jugador _computadora_

## Resolución

###  Matriz

La primer forma que salta a la mente a la hora de representar los datos es la trivial: una
matriz (o lista de listas). Esto tiende a ser bastante simple: un usuario dice que quiere N pilas,
entonces se crean N listas, y por cada una se va pidiendo la cantidad de fichas, agregando esa
cantidad de fichas (sea como fuera que las vayamos a representar, por ejemplo, ’O’).

Este método tiene la ventaja de ser una solución bastante simple. La desventaja que tiene
es la cantidad de espacio de memoria utilizado: teniendo N pilas, suponiendo que cada pila
tiene M fichas, se está consumiendo lugar para N*M valores (del tipo de dato a guardar cor-
respondiente). Ésto es claramente ineficiente, puesto que no nos interesa tener las fichas en
sı́ sino cuántas fichas tiene cada pila. 

Por esto surgió una segunda implementación posible: en vez de tener una matriz, utilizar una lista, que
tenga en orden la cantidad de fichas que le quedan a una determinada pila. Cuando el usuario
selecciona una pila para sacarle k fichas, simplemente restamos la cantidad k al actual (previas validaciones correspondientes). Por lo que se puede observar, la forma de tratar lógicamente al
tablero es bastante simple.
Se utilizo, por las razones antes mencionadas, la segunda implementación.

### Inteligencia Artificial

Para la inteligencia artificial, se eligió la pila de mayor cantidad de fichas (si hay más de una con esa cantidad, se elije la primera), y de esa pila se sacan todas las fichas, exceptuando una, a menos que sólo quedara una ficha en esa pila, o sólo quedara una pila con fichas (en cuyo caso se sacan todas las fichas). La idea es bastante simple, pero vislumbra un tipo de estrategia válida (sin recurrir simplemente a sacar una cantidad de fichas aleatoria de una pila aleatoria).
