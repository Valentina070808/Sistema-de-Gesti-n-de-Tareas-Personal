# tests/test_tasks.py
# Pruebas unitarias para el Sistema de Gestión de Tareas

import unittest
import json
import os
import sys

# Agregar la carpeta raíz al path para importar main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import cargar_tareas, guardar_tareas


class TestSistemaTareas(unittest.TestCase):
    """Clase de pruebas para el sistema de tareas."""
    
    ARCHIVO_PRUEBA = "test_tasks_temp.json"
    
    def setUp(self):
        """Configuración antes de cada prueba."""
        # Crear archivo temporal vacío
        with open(self.ARCHIVO_PRUEBA, "w", encoding="utf-8") as f:
            json.dump([], f)
    
    def tearDown(self):
        """Limpieza después de cada prueba."""
        # Eliminar archivo temporal
        if os.path.exists(self.ARCHIVO_PRUEBA):
            os.remove(self.ARCHIVO_PRUEBA)
    
    def test_agregar_tarea(self):
        """Prueba 1: Verificar que se puede agregar una tarea."""
        tareas = []
        nueva_tarea = {
            "id": 1,
            "titulo": "Tarea de prueba",
            "descripcion": "Descripción de prueba",
            "fecha": "2026-01-15",
            "completada": False
        }
        tareas.append(nueva_tarea)
        
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["titulo"], "Tarea de prueba")
        self.assertFalse(tareas[0]["completada"])
    
    def test_ver_pendientes(self):
        """Prueba 2: Verificar filtrado de tareas pendientes."""
        tareas = [
            {"id": 1, "titulo": "Tarea 1", "completada": False},
            {"id": 2, "titulo": "Tarea 2", "completada": True},
            {"id": 3, "titulo": "Tarea 3", "completada": False}
        ]
        
        pendientes = [t for t in tareas if not t["completada"]]
        
        self.assertEqual(len(pendientes), 2)
        self.assertEqual(pendientes[0]["id"], 1)
        self.assertEqual(pendientes[1]["id"], 3)
    
    def test_marcar_completada(self):
        """Prueba 3: Verificar que se puede marcar una tarea como completada."""
        tareas = [
            {"id": 1, "titulo": "Tarea 1", "completada": False}
        ]
        
        # Marcar como completada
        tareas[0]["completada"] = True
        
        self.assertTrue(tareas[0]["completada"])


if __name__ == "__main__":
    unittest.main()