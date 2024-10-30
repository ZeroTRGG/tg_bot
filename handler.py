import os
import time

from os.path import join
from aiogram import Bot, F, Router
from aiogram.filters import Command, Filter, CommandStart
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram.methods import DeleteMessage

from temp import change, add_to_startup
from camera import camera_image


router = Router()

current_dir = os.getcwd()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello, I'm a bot!")
    print("hello")

@router.message(Command('kill', prefix="/"))
async def kill(message: Message):
    os.system('shutdown -s')

@router.message(Command("taskkill", prefix="/"))
async def taskkill(message: Message):
    x = message.text
    x  = x[9:]
    await message.answer(x + ".exe, task killed")
    os.system('taskkill /f /im ' + x + '.exe')

@router.message(Command("taskopen", prefix="/"))
async def taskopen(message: Message):
    gif = FSInputFile(os.path.join(current_dir, "arts", "loading.gif"), filename="load.gif")
    msg = await message.answer_animation(animation=gif)
    x = message.text
    x  = x[15:] + ".exe"
    disk = message.text
    disk = disk[10:14]
    for root, dirs, files in os.walk(disk):
        if x in files:
            file_abth = join(root, files[files.index(x)])
            print("Полный путь к файлу: "+file_abth)
    time.sleep(1.5)
    await msg.delete()
    await message.answer("task opened")
    os.startfile(file_abth)

@router.message(Command("camera", prefix="/"))
async def camera(message: Message):
    do_photo = camera_image()
    image_path = FSInputFile(os.path.join(current_dir, 'dump', 'cam.png'))
    gif = FSInputFile(os.path.join(current_dir, "arts", "loading.gif"), filename="load.gif")
    msg = await message.answer_animation(animation=gif)
    time.sleep(3)
    await message.answer_photo(image_path)
    await msg.delete()

@router.message(Command("voice", prefix="/"))
async def voice(message: Message):
    msg = await message.answer("Voice recorded")
    await msg.delete()

x = change()

add_to_startup()