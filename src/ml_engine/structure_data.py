import chromadb

# Initialize a local Vector Database
client = chromadb.Client()
collection = client.create_collection(name="receipt_data")

# These are the lines the AI found
raw_text = [
    "FEE RECEIPT", "Name: Dev", "Branch: AI", "Mess Fee: 7000", "Total: 7000"
]

# Add them to the database
collection.add(
    documents=raw_text,
    metadatas=[{"source": "receipt"} for _ in raw_text],
    ids=[f"id{i}" for i in range(len(raw_text))]
)

# Test a "Semantic" query
results = collection.query(
    query_texts=["How much money?"],
    n_results=2
)

print("\n--- AI Search Results ---")
print(results['documents'])
