def mesMayorConsumo():

    contador=0
    enero=0
    febrero=0
    marzo=0
    abril=0
    mayo=0
    junio=0
    julio=0
    agosto=0
    setiembre=0
    octubre=0
    noviembre=0
    diciembre=0        
    
    while contador<6:

        mes=int(input("\nPor favor indique el mes del recibo: \n1.Enero\n2.Febrero\n3.Marzo\n4.Abril\n5.Mayo\n6.Junio\n7.Julio\n8.Agosto\n9.Setiembre\n10.Octubre\n11.Noviembre\n12.Diciembre\n"))
        mesKWH=float(input("\nDigite la cantidad de KWH consumidos: "))
        
        if mes==1:
            enero=mesKWH
        elif mes==2:
            febrero=mesKWH
        elif mes==3:
            marzo=mesKWH
        elif mes==4:
            abril=mesKWH
        elif mes==5:
            mayo=mesKWH
        elif mes==6:
            junio=mesKWH
        elif mes==7:
            julio=mesKWH
        elif mes==8:
            agosto=mesKWH
        elif mes==9:
            setiembre=mesKWH
        elif mes==10:
            octubre=mesKWH
        elif mes==11:
            noviembre=mesKWH
        elif mes==12:
            diciembre=mesKWH
        else:
            print("\n DIGITO UN MES INVALIDO \n")
        
        contador+=1

    m=max(enero,febrero,marzo,abril,mayo,junio,julio,agosto,setiembre,octubre,noviembre,diciembre)
    if m==enero:
        print("El mes de mayor consumo es enero con  ",enero," KWH")
    elif m==febrero:
        print("El mes de mayor consumo es febrero con  ",febrero," KWH")
    elif m==marzo:
        print("El mes de mayor consumo es marzo con  ",marzo," KWH")
    elif m==abril:
        print("El mes de mayor consumo es abril con  ",abril," KWH")
    elif m==mayo:
        print("El mes de mayor consumo es mayo con  ",mayo," KWH")
    elif m==junio:
        print("El mes de mayor consumo es junio con  ",junio," KWH")
    elif m==julio:
        print("El mes de mayor consumo es julio con  ",julio," KWH")
    elif m==agosto:
        print("El mes de mayor consumo es agosto con  ",agosto," KWH")
    elif m==setiembre:
        print("El mes de mayor consumo es setiembre con  ",setiembre," KWH")
    elif m==octubre:
        print("El mes de mayor consumo es octubre con  ",octubre," KWH")
    elif m==noviembre:
        print("El mes de mayor consumo es noviembre con  ",noviembre," KWH")
    else:
        print("El mes de mayor consumo es diciembre con  ",diciembre," KWH")    

    

def montoEnergia():
    
    mesNombre=input("Por favor ingrese el mes a facturar: ")
    mesNombre=mesNombre.upper()
    punta=float(input("Por favor ingrese los KWH en horario punta: \n"))
    valle=float(input("Por favor ingrese los KWH en horario valle: \n"))
    noct=float(input("Por favor ingrese los KWH en horario nocturno: \n"))
    
    global totalKWH
    totalKWH=punta+valle+noct
    
    if punta<=500:
        montoPunta=punta*167.72
    else:
        montoPunta=punta*207.39
    if valle<=500:
        montoValle=valle*68.75
    else:
        montoValle=valle*83.71
    if noct<=500:
        montoNoct=noct*28.77
    else:
        montoNoct=noct*38.74
    
    global totalConsumido
    totalConsumido=round((montoPunta+montoValle+montoNoct),2)
    
    print("************ECOFACTURA RESIDENCIAL************\n")
    print("************",mesNombre,"************\n")
    print(" ")
    print("KWH:       ",totalKWH)
    print("ENERGIA:   ",totalConsumido,)

def montoAlumbradoPublico():
    global mntAlumb
    mntAlumb=round(totalKWH*3.37,2)
    print("ALUMBRADO: ",mntAlumb,)

def montoTributoBomberos():
    global mntBomb    
    mntBomb=round(totalConsumido*0.0175,2)
    print("BOMBEROS:  ",mntBomb,)

def montoIVA():
    global iva
    if totalKWH>=280:
        iva=round(totalConsumido*0.13,2)
    else:
        iva=0
    print("I.V.A.:    ",iva,)

def totalFactura():

    totFactura = round(float(totalConsumido) + float(mntAlumb) + float(mntBomb) + float(iva),2)
    print("TOTAL FACTURA: ",totFactura," colones")

def imprimirEcoFactura():
    montoEnergia()
    montoAlumbradoPublico()
    montoTributoBomberos()
    montoIVA()
    totalFactura()


def menu():
    ans=True
    while ans:
        print("********************** MENU PRINCIPAL **********************")
        print(" ")
        print("\n","1. Calcular el mes con mas consumo.","\n 2. Calcular la eco-factura del mes. ",
        "\n 3. Salir del programa..","\n")
        
        menu_select=int(input("POR FAVOR INGRESE LA OPCION DESEADA "))    

        if menu_select==1:
            
            mesMayorConsumo()
            
            print(" ")
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")       
        
        elif menu_select==2:
            
            imprimirEcoFactura()
            print(" ")
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
            
        elif menu_select==3:
            
            print("\n","*****!GRACIAS¡ vuelva pronto*****", "\n")
        
            
            ans = False

menu()