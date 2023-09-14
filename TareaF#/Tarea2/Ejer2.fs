module Ejer2
let rec filtroSubCadenas (subcadena: string) (listaCadenas: string list) =
    match listaCadenas with
    | [] -> []
    | cabeza::cola ->
        if cabeza.Contains(subcadena) then
            cabeza :: (filtroSubCadenas subcadena cola)
        else
            filtroSubCadenas subcadena cola

let resultado = filtroSubCadenas "la" ["la casa"; "el perro"; "pintando la cerca"]
printfn "%A" resultado


