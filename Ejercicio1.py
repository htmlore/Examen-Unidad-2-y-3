import csv
import mysql
import pandas as pd
from enum import Enum
import mysql.connector
from sqlalchemy import create_engine


'''
	Crear una función que permita guardar el contenido del archivo en una sola tabla de una Base de Datos.
	Debe asumir que existe una Base de Datos llamada Ventas Coches,  la cual contiene una tabla llamada Ventas,
'''

class conectar(Enum):
    USER = "root"
    PASSWORD = "poyopio05"  # <--- Esta es MI contraseña de MySQL, cambiarla de ser necesario (Si) ☆⌒(ゝ。∂)
    NAME_BD = "Ventas_Coches"
    SERVER = "localhost"

def CargarDatos():
    #Creamos la cadena de conexion para conectarnos a nuestra base de datos ദ്ദി◝ ⩊ ◜.ᐟ
    cadena_conexion = (f"mysql+mysqlconnector://"
                       f"{conectar.USER.value}:"
                       f"{conectar.PASSWORD.value}@"
                       f"{conectar.SERVER.value}/"
                       f"{conectar.NAME_BD.value}")

    print(f"Cadena de conexión: {cadena_conexion}")

    try:
        engine = create_engine(cadena_conexion)
        conexion = engine.connect()
        print("Conexión exitosa a la base de datos!!!!")

        #Leemos el archivo CSV con pandas para poder hacer el registro
        df = pd.read_csv("coches.csv",
                         names=['Marca', 'Modelo', 'Tipo', 'Potencia', 'Precio'],
                         sep=';',
                         encoding='utf-8')

        print(f"Se leyeron correctamente los datos ◝(ᵔᗜᵔ)◜")

        #Ahora, insertamos los datos del CSV a la tabla que tenemos en MySQL, como ya
        #Esta creada, usamos append
        df.to_sql("ventas",
                  con=conexion,
                  if_exists="replace",
                  index=False)

        print(f"Se insertaron correctamente los datos a la tabla Ventas (ㅅ´ ˘ `)")

        conexion.close()

    except Exception as e:
        print(f"Error: {e} ՞߹ - ߹՞")



'''
   Crear una función que  se conecte a la base de datos y retorna un DataFrame con el número de autos vendidos por 
   Marca, y el total de ganancia (suma de precios), ordenado por el número de autos vendidos.
   Debe recibir como parámetro la marca que se desea calcular , además de incluir un valor default por si se 
   requiere que retorne la información de todas las marcas. NOTA: Los cálculos debe hacerlos con PANDAS no con la 
   consulta SQL, la consulta solo puede usar select, from.
'''






if __name__ == '__main__':
    #CargarDatos()
    print(". ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.")
