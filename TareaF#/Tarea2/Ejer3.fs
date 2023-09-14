module Ejer3
let n_esimo n lista =
    let indices = [0..List.length lista - 1]
    let elementos = List.map (fun i -> List.nth lista i) indices
    match List.tryFindIndex (fun (i, _) -> i = n) (List.zip indices elementos) with
    | Some index -> 
        let (_, resultado) = List.nth (List.zip indices elementos) index
        Some resultado
    | None -> None

let resultado1 = n_esimo 2 [1;2;3;4;5]
let resultado2 = n_esimo 3 [1;2;3;4;5]
let resultado3 = n_esimo 6 [1;2;3;4;5]

printfn "%A" resultado1 
printfn "%A" resultado2 
printfn "%A" resultado3 
