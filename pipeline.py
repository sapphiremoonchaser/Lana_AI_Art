# Imports
import os
from logging import disable

import torch
from diffusers import StableDiffusionPipeline
from torch.fft import ifftshift


def initailize_pipeline():
    """Initialize the Stable Diffusion pipeline with error handling."""
    pipe = None
    token = os.getenv("HUGGINGFACE_TOKEN")
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16,
            # use_auth_token=os.getenv("HUGGINGFACE_TOKEN")
            use_auth_token=token if token else None
        )
        if torch.cuda.is_available():
            pipe = pipe.to("cuda")
        pipe.set_progress_bar_config(disable=True)

    except Exception as e:
        print(f"Error loading model: {str(e)}")

    return pipe
