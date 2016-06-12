# dakopucp
Hackaton PUCP - AngelHack 2016

Explicación de código del equipo @DakoHack:

Objetivo principal_ 

Funcionamiento del código escrito_ Lo primero que hace nuestro programa es la Recolecta de Información.
A partir de unos usuarios específicos en twitter, unas palabras clave y unos hashtags seleccionados se registra
en una base de datos todos los twits a tiempo real que se van publicando y contienen estas palabras, así como todas
las notas de prensa que contengan alguna/s de esta/s palabras publicadas en la web oficial del Ministerio de Energia
y Minas del Perú (http://www.minem.gob.pe/_noticias.php?idSector=1&pagina=1).
Una vez tengamos la data recolectada, se clasifica según la mina del Perú (para la demostración detectamos las principales
49 minas en el Perú) a la cuál se refiere la publicación y se le otorga un nivel de satisfacción. Esto último se consigue 
"entendiendo" el sentimiento que expresa la publicación; nosotros lo entendemos como a favor o en contra de la minería 
en dicho lugar.
Por último, un bot de twitter creado expresamente para este proyecto, publica (pensando en la demostración) cada 15 segundos
(con la condición de haber registrado más de dos entradas nuevas) un twit con la información de sentimiento promediada de
entre las minas seleccionadas.

Funcionamiento del proyecto (sin completar por falta de tiempo)_ Se recopila data a tiempo real de todas las publicaciones
que se hagan en twitter con unos parámetros seleccionados (que contengan keyboars o hashtag a cerca de la minería o sean 
de cuentas que por lo general publican cosas acerca de la minería en el Perú) y se guarda en una base de datos. A s vez se 
recopilan las notas de prensa de la web oficial del Ministerio de Energia y Minas del Perú (http://www.minem.gob.pe/_noticias.php?idSector=1&pagina=1).
Una vez se tiene la data, se clasifica según la mina de la cuál habla la publicación (para este caso clasificamos según
las 49 priincipales minas del Perú) y se le asigna un "valor de sentimiento". Esto último se refiere a detectar la positividad
o la negatividad de la publicación acerca de la mina, la cual nombra, con el fin de poder clasificar en un "sentimiento a favor o en contra".
Con esta data, el bot de la aplicación debe publicar cada hora si ha detectado el ingreso a su base de datos de 1000 nuevos twits.
Por otro lado FALTA programar que nuestro bot pueda leer un twits donde se le mencione y se le acompañe (a dicha publicación)
un hashtag que indique un Producto (Oro, Cobre, Plata, Molibdeno, Selenio, Cadmio, Roca fosfórica o Hierro), el cual asociaremos
a una de las principales minas del país que lo pueda producir y se contestará la publicación prediciendo el mejor lugar
para extraer dicho producto en base a "los sentimientos" transmitidos a la mineria en ciertos lugares por los internautas.
Así pues tenemos el método desarollado (pero no codificado): El hashtag #Oro (por poner un ejemplo de producto) se leería 
y crearía tantos objetos Resultado, como posibles minas de donde se pueda extraer. Este objeto Resultado consta de dos 
variables, una primera Mina (identiificaría una de las Minas donde poder extraer el producto) y una segunda Sentimiento
(un Decimal de tres decimales, el cual indica el valor positivo del twit publicado). Así pues, se publicaría el "mejor Resultado",
es decir, la Mina en la cuál por la opinión de los internautas y de las notas de prensa relacionadas es más favorable
ponerse a extraer ese producto demandado.
A su vez, esta aplicación también tiene fines como "Control a tiempo real de eventos en las RRSS basandose en unos Keywords
de detección y el sentimiento que se genera alrededor de éste".

Con todo esto hemos querido llevar a cabo un proyecto funcional, escalable y con viabilidad para la vida real.
Detectamos, registramos y procesamos información digital que circula por la web, una  práctica informática que
está al orden del día.
