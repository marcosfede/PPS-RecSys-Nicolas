# Improvement and Fixes

## Improvement
* Añadir un método de test donde se pueda dividir la data en un porcentaje X de 'train' y un porcentaje 1-X de 'test'
* Añadir un modulo para cargar los principales datasets (como Movielens) o un dataset custom (desde un PATH o una URL)
* Añadir modelos de algoritmos de clustering o neural network
* Añadir metricas de error para recomendadores (como ALS)

## Fixes
* Cross validate: 
    - El método cross_validate() de sklearn necesita como parametro una metrica de error (scoring) que debe ser acorde a el tipo de estimador (si el estimador es de Clasificación o Regresion).
    - Sklearn no reconoce correctamente los 'estimadores' de otras librerias (como Suprise o LightFM). No es posible utilizar cross_validate() sin usar el scoring='neg_mean_absolute_error'
    - No es posible usar cross_validate() con modelos de LightFM (bpr y warp) por un fallo en la data de fit() --> error: ndarray is not C-contiguous
* Grid search: mismos problemas que en cross validate
* Poner los ejemplos en la carpeta example
    - Dificultades con el path para direccionar los modulos de la libreria desde dentro de la carpeta example
