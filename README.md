📌 Gestión de Tareas - Aplicación Web

Este proyecto es una aplicación web para la gestión de tareas, desarrollada con Flask (Python) en el backend y HTML/CSS/JavaScript en el frontend. Permite a los usuarios gestionar sus tareas de forma eficiente, cambiando su estado entre "pendiente", "en proceso" y "completada".

🚀 Características Principales

✅ Autenticación de Usuarios: Registro e inicio de sesión seguro mediante JWT (JSON Web Tokens).

✅ Gestión de Tareas: Crear, actualizar, eliminar y visualizar tareas.

✅ Cambio de Estado: Mover tareas entre los diferentes estados.

✅ Interfaz Intuitiva: Diseño amigable y responsive.

🛠️ Tecnologías Utilizadas

- **Backend**:
  - Python
  - Flask (Framework web)
  - SQLAlchemy (ORM para la base de datos)
  - Flask-JWT-Extended (Autenticación basada en tokens JWT)
- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript (Fetch API para solicitudes HTTP)
- **Base de Datos**:
  - PostgreSQL (Alojada en Supabase)

📋 Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior.
- PostgreSQL (o cualquier otra base de datos compatible con SQLAlchemy).
- Pip (Gestor de paquetes de Python).

⚙️ Configuración del Proyecto

. Clonar el Repositorio

2. Crear un Entorno Virtual (Opcional)

3. Instalar Dependencias

4. Configurar la Base de Datos

Crea una base de datos en PostgreSQL o en Supabase.

Configura la URL de conexión en tu archivo .env:

5. Ejecutar Migraciones

Si usas SQLAlchemy y tienes migraciones configuradas, ejecuta:

6. Iniciar la Aplicación

Accede a la aplicación en: http://127.0.0.1:5000

🗂️ Estructura del Proyecto
```bash
app_tareas/
├── app.py                  # Punto de entrada de la aplicación Flask
├── models.py               # Modelos de la base de datos (Usuario y Tarea)
├── routes.py               # Rutas y lógica del backend
├── methods.py              # Funciones auxiliares para la lógica de negocio
├── extensions.py           # Configuración de SQLAlchemy y JWT
├── templates/              # Archivos HTML (frontend)
│   ├── index.html          # Página principal
│   ├── login.html          # Página de inicio de sesión
│   ├── signup.html         # Página de registro
│   ├── tasks.html          # Página de gestión de tareas
│   └── error.html          # Página de error
├── static/                 # Archivos estáticos (CSS, JS, imágenes)
│   ├── styles.css          # Estilos CSS
│   └── scripts.js          # Lógica JavaScript
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno
└── README.md               # Documentación del proyecto
```

🧑‍💻 Uso de la Aplicación

-Crear una Tarea: Proporciona un nombre y una descripción.
-Actualizar Estado: Mueve la tarea a "En Proceso" o "Completada".
-Eliminar Tarea: Borra una tarea de la lista.
-Cerrar Sesión: Finaliza la sesión del usuario.
