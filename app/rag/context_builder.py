# app/rag/context_builder.py


def build_context(documents) -> str:
    if not documents:
        return ""

    return "\n".join(
        document.page_content
        for document in documents
    )