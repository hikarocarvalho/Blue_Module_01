#Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário
#é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha
#mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

#perform the calculus to define the salary
def calculateTheSalary(hours=0,valuebyhour=0):
    salary = hours * valuebyhour
    return salary
#get values from user
def getValuesByUser():
    hours = int(input("Enter with the number of hours worked: "))
    valuebyhour = float(input("Enter with the value by hour: "))
    return calculateTheSalary(hours,valuebyhour)
#show the salary result
print("The salary from this user is:",getValuesByUser())