lanzar un servidor RabbitMQ en docker para estos ejemplos:

tutorial de: https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668

    docker run -d --hostname my-rabbit -p 15672:15672 -p 5672:5672 --name rabbit-server -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management


Nota: recuerde abrir los puertos 5672 y 15672 en el Security Group de la máquina virtual.

# Recuerde tener previamente instalado python3 o verifique que ya este:

    si versión 3:

        python -V      (versión 3.x)

    sino, instalar:

        sudo yum install python3 -y

    sudo pip3 install pika
