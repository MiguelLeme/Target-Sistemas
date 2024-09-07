def inverter_string(s):
    # Inicializando uma string vazia para armazenar a string invertida
    string_invertida = ''
    
    # Iterar sobre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# Entrada da string (você pode alterar ou usar input)
string = input("Informe uma string para ser invertida: ")

# Chamar a função e exibir o resultado
string_invertida = inverter_string(string)
print(f"String invertida: {string_invertida}")
