nome=input ("Antes de começar, informe seu nome: ")
print('''
     Olá,''', nome,"!")
print("Seja bem-vindo(a) ao Quiz do The Chain Club." " Você irá responder 5 perguntas valendo 20 pontos cada. ")
message= input("Vamos começar? ")


def newquiz():
    if message == "sim":
        print ("Ok, vamos lá :D")
        # Primeira pergunta:
        pergunta1=print ("Qual desses estudiosos é considerado o pai do Iluminismo e precursor da Geográfia moderna:")
        print ('a) Ratzel')
        print ('b) Bismarck')
        print ('c) Kant')
        print ('d) John Locke')
        resposta= input ("Digite uma das opções: ")
        pontos1=0
        if resposta == "c":
            pontos1 =+ 20
        else:
            pontos1 == 0
        # Segunda pergunta:
        pergunta2=print ("A revolta da vacina que ocorreu no Brasil em 1904, emergiu sob o governo de qual presidente?")
        print ('a) Washington Luis')
        print ('b) Rodrigo Alves')
        print ('c) Campos Sales')
        print ('d) Getúlio Vargas')
        resposta= input ("Digite uma das opções: ")
        pontos2=0
        if resposta == "b":
            pontos2 =+20
        else:
            pontos2 == 0
        # Terceira pergunta:
            pergunta3=print ("O período histórico conhecido como Absolutismo teve como uma das suas principais características")
            print ('a) a relação de suserania e vassalagem')
            print ('b) a crítica à centralização do poder ao monarca')
            print ('c) a construção de burgos e nascimento da classe burguêsa')
            print ('d) o fomento de politícas econômicas e início do capitalismo comercial')
            print ('e) Todas alternativas estão corretas')
            resposta= input ("Digite uma das opções: ")
            pontos3=0
            if resposta == "d":
                pontos3 =+20 
            else:
                pontos3 == 0
        # Quarta pergunta:
        pergunta4=print ("Qual é a primeria fase dentre as eras literárias a ter um caráter depressivo e sombrio?")
        print ('a) Ultrarromantismo')
        print ('b) Simbolismo')
        print ('c) Parnasianismo')
        print ('d) Modernismo')
        resposta= input ("Digite uma das opções: ")
        pontos4=0
        if resposta == "a":
            pontos4 =+ 20
        else:
            pontos4 == 0
        # Quinta pergunta:
        pergunta4=print ("Qual é o termo ténico que define a 3ª revolução industrial?")
        print ('a) Revolução técnico-científica-informacional')
        print ('b) Indústria 4.0')
        print ('c) Revolução do maquinário')
        print ('d) Tecnologia petrolífera')
        resposta= input ("Digite uma das opções: ")
        pontos5=0
        if resposta == "a":
            pontos5 =+ 20
        else:
            pontos5 == 0
        result= pontos1+pontos2+pontos3+pontos4+pontos5
        if result > 20:
            print("NICE! você foi muito bem. Sua pontuação final é", result)
        else:
            print("Poxa, estude mais. Sua pontuação é", result)
            
    elif message == "não":
        print ("Que pena,", nome ,"!quando quiser é só retornar :D")
    else:
        print ('Responda somente com "sim"" e "não".')
        
     

newquiz()

