# Calculadora de Salud

# Tabla de Contenidos

- [Descripción](#descripcion)
- [Casos de uso](casos-de-uso)
- [Ejemplo de uso](ejemplo-de-uso)

## Descripción

Es un script en `python3` que dado un fichero con entradas tales como:

```
13-05-2013;M;56.4;163;20;44.5;7.2;60;72.4;45.1;13;6.6
```

> El delimitador puede ser cualquiera siempre y cuando no sea: `-`

> Para introducir valores decimal se utilizará el punto `.`, NO la coma `,`.

Es capaz de interpretar y gestionar (por orden):

- Fecha (Día-Mes-Año)
- Sexo (M/H)
- Peso (Kg.)
- Altura (cm.)
- Edad
- Perímetro del pecho (cm.)
- Perímetro del brazo (cm.) 
- Perímetro del cintura (cm.)
- Perímetro de la cadera (cm.)
- Perímetro del muslo (cm.)
- Perímetro del gemelo (cm.)
- Perímetro del tobillo (cm.)

Dado el fichero, el script lo interpretará y mostrará:

- Los valores más actuales dentro del fichero (últimos introducidos)
- Índices:
  - Índice Cintura Cadera
  - Índice Corpulencia
  - Índice Cintura Altura
  - Índice de Masa Grasa Relativa
  - Índice de Adiposidad Corporal (similar al de Porcentaje de Grasa Corporal)
  - Agua Corporal Total
- La diferencia de resultados entre la última entrada y la penúltima
  - De esta forma se puede verificar si se ha progresado respecto a la anterior medición, y así tener un seguimiento de ello.
- Gráficas temporales de los datos introducidos respecto de todas las entradas.
  - Así se puede tener a simple vista cuál es la evolución en cada aspecto.
  - Se guardan en una carpeta (`output`) por si se quisieran revisar sin ejecutar el script otra vez.

## Casos de uso

- Seguimiento de la evolución/progreso físico que se realiza a lo largo de las distintas mediciones (recomendable una vez por semana). Lo cual viene bien para adelgazar o controlar el nivel de musculación.

- Seguimiento del nivel de grasa pensando en las dietas posibles a realizar.

## Ejemplo de uso

Dado un fichero `ejemplo.txt`:

```
01-07-2020;H;80;185;20;93;31;80;97.3;52;30;26
08-07-2020;H;81;185;20;94;33;80.5;97.3;53;30;26
15-07-2020;H;82;185;20;96;33;80.5;97.2;53;30;26
22-07-2020;H;81;186;20;96;33;80.5;97.3;53;30.7;26.3
29-07-2020;H;79;186;20;98;33;80.5;97.4;55;31;26
01-08-2020;H;78;186;20;98;35;78;97.5;55;31;26.2
08-08-2020;H;77;186;20;98;35;77;97.5;55.5;31.3;26
15-08-2020;H;78;186;21;97;35;77;97.5;56;31.3;26.5
22-08-2020;H;79;186;21;97;35;77;97.5;56;31.5;26.1
29-08-2020;H;78;186;21;98;37;76.3;97.8;58.2;32.1;26.3
```

Ejecutamos el script tal que:

```bash
python3 calculadora.py ejemplo.txt ";"
```

Y se abrirá una página web (localizada en la carpeta `output`) en el buscador por defecto.

Esta página se genera a partir de Markdown a `html` con el CSS de [este](https://github.com/jasonm23/markdown-css-themes/blob/gh-pages/avenir-white.css) repositorio.

El ejemplo de este punto está en la carpeta `exampleOutput`, con abrir el archivo `resumen.html` se puede ver el resultado de la ejecución del script.
