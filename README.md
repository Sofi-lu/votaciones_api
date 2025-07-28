# API de Votaciones 

Esta es una API RESTful construida con FastAPI para gestionar un sistema de votaciones. Permite registrar votantes, candidatos y emitir votos, todo con validaciones y estadísticas.

## Requisitos

- Python 3.10 o superior
- Base de datos SQLite (por defecto)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Sofi-lu/votaciones_api.git
   cd votaciones_api
   ```

2. Crea un entorno virtual e instálalo:
   ```bash
   python -m venv env
   source env/bin/activate   # En Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Ejecuta la app:
   ```bash
   uvicorn main:app --reload
   ```

4. Accede a la documentación:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Estructura del Proyecto

```
.
├── main.py
├── database.py
├── models/
│   └── models.py
├── schemas/
│   └── schemas.py
├── routers/
│   ├── voters.py
│   ├── candidates.py
│   └── votes.py
├── requirements.txt
├── docs/
│   ├── swagger_estadisticas.png
│   ├── swagger_crear_votante.png
├── utils/
│   ├──auth.py
└── README.md
```

## Autenticación

La API ahora requiere **autenticación básica (HTTP Basic Auth)** para acceder a la mayoría de los endpoints protegidos como crear, eliminar o emitir votos.

### Credenciales por defecto

```
Usuario: admin  
Contraseña: admin123
```

Puedes modificarlas en el archivo `auth.py`.

### Cómo autenticarse en Swagger UI

1. Abre [http://localhost:8000/docs](http://localhost:8000/docs).
2. Haz clic en el botón **"Authorize"** en la parte superior derecha.
3. Ingresa las credenciales indicadas arriba.
4. Ya puedes consumir los endpoints protegidos.

### Ejemplo con `curl`

```bash
curl -u admin:admin123 http://localhost:8000/voters/
```

## Ejemplos de uso con `curl`

- Crear votante:
```bash
curl -X POST http://localhost:8000/voters/ -H "Content-Type: application/json" -d "{\"name\": \"Juan\", \"email\": \"juan@mail.com\"}"
```

- Crear candidato:
```bash
curl -X POST http://localhost:8000/candidates/ -H "Content-Type: application/json" -d "{\"name\": \"Ana\", \"party\": \"Verde\", \"email\": \"ana@mail.com\"}"
```

- Votar:
```bash
curl -X POST http://localhost:8000/votes/ -H "Content-Type: application/json" -d "{\"voter_id\": 1, \"candidate_id\": 2}"
```

- Ver estadísticas:
```bash
curl http://localhost:8000/votes/statistics
```

## Funcionalidades Implementadas

- [x] Registro de votantes y candidatos
- [x] Validación de que un email no puede estar en ambas entidades
- [x] Registro de votos (único por votante)
- [x] Estadísticas de votación
- [x] Swagger UI para documentación automática
- [x] Manejo de errores HTTP claros
- [x] Autenticación HTTP Basic para proteger los endpoints
- [x] Filtros de paginación (`skip`, `limit`) en las listas de votantes y candidatos
- [x] Estructura RESTful organizada por rutas (`/voters`, `/candidates`, `/votes`)
- [x] Validaciones con Pydantic para todos los esquemas
- [x] Código organizado en módulos (routers, models, schemas, database)

