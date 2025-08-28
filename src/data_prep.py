from sentence_transformers import SentenceTransformer
import h5py, numpy as np, os , torch
from load_data import load_data

if torch.cuda.is_available():
    print("Success! GPU is available and will be used.")
    print(f"Device Name: {torch.cuda.get_device_name(0)}")
else:
    print("Warning: GPU not found. The model will run on the CPU, which will be much slower.")

def generate_embeddings(data, output_file="embeddings.h5", batch_size=32):
    """
    creates embeddings in batches, and saves them
    incrementally to an HDF5 file to handle large datasets.
    """

    vision_model = SentenceTransformer("clip-ViT-B-32")
    print("Vision model loaded.")

    total_items = len(data)
    dimension = len(vision_model.encode(data["image"][0]))

    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', output_file)
    with h5py.File(output_path, "w") as h5f:
        embedding_dataset = h5f.create_dataset(
            "embeddings",
            shape=(0, dimension),
            maxshape=(None, dimension),
            dtype=np.float32,
        )

        for i in range(0, total_items, batch_size):
            end_idx = min(i + batch_size , total_items)
            batch_images = data["image"][i:end_idx]
            batch_embeddings = vision_model.encode(batch_images)

            current_size = embedding_dataset.shape[0]
            embedding_dataset.resize(current_size + len(batch_embeddings), axis=0)

            embedding_dataset[current_size :] = batch_embeddings

            print(f"Processed batch {i//batch_size + 1}, saved {end_idx}/{total_items} embeddings.")

    print(f"\nSuccessfully saved all embeddings to {output_file}")


fashion_data = load_data()
generate_embeddings(fashion_data)