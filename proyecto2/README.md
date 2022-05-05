# proyecto 2

## ref: https://github.com/bitnami/bitnami-docker-moodle/blob/master/docker-compose.yml

## en el DCA

Tenemos 5 máquinas para el proyecto:

    nginx-proxyinverso o nginx-lb -> 192.168.10.x1 -> visibilidad a internet mediante vplX.dis.eafit.edu.co

    moodle1 -> 192.168.10.x2

    moodle2 -> 192.168.10.x3

    mariadb -> 192.168.10.x4

    nfs-server -> 192.168.10.x5

# para pruebas, puede configurar el nginx como proxy inverso (opción1) o irse directamente ejecutar el balanceador con nginx-lb:

## Opción1: en nginx-proxyinverso -> 192.168.10.x1

1.Instalar docker y docker compose
2.close el repo de la materia:
    cd $HOME
    git clone https://github.com/st0263eafit/st0263-2261.git
    cd st0263-2261/proyecto2
3.
    mkdir $HOME/nginx-proxyinverso
    cp docker-compose-nginx-proxyinverso.yml $HOME/nginx-proxyinverso/docker-compose.yml
    cp nginx-proxyinverso.conf $HOME/nginx-proxyinverso/nginx.conf
    cd $HOME/nginx-proxyinverso
    # actualice las IP's en los archivos docker-compose.yml y nginx.conf
    # subir
    docker-compose up -d
    # bajarlo
    docker-compose down

## Opción2: en nginx-lb -> 192.168.10.x1

1.Instalar docker y docker compose
2.close el repo de la materia:
    cd $HOME
    git clone https://github.com/st0263eafit/st0263-2261.git
    cd st0263-2261/proyecto2
3.
    mkdir $HOME/nginx-lb
    cp docker-compose-nginx-lb.yml $HOME/nginx-lb/docker-compose.yml
    cp nginx-lb.conf $HOME/nginx-lb/nginx.conf
    cd $HOME/nginx-lb
    # actualice las IP's en los archivos docker-compose.yml y nginx.conf
    # subir
    docker-compose up -d
    # bajarlo
    docker-compose down

## en moodle1 -> 192.168.10.x2
1.Instalar docker y docker compose
2.close el repo de la materia:
    cd $HOME
    git clone https://github.com/st0263eafit/st0263-2261.git
    cd st0263-2261/proyecto2
3.
    mkdir $HOME/moodle
    cp docker-compose-moodle.yml $HOME/moodle/docker-compose.yml
    cd $HOME/moodle
    # actualice las IP's en los archivos docker-compose.yml
    # subir
    docker-compose up -d
    # bajarlo
    docker-compose down

## en moodle2 -> 192.168.10.x3
1.Instalar docker y docker compose
2.close el repo de la materia:
    cd $HOME
    git clone https://github.com/st0263eafit/st0263-2261.git
    cd st0263-2261/proyecto2
3.
    mkdir $HOME/moodle
    cp docker-compose-moodle.yml $HOME/moodle/docker-compose.yml
    cd $HOME/moodle
    # actualice las IP's en los archivos docker-compose.yml
    # subir
    docker-compose up -d
    # bajarlo
    docker-compose down

## en moodle2 -> 192.168.10.x3
1.Instalar docker y docker compose
2.close el repo de la materia:
    cd $HOME
    git clone https://github.com/st0263eafit/st0263-2261.git
    cd st0263-2261/proyecto2
3.
    mkdir $HOME/moodle
    cp docker-compose-moodle.yml $HOME/moodle/docker-compose.yml
    cd $HOME/moodle
    # actualice las IP's en los archivos docker-compose.yml
    # subir
    docker-compose up -d
    # bajarlo
    docker-compose down

## en mariadb -> 192.168.10.x4

1.Instalar docker y docker compose
2.close el repo de la materia:
    cd $HOME
    git clone https://github.com/st0263eafit/st0263-2261.git
    cd st0263-2261/proyecto2
3.
    mkdir $HOME/mariadb
    cp docker-compose-mariadb.yml $HOME/mariadb/docker-compose.yml
    cd $HOME/mariadb
    # actualice las IP's en los archivos docker-compose.yml
    # subir
    docker-compose up -d
    # bajarlo
    docker-compose down

## en nfs-server -> 192.168.10.x5

1.Instalar docker y docker compose
2.close el repo de la materia:
    cd $HOME
    git clone https://github.com/st0263eafit/st0263-2261.git
    cd st0263-2261/proyecto2
3. instalar nfs-server nativo en el sistema operativo:

ref: 

    
