# Chave, pode ser qualquer número natural inteiro diferente de zero
chave = 3

#OBS: ATIVIDADE 1 - INICIO
def cifra_cesar(texto, chave):
    texto_cifrado = ""
    for letra in texto:
        if letra.isalpha():
            # Determina se a letra é maiúscula ou minúscula
            if letra.isupper():
                limite = ord('Z')
            else:
                limite = ord('z')
            
            # Aplica o deslocamento da chave
            codigo = ord(letra) + chave
            
            # Verifica se o código ultrapassou o limite do alfabeto
            if codigo > limite:
                codigo -= 26
            
            # Adiciona a letra cifrada ao texto cifrado
            texto_cifrado += chr(codigo)
        else:
            # Se não for uma letra, mantém o caractere original
            texto_cifrado += letra
    return texto_cifrado

def decifra_cesar(texto_cifrado, chave):
    texto_decifrado = ""
    for letra in texto_cifrado:
        if letra.isalpha():
            # Determina se a letra é maiúscula ou minúscula
            if letra.isupper():
                limite = ord('Z')
            else:
                limite = ord('z')
            
            # Aplica o deslocamento inverso da chave para decifrar
            codigo = ord(letra) - chave
            
            # Verifica se o código ultrapassou o limite do alfabeto
            if codigo < limite - 25:
                codigo += 26
            
            # Adiciona a letra decifrada ao texto decifrado
            texto_decifrado += chr(codigo)
        else:
            # Mantém os caracteres não alfabéticos inalterados
            texto_decifrado += letra
    return texto_decifrado

#OBS: ATIVIDADE 1 - FIM
#OBS: ATIVIDADE 2 - INICIO

# Função para calcular a frequência das letras em um texto
def calcular_frequencia_letras(texto):
    frequencia = {}
    total_letras = 0

    for letra in texto:
        if letra.isalpha():
            letra = letra.lower()
            frequencia[letra] = frequencia.get(letra, 0) + 1
            total_letras += 1

    for letra, freq in frequencia.items():
        frequencia[letra] = freq / total_letras

    return frequencia

# Função para realizar a criptoanálise de César
def criptoanalise_cesar(texto_cifrado, frequencia_idioma):
    melhor_chave = None
    melhor_correlacao = 0

    # Testa todas as chaves possíveis
    for chave in range(1, 26):
        texto_decifrado = decifra_cesar(texto_cifrado, chave)
        frequencia_texto = calcular_frequencia_letras(texto_decifrado)

        correlacao = 0
        for letra in frequencia_texto:
            if letra in frequencia_idioma:
                correlacao += frequencia_texto[letra] * frequencia_idioma[letra]

        if correlacao > melhor_correlacao:
            melhor_correlacao = correlacao
            melhor_chave = chave

    return melhor_chave

# Frequência das letras no idioma português
frequencia_portugues = {'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99, 'e': 12.57, 'f': 1.02, 'g': 1.30, 'h': 1.28,
                        'i': 6.18, 'j': 0.40, 'k': 0.02, 'l': 2.78, 'm': 4.74, 'n': 5.05, 'o': 10.73, 'p': 2.52,
                        'q': 1.20, 'r': 6.53, 's': 7.81, 't': 4.34, 'u': 4.63, 'v': 1.67, 'w': 0.01, 'x': 0.21,
                        'y': 0.01, 'z': 0.47}

#OBS: ATIVIDADE 2 - FIM

# Executar a criptoanálise
# A encriptação aceita assentos, no entando a desencriptação não
print("Digite o texto a ser cifrado: \nOSB: (A encriptação aceita assentos, no entando, a desencriptação pode não funcionar corretamente)\n")
texto_original = input()

# Cifrar o texto original
texto_cifrado = cifra_cesar(texto_original, chave)
print("Texto cifrado:", texto_cifrado)

# Decifrar o texto usando a chave encontrada
texto_decifrado = decifra_cesar(texto_cifrado, chave)
print("Texto decifrado:", texto_decifrado)

# Executar a criptoanálise e revela qual é a chave através da análise de frequência
chave_encontrada = criptoanalise_cesar(texto_cifrado, frequencia_portugues)
print("Criptoanalise Cesar - Chave encontrada:", chave_encontrada)

# Calcular e imprimir as frequências das letras no texto cifrado
print("\nFrequência das letras no texto cifrado:")
frequencia_cifrado = calcular_frequencia_letras(texto_cifrado)
for letra, freq in frequencia_cifrado.items():
    print(f"{letra}: {freq * 100:.2f}%")

# Calcular e imprimir as frequências das letras no texto decifrado
print("\nFrequência das letras no texto decifrado:")
frequencia_decifrado = calcular_frequencia_letras(texto_decifrado)
for letra, freq in frequencia_decifrado.items():
    print(f"{letra}: {freq * 100:.2f}%")