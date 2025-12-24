from langchain_openai import ChatOpenAI
from env_utils import MODEL_NAME, API_KEY, BASE_URL

llm = ChatOpenAI(model=MODEL_NAME, temperature=1.3, api_key=API_KEY, base_url=BASE_URL)
