import random
lista = ["pedra","papel","tesoura"]
iten = ["""                       !@                         
                  @@@@@@@@@                       
            :@@@@@@@@@@@@@@@@                     
       @@@@@@@@@@@@@@@@@@@@@@@@                   
      .!!@@@@@@@@@@@@@@@@@@@@@@@@                 
      .!!!!@@@@@@@@@@@@@@@@@@@@@@@@               
       !!!!!!@@@@@@@@@@@@@@@@@@@@@@@@             
       !!!!!!!!@@@@@@@@@@@@@@@@@@@@@@@@           
       !!!!!!!!!!#@@@@@@@@@@@@@@@@@.:!!!          
       !!!!!!!!!!!!!@@@@@@@@@#!!!!!!!!!!          
       !!!!!!!!!!!!!!!@@!!!!!!!!!!!!!!!!          
       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!          
       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!          
       :!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!          
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!          
          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!          
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!          
              !!!!!!!!!!!!!!!!!!!!!!!!!!          
                !!!!!!!!!!!!!!!!!!!!!!!:          
                  !!!!!!!!!!!!!!!:                
                    !!!!!!!:                      
                      .                           
""",
        """                                                  
                                                  
                                                  
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@#################@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@!::::::::::::::::@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
                                                  
                                                  """,
        """                        #:                        
                       .#!                        
                       !#!                        
                       ###                        
                       ###.                       
                      !!::#                       
                      #####                       
                      #@###                       
                    .::: :.:.                     
                   !!::: !:.!!                    
                 #!@@@:: .:!@#!!                  
              #@@    @@: .#@    @#!               
            .!@       @: :@       @!              
             !@      !@:!:@!      @!              
              !#@#!@@@@   @#@#.#@@#               
                                                  """]
rodar = False
while rodar:
    maquina = random.randint(3)
    jogador = str(input("digite sua opção pedra, papel ou tesoura")).index(lista)
    if maquina == jogador :
        print(f""""empate.
                você:{iten[jogador]}

                maquina: {iten[maquina]}
                        \n você empatou!""")
    elif maquina > jogador or maquina == 1 and jogador == 3:
        print(f""""empate.
                você:{iten[jogador]}  

                maquina: {iten[maquina]}
                        """)
        print("você perdeu!")
    else:
        print(f""""empate.
                você:{iten[jogador]}

                maquina: {iten[maquina]}
                        """)
        print("você ganhou!")

    rodar = input("continuar jogando? sim | não : ").strip().lower().startswith('s')