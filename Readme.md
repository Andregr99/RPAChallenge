# 🌤️ ** Automação do RPA Challenge com Playwright** 🤩

Este projeto é um exemplo de automação avançada utilizando Python, Playwright e Pandas, demonstrando habilidades em web scraping, manipulação de dados e automação de processos empresariais. O código foi estruturado para seguir boas práticas, incluindo tratamento de erros, logging e execução parametrizada.

## ⚙️ **Funcionalidades**  

✅ **Leitura dinâmica de planilhas:** Carrega automaticamente os dados de um arquivo Excel.
✅ **Automação via Playwright:** Preenche formulários de forma eficiente, interagindo diretamente com os elementos da página.
✅ **Execução parametrizada:** Permite rodar o script em modo headless ou interativo.
✅ **Logging estruturado:** Registra eventos e erros, facilitando a depuração.
✅ **Tratamento de exceções:** Evita falhas inesperadas e melhora a confiabilidade do processo.

## 🚀 **Tecnologias Utilizadas**

- **Python 3.x:** Linguagem principal do projeto.

- **Playwright:** Biblioteca para automação de navegação web.

- **Pandas:** Manipulação e leitura de planilhas Excel.

- **Logging:** Registro estruturado de eventos.

- **Argparse:** Permite parametrização via linha de comando.

## ⚙️ **Instalação e Execução**  

1️⃣  **Clone o repositório:**

git clone https://github.com/Andregr99/RPAChallenge.git
cd RPAChallenge

2️⃣  **Crie e ative um ambiente virtual:**

python -m venv venv
Windows:
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate

3️⃣  **Instale as dependências:**

pip install -r requirements.txt

4️⃣ **Execute o script**

Modo interativo (abre o navegador):
python projeto.py challenge.xlsx
Modo headless (sem abrir o navegador):
python projeto.py challenge.xlsx --headless
