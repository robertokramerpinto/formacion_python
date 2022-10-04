"""
ENVIRONMENTS Y LA GESTION DE DEPENDENCIAS CON PIP

* venv
* conda


# Creación del virtual environment
-- linux/MacOs
$python3 -m venv <path_virtual_env/venv_name>

-- Windows
$ python -m venv venv_name

# Activar virtual environment
-- Linux/MacOS
$ source <path_to_env/bin/activate>

-- Windows
$venv\Scripts\activate

# Salir (deactivate) del virtual environemnt
$ deactivate

# Gestion de paquetes

* pip: PyPi -> instalador por defecto de los paquetes de Python
$ pip install <package_name>

* Actualizar a pip:
$ pip install --upgrade pip

-- example numpy installation
$ pip install numpy

# requirements.txt
-> Fichero que contiene todos los paquetes y sus versions para un determinado virtual env
$ pip install -r requirements.txt

-> crear un requirements.txt a partir de un entorno
$ pip freeze > requirements.txt
"""



