// Saw an IG post about a similar snippet of code (written in Java) pushed to production. 
// This is just a GO version of that code.
// The below code provides the wrong result. This is just for fun. 

package main

import "fmt"

func main(){

	if areBooleansEqual(true, false) {
		fmt.Print("The boolean values are equal!")
	}else{
		fmt.Print("You think they are the same booleans values?")
	}
}


func areBooleansEqual(a, b bool) (c bool) {

	 if a == b {
	 	return false
	 }

	 return true
}