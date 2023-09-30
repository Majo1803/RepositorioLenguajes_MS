%Definir el predicado para sumar los elementos de la lista.
sumlist([], 0).  % La suma de una lista vac�a es 0.
sumlist([X|Xs], S) :- sumlist(Xs, S1), S is X + S1.

% Definir el predicado revisarlist/2.
revisarlist(List, Resultado) :- sumlist(List, Sum), Sum = Resultado.
