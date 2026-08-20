from pathlib import Path

KNOWLEDGE_FILE = Path("data/knowledge.txt")


def search_knowledge(query: str):

    if not KNOWLEDGE_FILE.exists():
        return "Knowledge base is empty."

    text = KNOWLEDGE_FILE.read_text(
        encoding="utf-8"
    )

    query_words = query.lower().split()

    paragraphs = text.split("\n\n")

    results = []

    for paragraph in paragraphs:

        paragraph_lower = paragraph.lower()

        score = sum(
            1
            for word in query_words
            if word in paragraph_lower
        )

        if score > 0:
            results.append((score, paragraph))

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    if not results:
        return "No relevant information found."

    return "\n\n".join(
        paragraph
        for _, paragraph in results[:3]
    )