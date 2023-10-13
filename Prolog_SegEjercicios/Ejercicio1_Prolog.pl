% Laberinto
conectado(20,26,2).
conectado(26,27,3).
conectado(27,28,1).
conectado(28,29,4).
conectado(29,23,2).
conectado(23,17,3).
conectado(17,11,4).
conectado(11,5,2).
conectado(1,7,3).
conectado(5,6,1).
conectado(28,34,2).
conectado(34,35,3).
conectado(35,36,2).
conectado(36,30,4).
conectado(30,24,3).
conectado(24,18,2).
conectado(18,12,1).
conectado(32,31,2).
conectado(31,25,3).
conectado(25,19,2).
conectado(34,33,1).
conectado(33,32,2).
conectado(32,f,4).

% Encontrar una ruta entre dos puntos con peso
ruta(X, Y, [X, Y], Peso) :-
    conectado(X, Y, Peso).
ruta(X, Y, [X | RestoRuta], PesoTotal) :-
    conectado(X, Z, Peso),
    ruta(Z, Y, RestoRuta, PesoResto),
    PesoTotal is Peso + PesoResto.

% Encontrar la ruta más corta entre dos puntos
ruta_mas_corta(X, Y, RutaMasCorta, DistanciaMasCorta) :-
    findall((Ruta, Distancia), ruta(X, Y, Ruta, Distancia), RutasConDistancias),
    sort(2, @=<, RutasConDistancias, [(RutaMasCorta, DistanciaMasCorta) | _]).
