from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from env_utils import MODEL_NAME, API_KEY, BASE_URL

llm = ChatDeepSeek(
    model=MODEL_NAME, temperature=1.3, api_key=API_KEY, base_url=BASE_URL
)
