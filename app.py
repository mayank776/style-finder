import gradio as gr
from src.retrieval import retrieval
from src.image_processing import process_image


def generate_response(input_image):
    image_embedding = process_image(input_image)
    similar_images = retrieval(input_image_embedding=image_embedding)
    print(f"Similar images: {similar_images}")

    images = similar_images[0]["image"]
    return images
    return similar_images


app = gr.Interface(
    fn=generate_response,
    inputs=gr.Image(type="pil", label="Input Image"),
    outputs=gr.Gallery(label="Similar Images"),
    # outputs=gr.Textbox(label="AI Response", interactive=False),
    flagging_mode="never",
)

app.launch(server_port=7860).launch()
