from diffusers import DiffusionPipeline
import torch
import matplotlib.pyplot as plt

pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("mps")   #You may need to change "mps" depending on your GPUs/system. (Try "cpu" or "cuda")
image = pipeline("Dog in front of christmas tree in snow").images[0]

plt.imshow(image)
plt.show()