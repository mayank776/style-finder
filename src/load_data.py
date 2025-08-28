from datasets import load_dataset

def load_data(dataset="NexaAIalex/Dress"):
    """
    Loads a dataset
    """

    fashion_data = load_dataset(dataset, split="train")
    return fashion_data
