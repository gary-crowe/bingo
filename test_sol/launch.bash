# These are the "oc" commands to launch the application.
# Use the template in preference

oc new-app https://github.com/gary-crowe/bingo \
	--context-dir=test_sol/generator \
	--name bingo-generator

oc new-app https://github.com/gary-crowe/bingo \
	--context-dir=test_sol/client \
	--env RECOMMENDATIONS_HOST=generator \
	--name bingo

oc new-app mysql:8.0~https://github.com/gary-crowe/bingo \
        --name bingo-mysql \
        --context-dir=test_sol/ \
        --env MYSQL_DATABASE=games \
        --env MYSQL_USER=gary \
        --env MYSQL_PASSWORD=PassW0rd
