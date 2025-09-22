import json

# Carregue o JSON original
with open(
    "../../data/answers_json/Q14-fc39d1e9-cd98-46e5-8deb-828a21411f6c.json",
    "r",
    encoding="utf-8",
) as f:
    data = json.load(f)


# Função para extrair as mensagens do histórico
def extract_messages(history):
    # Ordena as mensagens pelo encadeamento (parentId/childrenIds)
    # Aqui, pega as mensagens na ordem de envio
    messages = []
    # Encontra a primeira mensagem (sem parentId)
    first = None
    for msg in history["messages"].values():
        if msg.get("parentId") is None:
            first = msg
            break
    if not first:
        return messages
    messages.append({"role": first["role"], "content": first["content"]})
    # Agora pega a resposta do assistant (se houver)
    if first.get("childrenIds"):
        child_id = first["childrenIds"][0]
        child = history["messages"][child_id]
        messages.append(
            {
                "role": child["role"],
                "content": child["content"],
                "model": child.get("model"),
                "modelName": child.get("modelName"),
                "sources": child.get("sources", [{}]),
            }
        )
    return messages


# Monta o novo dicionário limpo
cleaned = {
    "id": data["id"],
    "user_id": data["user_id"],
    "chat": {
        "id": data["chat"]["id"],
        "title": data["chat"]["title"],
        "models": data["chat"]["models"],
        "messages": extract_messages(data["chat"]["history"]),
    },
    "updated_at": data["updated_at"],
    "created_at": data["created_at"],
}

# Salva o novo JSON limpo
with open("Q14-clean.json", "w", encoding="utf-8") as f:
    json.dump(cleaned, f, ensure_ascii=False, indent=2)
print("Mensagens extraídas e JSON limpo salvo como 'Q14-clean.json'.")
