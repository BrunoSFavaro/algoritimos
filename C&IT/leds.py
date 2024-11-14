def calcula_total_leds(altura,largura):
  if(altura <= 0 or largura <= 0):
    leds = 0
  else:
    altura += 1
    largura += 1
    leds = altura * largura
  return leds

print(calcula_total_leds(3,4))