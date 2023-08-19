package main

import "fmt"

func main() {
	var texto string
	texto = "Hola Mundo, Soy Maria \n" +
		"Este es el primer ejercicio de la tarea del curso de Lenguajes\n" +
		"trata sobre escribir un programa capas de procesar un texto\n" +
		"y contar la cantidad de caracteres, palabras y lineas que tiene.\n" +
		"Bien, este es el texto que se va a procesar.\n" +
		"Espero que funcione bien.\n" +
		"A continuacion los resultados:\n"

	//metodo para contar caracteres, palabras y lineas de texto
	var caracteres, palabras, lineas int
	caracteres = 0
	palabras = 0
	lineas = 0
	for i := 0; i < len(texto); i++ {
		if texto[i] == '\n' {
			lineas++
		} else if texto[i] == ' ' {
			palabras++
		} else {
			caracteres++
		}
	}
	//imprimir resultados
	println(texto)
	println("Cantidad de caracteres: ", caracteres)
	println("Cantidad de palabras: ", palabras)
	println("Cantidad de lineas: ", lineas)

	println("Bien ahora, probare ingresando un texto por la consola")
	println("Ingrese un texto: ")
	//metodo por consola
	var texto2 string
	fmt.Scanln(&texto2)
	var caracteres2, palabras2, lineas2 int
	caracteres2 = 0
	palabras2 = 0
	lineas2 = 0
	for i := 0; i < len(texto2); i++ {
		if texto2[i] == '\n' {
			lineas2++
		} else if texto2[i] == ' ' {
			palabras2++
		} else {
			caracteres2++
		}
	}
	println("Cantidad de caracteres: ", caracteres2)
	println("Cantidad de palabras: ", palabras2)
	println("Cantidad de lineas: ", lineas2)

	println("Adios")
}
