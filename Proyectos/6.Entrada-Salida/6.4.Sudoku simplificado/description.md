#Actividad 6.4. Sudoku simplificado

En esta actividad tenés que construir un programa que permita jugar a una versión simplificada del Sudoku.
El objetivo del juego es completar la grilla con los números del 1 al 3, sin que se repita ningún número en ninguna fila 
ni ninguna columna. Podés hacer 2 versiones del programa; en ambas se debe permitir al jugador moverse por la grilla, 
e ingresar un número.

A) En la primera versión, más simple, el número puede ingresarse siempre

B) En la segunda, antes de ponerlo el programa debería verificar si el número es válido (por ejemplo, si toca el 
número 3 y ese número se puede poner en ese lugar, el número aparece; pero si no se puede poner en ese lugar, 
entonces no pasa nada).
¿Cómo harías para controlar que el dígito a ingresar es válido? 
Tendrías que mirar los demás dígitos de la fila y de la columna, para ver que no se repita. 
¿Qué herramienta podés usar para eso?

En las siguientes imágenes podés ver cómo se vería el tablero durante el juego, y cómo se vería al terminar, si hiciste 
todo bien.

<center>
![Un escenario durante el juego]()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Escenario de un juego exitoso]()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Escenario de un juego fallido]()
</center>

> **En Gobstones también hay eventos**
>
> Si indagás un poco vas a encontrar las definiciones de eventos, que se pueden usar en un programa interactivo.

[Enunciado en PDF][PDF]

[PDF]: https://raw.githubusercontent.com/gobstones/laprogramacionysudidactica2/master/Proyectos/Clase6/6.4.Sudoku%20simplificado/assets/resources/description.pdf "Enunciado de 'Sudoku simplificado' en PDF"
