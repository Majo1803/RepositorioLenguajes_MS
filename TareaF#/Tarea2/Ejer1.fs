module Ejer1

let desplazar direccion n lista =
    let len = List.length lista

    let rec eliminarYRellenar n lista =
        match n with
        | 0 -> lista
        | _ -> 
            match lista with
            | [] -> []
            | _::xs -> 0 :: (eliminarYRellenar (n-1) xs)

    match direccion with
    | "izq" when n > 0 -> 
        let eliminados = List.take n lista
        let izquierda = eliminarYRellenar n eliminados
        List.append (List.skip n lista) izquierda
    | "der" when n > 0 -> 
        let eliminados = List.take n lista
        let derecha = eliminarYRellenar n eliminados
        List.append derecha (List.skip n lista)
    | _ -> List.replicate len 0

let main =
    let lista1 = [1;2;3;4;5]
    let resultado1 = desplazar "izq" 3 lista1
    let resultado2 = desplazar "der" 2 lista1
    let resultado3 = desplazar "izq" 5 lista1

    printfn "Desplazar izquierda 3 posiciones: %A" resultado1
    printfn "Desplazar derecha 2 posiciones: %A" resultado2
    printfn "Desplazar izquierda 6 posiciones: %A" resultado3
