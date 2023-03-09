##o objetivo desse arquivo é resolver sistemas lineares de 3 variáveis e tres equações
##Euler Borges Ferreira Filho

def main():
    
    ##pegando as linhas do sistema linear
    l1_1,l1_2,l1_3, l1_r = input("Entre com os coeficientes da primeira linha separados por espaços: ").split()

    l2_1,l2_2,l2_3, l2_r = input("Entre com os coeficientes da segunda linha separados por espaços: ").split()

    l3_1,l3_2,l3_3, l3_r = input("Entre com os coeficientes da terceira linha separados por espaços: ").split()

    ##resolvendo por regra de crammer

    determinante_principal = (l1_1*l2_2*l3_3)+ (l1_2*l2_3*l3_1)+ (l1_3*l2_1*l3_2)-(l1_3*l2_2*l3_1)-(l1_2*l2_1*l3_3)-(l1_1*l2_3*l3_2)
    determinante_1 = (l1_r*l2_2*l3_3)+ (l1_2*l2_3*l3_r)+ (l1_3*l2_r*l3_2)-(l1_3*l2_2*l3_r)-(l1_2*l2_r*l3_3)-(l1_r*l2_3*l3_2)
    determinante_2 = (l1_1*l2_r*l3_3)+ (l1_r*l2_3*l3_1)+ (l1_3*l2_1*l3_r)-(l1_3*l2_r*l3_1)-(l1_r*l2_1*l3_3)-(l1_1*l2_3*l3_r)
    determinante_3 = (l1_1*l2_2*l3_r)+ (l1_2*l2_r*l3_1)+ (l1_r*l2_1*l3_2)-(l1_r*l2_2*l3_1)-(l1_2*l2_1*l3_r)-(l1_1*l2_r*l3_2)


    print("Valor da primeira variável: %f", determinante_1/determinante_principal)
    print("Valor da segunda variável: %f", determinante_2/determinante_principal)
    print("Valor da terceira variável: %f", determinante_3/determinante_principal)






if(__name__ == "__main__"):
    main()