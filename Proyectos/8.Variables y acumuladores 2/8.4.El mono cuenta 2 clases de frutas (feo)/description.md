#Actividad 8.4. El mono cuenta 2 clases de frutas

En esta actividad la idea es que el mono cuente las bananas y las manzanas, y las tilde como contadas cuando termina.
Para eso, hacen falta 2 variables.

Pero resulta que como las variables solo sirven dentro del procedimiento que las asigna, la división en subtareas es
más complicada.
Para poder dividir en subtareas, hay que recorrer 3 veces el escenario: una para contar las manzanas, una para contar
las bananas, y una para tildar (se podría hacer recorriendo una vez, pero sin dividir en subtareas, y el código quedaría
MUY feo).

Además, para poder contar las frutas en todo el escenario, el mono debe moverse. Pero como el propósito es informar la
cantidad, además de moverse, tiene que devolver el resultado. Entonces, hace falta una herramienta nueva: las funciones
con procesamiento.

<center>
![El escenario final]
</center>

> **Funciones con procesamiento**
>
> Una **función con procesamiento** describe un valor que es el resultado de una serie de acciones (por ejemplo, contar
> las frutas). Lo interesante en Gobstones es que las acciones que realiza una función con procesamiento no es real, sino
> imaginario; o sea, la función NO modifica para nada el escenario.
> Probá, para ver cómo funciona.

[Enunciado en PDF][PDF]

[PDF]: 
https://raw.githubusercontent.com/gobstones/laprogramacionysudidactica2/master/Proyectos/