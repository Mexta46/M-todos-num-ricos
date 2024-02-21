# Método de biseccón
conocido también como de corte binario, de partición de intervalos o de Bolzano, es un tipo de búsqueda incremental en el que el intervalo se divide siempre a la mitad. Si la función cambia de signo sobre un intervalo, se evalúa el valor de la función en el punto medio. La posición de la raíz se determina situándola en el punto medio del subintervalo, dentro del cual ocurre un cambio de signo. El proceso se repite hasta obtener una mejor aproximación.

Los pasos para realizar el método de bisección esta en el siguiente diagrama:
### Diagrama de flujo
[![Diagrama de método de bisección](https://drive.google.com/file/d/1fd_Iw6H35l_R5fmbTEGOioGTjV7njAfY/view?usp=drive_link "Diagrama de método de bisección")](https://drive.google.com/file/d/1fd_Iw6H35l_R5fmbTEGOioGTjV7njAfY/view?usp=drive_link "Diagrama de método de bisección")

### Ejemplo en excel
Obtener la raíz de la función f(x)=x^10-1.
se obtiene la siguiente tabla en excel:

[![Tabla de excel](https://drive.google.com/file/d/1PpvF_d5Y1ZhdfDkGCFmg1HjXjPXei_Ys/view?usp=sharing "Tabla de excel")](https://drive.google.com/file/d/1PpvF_d5Y1ZhdfDkGCFmg1HjXjPXei_Ys/view?usp=sharing "Tabla de excel")

Para comprobar esto resultados se usa el metodo grafico que es graficar la función:

[![Gafico](https://drive.google.com/file/d/1eYBuFTyhD7EZIwzqvnkQRUP8ja-tvU8T/view?usp=sharing "Gafico")](https://drive.google.com/file/d/1eYBuFTyhD7EZIwzqvnkQRUP8ja-tvU8T/view?usp=sharing "Gafico")

En este grafico se puede apreciar de simple vista la raiz de la función.

### Explicación del codigo
La primera parte muestra una libreria necesaria para que pythin pueda trabajar con expreciones regulares.

[![](https://drive.google.com/file/d/1esMoCxHQJR4dmYolgXpJ_Et6eVkor3Qt/view?usp=drive_link)](https://drive.google.com/file/d/1esMoCxHQJR4dmYolgXpJ_Et6eVkor3Qt/view?usp=drive_link)

El siguiente segmento es un metodo que traduce la expreción algebraica a una aritmetica.

[![](https://drive.google.com/file/d/1yMJKiXOfo2nZQPmikKj7DwzXF9p7LqVs/view?usp=drive_link)](https://drive.google.com/file/d/1yMJKiXOfo2nZQPmikKj7DwzXF9p7LqVs/view?usp=drive_link)

Este segmento del codigo es el más complicado y extenso del código ya que es un metodo donde se lleba a cabo los calculos de los intervalos y el porcentaje de error con el que va a trabajar el código ademas de calcular los limites y la raíz(x) de la expreción

[![](https://drive.google.com/file/d/11f7xCQh6PDgc9MzcsEUx9EmRIROnSh1B/view?usp=drive_link)](https://drive.google.com/file/d/11f7xCQh6PDgc9MzcsEUx9EmRIROnSh1B/view?usp=drive_link)

Este metodo representa el main del programa donde se pediran las variables con las que vamos a trabajar, llamara a los metodos anteriores e imprimira la respuesta del programa.

[![](https://drive.google.com/file/d/1ZOAf9Y3xEqVvN9yJLeV0NjDUnZ60RLrh/view?usp=drive_link)](https://drive.google.com/file/d/1ZOAf9Y3xEqVvN9yJLeV0NjDUnZ60RLrh/view?usp=drive_link)

Por ultimo este if verificara si el programa esta corriendo, si lo esta llamara al metodo principal (main) y si no no lo hara.

[![](https://drive.google.com/file/d/1GDoDYz56OcCw1E5OXB9okwvIQ2Lw4shi/view?usp=drive_link)](https://drive.google.com/file/d/1GDoDYz56OcCw1E5OXB9okwvIQ2Lw4shi/view?usp=drive_link)
