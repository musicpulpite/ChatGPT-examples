To use the `github.com/mattn/go-sqlite3` package, you need to first import it into your Go code. Here's a simple code to query and insert data.

```go
package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/mattn/go-sqlite3"
)

func main() {
	// Open database connection
	db, err := sql.Open("sqlite3", "./example.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Create table
	createTableSQL := `CREATE TABLE IF NOT EXISTS users (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
		"name" TEXT,
		"email" TEXT)`
	_, err = db.Exec(createTableSQL)
	if err != nil {
		log.Fatal(err)
	}

	// Insert data
	insertSQL := `INSERT INTO users(name, email) VALUES(?, ?)`
	res, err := db.Exec(insertSQL, "John Doe", "johndoe@example.com")
	if err != nil {
		log.Fatal(err)
	}

	// Get last inserted ID
	id, err := res.LastInsertId()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Last inserted ID: %d\n", id)

	// Query data
	querySQL := `SELECT * FROM users`
	rows, err := db.Query(querySQL)
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	// Iterate over rows
	for rows.Next() {
		var id int
		var name, email string
		err := rows.Scan(&id, &name, &email)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("id: %d, name: %s, email: %s\n", id, name, email)
	}
}
```

In this example, we first import the necessary packages including `database/sql` and `github.com/mattn/go-sqlite3`. 

Then, the database connection is opened and the `CREATE TABLE` statement is executed to create a `users` table with columns `id`, `name`, and `email`. The `IF NOT EXISTS` clause makes sure that the table is not created again if it already exists.

Next, we execute an `INSERT INTO` statement to insert a new user into the `users` table. We use prepared statements and placeholders (`?`) to avoid SQL injection attacks. We also use `db.Exec` instead of `db.Query` since we are not expecting any rows back from the database.

The `LastInsertId` method is used to get the ID of the last inserted row. 

Finally, we execute a `SELECT` statement using `db.Query` to retrieve all data from the `users` table. We use `rows.Scan` to retrieve each row's `id`, `name`, and `email` columns from the `rows` result set, and we print them out to the console.

That's it! This is a simple example of how to use `github.com/mattn/go-sqlite3` to query and insert data into a SQLite database with Go.