import pygame
import numpy as np

pygame.init()

ScreenWidth = 900
ScreenHeight = 600
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('plz draw img')

newImg = np.zeros((ScreenWidth, ScreenHeight))
currentImg = newImg.copy()

myFont = pygame.font.SysFont("malgungothic", 30)
radiusSize = 16

Run = True
pressing = False

def giveMeData():
	datas = []
	middleBits = 3
	heightBits = 3

	step = 100
	for x in range(0, ScreenWidth, step):
		maxVal, minVal = 0, 0
		for y in range(0, ScreenHeight):
			if currentImg[x][y] > 127:
				if minVal == 0:
					minVal = y
				maxVal = y
		#print(minVal, maxVal)
		if round(minVal*1000) == round(maxVal*1000):
			datas.append((0, 0))
		else:
			datas.append(((-minVal + ScreenHeight / 2)/(ScreenHeight/2),
						(-maxVal + ScreenHeight / 2)/(ScreenHeight/2)))
	midVals = []
	heightVals = []
	for maxV, minV in datas:
		middle = (maxV+minV)/2
		height = (maxV-minV)

		# middle / -1 ~ 1 => 0 ~ 2^bit-1
		# midVals.append((2**(middleBits-1)) + int(middle * ((2**middleBits) - 1)))
		midVals.append(
			int((middle + 1) / 2 * ((2**middleBits) - 1))
		)

		# height 0 ~ 2 => 0 ~ 2^bit-1
		heightVals.append(int(height / 2 * ((2**heightBits) - 1)))

	middleValue = 0
	heightValue = 0
	i = 0
	for m, h in zip(midVals, heightVals):
		# print(m * 2**(middleBits*i), h * 2**(heightBits*i))
		print(middleBits*(len(midVals) - i - 1), len(midVals) - i - 1)
		middleValue += m * (2**(middleBits*(len(midVals) - i - 1)))
		heightValue += h * (2**(heightBits*(len(midVals) - i - 1)))
		i += 1
	# print(midVals, heightVals)
	print("원래 가능하지만, 부동 소수점 이슈로 폐기됨")
	print(f"c = {int(ScreenWidth/step)}")
	print(f"p = -1")
	print("d_{0}="+str(heightValue))
	print("b_{0}="+str(heightBits))
	print("d_{1}="+str(middleValue))
	print("b_{1}="+str(middleBits))
	print("그래서 여기 밑에 껄 쓰면 됨")

	midVals = []
	heightVals = []
	for maxV, minV in datas:
		middle = (maxV+minV)/2
		height = (maxV-minV)

		midVals.append(round((middle + 1) / 2, 3))
		heightVals.append(round(height/2, 3))
	
	print(f"c = {int(ScreenWidth/step)}")
	print("b_{0} = "+str(heightVals))
	print("b_{1} = "+str(midVals))
	# print(f"p = -1")


while Run:
	# screen.fill((255, 255, 255))

	frame = pygame.surfarray.make_surface(currentImg)
	screen.blit(frame, (0, 0))
	screen.blit(myFont.render(f"z 눌러서 리셋, 클릭으로 그림, c로 출력", True, (255, 255, 255)), (0, 0))

	mousePos = pygame.mouse.get_pos()

	if pressing:
		center_x, center_y = mousePos

		# 원의 픽셀 계산
		x, y = np.ogrid[:ScreenWidth, :ScreenHeight]
		mask = (x - center_x)**2 + (y - center_y)**2 <= radiusSize**2

		# 원 영역을 True로 설정
		currentImg[mask] = 255

	pygame.draw.circle(screen, (255, 255, 255), mousePos, radiusSize, 0)

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Run = False
			pygame.quit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				currentImg = newImg.copy()

			elif event.key == pygame.K_UP:
				radiusSize *= 2

			elif event.key == pygame.K_DOWN:
				if radiusSize >= 2:
					radiusSize /= 2
			
			elif event.key == pygame.K_c:
				giveMeData()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: #좌클
				pressing = True
		
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				pressing = False