# Working prototype of the ticket-generation microservice with client.
Instructions:
1. Start the ticket-generator microservice
```bash
cd generator
python server.py &
```
2. Start the flask service for client
```bash
cd client
FLASK_APP=client.py flask run
```
3. Fire up your broswer and point to: ```http://localhost:5000```

The client flask program sends a request message to the ticket generator program.  That uses numpy to generate 6
tickets (3x9).  These are passed back to the client as an object.  The object is parsed and converted to a flattened list of all the balls.  The flask app then prints them in tables to represent the bingo tickets.

## To fix.
1. The numpy command doesn't return 6 bingo tickets that follow the rules for bingo tickets.  
This routine needs to be changed to generate 6, English style bing tickets.

2. Not sure a flattened array is the right idea for the ticket storage.
How will I check and mark off the tickets?

3. Instructions for firing up mysql as a container.

