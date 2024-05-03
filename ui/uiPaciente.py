import modules.corefiles as cf
import funciones.globales as gf
import funciones.medico as md
import funciones.paciente as pc

def MenuPaciente(op : int):
    title =  """
    ********************
    ** MENU PACIENTES **
    ********************
    """
    MenuPacienteOP =  '1. Buscar Paciente \n2 Agregar Paciente \n3. Editar \n4. Eliminar \n5. salir'
    gf.borrar_pantalla()
    if (op != 5):
       print(title)
       print(MenuPacienteOP)
       try:
           op  = int(input(",)"))
       except ValueError:
            print("opcion no tiene formato adecuado")   
            gf.pausar_pantalla()
            MenuPaciente(0)
       else:
         match (op):  
               case 1:
                    md.searchData
               case 2:   
                    md.NewMedic(0)
               case  2:  
                   md.Modifydata(0)
               case 3:
                   pass
               case 4:
                MenuPaciente(0)
               case _: 
                print('la opcion no es valida ')
                gf.pausar_pantalla    
                 