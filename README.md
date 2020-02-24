# Ejemplo de una blockchain para una criptomoneda.

## Como correr.
1. Clonar repositorio.
2. Entrar a la raiz del repositorio.
3. Crear un nuevo entorno virtual de python version >= 3.8.1 .

`python -venv blockchain_example_coin`

4. Activar el entorno virtual.

`source blockchain_example_coin/bin/activate`

5. Regresar a la raiz del repositiorio y instalar las dependencias que estan en `requirements.txt`

`pip3 install -r requirements.txt`

6. Dentro de `blockchain_coin_server` correr `flask run` para levantar el servidor.
    
## Endpoints.

### /chain
Retorna la blockchain completa del nodo actual.

### /transactions
Sirve para crear una nueva transaccion.
    
### /mine
Hace que el nodo actual mine un bloque.
    
### /register
Registra uno o mas nodos como pares para el nodo actual.
    
### /consensus
Sincroniza la blockchain actual corriendo el algoritmo de consenso para cada uno de los nodos pares registrados en el nodo actual.
    
### /nodes
Retorna la lista de pares registrados en el nodo actual.

## Algoritmo de ***proof of work***.
***Sea*** ***{ p, p’, h ∈ ℤ+ | h = p ‖ p’ , p = prueba anterior, p' = prueba nueva }***

Tal cual que, al generar un hash sha256 usando ***h***  y luego pasarlo a hexadecimal, resulte en una **cadena que termine con cuatro ceros.**
