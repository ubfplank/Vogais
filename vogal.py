def contar_vogais(texto):
    vogais = "aeiou"
    contagem = 0
    for letra in texto.lower():
        if letra in vogais:
            contagem += 1
    print(f"Número de vogais: {contagem}")

frase = input("Digite uma frase: ")
contar_vogais(frase)
