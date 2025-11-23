import os
from dotenv import load_dotenv
load_dotenv()
import re

from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# ---- SECTION GENERATION ----
section_prompt = PromptTemplate.from_template("""
Write the section in clean business English.

Section: "{title}"
Topic: "{topic}"

STRICT RULES:
- NO markdown.
- NO ##, ###, **bold**, *, -, or ---.
- Use clear paragraph writing.
- For bullet points, use this format only:
  - Like this
  - Another point
- No headings using symbols.
- No formatting symbols of any kind.
- Output must be plain text.

Write professionally and cleanly.
""")

def clean_markdown(text: str) -> str:
    if not text:
        return ""

    # Remove headings like ##, ###, ####
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)

    # Remove bold/italic **text**, *text*, _text_
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"_(.*?)_", r"\1", text)

    # Remove horizontal rules like ---
    text = re.sub(r"^-{3,}$", "", text, flags=re.MULTILINE)

    # Convert markdown bullets "* " or "- " to "- "
    text = re.sub(r"^\s*[\*\-]\s+", "- ", text, flags=re.MULTILINE)

    # Remove extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

section_chain = section_prompt | model

def generate_section_content(title, topic):
    res = section_chain.invoke({"title": title, "topic": topic})
    cleaned = clean_markdown(res.content)
    return cleaned


# ---- REFINEMENT ----
refine_template = PromptTemplate.from_template("""
Clean and rewrite the content based on the instruction.

RULES:
- Remove ALL markdown (#, ##, **text**, *, ---).
- Convert bullets to "- " only.
- Convert headings to plain text (no symbols).
- No bold, italics, code, or separators.
- Use simple readable English.

Instruction: {instruction}

Content:
{content}

Return only the cleaned version.
""")




refine_chain = refine_template | model

def generate_refined_content(instruction, content):
    res = refine_chain.invoke({"content": content, "instruction": instruction})
    cleaned = clean_markdown(res.content)
    return cleaned
