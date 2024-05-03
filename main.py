import modules.corefiles as cf
import funciones.globales as gf
import ui.UiMedico as uimd
import ui.uiPaciente as uipc
import ui.Uicitas as uict

def mainMenu(op):
    gf.borrar_pantalla()
    title = """
    ***************************************
    ** CENTRO MEDICO  CARLOS ARDILA LüLE **
    ***************************************
    """
    mainMenuop = "1. medicos\n2. pacientes\n3. agendar cita\n4. salir"
    if (op !=3):
        print(title)
        print(mainMenuop)
        try:
            opcion = int(input(':)'))
        except ValueError:
            print('opcion no valida')
            gf.pausar_pantalla()
            mainMenu()
        else:
            match (opcion):
                case 1:
                    uimd.MenuMedico(0)
                case 2:
                    uipc.MenuPaciente(0)
                case 3:
                    uict.menucitas(0)
                case _:
                    print()
                    gf.pausar_pantalla()
                    mainMenu()
if __name__=='__main__':
    cf.MY_DATABASE ='data/pacientes.json'
    cf.checkFile(gf.centroMedicoAL)
    mainMenu(0)
