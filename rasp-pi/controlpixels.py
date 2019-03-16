import time
import board
import neopixel


pixel_pin1 = board.D18
pixel_pin2 = board.D17
pixel_pin3 = board.D27
pixel_pin4 = board.D22
pixel_pin5 = board.D23
pixel_pin6 = board.D24
pixel_pin7 = board.D25
pixel_pin8 = board.D20
pixel_pin9 = board.D16
pixel_pin10 = board.D13
pixel_pin11 = board.D19
pixel_pin12 = board.D26


num_pixels = 7

ORDER = neopixel.RGBW
FREQ = 800000
DMA = 5
INVERT = True

#pulses
#pixels = neopixel.NeoPixel(pixel_pin1, num_pixels, brightness = 0.5)

pixels = neopixel.NeoPixel(pixel_pin1, num_pixels, brightness=0.5, auto_write = False, pixel_order=ORDER)

#print(lights1)
#print(lights2)

#pixels.fill((255,0,0,0))
#pixels.show()

#def wheel(pos):
	#if pos < 0 or pos > 255:
		#r = g = b = w = 0

	#elif pos < 85:
		#r = int(pos*3)
		#g = int(255 - pos*3)
		#b = 0
		#w = 0
	#elif pos < 170:
		#pos -= 85
		#r = int(255 - pos*3)
		#g = 0
		#b = int(pos*3)
	#else:
		#pos -=170
		#r = 0
		#g = int(pos*3)
		#b = int(255  - pos*3)
	#return (r,g,b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r,g,b,0)


#def rainbow_cycle(wait):
	#for j in range(255):
		#for i in range(num_pixels):
			#pixel_index = (i*256//num_pixels)+j
			#pixels[i] = wheel(pixel_index & 255)
		#pixels.show()
		#time.sleep(wait)

#while True:
	#pixels.fill((255,0,0,0))
	#pixels.show()
	#time.sleep(1)

	#pixels.fill((0,255,0,0))
	#pixels.show()
	#time.sleep(1)

	#pixels.fill((0,0,255,0))
	#pixels.show()
	#time.sleep(1)

	#rainbow_cycle(0.001)


neopix_gamma = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25, 25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36, 37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89, 90, 92, 93, 95, 96, 98, 99, 101, 102, 104, 105, 107, 109, 110, 112, 114, 115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 133, 135, 137, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 167, 169, 171, 173, 175, 177, 180, 182, 184, 186, 189, 191, 193, 196, 198, 200, 203, 205, 208, 210, 213, 215, 218, 220, 223, 225, 228, 231, 233, 236, 239, 241, 244, 247, 249, 252, 255]

def pulse_white(wait):
	for j in range(256):
		for i in range(num_pixels):
			pixels.fill((0,0,0,neopix_gamma[j]))
			pixels.show()

	for j in range(256,0,-1):
		for i in range(num_pixels):
			pixels.fill((0,0,0,neopix_gamma[j]))
			pixels.show()


pulse_white(0.1)
