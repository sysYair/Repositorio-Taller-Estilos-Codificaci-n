def calcular_precio_con_descuento(precio, porcentaje_descuento):
    
    # Validar que los valores sean correctos
    if precio < 0 or porcentaje_descuento < 0:
        return "Valores inválidos"

    # Calcular descuento
    descuento = precio * (porcentaje_descuento / 100)

    # Calcular precio final
    precio_final = precio - descuento

    return precio_final


# Prueba de la función
resultado = calcular_precio_con_descuento(100, 20)
print("Precio final:", resultado)