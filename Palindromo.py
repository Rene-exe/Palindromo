def encontrar_palindromo(palabra):
    palindromo = palabra[::-1]
    if palindromo == palabra:
        #return True
        print(f'{palabra} Sí es un palíndromo')
    else:
        #return False
        print(f'{palabra} No es un palíndromo')
        
print(encontrar_palindromo("reconocer"))