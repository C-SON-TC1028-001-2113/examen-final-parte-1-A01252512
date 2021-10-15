![Tec de Monterrey](../../images/logotecmty.png)
# Invertir dígitos
Ciclos - Invertir los dígitos de un número

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

El programa debe pedir un número entero al usuario, y después imprimir en
pantalla un número nuevo con los dígitos del primero en órden inverso.
El programa debe aceptar únicamente números de maximo 6 digitos. Para números
de más digitos, el programa debe imprimir `Too long`.

**Sugerencia**: Utiliza los operadores de division entera y módulo para
separar los dígitos.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Enter a number: 123
321
```

```
Enter a number: -8534
-4358
```

```
Enter a number: 12345678
Too long
```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`python -m pytest --tb=short -v`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
