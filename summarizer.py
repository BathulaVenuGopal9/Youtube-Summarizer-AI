import os
import zipfile
from dotenv import load_dotenv

from langchain_community.document_loaders import YoutubeLoader
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# ==============================
# Load API Key
# ==============================
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# ==============================
# Initialize LLM
# ==============================
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # ✅ FINAL MODEL
    google_api_key=api_key
)

# ==============================
# Summarizer Prompt
# ==============================
system_message = "You are a Professional Article Writer specializing in Medium, LinkedIn, and tech blogs."

human_message = """
Transform YouTube transcript into engaging professional articles.

RULES:
- Ignore intro, ads, promotions
- Focus only on technical content
- Use headings, lists, structured format
- Add actionable insights
- End with summary

Transcript:
{transcript}
"""

summarizer_prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("human", human_message)
])

# ==============================
# Extract Transcript
# ==============================
def extract_transcript(link: str) -> str:
    loader = YoutubeLoader.from_youtube_url(link)
    docs = loader.load()
    return docs[0].page_content

# ==============================
# Webpage Prompt
# ==============================
web_system = """You are a Senior Frontend Developer.

Output EXACT format:

--html--
HTML code
--html--

--css--
CSS code
--css--

--js--
JavaScript code
--js--
"""

web_human = """
Create a modern article webpage (Medium/Dev.to style).

Requirements:
- Responsive design
- Clean typography
- Dark/light mode
- Smooth UI
- SEO friendly

Content:
{article}
"""

web_prompt = ChatPromptTemplate.from_messages([
    ("system", web_system),
    ("human", web_human)
])

# ==============================
# FINAL PIPELINE
# ==============================
smart_pipeline = (
    RunnablePassthrough()
    | RunnableLambda(extract_transcript)
    | summarizer_prompt
    | llm
    | StrOutputParser()
    | RunnableLambda(lambda x: {"article": x})   # ✅ IMPORTANT FIX
    | web_prompt
    | llm
    | StrOutputParser()
)

# ==============================
# RUN
# ==============================
url = "https://www.youtube.com/watch?v=0QzopZ78w9M"

result = smart_pipeline.invoke(url)

# ==============================
# SAVE FILES
# ==============================
html = result.split("--html--")[1].split("--html--")[0]
css = result.split("--css--")[1].split("--css--")[0]
js = result.split("--js--")[1].split("--js--")[0]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)

# ZIP
with zipfile.ZipFile("website.zip", "w") as zipf:
    zipf.write("index.html")
    zipf.write("style.css")
    zipf.write("script.js")

print("Website generated successfully!")