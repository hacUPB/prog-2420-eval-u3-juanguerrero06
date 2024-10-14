[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Juan Sebastián Guerrero Giraldo
ID:  000541479
---
# Base de datos de un Cine
En este caso buscaremos por medio de un programa resolver el sistema de reservas de un cine cualquiera. Esto con el fin de reducir por completo perdidas a la hora de reservar un asiento, maximizando la eficiencia y el orden para que la experiecia de usuario sea siempre la mejor posibe.

## Alcance
En este caso, el programa se centrará solamente en reservar uno o más asientos de un cine generico (Definido previamente por mí) dentro una cartelera de una temporada de cintas cualquiera (Definida previamente por mí). La idea es que en una especie de matriz puedas elegir el puesto en el que quieres ver una de las peliculas disponibles. La matriz, según la gente vaya reservando se irá ocupando de forma que los asientos que ya se hayan reservado no se puedan pagar. 

Para la parte de la reservación de las sillas en el teatro la base de datos a utilizar en este caso sería una matriz, dado que me permite ordenar la silletería en Letras y Numeros, con filas de la A hasta la F (Siendo la fila A la que se encuentra al lado de la pantalla, y la F la que se encuentra al lado de la pared Trasera) y de 10 sillas por fila, de manera que:
[A1, A2, A3, ..., A10]. Luego un diccionario de listas (siendo estas últimas las matrices de las salas de cine con los asientos disponibles y los reservados) de modo que al hacer una reserva en cualquiera de estas listas, este elemento queda bloqueado, así, si se quiere volver a reservar en este, el programa avisa al usuario de que la reserva no se puede hacer dado que el asiento ya está ocupado. 

## Pseudocodigo
    Crear una lista de tres diccionarios que guardaran las peliculas disponibles y las salas de cine de cada una
    Crear una lista vacía para almacenar las reservas

    Mostrar_peliculas
        Funcion que imprime las peliculas disponibles en cartelera

    Mostrar_asientos
        Funcion que según la pelicula seleccionada imprime una matriz de asientos disponibles y ocupados

    Realizar_reserva
        Función en la que se elige la pelicula que se quiere ver, para luego de imprimir la matriz de asientos de la sala, elegir el asiento (Adicionalmente se corrobora si el asiento está disponible o no). Se indica el nombre y se guarda la reserva en una matríz vacía.

    Menu
        Con un bucle se crea un menú de 4 opciones, donde las primeras 3 de forma individual llaman a sus funciones correspondientes para realizar la acción necesaria


Notas
-- Falta comentar el código, falta el USERGUIDE, falta revisar PEP8 --