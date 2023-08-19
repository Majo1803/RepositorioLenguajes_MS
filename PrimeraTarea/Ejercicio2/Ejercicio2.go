package main

import "fmt"

func main() {
	var central int //almacena el numero de asteriscos de la fila central
	fmt.Println("Ingrese el numero de asteriscos para la fila central, debe ser una cantidad impar positiva: ")
	fmt.Scanln(&central)
	var impares []int //almacena cuales son los numeros impares que existen entre 1 y el numero central
	for i := 1; i <= central; i++ {
		if i%2 != 0 {
			impares = append(impares, i)
		}
	}
	//imprime la figura por mitades
	for i := 0; i < len(impares); i++ {
		for j := 0; j < (central-impares[i])/2; j++ {
			fmt.Print(" ")
		}
		for j := 0; j < impares[i]; j++ {
			fmt.Print("*")
		}
		fmt.Println()
	}
	for i := len(impares) - 2; i >= 0; i-- {
		for j := 0; j < (central-impares[i])/2; j++ {
			fmt.Print(" ")
		}
		for j := 0; j < impares[i]; j++ {
			fmt.Print("*")
		}
		fmt.Println()
	}

}
