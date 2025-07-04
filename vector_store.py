import google.generativeai as genai
import numpy as np
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

class LocalVectorDB:
    def __init__(self):
        self.items = []

    def embed(self, text):
        model = genai.get_model('embedding-001')
        return np.array(model.embed_content(content=text)["embedding"])

    def add(self, name, desc, url):
        vector = self.embed(desc)
        self.items.append((name, desc, url, vector))

    def search(self, query, top_k=3):
        q_vec = self.embed(query)
        ranked = sorted(self.items, key=lambda x: -np.dot(x[3], q_vec))
        return [(name, url) for name, _, url, _ in ranked[:top_k]]
