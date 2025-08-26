# ishaminfo
Ishamibrahim info website built using flask

## Also inlcudes a GRaphQL application
* Open graphiQL UI by running 
  * `python app.py`
* This should run by default in 
  * `http://127.0.0.1:5000`
* Go to `http://127.0.0.1:5000/graphql`
* Run commands as shown below

### 1. Fetch all items example (query)
```json lines
{	
  query: users {
    id 
  	username 
  	email 
  	fname
    lname
	}
}
```
### 2. Fetch a specific user using username example (query)
```json lines
{	
  query: user (username: "charlie1"){
    id 
  	username 
  	email 
  	fname
    lname
	}
}
```
### 3. Create item example (mutation)
```json lines

mutation {
  createUser(username: "majorroger2",
  email: "roger2@goodangadi.com",
  fname: "Major",
  lname: "Roger"
  ) {
    user {
      id
      username
      email
      fname
      lname
    }
  }
}

```

### 4. Update item example (mutation)
```json lines
mutation UpdateUser($id: ID!, $username: String, $fname: String, $lname: String) {
    updateUser(id: $id, username: $username, fname: $fname, lname: $lname) {
      user {
        id
        username
        fname
        lname
      }
    }
}
```
In the *Query variables* section at the bottom of the screen, add the updates in json form
```json lines
{
  "id": 6,
  "username": "thedarkknight",
  "fname": "Bruce", 
  "lname": "Wayne"
}
```
### 5. Delete item example (mutation)
```json lines

```
