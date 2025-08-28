from sentence_transformers import SentenceTransformer
model = SentenceTransformer("clip-ViT-B-32")
print("Vision model loaded.")

def process_image(image):
    print(f"Processing image...{image}")
    image_embedding = model.encode(image)
    return image_embedding