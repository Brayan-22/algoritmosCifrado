import math

def obtener_orden_columnas(clave):
    """
    Determina el orden de las columnas basado en la clave.
    Ejemplo: CLAVE -> A(0) C(1) E(2) L(3) V(4)
    Orden de lectura/escritura: [1, 2, 3, 0, 4] (C es la primera, L la segunda, etc. en orden alfabético)
    No, esto no es correcto.
    Ejemplo: "PYTHON"
    Letras ordenadas: H, N, O, P, T, Y
    Índices originales: P(0) Y(1) T(2) H(3) O(4) N(5)
    Orden para leer columnas (índices originales): 3 (H), 5 (N), 4 (O), 0 (P), 2 (T), 1 (Y)
    """
    indices_ordenados = sorted(range(len(clave)), key=lambda k: clave[k])
    # Lo anterior da el orden de las columnas si se ordenaran alfabéticamente.
    # Necesitamos un mapeo que nos diga, para la columna 0 (original), 1, 2... cuál es su
    # posición en la lectura cifrada.

    # Ejemplo: CLAVE = "ZEBRAS"
    # Z E B R A S
    # 0 1 2 3 4 5 (índices originales)
    # Orden alfabético: A(4), B(2), E(1), R(3), S(5), Z(0)
    # Entonces, la columna que se lee primero es la columna 4 (A), luego la 2 (B), etc.
    # orden_lectura = [4, 2, 1, 3, 5, 0]
    
    clave_con_indices = []
    for i, char_clave in enumerate(clave):
        clave_con_indices.append((char_clave, i)) # (carácter de la clave, índice original de la columna)
    
    # Ordenar basado en el carácter de la clave
    clave_con_indices.sort()
    
    # El orden de lectura son los índices originales en el orden alfabético de la clave
    orden_columnas = []
    for char_clave, indice_original in clave_con_indices:
        orden_columnas.append(indice_original)
        
    return orden_columnas

def imprimir_matriz(matriz, cabecera_clave=None):
    """Imprime la matriz de forma legible."""
    if not matriz:
        print("[]")
        return

    if cabecera_clave:
        print("    " + "   ".join(cabecera_clave))
        print("  " + "----" * len(cabecera_clave))


    for i, fila in enumerate(matriz):
        # Para la cabecera de filas (índice)
        print(f"{i} | {' | '.join(str(celda) if celda is not None else ' ' for celda in fila)} |")
    print()


def cifrar_transposicion(texto_plano, clave, caracter_relleno='X'):
    """
    Cifra un texto utilizando transposición columnar simple y muestra el proceso.
    Los espacios se incluyen en el cifrado.
    """
    if not clave:
        print("Error: La clave no puede estar vacía.")
        return ""
    if not clave.isalpha():
        print("Error: La clave debe contener solo letras.")
        return ""
    # Para simplificar, convertimos la clave a mayúsculas y eliminamos duplicados si se quisiera,
    # pero para la transposición simple estándar, los duplicados afectan el orden.
    # Aquí, usaremos la clave tal cual, y el orden se basará en la primera aparición en caso de duplicados.
    # Una mejor práctica sería exigir claves sin letras repetidas o definir cómo manejarlas.
    # Por ahora, sorted() manejará duplicados de forma estable si Python lo hace,
    # o podemos usar enumerate y sort como en obtener_orden_columnas.

    print("--- Proceso de Cifrado por Transposición Simple ---")
    print(f"Texto Plano   : '{texto_plano}'")
    print(f"Clave         : '{clave}'")
    print(f"Relleno       : '{caracter_relleno}'")

    num_columnas = len(clave)
    num_filas = math.ceil(len(texto_plano) / num_columnas)
    
    # Rellenar el texto plano si es necesario
    texto_plano_relleno = texto_plano.ljust(num_filas * num_columnas, caracter_relleno)
    print(f"Texto Rellenado: '{texto_plano_relleno}' (longitud: {len(texto_plano_relleno)})")
    print(f"Dimensiones Matriz: {num_filas} filas x {num_columnas} columnas")

    # 1. Crear y llenar la matriz
    matriz = [['' for _ in range(num_columnas)] for _ in range(num_filas)]
    print("\n1. Llenando la matriz fila por fila:")
    idx_texto = 0
    for r in range(num_filas):
        for c in range(num_columnas):
            if idx_texto < len(texto_plano_relleno):
                matriz[r][c] = texto_plano_relleno[idx_texto]
                idx_texto += 1
    imprimir_matriz(matriz, list(clave))

    # 2. Determinar el orden de lectura de las columnas
    orden_lectura_columnas = obtener_orden_columnas(clave)
    print("2. Determinando el orden de lectura de columnas (basado en clave ordenada alfabéticamente):")
    clave_ordenada_info = sorted([(char, i) for i, char in enumerate(clave)])
    print(f"   Clave original con índices: {list(enumerate(clave))}")
    print(f"   Clave ordenada con índices originales: {clave_ordenada_info}")
    print(f"   Orden de lectura de columnas (índices originales): {orden_lectura_columnas}\n")

    # 3. Leer la matriz por columnas según el orden para obtener el texto cifrado
    print("3. Leyendo la matriz columna por columna según el orden:")
    texto_cifrado = ""
    for col_idx_original in orden_lectura_columnas:
        col_char = clave[col_idx_original]
        print(f"   Leyendo columna del carácter '{col_char}' (índice original {col_idx_original}): ", end="")
        col_contenido = ""
        for r in range(num_filas):
            texto_cifrado += matriz[r][col_idx_original]
            col_contenido += matriz[r][col_idx_original]
        print(f"'{col_contenido}'")

    print("\n--- Fin del Proceso de Cifrado ---")
    print(f"Texto Cifrado: {texto_cifrado}")
    return texto_cifrado

