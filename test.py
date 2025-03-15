from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="pcsk_7EwQeU_QYQwhMtSDHT2GYbgDx3YDjmBZzUxfDJZByhsQDZtWp5wVXpoDfouELv5W6i1VC8")

index_list = pc.list_indexes()

print(index_list)