def calcular_precio_final(precio, porcentaje_descuento, impuesto=0):
   
    # Validaciones
    if precio < 0:
        return "El precio no puede ser negativo"
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        return "Descuento inválido"
    if impuesto < 0:
        return "Impuesto inválido"

    # Cálculo del descuento
    descuento = precio * (porcentaje_descuento / 100)
    precio_con_descuento = precio - descuento

    # Cálculo del impuesto
    valor_impuesto = precio_con_descuento * (impuesto / 100)
    precio_final = precio_con_descuento + valor_impuesto

    # Redondeo a 2 decimales
    return round(precio_final, 2)


# Prueba
resultado = calcular_precio_final(100, 20, 19)
print("Precio final:", resultado)