def descifrar_transposicion(texto_cifrado, clave, caracter_relleno='X'):
    """
    Descifra un texto utilizando transposición columnar simple y muestra el proceso.
    """
    if not clave:
        print("Error: La clave no puede estar vacía.")
        return ""
    if not clave.isalpha():
        print("Error: La clave debe contener solo letras.")
        return ""

    print("\n--- Proceso de Descifrado por Transposición Simple ---")
    print(f"Texto Cifrado : '{texto_cifrado}'")
    print(f"Clave         : '{clave}'")
    print(f"Relleno       : '{caracter_relleno}'")

    num_columnas = len(clave)
    num_filas = math.ceil(len(texto_cifrado) / num_columnas)

    if len(texto_cifrado) != num_columnas * num_filas:
        print(f"Advertencia: La longitud del texto cifrado ({len(texto_cifrado)}) "
              f"no es un múltiplo exacto de la longitud de la clave ({num_columnas}). "
              f"Esto puede suceder si el relleno no fue perfecto o se perdió.")
        # Ajustar num_filas es complejo si no se sabe cuántos caracteres faltan en la última fila de la "matriz original"
        # Para este ejemplo, asumimos que el texto cifrado tiene la longitud correcta para llenar la matriz de descifrado.
        # O que el texto cifrado es exactamente el producto de num_filas y num_columnas después del cifrado.
        # Si el cifrado siempre rellena, esto no debería ser un problema.

    print(f"Dimensiones Matriz: {num_filas} filas x {num_columnas} columnas")

    # 1. Determinar el orden de escritura de las columnas (mismo que el de lectura en cifrado)
    orden_escritura_columnas = obtener_orden_columnas(clave)
    print("\n1. Determinando el orden de escritura en columnas (basado en clave ordenada alfabéticamente):")
    clave_ordenada_info = sorted([(char, i) for i, char in enumerate(clave)])
    print(f"   Clave original con índices: {list(enumerate(clave))}")
    print(f"   Clave ordenada con índices originales: {clave_ordenada_info}")
    print(f"   Orden para escribir columnas (índices originales): {orden_escritura_columnas}\n")

    # 2. Crear una matriz vacía y llenarla con el texto cifrado columna por columna
    matriz = [['' for _ in range(num_columnas)] for _ in range(num_filas)]
    print("2. Llenando la matriz columna por columna según el orden:")
    
    idx_texto = 0
    # Iterar sobre el orden_escritura_columnas para saber a qué columna real (0 a num_columnas-1) va el texto
    for col_idx_original_destino in orden_escritura_columnas:
        col_char_clave = clave[col_idx_original_destino]
        print(f"   Escribiendo en columna del carácter '{col_char_clave}' (índice original {col_idx_original_destino}): ", end="")
        col_contenido_escrito = ""
        for r in range(num_filas):
            if idx_texto < len(texto_cifrado):
                matriz[r][col_idx_original_destino] = texto_cifrado[idx_texto]
                col_contenido_escrito += texto_cifrado[idx_texto]
                idx_texto += 1
        print(f"'{col_contenido_escrito}'")

    print("\nMatriz llenada para descifrar:")
    imprimir_matriz(matriz, list(clave)) # Mostrar la clave original como cabecera

    # 3. Leer la matriz fila por fila para obtener el texto descifrado
    print("3. Leyendo la matriz fila por fila para obtener el texto original:")
    texto_descifrado_con_relleno = ""
    for r in range(num_filas):
        fila_contenido = ""
        for c in range(num_columnas):
            texto_descifrado_con_relleno += matriz[r][c]
            fila_contenido += matriz[r][c]
        print(f"   Leyendo fila {r}: '{fila_contenido}'")
    
    # Eliminar el carácter de relleno del final
    texto_descifrado = texto_descifrado_con_relleno.rstrip(caracter_relleno)

    print("\n--- Fin del Proceso de Descifrado ---")
    print(f"Texto Descifrado (con relleno): '{texto_descifrado_con_relleno}'")
    print(f"Texto Descifrado (final)    : '{texto_descifrado}'")
    return texto_descifrado
