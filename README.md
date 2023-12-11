# FHE Multi Party Computation

## Build
El servidor se levanta con: 

```bash
docker compose up
```

El servidor se cierra con:

```bash
docker compose down
```
## Correr a los clientes


### Instalar dependencias
```bash
pip install requirements.txt
```

### Configuración
Modificar archivo client/.env con las configuraciones deseadas.

Desde la carpeta client/:

El Creador se corre con:

```bash
python3 client_creator.py 
```

Los N Participantes (N definido en el .env) se corren con:

```bash
python3 client_participant.py <nombre> <numero_a_enviar>
```

Por último, los resultados se obtienen con:

```bash
python3 client_results.py
```