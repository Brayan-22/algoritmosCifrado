# 🔐 Algoritmos de Cifrado: Vigenère y Transposición Simple

Este repositorio contiene un proyecto de implementación de dos algoritmos clásicos de criptografía: el **Cifrado de Vigenère** y el **Cifrado por Transposición Simple**. Ambos algoritmos se utilizan para ocultar el contenido de mensajes mediante técnicas de cifrado simétrico.

## 📌 Contenido

- [Descripción](#descripción)
- [Algoritmos Implementados](#algoritmos-implementados)
- [Requisitos](#requisitos)
- [Uso](#uso)
- [Ejemplos](#ejemplos)
- [Para Desarrolladores](#para-desarrolladores)
- [Licencia](#licencia)

---

## 📝 Descripción

Este proyecto tiene fines educativos y está orientado a la materia de redes de comunicación 3.

- **Cifrado de Vigenère**: utiliza una palabra clave para cifrar un mensaje mediante sustitución polialfabética.
- **Cifrado de Transposición Simple**: reorganiza los caracteres del mensaje original siguiendo un patrón definido por una clave.

---

## 🔐 Algoritmos Implementados

### 1. Cifrado de Vigenère

- Cifra un mensaje utilizando una clave repetida.
- Utiliza letras mayúsculas del alfabeto A-Z.
- Desplaza cada letra del mensaje según la letra correspondiente en la clave.

### 2. Cifrado de Transposición Simple

- Reordena los caracteres del texto claro según una clave numérica o alfabética.
- Implementa una matriz para aplicar la transposición.
- Adapta la longitud del mensaje según la clave.

---

## 🛠️ Requisitos

- Python 3.11.6
*o reemplazar por el lenguaje correspondiente si no es Python.*

- No requiere librerías externas (si aplica).

---

## ▶️ Uso

Para ejecutar el proyecto:

```bash
# Ejecutar cifrado de Vigenère
python vigenere.py "MENSAJE" "CLAVE"

# Ejecutar cifrado de Transposición Simple
python transposicion.py "MENSAJE" "CLAVE"
