from data.load_data import load_dataset

docs = load_dataset()

print("Total documents loaded:", len(docs))

if len(docs) > 0:
    print("\nSample document:\n")
    print(docs[0][:500])
else:
    print("No documents found.")