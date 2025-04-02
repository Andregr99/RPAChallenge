import pandas as pd
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import logging
import argparse

def configurar_logging():
    """Configura o sistema de logging."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ler_dados(nome_do_arquivo: str) -> pd.DataFrame:
    """Lê os dados da planilha e retorna um DataFrame."""
    try:
        df = pd.read_excel(nome_do_arquivo)
        df.columns = df.columns.str.strip()  # Remove espaços extras
        return df
    except Exception as e:
        logging.error(f"Erro ao ler o arquivo {nome_do_arquivo}: {e}")
        raise

def preencher_formulario(page, row):
    """Preenche o formulário com os dados da linha atual."""
    campos = {
        "First Name": "First Name",
        "Last Name": "Last Name",
        "Company Name": "Company Name",
        "Role in Company": "Role in Company",
        "Address": "Address",
        "Email": "Email",
        "Phone Number": "Phone Number",
    }
    
    try:
        for campo, valor in campos.items():
            seletor = f"xpath=//label[contains(text(),'{campo}')]/following-sibling::input"
            page.locator(seletor).fill(str(row[valor]))
        
        # Submeter formulário
        page.locator("xpath=//input[@type='submit']").click()
        logging.info(f"Formulário enviado para {row['First Name']} {row['Last Name']}")
    except KeyError as e:
        logging.error(f"Coluna ausente na planilha: {e}")
        raise
    except PlaywrightTimeoutError as e:
        logging.error(f"Timeout ao preencher o formulário: {e}")
        raise

def executar_automacao(nome_do_arquivo: str, headless: bool):
    """Executa o processo de automação do RPA Challenge."""
    df = ler_dados(nome_do_arquivo)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        
        try:
            page.goto("https://www.rpachallenge.com/")
            page.locator("xpath=//button[contains(text(),'Start')]").click()
            
            for _, row in df.iterrows():
                preencher_formulario(page, row)
            
            logging.info("Automação concluída com sucesso.")
            page.wait_for_timeout(5000)  # Aguarda 5 segundos antes de fechar
        except PlaywrightTimeoutError:
            logging.error("Erro ao carregar a página do RPA Challenge.")
        finally:
            browser.close()

def main():
    configurar_logging()
    
    parser = argparse.ArgumentParser(description="Automação do RPA Challenge com Playwright.")
    parser.add_argument("arquivo", type=str, nargs="?", default="challenge.xlsx", help="Caminho do arquivo Excel com os dados (padrão: challenge.xlsx).")
    parser.add_argument("--headless", action="store_true", help="Executar o navegador em modo headless.")
    args = parser.parse_args()
    
    executar_automacao(args.arquivo, args.headless)

if __name__ == "__main__":
    main()
