import os
import pandas as pd
import markdown
import csv  # Para o QUOTE_ALL correto
import re


def clean_md_text(md_text):
    """
    Limpa colchetes/aspas extras do início/fim, preservando o markdown interno.
    Corrige quebras de linha e escapes para garantir markdown puro.
    """
    if pd.isna(md_text):
        return ""
    md_text = str(md_text).strip()

    # Remove ['...'] ou ["..."] do início/fim (com ou sem espaços)
    md_text = re.sub(r"""^\s*[\[\(]\s*['"](.+?)['"]\s*[\]\)]\s*$""", r"\1", md_text)

    # Se ainda restar aspas no início/fim, remove
    md_text = re.sub(r"""^['"](.+?)['"]$""", r"\1", md_text)

    # Padroniza quebras de linha para \n
    md_text = md_text.replace("\r\n", "\n").replace("\r", "\n")

    # Substitui string literal '\\n' ou '\\\\n' por quebra de linha real
    md_text = md_text.replace("\\\\n", "\n")  # escape duplo primeiro!
    md_text = md_text.replace("\\n", "\n")

    # Remove excesso de quebras de linha (mais de 2 → 2)
    md_text = re.sub(r"\n{3,}", "\n\n", md_text)

    # Remove espaços extras no início/fim de cada linha
    md_text = "\n".join([line.strip() for line in md_text.splitlines()])

    return md_text


def convert_md_to_html(md_text, debug=False, col_name=None):
    """
    Converte texto Markdown limpo para HTML.
    Usa extensões para suportar blocos de código cercados, tabelas, etc.
    Se debug=True, faz print dos 5 primeiros e 5 últimos caracteres do markdown limpo.
    """
    md_text_clean = clean_md_text(md_text)
    if debug and col_name == "retrieved_contexts":
        # Mostra os 5 primeiros e 5 últimos caracteres para debug
        preview = md_text_clean[:5] + " ... " + md_text_clean[-5:]
        print(f"DEBUG markdown limpo: {preview}")
    html_output = markdown.markdown(
        md_text_clean, extensions=["fenced_code", "tables", "extra", "nl2br"]
    )
    return html_output


DATA_FILE_PATH = os.path.join("data", "testsets", "stratified_with_qa_eval.csv")
output_csv_file = "stratified_with_qa_eval_html.csv"

try:
    df = pd.read_csv(DATA_FILE_PATH, sep=",", quoting=csv.QUOTE_ALL)

    # Verifica as colunas necessárias
    if "retrieved_contexts" not in df.columns:
        print(
            f"A coluna 'retrieved_contexts' não foi encontrada em '{DATA_FILE_PATH}'."
        )
        exit()
    if "response" not in df.columns:
        print(f"A coluna 'response' não foi encontrada em '{DATA_FILE_PATH}'.")
        exit()

    print("Iniciando a conversão de Markdown para HTML...")

    # Para retrieved_contexts, remove os 2 primeiros e 2 últimos caracteres ANTES de tudo
    df["retrieved_contexts"] = df["retrieved_contexts"].apply(
        lambda x: x[2:-2] if isinstance(x, str) and len(x) > 4 else x
    )
    # Converter markdown para HTML nas colunas
    df["retrieved_contexts_html"] = df["retrieved_contexts"].apply(
        lambda x: convert_md_to_html(x, debug=True, col_name="retrieved_contexts")
    )
    df["response_html"] = df["response"].apply(convert_md_to_html)

    # Salvar CSV com as colunas novas
    df.to_csv(output_csv_file, index=False, quoting=csv.QUOTE_ALL)

    print(f"Conversão concluída! Arquivo salvo em '{output_csv_file}'.")

except FileNotFoundError:
    print(f"Erro: Arquivo '{DATA_FILE_PATH}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
