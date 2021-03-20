######## ---- LIBRERIAS A UTILIZAR ------ ##########
import re #Expreciones regulares
import os.path as path #la ruta del archivo
from nltk.corpus import stopwords #Libreria para elliminar "el" "un" "a" "una" entre otras
from nltk.tokenize import word_tokenize #Libreria para dividir una cadena en palabras
import string #Libreria para cadenas
from collections import Counter #Libreria que sirve como contador
from _collections import OrderedDict #Libreria para ordenamiento 
###################################################

nombre = input("Ingrese el nombre del archivo (sin el .txt): ") #Pedimos el nombre del archivo txt
archivo = nombre+".txt"#le agregamos la extencion txt al nombre que se ingresó
if path.exists(archivo): #verificamos que exista ese nombre en la ruta donde esta este archivo .py, en caso de que si continuamos
    with open(archivo,'r',encoding="utf-8") as miTexto:  #abrimos el archivo en solo lectura, con un encoding utf-8 para los signos de puntuacion
        texto = miTexto.read().lower() #leemos y guardamos el archivo en texto, ademas de pasar todo a minisculas
        result = re.sub(r'[^\w\s]','',texto) #eliminamos las comillas simples, comillas dobles, parentesis, etc.

    stop_words = set(stopwords.words('spanish')) #indicamos una "lista" de pronombres en español
    word_tokens = word_tokenize(result) #separamos las cadenas del texto en palabras

    word_tokens = list(filter(lambda token: token not in  string.punctuation,word_tokens)) #eliminamos los signos de puntuacion

    filtro = [] #arreglo que nos servira como filtro más adelante

    for palabra in word_tokens: #verificamos cada palabra que hay en la lista sin singnos de puntuacion
        if palabra not in stop_words: #verificamos si la palabra no esta en la lista de pronombres
            filtro.append(palabra) #si no esta, la añadimos a arreglo filtro

    c=Counter(filtro) #contamos las palabras que se repitan en el arreglo de filtro
    val = input("Ingrese el numero de palabras que desee que se muestren: ") #pedimos cuantas palabras repetidas quiere el usuario que se muestren
    try: #try para validar que ingrese un numero y no una cadena
        num = int(val) #convertimos el input de string a entero
        y=OrderedDict(c.most_common(num)) #le indicamos que las ordene de las más repetidas a las que menos se repitan, solo se mostraran el numero de palabras que se haya ingresado anteriormente
        print(y) #imprimimos en consola las palabras 

        with open('revision.txt','w',encoding="utf-8") as file: #creamos/reescribimos un archivo llamado revision para escribir las palabras
            for k,v in y.items(): #recorremos y que son las palabras mas comunes, "k" es la palabra y "v" es el numero que se repiten
                #no estamos imprimiendo el numero que se repiten, solo las palabras, por eso abajo solo se imprime "k"
                file.write(k + "\n")#en el archivo escribimos las palabras que hay en "y" con un salto de linea 
    except ValueError: #si el numero de palabras a mostrar no es un numero muestra el mensaje y termina el programa
        print("La entrada no es un numero entero.") #imprimimos el mensaje
    
else: #si no hay un archvio con el nombre ingresado en la ruta, se muestra el mensaje y termina el programa
    print("No existe el archivo en la ruta.")#imprimimos el mensaje.
