import sys
import argparse
import time
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config.logging_config import configure_logging
from src.config.settings import RPA_CHALLENGE_URL, DATA_DIR
from src.modules.data_processor import load_data
from src.modules.automation import RPAAutomation
from playwright.sync_api import sync_playwright

def run_automation(input_file: str, headless: bool = False) -> None:
    configure_logging()
    
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=headless,
                args=[
                    "--start-maximized",
                    "--kiosk",
                    "--disable-infobars",
                    "--disable-extensions"
                ],
                timeout=30000
            )
            
            context = browser.new_context(
                no_viewport=True,
                ignore_https_errors=True,
                java_script_enabled=True,
                screen={'width': 1920, 'height': 1080}
            )
            
            page = context.new_page()
            
            try:
                page.set_default_timeout(10000)
                page.goto(RPA_CHALLENGE_URL, wait_until="networkidle")
                
                if not headless:
                    page.evaluate("() => window.moveTo(0, 0)")
                    page.evaluate("() => window.resizeTo(screen.width, screen.height)")
                
                df = load_data(input_file)
                automation = RPAAutomation(page)
                automation.start_challenge()
                
                for _, row in df.iterrows():
                    automation.fill_form(row)
                
                if not headless:
                    logging.info("Automação concluída")
                    time.sleep(3)
                    
            except Exception as e:
                logging.error(f"Erro durante execução: {str(e)}")
                if not headless:
                    time.sleep(3)
                raise
            finally:
                context.close()
                browser.close()
                
    except Exception as e:
        logging.critical(f"Falha na inicialização: {str(e)}")
        raise

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Automação RPA Challenge",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Executar em modo headless (sem interface gráfica)"
    )
    parser.add_argument(
        "--input-file",
        type=str,
        default="challenge.xlsx",
        help="Caminho do arquivo de dados (relativo à pasta data/)"
    )
    args = parser.parse_args()
    
    try:
        run_automation(args.input_file, args.headless)
    except KeyboardInterrupt:
        logging.info("Execução interrompida pelo usuário")
        sys.exit(0)
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()