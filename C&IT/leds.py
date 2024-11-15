def calcula_total_leds(altura,largura):
  if(altura <= 0 or largura <= 0): #Tratando o caso de 0 de números negativos como entrada
    return 0
  else: 
    leds = (altura+1) * (largura+1) #Calcula os leds (Os vértices dos quadrados no retângulo)
    return leds

print(calcula_total_leds(3,4))