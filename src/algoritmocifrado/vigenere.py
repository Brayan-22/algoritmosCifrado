import sys

def generar_clave_vigenere(texto, clave):
    """
    Genera una clave Vigenère a partir del texto y la clave proporcionada.
    :param texto: Texto al que se le aplicará la clave.
    :param clave: Clave para el cifrado Vigenère.
    :return: Clave generada para el cifrado Vigenère.
    """
    clave_generada = ""
    longitud_texto = len(texto)
    longitud_clave = len(clave)
    
    for i in range(longitud_texto):
        clave_generada += clave[i % longitud_clave]
    return clave_generada

def cifrar_vigenere(texto_plano:str, clave_original:str):
    """
    Cifra un texto plano utilizando el cifrado Vigenère.
    :param texto_plano: Texto que se desea cifrar.
    :param clave_original: Clave para el cifrado Vigenère.
    :return: Texto cifrado.
    """
    
    if not texto_plano.isalpha() or not texto_plano.isupper():
        print("El texto debe contener solo letras mayúsculas sin espacios")
        return ""
    if not clave_original.isalpha() or not clave_original.isupper():
        print("La clave debe contener solo letras mayúsculas sin espacios")
        return ""
    texto_cifrado = ""
    clave_extendida = generar_clave_vigenere(texto_plano, clave_original)
    
    print("---Proceso de cifrado Vigenère---")
    print(f"Texto plano: {texto_plano}")
    print(f"Clave original: {clave_original}")
    print(f"Clave extendida: {clave_extendida}")
    
    print("Paso a Paso:")
    print("----------------------------------------------------")
    print("| Letra Texto | Letra Clave | Op. Numérica | Letra Cifrada |")
    print("|-------------|-------------|--------------|---------------|")
    
    for i in range(len(texto_plano)):
        letra_texto = texto_plano[i]
        letra_clave = clave_extendida[i]

        # Convertir letras a números (A=0, B=1, ..., Z=25)
        valor_texto = ord(letra_texto) - ord('A')
        valor_clave = ord(letra_clave) - ord('A')

        # Aplicar la fórmula del cifrado Vigenère: C = (P + K) mod 26
        valor_cifrado = (valor_texto + valor_clave) % 26

        # Convertir el resultado numérico de nuevo a letra
        letra_cifrada = chr(valor_cifrado + ord('A'))
        texto_cifrado += letra_cifrada
        print(f"|      {letra_texto}      |      {letra_clave}      |  ({valor_texto:2} + {valor_clave:2}) % 26 = {valor_cifrado:2} |       {letra_cifrada}       |")
        
    print("----------------------------------------------------")
    print(f"\nTexto Cifrado: {texto_cifrado}")
    print("--- Fin del Proceso ---")
    return texto_cifrado

def descifrar_vigenere(texto_cifrado, clave_original):
    """
    Descifra un texto utilizando el cifrado Vigenère y muestra el proceso.

    Args:
        texto_cifrado (str): El texto a descifrar (solo letras mayúsculas sin espacios).
        clave_original (str): La clave para el descifrado (solo letras mayúsculas).

    Returns:
        str: El texto descifrado.
    """
    if not texto_cifrado.isalpha() or not texto_cifrado.isupper():
        print("Error: El texto cifrado debe contener solo letras mayúsculas sin espacios.")
        return ""
    if not clave_original.isalpha() or not clave_original.isupper():
        print("Error: La clave debe contener solo letras mayúsculas.")
        return ""

    texto_descifrado = ""
    clave_extendida = generar_clave_vigenere(texto_cifrado, clave_original)

    print("\n--- Proceso de Descifrado Vigenère ---")
    print(f"Texto Cifrado: {texto_cifrado}")
    print(f"Clave Original: {clave_original}")
    print(f"Clave Ext.   : {clave_extendida}\n")

    print("Paso a Paso:")
    print("----------------------------------------------------")
    print("| Letra Cifrada | Letra Clave | Op. Numérica | Letra Texto |")
    print("|---------------|-------------|--------------|-------------|")

    for i in range(len(texto_cifrado)):
        letra_cifrada = texto_cifrado[i]
        letra_clave = clave_extendida[i]

        # Convertir letras a números (A=0, B=1, ..., Z=25)
        valor_cifrado = ord(letra_cifrada) - ord('A')
        valor_clave = ord(letra_clave) - ord('A')

        # Aplicar la fórmula del descifrado Vigenère: P = (C - K + 26) mod 26
        valor_texto = (valor_cifrado - valor_clave + 26) % 26

        # Convertir el resultado numérico de nuevo a letra
        letra_texto = chr(valor_texto + ord('A'))
        texto_descifrado += letra_texto

        print(f"|       {letra_cifrada}       |      {letra_clave}      | ({valor_cifrado:2} - {valor_clave:2} + 26) % 26 = {valor_texto:2} |      {letra_texto}      |")

    print("----------------------------------------------------")
    print(f"\nTexto Descifrado: {texto_descifrado}")
    print("--- Fin del Proceso ---")
    return texto_descifrado

