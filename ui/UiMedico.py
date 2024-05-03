import modules.corefiles as cf
import funciones.globales as gf
import funciones.medico as md
import funciones.paciente as pc

def MenuMedico(op : int):
    title =  """
    ******************
    ** MENU MEDICOS **
    ******************
    """
    MenuMedicoop ='1. Buscar Medico \n2. gregar Medico\n3. Editar\n4. Elminar\n5. salir'
    gf.borrar_pantalla()
    if (op != 5):
        print(title)
        print(MenuMedicoop)
        try:
           op  = int(input(",)"))
        except ValueError:
            print("opcion no tiene formato adecuado")   
            gf.pausar_pantalla()
            MenuMedicoop(0)
        else:
           match (op):  
               case 1:
                    md.searchData()
               case 2:   
                    md.NewMedic()
               case  3:  
                   md.Modifydata()
               case 4:
                   pass
               case 5:
                   MenuMedico
               case _: 
                print('la opcion no es valida')
                gf.pausar_pantalla    
                  



       
       
           
           


