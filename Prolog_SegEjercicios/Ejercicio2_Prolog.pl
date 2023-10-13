muestra([a, b, c, d, e, f, g, h, i, j]).
persona(p1, [a, b, c, d, e, f, g, h, i, j]).
persona(p2, [a, b, x, d, e, f, g, h, i, j]).
persona(p3, [a, b, c, d, e, f, g, h, i, y]).

%Calcular el porcentaje de exactitud.
cromosoma_sujeto_candidato(CromosomaSujeto, CromosomaCandidato, PorcentajeExactitud) :-
    length(CromosomaSujeto, Longitud),
    length(CromosomaCandidato, Longitud),
    contar_coincidencias(CromosomaSujeto, CromosomaCandidato, Coincidencias),
    PorcentajeExactitud is (Coincidencias / Longitud) * 100.

contar_coincidencias([], [], 0).
contar_coincidencias([X|RestoSujeto], [X|RestoCandidato], Coincidencias) :-
    contar_coincidencias(RestoSujeto, RestoCandidato, RestoCoincidencias),
    Coincidencias is RestoCoincidencias + 1.
contar_coincidencias([_|RestoSujeto], [_|RestoCandidato], Coincidencias) :-
    contar_coincidencias(RestoSujeto, RestoCandidato, Coincidencias).

% Encontrar el más parecido
sujeto_mas_parecido(Muestra, Personas, SujetoParecido) :-
    MejorSujeto = no_encontrado,
    MejorPorcentaje = -1,
    encontrar_mejor_sujeto(Muestra, Personas, MejorSujeto, MejorPorcentaje),
    SujetoParecido = MejorSujeto.

% Encontrar mejor porcentaje de exactitud.
encontrar_mejor_sujeto(_, [], MejorSujeto, MejorPorcentaje) :-
    MejorSujeto = MejorSujeto,
    MejorPorcentaje = MejorPorcentaje.
encontrar_mejor_sujeto(Muestra, [Persona|RestoPersonas], MejorSujeto, MejorPorcentaje) :-
    cromosoma_sujeto_candidato(Muestra, Persona, Porcentaje),
    (Porcentaje > MejorPorcentaje ->
        encontrar_mejor_sujeto(Muestra, RestoPersonas, Persona, Porcentaje)
    ;
        encontrar_mejor_sujeto(Muestra, RestoPersonas, MejorSujeto, MejorPorcentaje)
    ).














