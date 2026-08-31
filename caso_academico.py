def titulo():
    print("="*40)
def validar_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota and nota<=20:
                return nota
            else:
                print("ERROR fuera de rango[0-20]")
        except ValueError:
            print("Error, de ingresar un valor numerico") 
#funcion con retorno

def calcular_EF(proyecto_final,lab):
            nota_EF=proyecto_final*0.6+lab*0.4
            return nota_EF
#funcion con retorno
def bono_Cisco(nota_EF,tiene_cisco):
    if tiene_cisco=="s":
        nota_EF+=1
        if nota_EF>20:
            nota_EF=20
    return nota_EF
#funcion con retorno
def promedio_final(t1,t2,t3,ep,ef):
    promedio=t1*0.1+t2*0.1+t3*0.1+ep*0.2+ef*0.5
    return promedio
#funcion con retorno
def estado_acd(promedio):
    if promedio>=12:
        estado="Aprobado"
    else:
        estado="Desaprobado"
    return estado

titulo()
alumno=input("Ingresar Nombre del Estudiante: ")
print("*************Ingresar notas*************")
t1=validar_nota("Ingresar nota T1(10%)")
t2=validar_nota("Ingresar nota T2(10%)")
t3=validar_nota("Ingresar nota T3(10%)")
ep=validar_nota("Ingresar nota Examen Parcial(20%)")
print("Ingresar notas para el Examen Final(50%) ")
proyecto_final=validar_nota("Ingresar nota del proyecto final(60'%'EF):")
nota_lab=validar_nota("Ingresar nota del laboratorio(40'%'EF)")
while True:
    curso_cisco=input("Tiene certificacion de curso cisco[s/n]").lower()
    if curso_cisco in ["s","n"]:
        break
    print("Error: Ingresar solo[s ó n]...!!!")
    
nota_EF=calcular_EF(proyecto_final,nota_lab)
nota_EF_Cisco=bono_Cisco(nota_EF,curso_cisco)
promedio_pond=promedio_final(t1,t2,t3,ep,nota_EF_Cisco)
estado=estado_acd(promedio_pond)
print("*"*40)
print("REPORTE DE NOTAS")
print("*"*40)
print("Estudiante:  ",alumno)
if curso_cisco=="s":
    print("Felicitaciones por llevar el curso de Cisco")
print("Nota Examen Final:   ",nota_EF_Cisco)
print("Promedio ponderado:  ",promedio_pond)
print("Estado Academico:    ",estado)
print("*"*40)





    