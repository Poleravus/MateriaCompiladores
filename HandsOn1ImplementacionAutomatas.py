#Validación de Cadenas Alfabéticas

def validate_alpha(s):
    return s.isalpha()

input_str = "HelloWorld"
if validate_alpha(input_str):
    print("Cadena válida.")
else:
    print("Cadena inválida.")

#Validación de Números Reales

def validate_real(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

input_str = "-123.456"

if validate_real(input_str):
    print("Número válido.")
else:
    print("Número inválido.")


#Validación de Sentencias Selectivas

def validate_if_else(s):
    return "if" in s and "else" in s

input_str = "if x > 0: pass else: pass"
if validate_if_else(input_str):
    print("Sentencia valida")
else:
    print("Sentencia invalida")

