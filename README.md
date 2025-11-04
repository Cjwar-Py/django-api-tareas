# API RESTful de Tareas con Django

Este proyecto es una API RESTful robusta para la gestión de tareas, construida desde cero con Python, Django y Django REST Framework (DRF).

El proyecto está diseñado para ser seguro, escalable y fácil de probar, siguiendo las mejores prácticas de desarrollo de API.

## 🚀 Características Principales

* **Gestión Completa de Tareas (CRUD):** Funcionalidad completa para Crear, Leer, Actualizar y Borrar tareas.
* **Seguridad y Autenticación:** Los endpoints están protegidos. Solo los usuarios autenticados (vía sesión o token) pueden acceder y manipular los datos.
* **API Navegable de DRF:** Incluye la interfaz web de DRF (`Browsable API`) para probar y visualizar fácilmente los endpoints desde el navegador.
* **Integración con Admin de Django:** El modelo `Tarea` está registrado en el panel de administrador de Django para una gestión de datos sencilla.
* **Código Limpio y Refactorizado:** Utiliza `ViewSets` y `Routers` de DRF para agrupar la lógica y generar las URLs automáticamente.
* **Configuración Segura:** La `SECRET_KEY` y los ajustes de `DEBUG` se gestionan de forma segura fuera del código fuente usando un archivo `.env`.

## 💻 Tecnologías Utilizadas

* Python
* Django
* Django REST Framework (DRF)
* python-decouple (para variables de entorno)
* SQLite3 (para la base de datos de desarrollo)

## 🔑 Endpoints de la API

Todos los endpoints están bajo el prefijo `/api/`. Se requiere autenticación para todas las rutas.

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `GET` | `/api/tareas/` | Lista todas las tareas del usuario. |
| `POST` | `/api/tareas/` | Crea una nueva tarea. |
| `GET` | `/api/tareas/<id>/` | Obtiene los detalles de una tarea específica. |
| `PUT` | `/api/tareas/<id>/` | Actualiza una tarea específica (requiere todos los campos). |
| `PATCH`| `/api/tareas/<id>/` | Actualiza parcialmente una tarea específica. |
| `DELETE`| `/api/tareas/<id>/` | Elimina una tarea específica. |
| `POST` | `/api-auth/login/` | Endpoint para iniciar sesión (vía interfax de DRF). |
| `POST` | `/api-auth/logout/`| Endpoint para cerrar sesión (vía interfax de DRF). |

## ⚙️ Instalación y Ejecución Local

Sigue estos pasos para clonar y ejecutar el proyecto en tu máquina local.

**1. Clona el repositorio:**
```bash
git clone [https://github.com/Cjwar-Py/django-api-tareas.git](https://github.com/Cjwar-Py/django-api-tareas.git)
cd django-api-tareas
