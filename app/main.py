from fastapi import FastAPI
from pydantic import BaseModel

from app.pdf import extract_text_from_pdf
from app.ai import ask_ai
from app.chunks import split_text_into_chunks
from app.search import search_relevant_chunks
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Document Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "AI Document Agent online"
    }


@app.get("/document")
def read_document():
    text = extract_text_from_pdf("./documents/flowdesk.pdf")

    return {
        "text": text
    }


@app.get("/chunks")
def get_chunks():
    text = extract_text_from_pdf("./documents/flowdesk.pdf")

    chunks = split_text_into_chunks(text)

    return {
        "total_chunks": len(chunks),
        "chunks": chunks
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    text = extract_text_from_pdf("./documents/flowdesk.pdf")

    chunks = split_text_into_chunks(text)

    relevant_chunks = search_relevant_chunks(
        question=request.question,
        chunks=chunks
    )

    context = "\n\n".join(relevant_chunks)

    answer = ask_ai(
        context=context,
        question=request.question
    )

    return {
        "question": request.question,
        "answer": answer,
        "chunks_used": len(relevant_chunks)
    }
    text = extract_text_from_pdf("./documents/flowdesk.pdf")

    answer = ask_ai(
        context=text,
        question=request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }