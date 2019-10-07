# Stores REST api

This is a REST api written in Python.  
It uses Flask, Flask-RESTful, Flask-JWT and FlaskSQLAlchemy.  
It is deployed at [Heroku.](https://stores-rest-api-bhombal.herokuapp.com)

The end points for the api are as follows:  
- /register __[POST]__
register a user with username and password.
  Requires a json object with the follwing format  
  ```JSON
  {
      "username" : "username",
      "password" : "password"
  }
  ```
- /auth  __[POST]__
Returns a json body with an __access token__ for further use with the __/item/<<string:name>>__ endpoint with the __GET__ request. Requires a json object with the following format
  ```JSON
  {
      "username" : "username",
      "password" : "password"
  }
  ```  
- /items __[GET]__
Returns all the items inside of the database  
- /stores __[GET]__
Returns all the stores and all the items inside of a store 
### GET requests
#### The following endpoints accept GET requests
- /item/<<string:name>>
Returns item with specified name. Requires an Authorization token in the header of the request.
- /store/<<string:name>>  
Returns a store with a specified name along with items which have a matching store ID. 
### POST requests
#### The following endpoints accept POST requests
- /item/<<string:name>>
Creates an item with the supplied name, price and store ID. The request body must include a price value and a store ID as follows.
```JSON
{
    "price" : 56.00,
    "store_id" : 1
}
```
- /store/<<string:name>>
Creates a store with the supplied name.
### PUT requests
#### The following end points accept PUT requests
- /item/<<string:name>>
Creates or updates an item with the supplied name, price and store ID. The request body must include a price value and a store ID as follows.
```JSON
{
    "price" : 56.00,
    "store_id" : 1
}
```
###DELETE requests
####The following endpoints accept DELETE requests
- /store/<<string:name>>
Deletes an item with the specified name
- /store/<<string:name>>
Deletes a store with the specified name 

The emphasis in this project has been solely given towards understanding the REST framework so there may be gaping security flaws in my implementation of it.