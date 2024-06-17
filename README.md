# MODULO 2 - TRABAJO FINAL (Nombre y Apellido del AUTOR: STACUL, Braian Rito Elias)
## Sistema de un catálogo de productos
Este sistema permite gestionar productos, en donde existirán tres tipos de 'usuarios' (administradores, registrados o 'normales' y anónimos).

### Usuarios 'anónimos'
Los usuarios anónimos podrán:
* Visualizar la lista de productos de la página web.
* Ver detalles de un producto.
* Registrarse al sitio web.

### Usuarios 'registrados'
Los usuarios que se encuentran registrados podran:
* Iniciar/Cerrar Sesion.
* Marcar un producto como favorito, desde el catálogo o desde el detalles del producto.
* Quitar productos de la lista de favoritos.
* Listar los productos que haya agregado como favoritos.
* Ver su información de perfil.
* Editar datos personales.

### Usuarios 'administradores'
Un usuario administrador podrá:
* Crear productos.
* Editar productos.
* Eliminar productos.
* Crear categorías.
* Editar categorías.
* Eliminar categorias.
* Desactivar productos.
* Listar los usuarios creados y poder diferenciarlos de los administradores


## Instalación
***
Versión de Python: Python 3.10.11

Creamos un repositorio nuevo en GitHub: catalogo_productos y clonamos repositorio en una ruta deseada

```
$ git clone https://github.com/BraianStacul/catalogo_productos
```

Creamos un entorno virtual para instalar las dependencias del proyecto
```
$ python -m venv ve_catalogo_productos
```

Creamos el proyecto al cual denominamos: catalogo_productos

```
$ django-admin startproject catalogo_productos
```

Configuramos la base de datos installando el paquete que permite la conexión a la misma (esta depende de cada BD específica)

```
$ pip install https://pypi.org/project/psycopg/
```

Creamos la primera app


```
django-admin startapp nombre_de_la_app
```

Nos dirigimos al directorio 'catalogo_productos' y ejecutar el archivo 'manage.py'

```
$ cd catalogo_productos
```
```
$ python manage.py runserver
```



