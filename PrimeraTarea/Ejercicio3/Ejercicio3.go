package main

import (
	"fmt"
)

func rotateArray(arrRo []string, nRotacion int, sentido int) {
	fmt.Println("Si el sentido es 0, se rota a la izquierda, si es 1, se rota a la derecha")
	fmt.Println("Rotación:", nRotacion, "veces hacia", sentido)
	for i := 0; i < nRotacion; i++ {
		if sentido == 0 {
			// Rotación a la izquierda
			temp := arrRo[0]
			for j := 0; j < len(arrRo)-1; j++ {
				arrRo[j] = arrRo[j+1]
			}
			arrRo[len(arrRo)-1] = temp
		} else {
			// Rotación a la derecha
			temp := arrRo[len(arrRo)-1]
			for j := len(arrRo) - 1; j > 0; j-- {
				arrRo[j] = arrRo[j-1]
			}
			arrRo[0] = temp
		}
	}

}

func main() {
	arr := []string{"a", "b", "c", "d", "e"}
	fmt.Println("Arreglo original:", arr)
	rotateArray(arr, 6, 0)
	fmt.Println("Arreglo después:", arr)

}
