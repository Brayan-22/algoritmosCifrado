import sys
from vigenere import cifrar_vigenere, descifrar_vigenere
from transposicion import cifrar_transposicion, descifrar_transposicion
def main():
    # --- Ejemplo de Uso ---
    texto_defaul = "HOLAMUNDO"
    clave_defaul = "SECRETO"
    cifrado = 1  # 1 para Vigenère, 0 para Transposición simple
    if len(sys.argv) >= 1:
        cifrado = sys.argv[1]
        if cifrado.isdigit():
            cifrado = int(cifrado)
            print(f"Modo de cifrado seleccionado: {cifrado}")
        else:
            print("El primer argumento debe ser 1 (Vigenère) o 0 (Transposición simple).")
            return
    if len(sys.argv) > 2:
        texto = sys.argv[2]
        clave = sys.argv[3]
        if cifrado == 1:
            print("Cifrado Vigenère")
            print(f"\nCifrando {texto} con la clave {clave}")
            texto_cifrado = cifrar_vigenere(texto, clave)
            print(f"\nDescifrando {texto_cifrado} con la clave {clave}")
            descifrado = descifrar_vigenere(texto_cifrado, clave)
            print(descifrado)
        elif cifrado == 0:
            relleno = "_"
            print("Cifrado Transposición simple")
            print(f"\nCifrando {texto} con la clave {clave}")
            texto_cifrado = cifrar_transposicion(texto, clave, relleno)
            print(texto_cifrado)
            print(f"\nDescifrando {texto_cifrado} con la clave {clave}")
            descifrado = descifrar_transposicion(texto_cifrado, clave, relleno)
            print(descifrado)
        else:
            print("Opción no válida. Use 1 para Vigenère o 0 para Transposición simple.")
            print("Uso: python vigenere.py <1 ó 0> <texto> <clave>")
    elif len(sys.argv) > 4:
        print("Demasiados argumentos. Uso: python vigenere.py <1 ó 0> <texto> <clave>")
    else:
        if cifrado == 1:
            print("Cifrado Vigenère")
            print(f"\nCifrando {texto_defaul} con la clave {clave_defaul}")
            texto_cifrado = cifrar_vigenere(texto_defaul, clave_defaul)
            print(f"\nDescifrando {texto_cifrado} con la clave {clave_defaul}")
            descifrado = descifrar_vigenere(texto_cifrado, clave_defaul)
            print(descifrado)
        elif cifrado == 0:
            relleno = "_"
            print("Cifrado Transposición simple")
            print(f"\nCifrando {texto_defaul} con la clave {clave_defaul}")
            texto_cifrado = cifrar_transposicion(texto_defaul, clave_defaul, relleno)
            print(texto_cifrado)
            print(f"\nDescifrando {texto_cifrado} con la clave {clave_defaul}")
            descifrado = descifrar_transposicion(texto_cifrado, clave_defaul, relleno)
            print(descifrado)


if __name__ == "__main__":
    main()



