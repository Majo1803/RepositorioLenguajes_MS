sub_cadenas(Subcadena, Lista, Filtradas) :-
    sub_cadenas_aux(Subcadena, Lista, Filtradas).

sub_cadenas_aux(_, [], []).
sub_cadenas_aux(Subcadena, [Cadena|Resto], Filtradas) :-
    sub_atom(Cadena, _, _, _, Subcadena),
    sub_cadenas_aux(Subcadena, Resto, RestFiltradas),
    Filtradas = [Cadena|RestFiltradas].
sub_cadenas_aux(Subcadena, [_|Resto], Filtradas) :-
    sub_cadenas_aux(Subcadena, Resto, Filtradas).

