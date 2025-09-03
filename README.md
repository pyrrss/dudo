# 🎲 Dudo (Cacho)


[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-pytest%20--cov-green)]()

---

## 📖 Descripción

Este proyecto implementa el juego de **Dudo en Cacho** en Python.

Dudo es un juego de dados tradicional conocido también como "Dudo en Cacho" en Chile y algunos países.  
Es un juego de engaño, probabilidad y estrategia donde los jugadores intentan adivinar cuántos dados de cierto valor (o pintas) hay en total entre todos los participantes.  

En cada ronda, un participante realiza una apuesta sobre la cantidad y el valor de los dados, y los jugadores restantes pueden:
- **Subir la apuesta** 🎯  
- **Dudar** ❓  
- **Calzar** ✅  

Si alguien duda o calza, se revelan los dados y se determina si fue correcto o no.  
El objetivo es ser el **último jugador con dados en la mesa** para ganar.  

Las reglas que se usaron en esta adaptación fueron las de la siguiente web:  
👉 [Cómo jugar Dudo en Cacho](https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho)

---

## ⚙️ Requisitos

- Python **3.11 o superior**
- Instalar las dependencias listadas en `requirements.txt`

## 🚀 Instalación

1. Clona el repositorio o descarga los archivos.  
2. Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```
🧪 Ejecución de Pruebas
Para ejecutar los tests, usando pytest:
```bash
pytest
o
python3 -m pytest
```
Con más detalle:
```bash
pytest -v
o
python3 -m pytest -v

```
Para ver el coverage de los tests:
```bash
pytest --cov=src --cov-report=term-missing
python3 -m pytest --cov=src --cov-report=term-missing
```
📂 Estructura del proyecto
```bash
src/
 ├── juego/        # Lógica principal del juego
 ├── servicios/    # Servicios auxiliares
tests/             # Pruebas unitarias
requirements.txt   # Dependencias
```

👥 Colaboradores
1. [Felipe Alejandro Tilleria Morales](https://github.com/hooooooooola)
2. [Oliver Isaías Peñailillo Sanzana](https://github.com/pyrrss)
3. [Cristóbal Alonso González Cifuentes](https://github.com/Lunara02)
