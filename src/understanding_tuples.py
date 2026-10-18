"""
  tuplas 

  las tuplas son listas que no cambian de tamaño.
  las tuplas son listas inmutables .


  se utlilizan los parentesis ()  para definir una tupla.

  ejemplo: 

     si tenemos un rectangulo (largo, ancho) 
     que siempre vaa tener cierto tamaño, podemos asegurar 
     que sus dimenciones no van a cambiar si colocamos sus 
     valores en una tupla.

     """
     dimensions = (200, 50) # 200 de largo x 50 de ancho
     print(dimensions)

     # vamos a imprimir elemtos de una tupla 
     # se raliza de la misma forma que con una 
     print(dimensions[0])
     print(dimensions[1])
     print(dir(dimensions))

     #Vmos a modificar el valor de una lista 
     names = ["carlos", "charly", "juan", "wendy"]
     print(names)
     names(0) = "mercury"
     names(1) = "mercury"
     names(2) = "mercury"
     print(names)


     # dimensios [0] = 500 # esta operacion no esta permitida 

    # looping throgh a tuple
    for dimensions in dimensions
       print(dimensions)

     """
     no podemos modificar una tupla,
     lo que si podemos hacer es cambiar 
     las asignaciones de una variable que 
     almacena una tupla 
     """
     dimensions = (500, 1000, 20)
     print("tupla re-definida:", dimensions)

     # lista 
     # dimensions_2 =[200, 50]
     # print(dir(dimensions_2))

     # strings




     # 
     # age  = 34 
     # print(dir(age))

     # tipos de datos boleanos 
     answer = True
     print(answer)
     # print (dir(answer))
     

