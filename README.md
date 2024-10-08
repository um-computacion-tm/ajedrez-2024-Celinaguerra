## Descripción

Este proyecto es una implementación del juego de ajedrez utilizando Python, ejecutable mediante Docker, se han modificado algunas reglas tradicionales del juego, las cuales se describen a continuación.

## Reglas del Juego

El ajedrez es un juego de estrategia para dos jugadores, que se juega sobre un tablero de 8x8 casillas alternas en colores claros y oscuros. 
Cada jugador controla 16 piezas con el objetivo de capturar al rey del oponente.
El ganador se decidirá por quien capture primero al rey enemigo o por un empate acordado por ambos jugadores.

**Movimiento de las Piezas**:
   - **Peón**: Avanza una casilla hacia adelante, pero captura en diagonal. Puede moverse dos casillas hacia adelante en su primer movimiento.
   - **Torre**: Se mueve horizontal o verticalmente cualquier número de casillas.
   - **Caballo**: Se mueve en forma de "L", dos casillas en una dirección y una en perpendicular.
   - **Alfil**: Se mueve diagonalmente cualquier número de casillas.
   - **Dama**: Combina los movimientos de la torre y el alfil.
   - **Rey**: Se mueve una casilla en cualquier dirección.

**Promoción del Peón**: Cuando un peón alcance la última fila, este promocionará a reina.

## Instrucciones para Ejecutar el Juego

Este proyecto está preparado para ejecutarse mediante Docker. A continuación, se detallan los pasos para su correcta ejecución:

### Requisitos Previos

Asegúrate de tener instalado Docker en tu sistema. Puedes consultar la documentación oficial de Docker para su instalación: [Docker Installation Guide](https://docs.docker.com/get-docker/).

### Clonación del Repositorio

Clona el repositorio en tu máquina local usando el siguiente comando:

git clone https://github.com/tu-usuario/ajedrez-2024-Celinaguerra.git
cd ajedrez-2024-Celinaguerra

### Para construir la imagen Docker del juego, ejecuta el siguiente comando:
docker buildx build -t ajedrez-2024 .

### Una vez construida la imagen, puedes ejecutar el juego con el siguiente comando:
docker run -i ajedrez-2024


# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-Celinaguerra/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-Celinaguerra/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/5f076d49e1fa7b511f94/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Celinaguerra/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/5f076d49e1fa7b511f94/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Celinaguerra/test_coverage)

Alumno: Celina Guerra Díaz