package main

import (
	"fmt"
	"sort"
)

type producto struct {
	nombre   string
	cantidad int
	precio   int
}

type listaProductos []producto

var lProductos listaProductos
var lProductosMinimos listaProductos

const existenciaMinima int = 10

func (l *listaProductos) agregarProducto(nombre string, cantidad int, precio int) {
	pIdx, _ := l.buscarProducto(nombre)
	if pIdx == -1 {
		*l = append(*l, producto{nombre: nombre, cantidad: cantidad, precio: precio})
	} else {
		p := &(*l)[pIdx]
		p.cantidad += cantidad
		p.precio = precio
	}
}

func (l *listaProductos) agregarProductos(productos ...producto) {
	for _, p := range productos {
		l.agregarProducto(p.nombre, p.cantidad, p.precio)
	}
}

func (l *listaProductos) buscarProducto(nombre string) (int, int) {
	for i := 0; i < len(*l); i++ {
		if (*l)[i].nombre == nombre {
			return i, 0
		}
	}
	return -1, -1
}

func (l *listaProductos) venderProducto(nombre string, cantidad int) {
	idx, err := l.buscarProducto(nombre)
	if err == 0 {
		product := &(*l)[idx]
		product.cantidad -= cantidad
		if product.cantidad <= 0 {
			*l = append((*l)[:idx], (*l)[idx+1:]...)
			fmt.Printf("Producto %s se ha agotado y se ha eliminado de la lista.\n", nombre)
		}
	} else if err == -1 {
		fmt.Println("Producto no encontrado.")
	}
}

func (l *listaProductos) modificarPrecio(nombre string, precio int) {
	idx, err := l.buscarProducto(nombre)
	if err == 0 {
		p := &(*l)[idx]
		p.precio = precio
	} else if err == -1 {
		fmt.Println("Producto no encontrado.")
	}
}

func (l *listaProductos) listarProductosMinimos() listaProductos {
	for _, p := range *l {
		if p.cantidad <= existenciaMinima {
			lProductosMinimos = append(lProductosMinimos, p)
		}
	}
	return lProductosMinimos
}

// ------TAREA----
func (l *listaProductos) aumentarStockListMinimos(listaMinimos listaProductos) {
	for i, p := range *l {
		for _, minimo := range listaMinimos {
			if p.nombre == minimo.nombre {
				cantidadAComprar := existenciaMinima - p.cantidad
				(*l)[i].cantidad += cantidadAComprar
				fmt.Printf("Aumentando el stock de: %s\n", p.nombre)
			}
		}
	}
}

// Ordenar lista de productos por precio utilizando sort
func (l *listaProductos) ordenarPorPrecio() {
	sort.Slice(*l, func(i, j int) bool {
		return (*l)[i].precio < (*l)[j].precio
	})
}

func llenarDatos() {
	lProductos.agregarProducto("arroz", 15, 2500)
	lProductos.agregarProducto("frijoles", 4, 2000)
	lProductos.agregarProducto("leche", 8, 1200)
	lProductos.agregarProducto("café", 12, 4500)
}

func main() {
	llenarDatos()
	fmt.Println("Lista de productos: ")
	fmt.Println(lProductos)
	fmt.Println("Vendiendo productos: ")
	lProductos.venderProducto("arroz", 5)
	lProductos.venderProducto("frijoles", 2)
	fmt.Println("Lista de productos actualizada: ")
	fmt.Println(lProductos)
	fmt.Println("\nModificando precios y agregando productos: ")
	lProductos.modificarPrecio("leche", 1500)
	lProductos.agregarProducto("huevos", 30, 500)
	lProductos.agregarProducto("pan", 20, 1000)
	fmt.Println("\nLista de productos actualizada: ")
	fmt.Println(lProductos)
	fmt.Println("\nLista de productos minimos: ")
	fmt.Println(lProductos.listarProductosMinimos())
	fmt.Println("\nAumentando stock de productos minimos: ")
	lProductos.aumentarStockListMinimos(lProductosMinimos)
	fmt.Println("\nLista de productos actualizada: ")
	fmt.Println(lProductos)
	fmt.Println("\nOrdenando lista de productos por precio: ")
	lProductos.ordenarPorPrecio()
	fmt.Println(lProductos)
}
