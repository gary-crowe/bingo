# Working prototype of the ticket-generation microservice with client.
## For local development
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

## Using Openshift
Instructions:
1. Login to your Openshift instance
2. Launch the generator code:
```yaml
oc new-app https://github.com/gary-crowe/bingo \
	--context-dir=code/generator \
	--name bingo-generator
```
3. Launch the bingo client
```yaml
oc new-app https://github.com/gary-crowe/bingo \
	--context-dir=code/client \
	--env GENERATOR_HOST=bingo-generator \
	--name bingo
```
4. Launch the mysql database
```yaml
oc new-app mysql:8.0~https://github.com/gary-crowe/bingo \
        --name bingo-mysql \
        --context-dir=code/ \
        --env MYSQL_DATABASE=games \
        --env MYSQL_USER=gary \
        --env MYSQL_PASSWORD=PassW0rd
```

## To fix.
1. Instructions for firing up mysql as a container.
2. It appears that gRPC doesn't work? out of the box.
See: https://cloud.redhat.com/blog/grpc-or-http/2-ingress-connectivity-in-openshift
