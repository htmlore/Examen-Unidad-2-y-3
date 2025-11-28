import pandas as pd
""" 
    Se crea un programa con cuatro funciones:
    a. Crear un DataFrame con datos de empleados.
    b. Calcular estadísticas (media, desviación estándar, mínimo y máximo) de edad
         y salario para un departamento específico.
    c. Unir dos DataFrames de empleados y guardar el resultado en un archivo CSV.
    d. Agregar información adicional a un DataFrame de empleados desde otro archivo CSV.
"""

def a_crear_primer_dataframe():
    data = {
        "Departamento": ["Ventas", "Ventas", "HR", "HR", "IT", "IT"],
        "Id": [1001, 1002, 2001, 2002, 3001, 3002],
        "Nombre": ["Juan", "Ana", "Luis", "Maria", "Pedro", "Sofía"],
        "Edad": [30, 24, 29, 25, 32, 28],
        "Salario": [40000, 42000, 38000, 39000, 50000, 52000]
    }
    df1 = pd.DataFrame(data)
    df_bonito = df1.set_index(["Departamento", "Id"], drop=False)
    return df_bonito

def b_estadisticas_df1(df_depa, df_bonito, Departamento):
    df_depa = df_bonito[df_bonito["Departamento"] == Departamento]
    df_depa = df_depa.reset_index(drop=True)
    depa_estadis = (
        df_depa.groupby("Departamento")[["Edad", "Salario"]]
        .agg(["mean", "std", "min", "max"])
    )
    return depa_estadis

def c_dfa_dfb(df_unido,salida):
    df1 = pd.read_csv("empleados1.csv")
    df2 = pd.read_csv("empleados2.csv")

    df_unido = pd.concat([df1, df2], ignore_index=True)
    df_unido = df_unido.sort_values("Id")
    df_unido.to_csv(salida, index=False)
    return df_unido

def d_agregar(df_empleados, archivo_extra):
    df_extra = pd.read_csv(archivo_extra)
    df_final = pd.merge(df_empleados, df_extra, on="Id", how="left")
    return df_final


def main():
    df_a = pd.DataFrame({
        "Departamento": ["Ventas", "HR"],
        "Id": [1001, 2001],
        "Nombre": ["Juan", "Luis"],
        "Edad": [30, 29],
        "Salario": [40000, 38000]
    })

    df_b = pd.DataFrame({
        "Departamento": ["IT", "Ventas"],
        "Id": [3001, 1002],
        "Nombre": ["Pedro", "Ana"],
        "Edad": [32, 24],
        "Salario": [50000, 42000]
    })
    df_a.to_csv("empleados1.csv", index=False)
    df_b.to_csv("empleados2.csv", index=False)

    df_extra = pd.DataFrame({
        "Id": [1001, 2001, 3001, 1002],
        "Direccion": ["Av 1", "Calle 2", "Av 3", "Calle 4"],
        "Telefono": ["111-111", "222-222", "333-333", "444-444"],
        "EstadoCivil": ["Soltero", "Casado", "Soltero", "Casado"],
        "Correo": ["a@a.com", "b@b.com", "c@c.com", "d@d.com"],
        "Experiencia": [5, 3, 7, 2]
    })
    df_extra.to_csv("empleados_extra.csv", index=False)

    print("Inciso A: retorne un DataFrame:")
    print(a_crear_primer_dataframe())
    df_bonito = a_crear_primer_dataframe()
    df_bonito.to_csv("DataFrameEmpleados.csv", index=False)

    print("Inciso B: Estadisticas de DataFrame 1")
    print(b_estadisticas_df1(None, df_bonito, "Ventas"))
    df_estadis = b_estadisticas_df1(None, df_bonito, "Ventas")
    df_estadis.to_csv("Estadisticas_Departamento.csv", index=False)

    print("Inciso C: Unir dfa y dfb")
    print(c_dfa_dfb(None, "empleados_unidos.csv"))
    df_unido = c_dfa_dfb(None, "empleados_unidos.csv")
    df_unido.to_csv("empleados_unidos.csv", index=False)

    print("Inciso D: Agregar:")
    print(d_agregar(df_unido, "empleados_extra.csv"))
    df_final = d_agregar(df_unido, "empleados_extra.csv")
    df_final.to_csv("empleados_final.csv", index=False)

main()