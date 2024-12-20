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
	step = 100
	for x in range(0, ScreenWidth, step):
		for y in range(0, ScreenHeight):
			print(currentImg[x][y])
		break

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