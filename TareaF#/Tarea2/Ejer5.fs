module Ejer5
open System.Collections.Generic

type Grafo = Dictionary<int, List<int>>

let laberintoAGrafo laberinto =
    let numRows = Array2D.length1 laberinto
    let numCols = Array2D.length2 laberinto
    let grafo = Dictionary()

    let nodoId x y = x * numCols + y

    let rec esSeguro x y =
        x >= 0 && x < numRows && y >= 0 && y < numCols && laberinto.[x, y] <> 1

    for x = 0 to numRows - 1 do
        for y = 0 to numCols - 1 do
            if esSeguro x y then
                let nodo = nodoId x y
                let vecinos =
                    [ (x - 1, y); (x + 1, y); (x, y - 1); (x, y + 1) ]
                    |> List.filter (fun (nx, ny) -> esSeguro nx ny)
                    |> List.map (fun (nx, ny) -> nodoId nx ny)
                grafo.Add(nodo, vecinos)
    grafo

let bfs grafo inicio destino =
    let cola = Queue()
    let visitado = HashSet()

    let rec bfsAux nodo camino =
        if nodo = destino then
            camino
        else
            match grafo.TryGetValue(nodo) with
            | true, vecinos ->
                vecinos
                |> List.filter (fun vecino -> not (visitado.Contains(vecino)))
                |> List.iter (fun vecino ->
                    visitado.Add(vecino)
                    cola.Enqueue((vecino, camino @ [vecino]))
                )
                if cola.Count > 0 then
                    let (nuevoNodo, nuevoCamino) = cola.Dequeue()
                    bfsAux nuevoNodo nuevoCamino
                else
                    []
            | _ -> []

    if grafo.ContainsKey(inicio) then
        visitado.Add(inicio)
        cola.Enqueue((inicio, [inicio]))
        bfsAux inicio [inicio]
    else
        []

// Ejemplo de uso:
let laberinto =
    [| [| 0; 2; 0; 0; 1 |]
       [| 0; 3; 0; 1; 0 |]
       [| 0; 1; 0; 1; 2 |]
       [| 0; 2; 0; 0; 0 |]
       [| 0; 0; 0; 1; 0 |] |]

let grafo = laberintoAGrafo laberinto
let inicio = 0
let destino = 24

let rutaMasCorta = bfs grafo inicio destino

if List.isEmpty rutaMasCorta then
    printfn "No se encontró una ruta."
else
    printfn "Ruta más corta encontrada: %A" rutaMasCorta
