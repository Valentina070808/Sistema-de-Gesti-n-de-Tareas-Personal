# Sistema de Gestión de Tareas Personal

Un sistema simple y eficiente desarrollado en Python para gestionar tareas diarias desde la terminal.

## ✨ Características

| Funcionalidad | Descripción |
|---------------|-------------|
| ✅ Agregar tareas | Con título, descripción y fecha (YYYY-MM-DD) |
| ✅ Ver pendientes | Filtra y muestra solo tareas no completadas |
| ✅ Completar tareas | Marca tareas como finalizadas por ID |
| ✅ Persistencia | Los datos se guardan en `tasks.json` |
| ✅ Validaciones | Campos vacíos, formato de fecha, ID existentes |
| ✅ Sin dependencias | Solo librerías estándar de Python |


## 📁 Estructura del Proyecto

| Tecnología | Propósito |
|------------|-----------|
| **task-manager** | Caperta con todos los archivos |
| **main.py** |  Código principal del sistema |
| **tasks.json** | Almacenamiento de tareas (auto-generado)  |
| **.gitignore** | Archivos ignorados por Git |
| **__init__.py** | Inicializador de paquete |
| **test_tasks.py** | 3 pruebas unitarias |


## 🛠️ Tecnologías

| Tecnología | Propósito |
|------------|-----------|
| **Python 3.x** | Lenguaje de programación |
| **JSON** | Almacenamiento de datos local |
| **unittest** | Pruebas unitarias |
| **Git** | Control de versiones |

## 🔧 Validaciones Incluidas

Campo vacío
❌ El título no puede estar vacío.

Fecha inválida
❌ Fecha inválida. Use formato YYYY-MM-DD

ID no existente
❌ No se encontró una tarea con ese ID.

ID negativo
❌ El ID debe ser un número positivo.

Tarea ya completada
⚠️ Esta tarea ya está completada.

## 📋 Requisitos Previos
Python 3.x instalado (Descargar)

## 📦 Instalación

### Opción: Clonar desde GitHub

```bash
git clone https://github.com/TU-USUARIO/task-manager.git
cd task-manager



