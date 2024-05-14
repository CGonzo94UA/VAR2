# VAR2



Para correr en local:

docker run --rm -it -p 7164:7164 -p 2303:2303 -p 1905:1905 -p 8765:8765 -p 6080:6080 -p 1108:1108 -p 7163:7163 jderobot/robotics-academy:3.4.28


Para comprobar id del contenedor:
docker ps 

Para copiar archivos desde el docker a local:
docker cp id_contenedor:/rutaArchivosEnDocker/ /rutaLocal


Para copiar archivos desde local al docker:
docker cp /rutaLocal id_contenedor:/rutaArchivosEnDocker/