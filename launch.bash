# These are the "oc" commands to launch the application.
# Use the template in preference
# Card generator
oc new-app https://github.com/gary-crowe/bingo#latest \
	--context-dir=code/generator \
	--name bingo-generator

# Client App
oc new-app https://github.com/gary-crowe/bingo#latest \
	--context-dir=code/client \
	--env GENERATOR_HOST=bingo-generator \
	--name bingo

# MySQL database backend
oc new-app mysql:8.0~https://github.com/gary-crowe/bingo#latest \
        --name bingo-mysql \
        --context-dir=code/ \
        --env MYSQL_DATABASE=games \
        --env MYSQL_USER=gary \
        --env MYSQL_PASSWORD=PassW0rd

# Espose the service
oc expose svc bingo
