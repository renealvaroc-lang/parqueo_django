# Sistema de Gestión de Parqueo - Django

# Integrantes
Ing. Rene Alvaro Chavez Ordoñez

## Descripción
Este proyecto es un sistema de gestión de parqueo desarrollado con Django y Django Rest Framework. Permite administrar clientes, vehículos, espacios y registros de estacionamiento.

---

## Tecnologías utilizadas
- Python
- Django
- Django Rest Framework
- SQLite

---

## Estructura del Proyecto

- Cliente
- Vehiculo
- Espacio
- Registro

---

## Instalación y ejecución


1. Clonar el repositorio
git clone <https://github.com/renealvaroc-lang/parqueo_django.git>
cd parqueo_django
2. Crear entorno virtual
python -m venv venv
3. Activar entorno virtual

En Windows:

venv\Scripts\activate

En Linux/Mac:

source venv/bin/activate
4. Instalar dependencias
pip install -r requirements.txt
5. Ejecutar migraciones
python manage.py migrate
6. Ejecutar el servidor
python manage.py runserver

## Acceso al panel admin

Para crear un usuario administrador ejecutar:

python manage.py createsuperuser

Luego abrir en el navegador:

http://127.0.0.1:8000/
API Endpoints
/api/clientes/
/api/vehiculos/
/api/espacios/
/api/registros/
/api/vehiculos-activos/