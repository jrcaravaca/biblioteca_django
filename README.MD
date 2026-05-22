# Biblioteca Django

Este es un sistema de gestión de biblioteca desarrollado en Django que permite administrar libros, autores, perfiles de usuario, préstamos y reseñas.

## 🚀 Características

- **Gestión de Usuarios:** Registro, inicio de sesión y perfiles de usuario personalizados con fotos y datos personales.
- **Catálogo de Libros:** Listado de libros con información detallada, incluyendo autores, géneros, sinopsis y portadas.
- **Búsqueda Dinámica:** Filtro de búsqueda por título o autor en la página principal.
- **Sistema de Préstamos:** Control de stock y seguimiento de préstamos de libros.
- **Reseñas y Calificaciones:** Los usuarios pueden dejar comentarios y puntuar los libros (1-10), calculándose automáticamente el promedio.
- **Panel de Administración para Staff:** Vista protegida para revisar el historial completo de préstamos.

## 🛠️ Tecnologías utilizadas

- **Backend:** Python / Django
- **Base de datos:** SQLite (por defecto)
- **Frontend:** Plantillas de Django (HTML/CSS)

## 📂 Estructura del Proyecto (Modelos)

- **Library (App):**
    - `Book`: Gestiona el inventario, ISBN, idioma y géneros.
    - `Author`: Información biográfica y fotografías de los escritores.
    - `Loan`: Registro de libros prestados y fechas de devolución.
    - `Review`: Sistema de feedback de usuarios sobre libros.
- **Users (App):**
    - `UserProfile`: Extensión del modelo `User` de Django para incluir DNI, fecha de nacimiento y foto de perfil.

## ⚙️ Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd biblioteca_django
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar las migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```
   Accede a `http://127.0.0.1:8000` en tu navegador.