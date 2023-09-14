module RutaCorta

open System
open System.Collections.Generic
// grafo para el laberinto
let grafoLaberinto = [
    (1, [2; 7]); (2, [1; 3; 8]); (3, [2; 4; 9]);
    (4, [3; 10]); (5, [6; 11]); (6, [5; 12]);
    (7, [1; 13]); (8, [2; 9; 14]); (9, [3; 8; 15]);
    (10, [4; 16]); (11, [5; 17]); (12, [6; 18]);
    (13, [7; 14; 19; 20]); (14, [8; 13; 15; 21]); (15, [9; 14; 22]);
    (16, [10; 23]); (17, [11; 24]); (18, [12; 25]);
    (19, [13; 26]); (20, [14; 27]); (21, [15; 22]);
    (22, [21; 28]); (23, [16; 29]); (24, [17; 30]);
    (25, [18; 31]); (26, [19; 32]); (27, [20; 33]);
    (28, [22; 27; 34]); (29, [23; 35]); (30, [24; 36]);
    (31, [25; 32]); (32, [31; 33]); (33, [32; 34]);
    (34, [28; 33; 35; 36]); (35, [29; 34])
]

// vecinos
let vecinos nodo grafo =
    match List.tryFind (fun (n, _) -> n = nodo) grafo with
    | Some (_, neighbors) -> neighbors
    | None -> []

// búsqueda en profundidad
let rec prof2 ini fin grafo =
    let rec prof_aux ruta grafo =
        match ruta with
        | [] -> []
        | current::rest ->
            if List.head current = int fin then 
                List.rev current
            else
                let vecinosDeNodo = vecinos (List.head current) grafo
                let nuevasRutas = List.map (fun vecino -> vecino::current) vecinosDeNodo
                let rutasFiltradas = List.filter (fun ruta -> not (List.contains (int fin) ruta)) nuevasRutas 
                prof_aux (rest @ rutasFiltradas) grafo
    prof_aux [[int ini]] grafo 

// imprimir la ruta
let imprimirRuta ruta =
    printfn "Ruta encontrada:"
    ruta |> List.iter (fun node -> printf "%d -> " node)
    printfn "Fin"

[<EntryPoint>]
let main argv =
    let rutaMasCorta = prof2 "1" "6" grafoLaberinto
    match rutaMasCorta with
    | [] -> printfn "No se encontró una ruta."
    | _ -> imprimirRuta rutaMasCorta
    0 
