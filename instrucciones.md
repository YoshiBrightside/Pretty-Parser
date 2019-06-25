Archivo de entrada: input.txt
  * El primer renglón contiene el trimestre a analizar (por ejemplo, 2T2019 es el segundo trimestre del 2019). 
    * Se deben omitir todos los renglones donde la columna Fecha se encuentra fuera del rango del trimestre. Por ejemplo, para 2T2019 las fechas a considerar son solamente del 2019-04-01 al 2019-06-30 inclusive.
  * Cada bloque (separado por un renglón vacío) contiene datos de un proveedor
  * El primer renglón del bloque es el nombre del proveedor
  * Los renglones subsecuentes están formados por varias columnas separadas por `|`:
    - Fecha
    - Cantidad
    - Unidades
    - Descripción del concepto. Para propósitos de agrupación hay que :
       - Ignorar todo excepto letras y dígitos (a b_c -> abc)
       - Eliminar acentos (á -> a, ñ -> n)
       - Convertir a mayúsculas
    - Monto total  

El resultado debe de contener, por cada concepto:
  * Descripción, transformada de acuerdo a lo descrito arriba
  * Cantidad total en unidades métricas. Por ejemplo, 10 lbs se convierten a 4.54 kg.
  * Precio unitario ponderado (utilizando las unidades métricas)
  * El nombre del proveedor con el menor precio unitario (utilizando las unidades métricas)

