   - # Peticiones HTTP mas usadas
   
##### head:
pide una respuesta idéntica a una petición GET, pero sin el cuerpo de la respuesta.

##### Get:
 Pide una representación del recurso especificado. Por seguridad no debería ser usado por aplicaciones que causen efectos ya que transmite información a través de la URI 
##### Post:
Envía los datos para que sean procesados por el recurso identificado. Los datos se incluirán en el cuerpo de la petición.
##### Put:
Sube, carga un recurso especificado a un servidor. 
##### Delete:
Borra el recurso especificado
##### trace:
Este método solicita al servidor que envíe de vuelta en un mensaje de respuesta con fines de comprobación y diagnóstico
##### Options:
Devuelve los métodos HTTP que el servidor soporta para un URL específico. Esto puede ser utilizado para comprobar la funcionalidad de un servidor web mediante petición en lugar de un recurso específico.
##### Connect:
Se utiliza para saber si se tiene acceso a un host, no necesariamente la petición llega al servidor.

   - # Códigos de respuesta HTTP más comunes
  
 HTTP utiliza múltiples códigos de respuesta, los cuales se identifica por el primer numero, que representa el tipo de mensaje, seguido de otros dos números mas que representa en especifico el mensaje

   -  ###### 1xx Mensajes 
   -  ###### 2xx Operaciones exitosas
   -  ###### 3xx Redirecciones
   -  ###### 4xx Error por parte del cliente
   -  ###### 5xx Error del servidor

# Ejemplo:

![Image of Yaktocat](https://plataforma.josedomingo.org/pledin/cursos/flask/curso/u01/img/dia2.png )


### fuente: 
https://es.slideshare.net/jalvarezpiedra/presentacion-httphttpsdns