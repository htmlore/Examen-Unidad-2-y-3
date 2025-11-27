import mysql
from enum import Enum


def conectar(Enum):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="p0y0pi005",
        database="Ventas_Coches"
    )
    cursor = conexion.cursor()
    return cursor, conexion


def CargarDatos():
    pass


if __name__ == '__main__':
    CargarDatos()