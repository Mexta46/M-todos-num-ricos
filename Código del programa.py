import re #es la libreria que le permite a python tabajar con expreciones regulares

def parse_function(expression):#Metodo para calcular las expreciones cuadraticas
    # Reemplazar ^ con **
    expression = expression.replace("^", "**")
    # Reemplazar x con *x
    expression = re.sub(r'(?<=[0-9a-zA-Z)])\(', '*(', expression)
    expression = re.sub(r'(?<=[0-9a-zA-Z)])x', '*x', expression)
    # Permitir el uso de constantes como 2x^2+4
    expression = re.sub(r'(?<=[0-9)])(?=[a-zA-Z(])', '*', expression)
    return expression

def bisection_method(func, a, b, error_percent):#Es el metodo que verifica la funcion y el contador que dira hasta cuando parar y que variable es x(la media o la raiz de la función)
    if func(a) * func(b) >= 0:
        print("El método de bisección no es aplicable en este intervalo.")
        return None

    tol = (b - a) * error_percent / 100 #calcula el error aceptable
    iter_count = 0 #incia el conteo de las iteraciones
    while (b - a) / 2 > tol:# compara la media con el porcentaje aceptable
        c = (a + b) / 2 #obtiene x(media)
        if func(c) == 0: #si esta llega a cero se detiene 
            break
        elif func(c) * func(a) < 0: #compara la multiplicación de la primera funcion intervalo por la funcion de x
            b = c #si este es menor que x el limite menor valdra lo mismo que x
        else:
            a = c #si este es mayor que x el limite menor valdra lo mismo que x
        iter_count += 1

    root = (a + b) / 2 #obtiene la raiz o x
    return round(root, 2) #retorna el valor de la raiz o x, reduciendo el resultado a 2 cifras significativas depues del punto


def main():
    #obtiene los datos solicitador
    user_function = input("Ingrese la función (utilice 'x' como la variable): ")
    func = lambda x: eval(parse_function(user_function)) #llama a la funcion que traduce las expreciones a una solucion aritmetica
    a = float(input("Ingrese el límite inferior del intervalo: "))
    b = float(input("Ingrese el límite superior del intervalo: "))
    error_percent = float(input("Ingrese el porcentaje de error permitido: "))
    
    #llama a la funcion para calcular la raiz
    root = bisection_method(func, a, b, error_percent)
    if root is not None:
        print("Raíz encontrada en:", root)
    else:
        print("No se encontró una raíz en el intervalo dado.")

#llama a la funcion principal donde se obtiene y se llaman las demas funciones solo si se ejecuta el script
if __name__ == "__main__":
    main()

