# Style Finder

Style Finder is an advanced computer vision application that leverages deep learning to analyze fashion elements in images. Using an open source Vision Instruct model, this system identifies clothing items, retrieves relevant metadata, and provides actionable insights based on visual inputs.

## Features
- Upload any fashion photo and Style Finder will:
  - Identify garments
  - Analyze style elements
  - Provide detailed information about each item
  - Find similar items at different price points
- Makes high-end fashion more accessible by suggesting alternatives

## Dataset
The system uses a dataset based on Taylor Swift's iconic outfits, demonstrating how to connect visual inputs with structured fashion data for precise identification of garments, accessories, and styling elements, along with corresponding commercial availability information.

## Getting Started

style-finder-multi-modal-RAG/
├── data/
│   └── your_dataset.pkl
├── src/
│   ├── data_loader.py
│   └── embedder.py
4. **Configure the `config.py` file**
  - Update the configuration settings in `config.py` (such as API keys, debug mode, or other parameters) as needed for your environment.

5. **Run the application**
  - To launch the Gradio app, run:
    ```bash
    python app.py
    ```

  - The app will start a web server (default: http://localhost:7860) where you can upload a fashion image and view similar items.
1. **Start the virtual environment**

   - On Windows (PowerShell):
     ```powershell
     ./venv/Scripts/Activate.ps1
     ```
   - On macOS/Linux:
     ```bash

  ```bash
  pip install -r requirements.txt
  ```

3. **Download the dataset**
  ```bash
  wget -O swift-style-embeddings.pkl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/95eJ0YJVtqTZhEd7RaUlew/processed-swift-style-with-embeddings.pkl
  ```

4. **Configure the `config.py` file**
  - Update the configuration settings in `config.py` (such as API keys, debug mode, or other parameters) as needed for your environment.

---

## Usage
1. Upload a fashion photo.
2. View identified garments and style analysis.
3. Explore similar items and commercial options.

## Technology
- Deep learning
- Computer vision
- Vision Instruct model (open source)

---

*For research, prototyping, and educational purposes.*
