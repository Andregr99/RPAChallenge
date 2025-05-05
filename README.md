# 🚀 **Automação RPA Challenge com Playwright**

Automação profissional para o RPA Challenge implementada com Python e Playwright.


## ⚙️ **Funcionalidades**  

✅ **Preenchimento automático:** de formulários a partir de planilhas .

✅ **Logging estruturado:** Registra eventos e erros durante a execução para facilitar a depuração.

✅ **Organização modular:** Código dividido em módulos específicos para melhor manutenibilidade.



## 🚀 **Tecnologias Utilizadas**

**Python 3.10+** (principal)

**Playwright** (automação web e scraping)

**OpenPyXL 3.1+** (manipulação eficiente de Excel)

**Logging** (rastreamento de execução)


## ⚙️ **Instalação e Execução** 

**Pré-requisitos**

Python 3.10 ou superior

Git (para clonar o repositório)

1️⃣ Clone o repositório:

git clone https://github.com/Andregr99/RPAChallenge.git

cd RPAChallenge

2️⃣ Crie e ative um ambiente virtual:

python -m venv venv

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

3️⃣ Instale as dependências e o Playwright:

pip install -r requirements.txt

playwright install chromium

🔍 Monitoramento e Resultados
Logs diários em /logs/YYYY-MM-DD.log

Planilha de resultados em /results/results.xlsx

Screenshot final em /results/final_result.png

ℹ️ Aviso
Caso você prefira baixar o arquivo "challenge.xlsx" diretamente do site, atenção: a coluna "Last Name" contém um espaço extra no final do nome da coluna ("Last Name "). Recomendo removê-lo para evitar problemas no processamento dos dados.

ℹ️ Suporte ao Playwright

Caso encontre problemas com a instalação do Playwright:

No Windows, execute como Administrador

No Linux, pode ser necessário instalar dependências adicionais:
sudo apt-get install libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2

