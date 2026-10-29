def cifraCesar (senha, chave):
    resultado = ""

    for letra in senha:
        if letra.isalpha() and letra.isascii():
            base = ord('A') if letra.isupper() else ord('a')

            posicao = ord(letra) - base
            nova_posicao = (posicao + chave) % 26

            nova_letra = chr(base + nova_posicao)
            resultado += nova_letra

        elif letra.isdigit() and letra.isascii():
            posicao = int(letra)
            novo_numero = (posicao + chave) % 10

            resultado += str(novo_numero)

        else:
            resultado += letra

    return resultado

def withoutCifraCesar(senha, chave):
    return cifraCesar(senha, -chave)