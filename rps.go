//Rock, paper, scissors in GO

//Author: Nitin Jilla

package main

import (
	"fmt"
	"math/rand"
	"slices"
	"strings"
)

func main() {

	var pName, pChoice string

	rps := []string{"rock", "paper", "scissors"}
	scores := map[string]int{"Computer": 0, pName: 0}

	fmt.Scanf("Enter player name: \n", &pName)

	fmt.Printf("Computer v/s %s\n", pName)
	for counter := 1; counter <= 5; counter++ {
		fmt.Printf("Game %d:\n", counter)
		fmt.Scanf("Enter rock, paper or scissors: %s\n", &pChoice)

		pChoice = strings.ToLower(pChoice)
		pChoice = strings.TrimSpace(pChoice)
		fmt.Printf("You played %s.\n", pChoice)

		cChoice := rand.Intn(len(rps))
		fmt.Printf("Computer played %s.\n", rps[cChoice])

		switch slices.Contains(rps, pChoice) {

		case cChoice == slices.Index(rps, pChoice):
			fmt.Printf("Game %d: Tie!\n", counter)

		case cChoice == 0 && slices.Index(rps, pChoice) == 2:
			scores["Computer"] += 1
			fmt.Printf("Game %d: Computer won!\n", counter)

		case cChoice == 2 && slices.Index(rps, pChoice) == 0:
			scores[pName] += 1
			fmt.Printf("Game %d: %s won!\n", counter, pName)

		case cChoice < slices.Index(rps, pChoice):
			scores[pName] += 1
			fmt.Printf("Game %d: %s won!\n", counter, pName)

		case cChoice > slices.Index(rps, pChoice):
			scores["Computer"] += 1
			fmt.Printf("Game %d: Computer won!\n", counter)

		default:
			fmt.Println("\nEnter a valid choice")

		}

		fmt.Println("\n--------------------------------")
	}

	if scores["Computer"] == scores[pName] {
		fmt.Printf("This game was a tie!")

	} else if scores["Computer"] > scores[pName] {
		fmt.Printf("Computer %v - %v %s \n", scores["Computer"], scores[pName], pName)
		fmt.Println("Computer won!")

	} else {
		fmt.Printf("Computer %v - %v  %s \n", scores["Computer"], scores[pName], pName)
		fmt.Printf("%s won!", pName)

	}

}
