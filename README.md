# Find my Office

**Find my office** es una herramienta que permite localizar la mejor oficina en base a criterios. En este caso los criterios eran satisfaccer las necesidades de los trabajadores de la empresa. Estas necesidades estaban basadas en cercania a otras empresas del sector, disfrutar de distintos servicio en un area cercana para que, en difinitiva, el area donde montasen la oficina les permitar desarrollar gran parte de su vida cotidiana. Para ello contamos con un json con todas las empresas que tiene su su base de datos Crunchbase.

**¿Como hemos llegado al resultado?** 
___

Funciones  | Descripción 
---------- | ----------- 
Cargado    | Contamos con una base de datos en Mongodb donde hacemos una query para obtener datos revevantes.
Limpieza   | En la query eliminamos lo que no queremos: empresas que han cerrado y empresas que no tiene coordenadas.
Transformar| Queremos conocer que ciudades tienen la mejor relacion num. empresas/recaudación. Para ellos pasamos el total money raised a un entero que se pueda evaluar. Nos quedaremos con las 15 mejores ciudades del mundo.
2ª Limpieza| Ahora vamos a por empresas con una recaudación mayor de $1M fundadas a partir del 2005.
Final      | Una función que permite elegir ciudad, radio de cercania a otras empresas, un lugar de interes y un Meetup por tematica.

**La finalidad** es conseguir una localización donde se encuentren el mayor número de empresas posibles con una recaudación alta para así poder tener mas posiblidades de crecimiento. 



**Recursos empleados:** 
___

Recursos  | Descripción 
---------- | ----------- 
Folium     | Todos los mapas han sido realizados en Folium.
Google Places API | Usamos esta API encontrar una oficina real en la locación ideal y para encontrar puntos de interes cercanos.
Meetup API |  Para poder conocer eventos geolocalizados cerca y filtrados por temática.
GeoQueries Mongodb | Realizando una Query con $near podemos saber que empresa tiene mas empresas cerca con un radio determinado.

**Resultado final:** 
___

(https://github.com/Pacoanes/find_my_office/blob/master/Map.png)
