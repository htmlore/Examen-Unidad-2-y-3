import pandas as pd
df = pd.read_csv("bank-loans.csv")

# a. Función simple para obtener clientes dentro de un rango de edad
def rango_edades(df, min_age, max_age):
    return df[(df["age"] >= min_age) & (df["age"] <= max_age)]

# b. Función simple para mostrar la edad media según nivel de estudios
def edad_media_por_nivel_estudios(df):
    return df.groupby("education")["age"].mean()

if __name__ == "__main__":
    min_age = 25
    max_age = 35

    print("Clientes entre 25 y 35 años:")
    print(rango_edades(df, min_age, max_age))
    df_rango = rango_edades(df, min_age, max_age)
    df_rango.to_csv("clientes_25_35.csv", index=False)

    print("\nEdad media por nivel de estudios:")
    print(edad_media_por_nivel_estudios(df))
