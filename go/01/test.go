package main

import (
	"fmt"
)

func main1() {
	fmt.Println("Hello, World! What is your name?")
}

func get_name() string {
	var temp string
	fmt.Scanln(&temp)
	return temp
}

func main() {
	main1()
	temp := get_name()
	fmt.Printf("Hi %s!\n", temp)
}
