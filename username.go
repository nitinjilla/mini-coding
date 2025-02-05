package main

import "fmt"

type gitUser struct {
	name string
}

func (g *gitUser) setUserName(s string) {
	g.name = s
}

func main() {

	g := &gitUser{
		name: "",
	}

	if g.name == "" {
		fmt.Printf("GitHub username is <empty>\n")
		g.setUserName("@nitinjilla")
		fmt.Printf("GitHub username set to %s\n", g.name)
	} else {
		fmt.Printf("GitHub username is %s\n", g.name)
	}

}
