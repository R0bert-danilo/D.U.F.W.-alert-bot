import discord
import asyncio
import os
import pyfiglet
from colorama import Fore, Style, init
from datetime import datetime
import re
import requests

init()

TELEGRAM_BOT_TOKEN = 'TOKEN TELEGRAM BOT AQUI'
TELEGRAM_CHAT_ID = 'ID AQUI'

PALAVRAS_ESPECIFICAS = ["PALAVRAS PROIBIDAS AQUI"]

TOKEN = 'TOKEN BOT DISCORD AQUI'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

async def apresentacao():
    letras = ['D . U . F . W . alert']
    cores = [Fore.RED, Fore.GREEN, Fore.BLUE]

    for i, letra in enumerate(letras):
        result = pyfiglet.figlet_format(letra)
        print(cores[i] + result + Style.RESET_ALL)
        await asyncio.sleep(2)
        clear_screen()

    print(Fore.MAGENTA + "Iniciando o monitoramento..." + Style.RESET_ALL)

def normalizar_texto(texto):
    texto = re.sub(r'[^a-zA-Z0-9 ]', '', texto.lower())
    return texto

def palavra_proibida_detectada(mensagem):
    mensagem_normalizada = normalizar_texto(mensagem)
    palavras_mensagem = mensagem_normalizada.split()

    for palavra in PALAVRAS_ESPECIFICAS:
        palavra_normalizada = normalizar_texto(palavra)
        if palavra_normalizada in palavras_mensagem:
            return True
    return False

def enviar_notificacao_telegram(usuario, mensagem, data_hora):
    texto = f"Alerta de palavra proibida!\nUsuário: {usuario}\nHora: {data_hora}\nMensagem: {mensagem}"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto,
        "parse_mode": "HTML"
    }

    print(f"Enviando mensagem para {TELEGRAM_CHAT_ID}: {texto}")

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Notificação enviada via Telegram!")
    else:
        print(f"Erro ao enviar notificação. Código de status: {response.status_code}, Resposta: {response.text}")

def salvar_relatorio(nome_grupo, usuario, data_hora, mensagem):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    pasta_grupo = os.path.join(desktop, nome_grupo)

    if not os.path.exists(pasta_grupo):
        os.makedirs(pasta_grupo)

    arquivo_relatorio = os.path.join(pasta_grupo, "relatorio.txt")

    with open(arquivo_relatorio, "a", encoding='utf-8') as f:
        f.write(f"{data_hora} - Usuário: {usuario} - Mensagem: {mensagem}\n")

def gerar_relatorio_membros(nome_grupo, membros):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    pasta_grupo = os.path.join(desktop, nome_grupo)

    if not os.path.exists(pasta_grupo):
        os.makedirs(pasta_grupo)

    arquivo_relatorio = os.path.join(pasta_grupo, "relatorio_membros.txt")

    with open(arquivo_relatorio, "w", encoding='utf-8') as f:
        for membro in membros:
            tipo_membro = "Bot" if membro.bot else "Usuário"
            adm_status = " ADM" if membro.guild_permissions.administrator else ""
            f.write(f"{tipo_membro}: {membro.name}{adm_status} - ID: {membro.id}\n")

class MonitoramentoBot(discord.Client):
    async def on_ready(self):
        print(f'Conectado como {self.user}')
        await apresentacao()

        for guild in self.guilds:
            print(f"=== Membros do servidor '{guild.name}': ===")
            gerar_relatorio_membros(guild.name, guild.members)
            for membro in guild.members:
                tipo_membro = "Bot" if membro.bot else "Usuário"
                adm_status = " ADM" if membro.guild_permissions.administrator else ""
                print(f"{tipo_membro}: {membro.name}{adm_status} (ID: {membro.id})")

    async def on_message(self, message):
        if message.author == self.user:
            return

        data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if palavra_proibida_detectada(message.content):
            print(f"\n=== Palavra Proibida Detectada ===")
            print(f"Usuário: {message.author.name}")
            print(f"ID do Usuário: {message.author.id}")
            print(f"Data e Hora: {data_hora_atual}")
            print(f"Mensagem: {message.content}")
            print("=========================\n")

            enviar_notificacao_telegram(message.author.name, message.content, data_hora_atual)

            salvar_relatorio(message.channel.name, message.author.name, data_hora_atual, message.content)

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
client = MonitoramentoBot(intents=intents)

try:
    client.run(TOKEN)
except Exception as e:
    print(f"Ocorreu um erro ao executar o bot: {e}")
