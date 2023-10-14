//printFUCK, just because

package main

import (
	"errors"
	"fmt"
)

func main() {

	//fuck := []byte{70, 85, 67, 75, 33}
  
	fuck := make([]byte, 0, 5)

    fmt.Println("Guess the ASCII to print the word 'FUCK!' One character at a time.")
    
	for i := 0; i < (cap(fuck)); i++ {

	var a byte       
	_, err := fmt.Scan(&a)
        if err != nil{
            fmt.Println(err)
        }
		fuck = append(fuck, a)
	}

	opfuck, err := printFUCK(fuck)

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(opfuck)
	}

}

func printFUCK(m []byte) (fuck string, err error) {

	var (
		errEmptyString = errors.New("Empty string")
		errNotTheWord  = errors.New("Not the word.")
	)

	if string(m) == "" {
		err = errEmptyString
	} else if string(m) != "FUCK!" {
        fmt.Println(string(m))
		err = errNotTheWord
	} else {
		fuck = string(m)
	}

	return fuck, err

}
