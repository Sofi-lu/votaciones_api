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
└── README.md
```

## Autenticación

Por ahora la API no requiere autenticación, pero se puede extender fácilmente con JWT o HTTP Basic Auth.

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
