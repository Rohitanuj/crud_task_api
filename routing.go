package main

import (
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func HandlerRoutiong() {
	r := mux.NewRouter()
	r.HandleFunc("/employees", GetEmployees).Methods("GET")
	r.HandleFunc("/employee/{eid}", GetEmployeeById).Methods("GET")
	r.HandleFunc("/employee", createEmployee).Methods("POST")
	r.HandleFunc("/employee/{eid}", UpdateEmployee).Methods("PUT")
	r.HandleFunc("/employee/{eid}", DeleteEmployee).Methods("DELETE")
	log.Fatal(http.ListenAndServe(":8080", r))
}
