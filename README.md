# Proyecto de Ciclo IV: Tienda alquiler trajes y disfraces - arquitectura microservicios
Este proyecto está enfocado en la creación de una aplicación web que permita de forma sistemática el almacenamiento y gestion de inventarios de productos elaborados por las comunidades indigenas del pais y en una versión siguiente de manera adicional se planea mejorar el frontend con imagenes referentes a cada producto ingresado.

### Backend: autenticación de usuarios
para la realizacion de este microservicio se utilizo el framework django, con el lenguaje de programacion python, las pruebas correspondientes se realizaron en postman 

### Contenido de Este repositorio: 

 1. Se tiene una carpeta llamada authAppComInd donde donde se administran las aplicaciones que el proyecto este utiliza, esta carpeta contiene las carpetas: models, migrations, serializers y views, asi como los archivos admin.py, apps.py y test.py. 

 2. Se tiene una carpeta llamada authModuleComInd donde se guardan todas las configuraciones del servidor del componente, esta carpeta contiene los archivos: asgi.py, settings_dev.py, settings_prod.py, urls.py y wsgi.py. 

 3. se creo un archivo dockerfile el cual es un archivo de texto plano que contiene una serie de instrucciones necesarias para crear una imagen en un contenedor

 4. se tienen dos archivos que permiten iniciar un servidor web de manera local y en la nube, estos archivos son manage_dev.py y manage.py

 ### Requerimientos 
```
Django==4.0.4
djangorestframework==3.13.1
djangorestframework-simplejwt==5.1.0
psycopg2-binary==2.9.3
PyJWT==2.1.0
gunicorn==20.1.0
django-heroku==0.3.1
drf-spectacular==0.21.0
```

### Ejecución del proyecto

para ejecutar el proyecto en local:

1. Se descarga el proyecto comprimido o se clona de GitHub
   ```
    git clone https://github.com/proyecto-AlquilerTrajesydisfraces/alquiler-auth-ms.git
   ```
2. Al tener el proyecto en el ordenador, por la consola de comandos de ingresa al proyecto utilizando el comando cd:
   ```
    cd alquiler-auth-ms-main
   ```
3. se debe inicializar el entorno virtual:

   ```
    env/Scripts/activate
   ```
4. se debe ingresar el siguiente comando para ejecutar el proyecto en local(computador personal o servidor):

   ```
    python manage_dev.py runserver 
   ```
El proyecto se encuentra desplegado en la plataforma heroku:

xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### Diagrama de despliegue 

la parte sombreada hace referencia al despliegue de componentes de la parte backend del proyecto

![image](https://user-images.githubusercontent.com/84297258/175609307-797dc175-4444-45ec-85a6-5427f8d98a48.png)


### Documentación de API

https://app.swaggerhub.com/apis/tiendaAlquilerTyD/alquiler-de_trajes_y_disfraces_auth/1.0.0


### Pruebas

La ejecución de los casos de prueba se hizo por medio de la aplicacion postman:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/666c2542f2ecac394cb2?action=collection%2Fimport)
