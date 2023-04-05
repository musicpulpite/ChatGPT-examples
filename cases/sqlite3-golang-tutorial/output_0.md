To write a simple query and run an insert using `github.com/mattn/go-sqlite3`, the following steps need to be taken:

1. Import the required packages for SQLite3 and database access:
```go
import (
    "database/sql"
    "fmt"
    "log"
    _ "github.com/mattn/go-sqlite3"
)
```

2. Open a database connection using `sql.Open` which takes two arguments, the driver name and the data source name (DSN). In this case, we are using a file-based database, so the DSN is just the file path where our database file will be stored.

```go
db, err := sql.Open("sqlite3", "./example.db")
if err != nil {
    log.Fatal(err)
} 
defer db.Close()
```

3. Create a table in the database using `db.Exec`. In this example, we are creating a `users` table with columns `id`, `name`, and `email`.

```go
sqlStmt := `
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    );
`
_, err = db.Exec(sqlStmt)
if err != nil {
    log.Printf("%q: %s\n", err, sqlStmt)
    return
}
```

4. Insert some rows into the `users` table using `db.Exec`. In this example, we are inserting two rows.

```go
sqlStmt := `
    INSERT INTO users(name, email) VALUES
        ('John Doe', 'john.doe@example.com'),
        ('Jane Doe', 'jane.doe@example.com');
`
_, err = db.Exec(sqlStmt)
if err != nil {
    log.Printf("%q: %s\n", err, sqlStmt)
    return
}
```

5. Query the rows using `db.Query` and iterate over the results:

```go
rows, err := db.Query("SELECT id, name, email FROM users")
if err != nil {
    log.Fatal(err)
}
defer rows.Close()
for rows.Next() {
    var id int
    var name string
    var email string
    err := rows.Scan(&id, &name, &email)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("id=%d, name=%s, email=%s\n", id, name, email)
}
```

The above code will create a SQLite database file (if it doesn't exist) called `example.db`, create a `users` table in the database, insert two rows into the `users` table, and then query the rows and print out the results.