## TP_Coder: Base de datos para concesionaria

Este proyecto es una aplicación web desarrollada con **Django** que permite gestionar una base de datos de una concesionaria de autos y motos. Se pueden cargar vehículos con sus respectivas características, así como también administrar vendedores y usuarios que interactúan con la aplicación.

## Características

- Registro de vehículos con:
  - **Marca**
  - **Modelo**
  - **Kilometraje**
  - **Año**
  - **Chasis**
- Administración de vendedores y usuarios.
- Base de datos en **SQLite3**.
- Interfaz de usuario para la gestión de los datos.

## Configuración y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
```

### 2. Crear y activar un entorno virtual
```bash
python -m venv env
env\Scripts\activate  # En Windows
source env/bin/activate  # En macOS/Linux
```

### 3. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Ejecutar el servidor
```bash
python manage.py runserver
```

## Notas Importantes
- **Es necesario actualizar en `settings.py` la ruta de la carpeta `Templates` para que funcione correctamente.**
- Asegurarse de que el archivo `db.sqlite3` se encuentra en la raíz del proyecto antes de ejecutar las migraciones.

