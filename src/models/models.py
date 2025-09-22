import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from ragas.cache import DiskCacheBackend
from langchain_openai import ChatOpenAI


load_dotenv()
cacher = DiskCacheBackend()


def load_google_llm(model_name="gemini-2.5-flash", temperature=0.6, api_key=None):
    """Loads Google Gemini LLM."""
    return LangchainLLMWrapper(
        ChatGoogleGenerativeAI(
            model=model_name,
            temperature=temperature,
            google_api_key=api_key or os.getenv("GOOGLE_API_KEY"),
        ),
        cache=cacher,
    )


def load_openai_llm(model_name="gpt-4o", temperature=0.6, api_key=None):
    """Loads OpenAI LLM."""
    return LangchainLLMWrapper(
        ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=api_key or os.getenv("OPENAI_API_KEY"),
        ),
        cache=cacher,
    )


def load_local_llm(
    model_name="llama3",
    endpoint_url="http://localhost:11434/v1",
    api_key="ollama",
    temperature=0.6,
):
    """Loads local LLM via OpenAI API-compatible endpoint (Ollama, liteLLM, llama.cpp, etc)."""
    return LangchainLLMWrapper(
        ChatOpenAI(
            model=model_name,
            temperature=temperature,
            openai_api_base=endpoint_url,
            api_key=api_key,
        ),
        cache=cacher,
    )


def load_hf_embedding_model(model_name="Qwen/Qwen3-Embedding-0.6B"):
    """Loads embedding model from HuggingFace."""
    return LangchainEmbeddingsWrapper(
        HuggingFaceEmbeddings(
            model_name=model_name, model_kwargs={"trust_remote_code": True}
        )
    )


def load_lmstudio_embedding_model(
    model_name="text-embedding-qwen3-embedding-0.6b@f16",
    endpoint_url="http://localhost:1234/v1",
    api_key="lm-studio",
):
    """Loads embedding model via local LM Studio (OpenAI API)."""
    return LangchainEmbeddingsWrapper(
        OpenAIEmbeddings(
            model=model_name,
            openai_api_base=endpoint_url,
            openai_api_key=api_key,
            check_embedding_ctx_length=False,
        )
    )
