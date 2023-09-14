module RutaCorta

open System
open System.Collections.Generic

// Definición del grafo para el laberinto
let grafoLaberinto = [
    ("0", ["1"; "3"]);
    ("1", ["0"; "2"]);
    ("2", ["1"; "3"]);
    ("3", ["0"; "2"; "4"]);
    ("4", ["3"; "5"]);
    ("5", ["4"; "6"]);
    ("6", ["5"])
]

// Función para generar vecinos
let vecinos nodo grafo =
    match List.tryFind (fun (n, _) -> n = nodo) grafo with
    | Some (_, neighbors) -> neighbors
    | None -> []

// Función principal de búsqueda en profundidad
let rec prof2 ini fin grafo =
    let rec prof_aux ruta grafo =
        match ruta with
        | [] -> []
        | current::rest ->
            if List.head current = fin then
                List.rev current
            else
                let vecinosDeNodo = vecinos (List.head current) grafo
                let nuevasRutas = List.map (fun vecino -> vecino::current) vecinosDeNodo
                let rutasFiltradas = List.filter (fun ruta -> not (List.contains fin ruta)) nuevasRutas
                prof_aux (rest @ rutasFiltradas) grafo
    prof_aux [[ini]] grafo

// Función para imprimir la ruta
let imprimirRuta ruta =
    printfn "Ruta encontrada:"
    ruta |> List.iter (printf "%s -> ")
    printfn "Fin"

[<EntryPoint>]
let main argv =
    let rutaMasCorta = prof2 "0" "6" grafoLaberinto
    match rutaMasCorta with
    | [] -> printfn "No se encontró una ruta."
    | _ -> imprimirRuta rutaMasCorta
    0 // Salir del programa
