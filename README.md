# D . U . F . W . alert

## Descrição

O D . U . F . W . alert é um bot para Discord que monitora mensagens em tempo real em busca de palavras proibidas. Ao detectar uma palavra indesejada, o bot envia notificações instantâneas para um canal do Telegram, permitindo que administradores e moderadores mantenham o controle sobre o conteúdo. Fácil de configurar e personalizar.

## Pré-requisitos

Antes de rodar o projeto, você precisa ter os seguintes itens instalados:

- **Python 3.x**
- **pip** (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/R0bert-danilo/D.U.F.W.-alert-bot.git
   cd D.U.F.W.-alert-bot
2. **Instalação de dependências:**
   ```bash
   pip install -r requeriments.txt
3. **Configure as variáveis de ambiente dentro do arquivo:**
TELEGRAM_BOT_TOKEN: Token do seu bot do Telegram.
TELEGRAM_CHAT_ID: ID do chat ou grupo no Telegram.
PALAVRAS_ESPECIFICAS: Liste as palavras proibidas que o bot deve monitorar.
TOKEN: Token do seu bot do Discord.
4. **Estrutura de Código:**
clear_screen(): Limpa a tela do console.
apresentacao(): Apresenta uma mensagem de boas-vindas ao iniciar o bot.
normalizar_texto(texto): Normaliza o texto para verificar palavras.
palavra_proibida_detectada(mensagem): Detecta se uma mensagem contém palavras proibidas.
enviar_notificacao_telegram(usuario, mensagem, data_hora): Envia notificações para um chat do Telegram.
salvar_relatorio(nome_grupo, usuario, data_hora, mensagem): Salva um relatório em um arquivo no Desktop.
gerar_relatorio_membros(nome_grupo, membros): Gera um relatório dos membros do servidor.
MonitoramentoBot: Classe principal que gerencia eventos do Discord.

# comentário
Esse projeto ainda não está 100% concluído. O grande ponto negativo dele é que é necessário fazer a configuração manual diretamente no código, mas futuramente haverá mudanças para facilitar o uso.

## Conecte-se comigo
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/robertdanilom)
## Linguagem de Programação
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
##[D.U.F.W. alert bot.py](D.U.F.W.%20alert%20bot.py)
![Windows](https://img.shields.io/badge/Windows-000?style=for-the-badge&logo=windows&logoColor=2CA5E0)

![Kali](https://img.shields.io/badge/Kali-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)

![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)
