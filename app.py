from fastapi import FastAPI
import chromadb
import ollama

app = FastAPI()
chrom = chromadb.PersistentClient(path="./db")
collection = chrom.get_or_create_collection("docs")
ollama_client = ollama.Client(host="http://host.docker.internal:11434")

@app.post("/query")
def query(q: str):
    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    answer = ollama_client.generate(
        model="tinyllama",
        prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )
    return {"answer": answer["response"]}

@app.post("/add")
def add_knowledge(text: str):
    """Add new knowledge to the database."""    
    try:
        import uuid
        doc_id = str(uuid.uuid4())

        collection.add(documents=[text], ids=[doc_id])

        return {
            "status": "success", 
            "id": doc_id,
            "message": "Content added successfully."
            }
    except Exception as e:
        return {
            "status": "error", 
            "message": str(e)
        }