# VAR2

Para correr Unibotics en local:

docker run --rm -it -p 7164:7164 -p 2303:2303 -p 1905:1905 -p 8765:8765 -p 6080:6080 -p 1108:1108 -p 7163:7163 jderobot/robotics-academy:3.4.28

Para comprobar id del contenedor:
docker ps 

Para copiar archivos desde el docker a local:
docker cp id_contenedor:/rutaArchivosEnDocker/ /rutaLocal


Para copiar archivos desde local al docker:
docker cp /rutaLocal id_contenedor:/rutaArchivosEnDocker/

# Instrucciones para ejecutar la práctica

1. Correr Unibotics en local

2. En una nueva terminal ejecutar docker ps para ver la ID del contenedor

3. Ejecutar el comando docker cp id_contenedor:/ /rutaLocalHastaElProyecto/models

4. Si se quiere probar el estandarizado y la normalización: Ejecutar el comando docker cp id_contenedor:/ /rutaLocalHastaElProyecto/scalers

5. En la terminal del docker: pip install scikit-learn joblib tensorflow. (Este último es opcional, sólo en caso de querer probar la NN)

6. Copiar el código del archivo autonomous_driver.py

7. Ejecutar


Es recomendable iniciar el docker para probar cada modelo, ya que con el tiempo el contenedor funciona peor.


