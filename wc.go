/* Use "go run wc.go".*/

package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/signal"

	"github.com/gorilla/mux"
)

var port string = ":8000"

func main() {
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt)

	r := mux.NewRouter()
	srv := http.Server{
		Addr:    port,
		Handler: r,
	}
	r.HandleFunc("/", homePage)

	go func() {
		err := srv.ListenAndServe()
		if err != nil {
			log.Println(err)
		}
	}()

	<-c
	log.Println("Shutting down...")
	srv.Shutdown(context.Background())
}

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome!\n")
}
