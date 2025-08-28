import h5py, faiss, os, numpy as np
from .load_data import load_data

file="embeddings.h5"


def load_embeddings(file_path):
    embeddings = None
    with h5py.File(file_path, "r") as h5f:
        embeddings = h5f["embeddings"][:]
    return embeddings


def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index


def search_similar_items(query_vector, index, k=5):
    """
    Searches for the top-k most similar items to the query_vector in the FAISS index.
    """
    query_vector = np.array(query_vector).astype("float32").reshape(1, -1)
    distances, indices = index.search(query_vector, k)
    return distances, indices


def retrieve_image(indices):
    data = load_data()
    print(len(data))
    return [data[i] for i in indices]


path = os.path.join(os.path.dirname(__file__), "..", "data", file)
embeddings = load_embeddings(path)
index = create_faiss_index(embeddings)

def retrieval(input_image_embedding=None):
    (distances, indices) = search_similar_items(input_image_embedding, index, k=3)
    images = retrieve_image(indices)
    return images
