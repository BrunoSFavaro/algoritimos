altura = int(input())
largura = int(input())
largura += 1
altura += 1
if(altura <= 0 or largura <= 0):
	leds = 0
elif (altura <= 0 and largura <= 0):
    leds = 0
else:
	leds = altura * largura
print(leds)