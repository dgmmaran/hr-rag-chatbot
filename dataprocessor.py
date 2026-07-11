from pdfreader import read_pdf
from chunker import chunk_pages
from embedder import embed_chunks
from vectorstore import store_in_pinecone
from typing import List

pdf_path = "./resources/HRPolicy.pdf"


def run():
    # Read HR Policy PDF and extract text
    pages = read_pdf(pdf_path)
    """print(f"Extracted {len(pages)} pages from the PDF.")
    print("First page content:")
    print(pages[0] if pages else "No content to display.")"""

    # Chunk the extracted text into manageable pieces
    chunks = chunk_pages(pages, chunk_size=900, chunk_overlap=150)
    """print(f"Created {len(chunks)} chunks from the extracted pages.")
    print("First chunk content:")
    print(chunks[0] if chunks else "No chunks to display.")"""

    embedded_chunks = embed_chunks(chunks)
    """print(f"Embedded {len(embedded_chunks)} chunks into vector representations.")
    print("First embedded chunk vector:")
    print(embedded_chunks[0] if embedded_chunks else "No embedded chunks to display.")"""

    store_in_pinecone(chunks, embedded_chunks, namespace="")


if __name__ == "__main__":
    run()
