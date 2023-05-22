
from PIL import Image, ImageFilter




'''Подготовьте любой графический файл для выполнения практической работы.
Напишите программу, которая открывает и выводит этот файл на экран. 
Получите и выведите в консоль информацию о размере изображения, его формате, его цветовой модели.'''
def lab1():
    filename = "kotek.jpg"
    with Image.open(filename) as img:
        img.load()

    img.show()
    width, height = img.size

    format = img.format

    mode = img.mode

    print("Ширина: ", width)
    print("Высота:  ", height)
    print("Формат: ", format)
    print("Цветовая модель:", mode)

'''Напишите программу, которая создаёт уменьшенную в три раза копию изображения. 
Получите горизонтальный и вертикальный зеркальный образ изображения. 
Сохраните изображения в текущую папку под новым именем.'''

def lab2():
    filename = "kotek.jpg"
    with Image.open(filename) as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))

    new_img.save("resized_kotek.jpg")

    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.save("image_flipkotek_top.jpg")
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save("image_flip_kotek.jpg")

'''Подготовьте 5 графических файлов с именами 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg. 
Напишите программу, которая применит ко всем этим файлам сразу любой фильтр (кроме размытия, т.к. он рассматривался на лекции). 
Сохраните изображения в новую папку под новыми именами.'''
def lab3():
    filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.save("new_" + file)

'''Напишите программу, которая добавляет на изображение водяной знак. 
Можно тоже применять сразу к нескольким изображениям.'''

def lab4():
    water = "watermark.png"
    with Image.open(water) as img_water:
        img_water.load()

    img_water = Image.open(water)
    img_water = img_water.resize((img_water.width // 2, img_water.height // 2))

    filename = "kotek.jpg"
    with Image.open(filename) as img:
        img.load()

    img.paste(img_water, (10, 200), img_water)
    img.save("watermark_kotek.jpg")

lab1()
lab2()
lab3()
lab4()