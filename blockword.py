# SISTEMA QUE BLOQUEIA PALAVROES PARA SEU SERVIDOR
# FEITO POR: Crazy_ArKzX
# GitHub: https://github.com/crazy-arkzx

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

palavroes = [
    "porra", "put", "safad", "arrombad", "molestad", "vagina", "pênis",
    "corn", "merda", "bosta", "foda", "bolsonaro", "nazis", "anus", "consolo",
    "1945", "coisa ruim", "ruim", "fortune", "discord.gg/", "chata", "anal",
    "http://", "delícia", "estrupa", "sua mae", "lixo", "fdp", "vsfd", "bunda",
     "vtmnc", "cu", "pau", "pica", "caralho", "crl", "krl", "viad", "gore", "ódio",
     "ridicul", "gay", "lula", "rittler", "🙋‍♂️🇩🇪", "matar", "capeta", "chato",
     "cassino", "foder", ".gg/", "https://", "www", "pinto", "teu pai", "odeio",
     "tua mae", "adotad", "piranha", "gostos", "goz", "esperma", "odiei", "brasileirinhas",
     "tua mãe", "sua mãe", "pqp", "piroca", "piroka", "feio", "ridícul", "porn",
     "desgraça", "11/09", "demônio", "louc", "louça", "pqp", "dc.gg/", "xvid",
     "dsc.gg/", "cacet", "portaldoz", "portal do z", "ruela", "seu pai", "xvir"
]

@bot.event
async def on_ready():
    print("Sistema Carregado com Sucesso!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 

    mensagem_lower = message.content.lower()
    
    for palavra in palavroes:
        if palavra in mensagem_lower:
            print(f"{message.author} Falou uma Palavra Inapropriada: {palavra}")
            await message.delete()
            await message.channel.send(
                f"{message.author.mention}, Sua Mensagem foi Removida por Conter Palavras Inapropriadas.", 
                delete_after=3
            )
            break

    await bot.process_commands(message)

TOKEN = "SEU_TOKEN"
bot.run(TOKEN)