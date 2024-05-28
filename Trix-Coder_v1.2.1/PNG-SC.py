import os
import sys
import platform
from PIL import Image

sys.path.append('./System')

SystemName = platform.system()

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if SystemName == 'Windows':
	Specifier = ''
else:
	Specifier = '3'

def GameSelect():
	global PixelType, FileType

	print('1 - Бравл Старс')
	Game = input('Выбери игру: ')

	if Game == '1':
		from DataBase import PixelTypeBS as PixelType
		from DataBase import FileTypeBS as FileType

	else:
		Clear()
		GameSelect()

def Conversion():
	global ConvEnable

	print('1 - Да')
	print('2 - Нет')
	ConvEnable = input('использовать 32 битный конвертор изображения?: ')

	if ConvEnable != '1' and ConvEnable != '2':

		Clear()
		Conversion()

Clear()
GameSelect()
Clear()
Conversion()
Clear()

SystemPath = './System/Main.py'
InDecompressedScPath = './3сюда-PNG/'
OutCompressedScPath = './4отсюда-SC/'
SubPath = [i for i in os.listdir(InDecompressedScPath)]

for i in SubPath:

	CurrentSubPath = i + '/'
	ImagesPath = InDecompressedScPath + '/' + i
	Images = [i for i in os.listdir(ImagesPath)]
	Images.sort()
	ImagesToCompressPath = [InDecompressedScPath + CurrentSubPath + i for i in Images]
	ImagesToCompressPath.sort()
	ImagesToCompress = ' '.join(ImagesToCompressPath)
	OutNameList = [i for i in (Images[0])]
	DotIndex = OutNameList.index('.')
	OutName = ''.join(OutNameList[:DotIndex])

	while OutName.endswith('_'):

		OutName = OutName[:-1]

	ImagesPixelList = []
	ImagesTypeList = []

	for i in Images:

		ImagesPixelList.append(str(PixelType[i]))
		ImagesTypeList.append(str(FileType[i]))

		if ConvEnable == '1':

			print('[INFO] конвертация ' + i + ' в 32bit картинку...')
			ConvImage = Image.open(InDecompressedScPath + CurrentSubPath + i).convert('RGBA')
			ConvImage.save(InDecompressedScPath + CurrentSubPath + i)

	ImagesPixelType = ' '.join(ImagesPixelList)
	ImagesFileType = ' '.join(ImagesTypeList)

	if '1' in ImagesFileType:

		Splitter = ''

	else:

		Splitter = '-s '

	if ConvEnable == '1':

		print()

	os.system('python' + Specifier + ' ' + SystemPath + ' ' + ImagesToCompress + ' -p ' + ImagesPixelType + ' -c -header ' + Splitter + '-o ' + OutCompressedScPath + OutName + '.sc')
	print()
