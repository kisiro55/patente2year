import streamlit as st

def determinar_año_patente(patente):
    patente = patente.upper()  # Normalizar a mayúsculas

    # Patentes antes de 1995
    if patente[0] in ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']:
        return "Antes de 1995"

    # Patentes de 1995 a 2016 (formato 3 letras + 3 números)
    if len(patente) == 6:
        letras_año = patente[:2]
        patentes_1995_a_2016 = [
            ('PM', 2016), ('ON', 2015), ('NM', 2014), ('MB', 2013), ('KU', 2012),
            ('JN', 2011), ('IM', 2010), ('HT', 2009), ('GV', 2008), ('GB', 2007),
            ('FI', 2006), ('ET', 2005), ('EI', 2004), ('ED', 2003), ('DX', 2002),
            ('DO', 2001), ('DC', 2000), ('CM', 1999), ('BU', 1998), ('BD', 1997),
            ('AP', 1996)
             #,('AAA', 1995)
        ]
        for letras, año in (patentes_1995_a_2016):
            if letras_año >= letras:
                return año

    # Patentes de 2016 en adelante (formato 2 letras + 3 números + 2 letras)
    if len(patente) == 7:
        numero = int(patente[2:5])
        patentes_info = [
            ('AF', 2023, 770), ('AF', 2022, 600), ('AF', 2021, 0),  # AF000AA y adelante para 2021
            ('AE', 2021, 600), ('AE', 2020, 100), ('AE', 2019, 0),  # AE000AA y adelante para 2019
            ('AD', 2019, 400), ('AD', 2018, 0),  # AD000AA y adelante para 2018
            ('AC', 2018, 200), ('AC', 2017, 0),  # AC000AA y adelante para 2017
            ('AB', 2017, 0), ('AA', 2017, 900), ('AA', 2016, 0),  # AA000AA y adelante para 2016
        ]

        for letras, año, min_numero in (patentes_info):
            if patente[:2] == letras and numero >= min_numero:
                return año

    return "No se pudo determinar el año"


# Streamlit app interface
st.title('Buscador de año de su auto con la patente')

# User input for the license plate
license_plate = st.text_input("Ingrese el nro de su patente para obtener el año de su auto")

if st.button('Find Car Year'):
    if license_plate:  # Check if input is not empty
        year = determinar_año_patente(license_plate)
        st.success(f"El año del auto es: {year}")
    else:
        st.error("Por favor proveer un dominio/patente valida.")
