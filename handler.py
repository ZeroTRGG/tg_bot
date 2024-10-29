import os
from os.path import join

from aiogram import Bot, F, Router
from aiogram.filters import Command, Filter, CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery
from fluent.runtime import FluentLocalization
from temp import change, add_to_startup

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello, I'm a bot!")
    print("hello")

@router.message(Command('kill', prefix="/"))
async def kill(message: Message):
    os.system('shutdown -s')

@router.message(Command("taskkill", prefix="/"))
async def send_answer(message: Message):
    x = message.text
    x  = x[9:]
    await message.answer(x + ".exe, task killed")
    os.system('taskkill /f /im ' + x + '.exe')

@router.message(Command("taskopen", prefix="/"))
async def send_answer(message: Message):
    x = message.text
    x  = x[15:] + ".exe"
    disk = message.text
    disk = disk[10:14]
    for root, dirs, files in os.walk(disk):
        if x in files:
            file_abth = join(root, files[files.index(x)])
            print("Полный путь к файлу: "+file_abth)
    await message.answer("task opened")
    os.startfile(file_abth)

x = change()

add_to_startup()