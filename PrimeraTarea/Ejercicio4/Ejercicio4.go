package main

import (
	"fmt"
	"golang.org/x/exp/slices"
)

type Calzado struct {
	marca  string
	talla  int
	precio int
}
type ListaCalzados []Calzado

var lCalzados ListaCalzados

type CalzadoCantidad struct {
	calzado  *Calzado
	cantidad int
}
type ListaCalzadosCantidad []CalzadoCantidad

var lCalzadosCantidad ListaCalzadosCantidad

func (l *ListaCalzados) agregarCalzado(marca string, talla int, precio int) {
	idx := slices.IndexFunc(*l, func(c Calzado) bool { return c.marca == marca && c.talla == talla })
	if idx == -1 {
		if talla >= 34 && talla <= 44 {
			*l = append(*l, Calzado{marca, talla, precio})
		}
	}
	idx2 := slices.IndexFunc(lCalzadosCantidad, func(c CalzadoCantidad) bool { return c.calzado.marca == marca && c.calzado.talla == talla })
	if idx2 == -1 {
		lCalzadosCantidad = append(lCalzadosCantidad, CalzadoCantidad{&Calzado{marca, talla, precio}, 1})
	} else {
		lCalzadosCantidad[idx2].cantidad++
	}
}

func (l *ListaCalzados) ventaCalzado(marca string, talla int) {
	idx2 := slices.IndexFunc(lCalzadosCantidad, func(c CalzadoCantidad) bool {
		return c.calzado.marca == marca && c.calzado.talla == talla
	})
	if idx2 != -1 {
		// Disminuye el stock
		lCalzadosCantidad[idx2].cantidad--
		fmt.Println("Venta Realizada")
		// Verifica si el stock es 0 para eliminar el calzado
		if lCalzadosCantidad[idx2].cantidad == 0 {
			lCalzadosCantidad = append(lCalzadosCantidad[:idx2], lCalzadosCantidad[idx2+1:]...)
			fmt.Println("El calzado no está disponible")
		}
	}
}

func (l *ListaCalzados) mostrarCalzados() {
	for _, c := range lCalzadosCantidad {
		fmt.Println("Marca: ", c.calzado.marca, " Talla: ", c.calzado.talla, " Precio: ", c.calzado.precio, " Cantidad: ", c.cantidad)
	}
}

// main
func main() {
	//agrega calzados
	lCalzados.agregarCalzado("nike", 34, 1000)
	lCalzados.agregarCalzado("nike", 34, 1000)
	lCalzados.agregarCalzado("nike", 34, 1000)
	lCalzados.agregarCalzado("nike", 35, 1000)
	//muestra calzados
	fmt.Println("Calzados disponibles:")
	lCalzados.mostrarCalzados()
	//venta
	fmt.Println("Venta de calzados:")
	lCalzados.ventaCalzado("nike", 34)
	lCalzados.ventaCalzado("nike", 35)
	lCalzados.ventaCalzado("nike", 35)
	//muestra calzados
	fmt.Println("Stock de Calzados luego de la venta:")
	lCalzados.mostrarCalzados()
}
