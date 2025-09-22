### `src/models`

This folder contains the `models.py` script, which centralizes the functions for loading and managing the large language models (LLMs) and embedding models used in the project.

---

### **Supported Models**

- **LLMs:**
  - **Google Gemini:** `load_google_llm`
  - **OpenAI GPT:** `load_openai_llm`
  - **Local LLMs:** `load_local_llm` (via Ollama, LM Studio, etc.)
- **Embeddings:**
  - **Hugging Face:** `load_hf_embedding_model`
  - **LM Studio:** `load_lmstudio_embedding_model`

---

### **Configuration**

API keys for Google and OpenAI models are loaded from environment variables. Create a `.env` file in your repository's root with the following keys:

```
GOOGLE_API_KEY="your_key"
OPENAI_API_KEY="your_key"
```

---

### **Usage**

To use any of the models, simply import the desired function from `models.py`:

```python
from src.models.models import load_openai_llm

llm = load_openai_llm(model_name="gpt-4o")
# Now you can use the 'llm' object in your code
```
