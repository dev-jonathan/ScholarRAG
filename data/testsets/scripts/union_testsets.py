# from pathlib import Path
# import pandas as pd

# # Lista com os arquivos na ordem desejada
# arquivos = [
#     # # "testset_week_0.csv",
#     # "custom_graphs/testset_week_0.csv",
#     # # "testset_week_1.csv",
#     # "custom_graphs/testset_week_1.csv",
#     # # "testset_week_2.csv",
#     # "custom_graphs/testset_week_2.csv",
#     # # "testset_week_3.csv",
#     # "custom_graphs/testset_week_3.csv",
#     # # "testset_week_4.csv",
#     # "custom_graphs/testset_week_4.csv",
#     # # "testset_week_5.csv",
#     # "custom_graphs/testset_week_5.csv",
#     # # "testset_week_6.csv",
#     # "custom_graphs/testset_week_6.csv",
#     # # "testset_week_7.csv",
#     # "custom_graphs/testset_week_7.csv",
#     # # "testset_week_8.csv",
#     # "custom_graphs/testset_week_8.csv",
#     # # "testset_week_9.csv",
#     # "custom_graphs/testset_week_9.csv",
#     # # "testset_week_10.csv",
#     # "custom_graphs/testset_week_10.csv",
#     # # "testset_week_ai.csv",
#     # "custom_graphs/testset_week_ai.csv",
#     "testset_stratified_eval_results_qa_0-9.csv",
#     "testset_stratified_eval_results_qa_10-39.csv",
#     "testset_stratified_eval_results_qa_40-59.csv",
#     "testset_stratified_eval_results_qa_60-89.csv",
#     "testset_stratified_eval_results_qa_90-119.csv",
# ]

# # Lista para armazenar os DataFrames
# dfs = []

# base_dir = Path(__file__).resolve().parent

# dfs = []
# for arquivo in arquivos:
#     caminho_arquivo = base_dir / arquivo  # monta caminho completo
#     df = pd.read_csv(caminho_arquivo)
#     dfs.append(df)

# df_final = pd.concat(dfs, ignore_index=True)
# df_final.to_csv(base_dir / "stratified_qa_eval.csv", index=False)


# # total_normais = 0
# # total_custom = 0

# # for arquivo in arquivos:
# #     caminho_arquivo = base_dir / arquivo
# #     df = pd.read_csv(caminho_arquivo)
# #     num_linhas = len(df)
# #     print(f"{arquivo}: {num_linhas} linhas")

# #     if arquivo.startswith("custom_graphs/"):
# #         total_custom += num_linhas
# #     else:
# #         total_normais += num_linhas

# # print(f"\nTotal linhas arquivos normais: {total_normais}")
# # print(f"Total linhas arquivos custom_graphs: {total_custom}")
import pandas as pd

# Carregar os dois arquivos
main_df = pd.read_csv("data/testsets/stratified_qa_eval.csv")
missings_df = pd.read_csv("data/testsets/testset_stratified_missings_36-95.csv")

# Fazer o merge usando as colunas-chave
merged_df = pd.merge(
    main_df,
    missings_df[
        [
            "user_input",
            "retrieved_contexts",
            "response",
            "faithfulness",
            "answer_relevancy",
            "question_quality",
        ]
    ],
    on=["user_input", "retrieved_contexts", "response"],
    how="left",
    suffixes=("", "_missing"),
)

# Preencher os campos faltantes no main_df com os valores do missings_df
for col in ["faithfulness", "answer_relevancy", "question_quality"]:
    merged_df[col] = merged_df[col].combine_first(merged_df[f"{col}_missing"])

# Remover as colunas extras
merged_df = merged_df.drop(
    columns=[
        f"{col}_missing"
        for col in ["faithfulness", "answer_relevancy", "question_quality"]
    ]
)

# Salvar o resultado final
merged_df.to_csv("data/testsets/stratified_qa_eval_merged.csv", index=False)
