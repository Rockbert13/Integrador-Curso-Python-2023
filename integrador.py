import random
import os
import numpy as np
import matplotlib.pyplot as plt

class Juegos:
    def __init__(self):                                                         # SE CREA EL DICCIONARIO CON LAS OPCIONES PARA EL MENU
         
        self.opciones_de_juegos = {
            "1": "Piedra, Papel, Tijera",
            "2": "Adivinar un Numero",
            "3": "Tirar Dado",
            "4": "Graficar una Funcion Matematica"
            }
    
    def menu(self):                                                             # RECORREMOS EL DICCIONARIO PARA MOSTRAR LAS OPCIONES A ELEGIR
        os.system('CLS')
        print('Elige una opcion:\n')
        for opcion, juego in self.opciones_de_juegos.items():
            print(f'{opcion}. {juego}')
        print('0. Salir')
    
    def jugar(self):                                                            # IMPRIMIMOS EN PANTALLA LAS OPCIONES A ELEGIR Y PASAR A CADA UNA
        os.system('CLS')
        while True:
            self.menu()
            opcion = input("\nPor favor, ingresa el número del juego que quieras participar: ")
            if opcion == "0":
                print("\n*****   Gracias por participar   *****\n")
                break
            elif opcion in self.opciones_de_juegos:
                if opcion == "1":
                    self.piedra_papel_tijera()
                elif opcion == "2":
                    self.adivinar_un_numero()
                elif opcion == "3":
                    self.tirar_un_dado()
                elif opcion == "4":
                    self.graficar_funcion()
            else:
                print("Opcion incorrecta. Por favor, selecciona una opcion valida.") 
                
    def piedra_papel_tijera(self):                                              # JUEGO PIEDRA PAPEL O TIJERAS FUNCION DEL JUEGO
        os.system('CLS')
        print('--- Jugaremos Piedra, Papel y Tijera contra la computadora ---\n')
        os.system('pause')
        os.system('CLS')
        lista_opciones = ['piedra','papel','tijera']
        while True:
            eleccion_jugador = input('Ingrese piedra, papel o tijera: ').upper()
            eleccion_computadora = random.choice(lista_opciones).upper()
            print(f'\nTu eleccion es: {eleccion_jugador}, la eleccion de la computadores es: {eleccion_computadora}\n')
            if eleccion_jugador == eleccion_computadora:
                print('¡¡¡   EMPATARON   !!!')
            elif eleccion_jugador == 'PAPEL' and eleccion_computadora == 'PIEDRA':
                print('*****   GANASTE   *****')         
            elif eleccion_jugador == 'TIJERA' and eleccion_computadora == 'PAPEL':
                print('*****   GANASTE   *****')
            elif eleccion_jugador == 'PIEDRA' and eleccion_computadora == 'TIJERA':
                print('*****   GANASTE   *****')   
            else:
                print('Perdistes contra la Computadora')
        
            opcion = input('\nQUIERES JUGAR DE NUEVO (S/N): ').upper()      
            if opcion == 'N':
                break
            os.system('CLS')
            
    def adivinar_un_numero(self):                                               # JUEGO PARA ADIVINAR UN NUMERO CONTRA LA COPUTADORA
        os.system('cls')
        print('--- Jugaremos a adivinar un numero entre el 1 y 10 contra la Computadora ---\n')  
        os.system('pause')  
        while True:
            os.system('cls')
            eleccion_computadora = random.randint(1,10)
            eleccion_jugador = int(input('\nIngrese un numero entre el 1 y el 10: '))
            if eleccion_jugador == eleccion_computadora:
                print('\n*****   GANASTE   *****\n')
                print(f'Tu numero elegido es: {eleccion_jugador} y el de la computadora era: {eleccion_computadora}')
            else:
                print('\n¡¡¡ NO ADIVINASTES EL NUMERO !!!\n')
                print(f'Tu numero elegido fue: {eleccion_jugador} y el de la computadora era: {eleccion_computadora}')

            opcion = input('\nQUIERES JUGAR DE NUEVO (S/N): ').upper()   
            if opcion == 'N':
                break
            os.system('CLS')


    def  tirar_un_dado(self):                                                   # JUEGO PARA JUGAR A LOS DADOS CONTRA LA COMPUTADORA                
        os.system('cls')
        print('--- Jugaremos a tirar un dado contra la computadora, el numero mas alto ¡GANA! ---\n')  
        os.system('pause')  
        while True:
            eleccion_jugador= input('Para tirar el dado pulse T: ').upper()
            if eleccion_jugador != 'T':
                print('\npor favor pulse la letra correcta (T)')
            else:
                eleccion_jugador = random.randint(1, 6)
                eleccion_computadora = random.randint(1, 6)
                print(f'\nTu dado salio con el numero: {eleccion_jugador}\nEl dado de la computadora salio con el numero: {eleccion_computadora}\n')
                if eleccion_jugador == eleccion_computadora:
                    print('¡¡¡   EMPATARON   !!!')
                elif eleccion_jugador < eleccion_computadora:
                    print('Perdistes contra la Computadora')
                else:
                    print('*****   GANASTE   *****') 
            
            opcion = input('\nQUIERES JUGAR DE NUEVO (S/N): ').upper()   
            if opcion == 'N':
                break          
        os.system('cls')
 
    def graficar_funcion(self):                         #ACA GRAFICAREMOS LA ECUACION LINEAL Y = 3X - 2
        os.system('cls')
        print('''Graficaremos la ecuacion lineal y = 3x - 2
con el numero ingresado usaremos un rango de 5 numeros mas\n''')
        A = int(input("ingrese un numero por favor: "))
        
        x = np.arange(A, A+5)
        y = 3 * x - 2
        plt.plot(x, y)
            
        plt.xlabel('Eje X')
        plt.ylabel('Eje y')
        plt.title('Grafica de Ecuacion lineal y = 3x - 2')
        plt.grid(True)
        plt.show()
        os.system('pause')
           





os.system('CLS')    
menu_seleccion = Juegos()
menu_seleccion.jugar()