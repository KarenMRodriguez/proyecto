import funciones.globales as gf
import modules.corefiles as cf
import funciones.citas as ct
import main

def menucitas(op : int):
 
    title =  """
    ****************
    ** MENU CITAS **
    ****************
    """
    menucitasop= '1.buscar \n2.Agendar\n3. Editar\n4. Eliminar\n5. salir'
    if (op != 5):
        print(title)
        print(menucitasop)
        try:
           op  = int(input(",)"))
        except ValueError:
            print("opcion no tiene formato adecuado")   
            gf.pausar_pantalla()
            menucitasop(0)
        else:
           match (op):  
               case 1:
                   ct.searchData
               case 2:
                    ct.newcita()
               case  3:  
                   ct.Modifydata()
               case 4:
                   pass
               case 5:
                   main.mainMenu
               case _:
                   print("la opcion no esta disponible")
                   gf.pausar_pantalla()
