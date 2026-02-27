# main.py
# Sistema de Gestión de Tareas Personal

import json
import os
from datetime import datetime

ARCHIVO_TAREAS = "tasks.json"


def cargar_tareas():
    """Carga las tareas desde el archivo JSON."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_tareas(tareas):
    """Guarda las tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=2, ensure_ascii=False)

def agregar_tarea(tareas):
    """Agrega una nueva tarea a la lista."""
    print("\n--- AGREGAR NUEVA TAREA ---")
    titulo = input("Título: ").strip()
    descripcion = input("Descripción: ").strip()
    fecha = input("Fecha (YYYY-MM-DD): ").strip()
    
    # Validar campos vacíos
    if not titulo:
        print(" El título no puede estar vacío.")
        return
    if not descripcion:
        print("La descripción no puede estar vacío.")
        return
    if not fecha:
        print(" La fecha no puede estar vacía.")
        return

    # Crear nueva tarea
    nueva_tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha": fecha,
        "completada": False
    }
    
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(" Tarea agregada exitosamente!")


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "=" * 40)
    print("   SISTEMA DE GESTIÓN DE TAREAS")
    print("=" * 40)
    print("1. Agregar nueva tarea")
    print("2. Ver tareas pendientes")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    print("=" * 40)


def ver_pendientes(tareas):
    """Muestra todas las tareas pendientes."""
    print("\n--- TAREAS PENDIENTES ---")
    pendientes = [t for t in tareas if not t["completada"]]
    
    if not pendientes:
        print("No hay tareas pendientes.")
        return
    
    for tarea in pendientes:
        estado = "✓" if tarea["completada"] else "○"
        print(f"[{estado}] ID {tarea['id']}: {tarea['titulo']}")
        print(f"    Descripción: {tarea['descripcion']}")
        print(f"    Fecha: {tarea['fecha']}")
        print()

def marcar_completada(tareas):
    """Marca una tarea como completada."""
    print("\n--- MARCAR TAREA COMO COMPLETADA ---")
    ver_pendientes(tareas)
    
    # Validar que haya tareas pendientes
    pendientes = [t for t in tareas if not t["completada"]]
    if not pendientes:
        print("No hay tareas pendientes para completar.")
        return
    
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
        
        # Validar que el ID sea positivo
        if id_tarea <= 0:
            print("El ID debe ser un número positivo.")
            return
        
        for tarea in tareas:
            if tarea["id"] == id_tarea:
                if tarea["completada"]:
                    print("Esta tarea ya está completada.")
                    return
                tarea["completada"] = True
                guardar_tareas(tareas)
                print(f"Tarea '{tarea['titulo']}' marcada como completada!")
                return
        
        print("No se encontró una tarea con ese ID.")
    except ValueError:
        print(" ID inválido. Debe ser un número.")

def menu_principal():
    """Función principal del menú."""
    tareas = cargar_tareas()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_pendientes(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            guardar_tareas(tareas)
            print(" ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()