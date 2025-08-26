
import requests

# Using http://localhost  wont work
LOCAL_URL = "http://127.0.0.1:5000/graphql"
headers = {"Content-Type": "application/json"}

# List all users QUERY operation
gquery = """
query {
    users {
        id 
        username 
        email 
    }
}
"""

qvariables = None
query_params = {"query": gquery, "variables": qvariables}

# resp = requests.post(url=LOCAL_URL, json=query_params, headers=headers)
# if resp.status_code == 200:
#     data = resp.json()
#     print(data)
# else:
#     print("STATUS", resp.status_code)
#     print(resp.text)


# Fetch a specific user QUERY operation
fetch_query = """
query GetUser($username: String!) {
    user(username: $username) {
        id 
        username 
        email 
        fname
        lname
    }
}
"""
fetch_variables = {"username": "nickyy"}
fetch_query_params = {"query": fetch_query, "variables": fetch_variables}

resp = requests.post(url=LOCAL_URL, json=fetch_query_params, headers=headers)
if resp.status_code == 200:
    data = resp.json()
    print(data)
else:
    print("STATUS", resp.status_code)
    print(resp.text)

# UPSERT/MUTATION operation
mparams = """
mutation CreateUser($username: String!, $email: String!, $fname: String!, $lname: String!) {
  createUser(username: $username, email: $email, fname: $fname, lname: $lname) {
    user {
      id
      username
      email
      fname
      lname
    }
  }
}
"""
mvariables = {
    "username": "majorroger",
    "email": "roger@goodangadi.com",
    "fname": "Major",
    "lname": "Roger"
}
mutation_params = {"query": mparams, "variables": mvariables}

# resp = requests.post(url=LOCAL_URL, json=mutation_params, headers=headers)
# if resp.status_code == 200:
#     data = resp.json()
#     print(data)
# else:
#     print("STATUS", resp.status_code)
#     print(resp.text)
