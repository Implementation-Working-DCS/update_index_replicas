<h1 align="center">
  <br>
  <a href="http://www.dcs.ar"><img src="https://i.imgur.com/GgjNXNl.png" alt="DCSolutions" width="200"></a>
  <br>
Script Updater for Replicas ELK
  <br>
</h1>

<h4 align="center">Script que actualiza el numero de replicas de 0 a 1 de todos los indices de ELK

<p align="center">
  <a href="#Funciones">Funciones</a> •
  <a href="#Como se usa">Como se usa</a> •
  <a href="#Creditos">Creditos</a> •
</p>


## Funciones

* Actualiza el dato de los indices que representan el numero de replicas.
* Lo hace en todos los indices

## Como se usa

Para clonar esta repositorio, vas a necesitar [Git](https://git-scm.com) y [Python](https://www.python.org/downloads/) (que viene con [pip](https://pypi.org/project/pip/)) intalados en tu PC

```bash
# Clone el repositorio.
$ git clone https://github.com/Implementation-Working-DCS/update_index_replicas.git

# Ir al repo
$ cd update_index_replicas

# Instalar dependencias
$ pip install elasticsearch
$ pip install urllib3

# Iniciar la app
$ python3 -m main.py
```

## Creditos

- [Matias Dante](https://github.com/matiasdante)
  
![image](https://github.com/Implementation-Working-DCS/alertOPS-auto-ack/assets/70301149/af05d4c1-5d7a-411b-86ba-b10ce41a8407)

